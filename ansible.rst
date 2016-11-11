.. _ansible:

*******
Ansible
*******

This chapter describes how OCP 3.3 can be deployed according to the FISMA
High security controls listed in this guide. Further, the deployed reference
architecture is "air-gapped" in a private AWS VPC with not direct access
to the Internet.

Automation
==========

Concept of Operation
--------------------

Manual Workarounds
==================

User Authentication
-------------------
Cluster Admins and Application developers gain access to OCP through a WebUI or CLI.  In order to authenticate with the CLI, the user must first log in to the WebUI and obtain a CLI token.  The following details how to enable PKI authentication in the WebUI.

Request Header Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The request header authentication passes the authentication request to another Apache process.  If that process successfully authenticates (and authorizes if desired) the user, then it passes the username back to the OpenShift master in an HTTP header.

This Apache process may be run on the OpenShift master or separate host.  This example assumes the Apache process is on a separate host.

1. OpenShift Master – master.example.com
2. Apache proxy for authentication – proxy.example.com

OpenShift Master – Creating Certificates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OpenShift manages its own certificates to encrypt inter-nodal communication.  This is beneficial in another way.  We don’t want someone to spoof our proxy and authenticate by passing in a remote header from some random host.  Therefore, we will create a certificate for the Apache proxy using the CA on the OpenShift master.

SSH to the OpenShift master and elevate your privileges to root.::
  # oadm ca create-signer-cert \
  --cert='/etc/origin/master/proxyca.crt' \
  --key='/etc/origin/master/proxyca.key' \
  --name='openshift-proxy-signer@1432232228' \
  --serial='/etc/origin/master/proxyca.serial.txt'

  # oadm create-api-client-config \
  --certificate-authority='/etc/origin/master/proxyca.crt' \
  --client-dir='/etc/origin/master/proxy' \
  --signer-cert='/etc/origin/master/proxyca.crt' \
  --signer-key='/etc/origin/master/proxyca.key' \
  --signer-serial='/etc/origin/master/proxyca.serial.txt' \
  --user='system:proxy'

  # pushd /etc/origin/master
  # cp ca.crt /root/authproxyca.crt
  # cat proxy/system\:proxy.crt \
  proxy/system\:proxy.key > \
  /root/authproxy.crt
  # popd

Using your favorite file transfer method, copy the authproxy.crt and authproxyca.crt from the OpenShift Master to the Apache proxy host.

Apache Proxy
~~~~~~~~~~~~
SSH into the Apache Proxy and install some basic packages as root.::
  # yum install -y httpd mod_ssl mod_session apr-util-openssl

Also, as root, create a new Apache configuration file with the following content in /etc/httpd/conf.d/::
  # vi /etc/httpd/conf.d/ose-proxy.conf

  LoadModule session_module modules/mod_session.so
  LoadModule request_module modules/mod_request.so

  # Nothing needs to be served over HTTP. This virtual host simply redirects to
  # HTTPS.
  <VirtualHost *:80>
  DocumentRoot /var/www/html
  RewriteEngine On
  RewriteRule ^(.*)$ https://%{HTTP_HOST}$1 [R,L]
  </VirtualHost>

  <VirtualHost *:443>
  # This needs to match the certificates you generated. See the CN and X509v3
  # Subject Alternative Name in the output of:
  # openssl x509 -text -in /etc/pki/tls/certs/localhost.crt
  ServerName proxy.example.com

  DocumentRoot /var/www/html
  SSLEngine on
  SSLCertificateFile /etc/pki/tls/certs/localhost.crt
  SSLCertificateKeyFile /etc/tls/private/localhost.key

  #This is the CA against which your user’s certificates will be checked.
  SSLCACertificateFile /etc/pki/tls/certs/ca-bundle.crt

  SSLProtocol ALL -SSLv2 -SSLv3
  SSLCipherSuite ECDHE-RSA-AES256-SHA384:AES256-SHA256:RC4:HIGH:!MD5:!aNULL:!EDH:!EXP:!SSLV2:!eNULL
  SSLUserName SSL_CLIENT_S_DN_CN
  SSLOptions +StdEnvVars +ExportCertData
  #For PKI
  SSLVerifyClient require

  SSLProxyEngine on

  #These were created per the instructions in the OSE installation docs
  SSLProxyCACertificateFile /etc/pki/CA/certs/authproxyca.crt
  SSLProxyMachineCertificateFile /etc/pki/tls/certs/authproxy.crt

  ErrorLog logs/ssl_error_log
  TransferLog logs/ssl_access_log
  LogLevel debug
  CustomLog logs/ssl_request_log \
  “%t %h %{SSL_PROTOCOL}x %{SSL_CIPHER}x \”%r\” %b”
  # Send all requests to the console
  RewriteEngine On
  RewriteRule ^/console(.*)$ https://%{HTTP_HOST}:8443/console$1 [R,L]

  # In order to using the challenging-proxy an X-Csrf-Token must be present.
  RewriteCond %{REQUEST_URI} ^/challenging-proxy
  RewriteCond %{HTTP:X-Csrf-Token} ^$ [NC]
  RewriteRule ^.* – [F,L]

  <Location /challenging-proxy/oauth/authorize>
  # Insert your backend server name/ip here.
  AuthName openshift
  ProxyPass https://master.example.com:8443/oauth/authorize
  </Location>

  <Location /login-proxy/oauth/authorize>
  # Insert your backend server name/ip here.
  AuthName openshift
  ProxyPass https://master.example.com:8443/oauth/authorize
  </Location>

  <ProxyMatch /oauth/authorize>
  #This require directive is very important
  require valid-user
  RequestHeader set X-Remote-User %{SSL_CLIENT_S_DN_CN}s
  </ProxyMatch>

  </VirtualHost>
  RequestHeader unset X-Remote-User

Please note the SSLCACertificateFile directive.  This is the CA against which the clients (your users) will be validated.  Out of the box, the specified file won’t work.  Please replace this will the valid CA file or chain.

OpenShift Master - Auth Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now that we have Apache configured, we need to configure the authentication provider for the OpenShift Master.  SSH into the OpenShift Master and elevate your privileges to root.  Then edit the Master’s configuration file:::
  # vi /etc/origin/master/master-config.yaml

Now, in the oathConfig section, enter the following::
  oauthConfig:
    ...
    identityProviders:
    - name: requestheader
      challenge: true
      login: true
      provider:
        apiVersion: v1
        kind: RequestHeaderIdentityProvider
        challengeURL: "https://proxy.example.com/challenging-proxy/oauth/authorize?${query}"
        loginURL: "https://proxy.example.com/login-proxy/oauth/authorize?${query}"
        clientCA: /etc/origin/master/proxyca.crt
        headers:
        - X-Remote-User

YAML is delimited by spaces.  Please ensure you have the correct spacing.

Once you have saved the file, go ahead and restart your master.::
  # systemctl restart atomic-openshift-master.service

Now navigate to your OpenShift master in a web browser.  If you have a valid client certificate, you should just be authenticated.
