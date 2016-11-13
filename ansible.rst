.. _ansible:

*******
Ansible
*******

This chapter describes how OCP 3.3 can be deployed according to the FISMA
High security controls listed in this guide. Further, the deployed reference
architecture is `air-gapped`_ in a private AWS VPC with not direct access
to the Internet.

Reference Architecture
======================

The :ref:`sec_conops` chapter describes the OpenShift FISMA High reference
architecture. That architecture can be implemented in AWS with the
`openshift-disconnected`_ project.

`openshift-disconnected`_ is implemented with Ansible. It can be deployed
automatically, kept compliant with its CM baseline, and audited with
`OpenSCAP`_. The AWS VPC layout replicates an `air-gapped`_ deployment that is
unable to access the Internet. This requires many services that are typically
taken for granted like DNS to be deployed into the private VPC.

`openshift-disconnected`_ automatically deploys all of the required services
to run OCP 3.3 in the private VPC. Many of the functions implemented by
`openshift-disconnected`_ are pluggable and can be added to your Ansible
project with `Ansible Galaxy`_ from the `RHTPS`_ organization.

Some of the most reusable roles are:

+------------------+-----------------------------------------------------------+
| Role             | Description                                               |
+==================+===========================================================+
| `800-53`_        | Implements RHEL FISMA compliance and scans the resultant  |
|                  | configuration with OpenSCAP.                              |
+------------------+-----------------------------------------------------------+
| `bind`_          | Deploys DNS services into the private VPC                 |
+------------------+-----------------------------------------------------------+
| `private-aws`_   | Sets up the public and private VPCs and deploys the EC2   |
|                  | instances.                                                |
+------------------+-----------------------------------------------------------+
| `registry`_      | Sets up a private docker registry and populates it with   |
|                  | all of the images required by OpenShift.                  |
+------------------+-----------------------------------------------------------+
| `yum`_           | Sets up a yum server with all of the RPM content required |
|                  | for the OpenShift deployment.                             |
+------------------+-----------------------------------------------------------+

For instructions on how to use the `openshift-disconnected`_ project, refer to
the `README`_.

Manual Workarounds
==================

Some aspects of the reference architecture expressed in the :ref:`sec_conops`
has not yet been implemented in the `openshift-disconnected`_ project. Those
missing components are being tracked in the `Issues`_ page for that repo.
As a work around, manual implementation instructions are below.

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

SSH to the OpenShift master and elevate your privileges to root.

.. code-block:: none

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
SSH into the Apache Proxy and install some basic packages as root.

.. code-block:: none

    # yum install -y httpd mod_ssl mod_session apr-util-openssl

Also, as root, create a new Apache configuration file with the following content in /etc/httpd/conf.d/

.. code-block:: none

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
Now that we have Apache configured, we need to configure the authentication provider for the OpenShift Master.  SSH into the OpenShift Master and elevate your privileges to root.  Then edit the Master’s configuration file.

.. code-block:: none

    # vi /etc/origin/master/master-config.yaml

Now, in the oathConfig section, enter the following

.. code-block:: yaml

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

Once you have saved the file, go ahead and restart your master.

.. code-block:: none

    # systemctl restart atomic-openshift-master.service

Now navigate to your OpenShift master in a web browser.  If you have a valid client certificate, you should just be authenticated.

.. _`openshift-disconnected`: https://github.com/jason-callaway/openshift-disconnected
.. _`Issues`: https://github.com/jason-callaway/openshift-disconnected/issues
.. _`OpenSCAP`: https://www.open-scap.org/
.. _`Ansible Galaxy`: https://galaxy.ansible.com/
.. _`RHTPS`: https://galaxy.ansible.com/rhtps
.. _`800-53`: https://galaxy.ansible.com/rhtps/800-53/
.. _`air-gapped`: https://en.wikipedia.org/wiki/Air_gap_(networking)
.. _`bind`: https://galaxy.ansible.com/rhtps/bind/
.. _`private-aws`: https://galaxy.ansible.com/rhtps/private-aws/
.. _`yum`: https://galaxy.ansible.com/rhtps/yum/
.. _`registry`: https://galaxy.ansible.com/rhtps/registry/
.. _`README`: https://github.com/jason-callaway/openshift-disconnected/blob/master/README.md
