.. _reference_architecture:

*********************
Reference Architeture
*********************
Introduction
============
The reference architecture details, at various levels of abstraction, a
deployment of Red Hat's OpenShift Container Platform (OCP) deployed on Amazon Web Services (AWS).  The NIST *Definition of Cloud Computing* `NIST 800-145`_ succinctly describes different cloud service models and the attributes of a cloud platform.  The architecture described herein follows the definitions found in the NIST 800-145.  For example, Red Hat's OCP is a Platform as a Service (PaaS) under NIST 800-145.  Similarly, AWS is an Infrastrucutre as a Service (IaaS) per the NIST definition.

Security Standards
------------------
The Fedral Information Security Modernization Act (`FISMA`_), originally enacted in 2002, directs United States Federal Agencies to develop and implement programs to implement information and information systems security.  This reference architecture aims to describe an OCP deployment on AWS as FISMA high: high confidentiality, high integrity, high availability.

In order to demonstrate FISMA high, this architecture is traced to `NIST 800-53`_ *Security and Privacy Controls for Federal Information Systems and Organizations*.  The NIST 800-53 provides a catalog of controls accross multiple categories.  Many controls relate to organizational processes.  These controls will be mapped as appropriate.  The controls that are technical in nature are addressed by this architecture.

Architecture
============
This architecture is divided into architectural views loosely mapped to the NIST 800-145 *Definition of Cloud Computing*.  The nature of cloud computing affords the adoption of a Landlord/Tenant model.  This model allows the Landlord to take responsibility for a set of controls under NIST 800-53, relieving the tenant of the need to address those controls.  The following table lists lists the relationship of Landlord to Tenant in this reference architecture.

+--------------+---------------+
| Landlord     |        Tenant |
+==============+===============+
| AWS          |       OCP     |
+--------------+---------------+
| OCP          |  Applications |
+--------------+---------------+

As stated prviously, the IaaS in this architecture is AWS.  Red Hat's OCP is the PaaS.  Tenant applications are deployed in containers, managed by OCP.

Infrastructure View
-------------------
The infrastructure view describes the OCP components at the infrastructure level.  These components are necessary to serve OCP in AWS and achieving FISMA high.

IaaS Definition - NIST 800-145
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The capability provided to the consumer is to provision processing, storage, networks, and other fundamental computing resources where the consumer is able to deploy and run arbitrary software, which can include operating systems and applications. The consumer does not manage or control the underlying cloud infrastructure but has control over operating systems, storage, and deployed applications; and possibly limited control of select networking components (e.g., host firewalls).

Description
~~~~~~~~~~~
AWS provides this capability.  Amazon provides the underlying hardware infastructure that supports the self-service provisioning into the cloud of what has traditionaly been based in hardware.  This includes, but is not limited to compute, storage, and networking services.

Stakeholders
~~~~~~~~~~~~
**OCP administrators** require AWS console access and the ability to deploy and/or configure the following AWS components.

 - VPC
 - Elastic IP
 - Elastic Cloud Compute (EC2)
 - VPC Peering
 - Route Tables

**Application developers** do not have a role at the infrastructure level.

**Application consumers** do not have a role at the infrastructure level.

Diagram
~~~~~~~
The following diagram illustrates the high level deployment of OCP in AWS and the necessary AWS components to support OCP.
|Infrastructure View|

Components
~~~~~~~~~~
The following table describes each AWS component and relates it to the implementation in the OCP reference architecture.

+---------------+---------------------------------------------------------+------------------------+
| AWS Component | Description                                             |  OCP Component         |
+===============+=========================================================+========================+
| VPC           | A logically isolated section of AWS in which resources  | Red Hat VPC            |
|               | are connected via a virtual networking environment.     +------------------------+
|               |                                                         | 1..n Dedicated VPC's   |
+---------------+---------------------------------------------------------+------------------------+
| Subnet        | Virtually isolated network used on which traffic        | Management Subnet      |
|               | is isolatedbecause isolation makes for great neighbors. +------------------------+
|               |                                                         | Staging Subnet         |
|               |                                                         +------------------------+
|               |                                                         | Operations Subnet      |
|               |                                                         +------------------------+
|               |                                                         | Dedicated Subnet       |
+---------------+---------------------------------------------------------+------------------------+
| EC2 Compute   | A scalable compute capacity in AWS.  Compute instances  | All OCP Platform       |
| Instance      | are instantiated from cloud images with pre-installed   | components.            |
|               | operating systems, for example Red Hat Enterprise Linux.|                        |
+---------------+---------------------------------------------------------+------------------------+
| Route Table   | A route table defines rules as to how network traffic   | Red Hat VPC            |
|               | in a VPC is routed internally.                          |                        |
+---------------+---------------------------------------------------------+------------------------+
| Elastic IP    | An Elastic IP is associated with an EC2 Instance and is | Staging HA Proxy       |
|               | publically reacheable.                                  +------------------------+
|               |                                                         | Staging Authentication |
|               |                                                         +------------------------+
|               |                                                         | Staging App. Traffic   |
|               |                                                         +------------------------+
|               |                                                         | Bastion                |
|               |                                                         +------------------------+
|               |                                                         | Ansible Tower          |
+---------------+---------------------------------------------------------+------------------------+
| VPC Peering   | A VPC peering connection is a networking connection     | Between the Red Hat    |
|               | between two VPCs that enables traffic to be routed      | VPC and any Dedicated  |
|               | between them using private IP addresses.                | VPC                    |
+---------------+---------------------------------------------------------+------------------------+
| Elastic Load  | An ELB automatically distributes traffic among EC2      | Operations API         |
| Balancer      | instances.                                              +------------------------+
|               |                                                         | Operations Application |
|               |                                                         +------------------------+
|               |                                                         | Dedicated API          |
|               |                                                         +------------------------+
|               |                                                         | Dedicated Application  |
+---------------+---------------------------------------------------------+------------------------+

Network Architecture
~~~~~~~~~~~~~~~~~~~~
The **Staging Subnet** provides an isolated area for platform administrators to apply regular patches and test configuration changes before applying these to the operations cluster.  One cluster of OCP is deployed in this VPC.

The **Operations Subnet** contains a single deployment of OpenShift where tenants will deploy applications.  OCP Nodes will be labled and functionally grouped to support development, test, and production deployments of an application.  This is described in detail in the *Platform View*.

The **Management Subnet** contains the Trusted Container Repository as well as the Package Repository.  A route table allows the **Managent Subnet** to communicate to the **Staging Subnet**, **Operations Subnet**.  The **Staging Subnet** and **Operations Subnet** are not permitted to communicate with each other. A VPC peering connection allows the **Management Subnet** in the **Red Hat VPC** to communicate with any **Dedicated VPC's**.

**Dedicated VPC's** are VPC's that are deployed to support specific isolation needs of a particular tenant.  These may be created and destroyed per organizational needs.

The **bastion host** allows OCP Administrators and only OCP Administrators the ability to access the underlying hosts in each VPC.

**Application Developers** interact with OCP via a command line interface (CLI) and web user interface (WebUI).  An application router, internal to OCP, handles application traffic.  Therefore certain ports in a security group must be exposed on the **Red Hat VPC** to allow ths traffic.  The same is true of any **Dedicated VPC's**.  The following table details this information.

+----------+---------------------+-------------------------------------------+
| VPC Port | VPC/Subnet          | Exposed Component                         |
+==========+=====================+===========================================+
| 443/TCP  | Red Hat/Operations  | ELB - API Traffic                         |
+          +                     +-------------------------------------------+
|          |                     | ELB - Application Traffic                 |
+          +---------------------+-------------------------------------------+
|          | Red Hat/Staging     | Elastic IP - API HA Proxy                 |
+          +                     +-------------------------------------------+
|          |                     | Elastic IP - Application Traffic          |
+          +---------------------+-------------------------------------------+
|          | Red Hat/Management  | Elastic IP - Ansible Tower                |
+          +---------------------+-------------------------------------------+
|          | Dedicated/Dedicated | ELB - API Traffic                         |
+          +                     +-------------------------------------------+
|          |                     | ELB - Application Traffic                 |
+----------+---------------------+-------------------------------------------+
| 4444/TCP | Red Hat/Operations  | ELB - API Traffic - Authentication        |
+          +---------------------+-------------------------------------------+
|          | Red Hat/Staging     | Elastic IP - API Traffic - Authentication |
+          +---------------------+-------------------------------------------+
|          | Dedicated/Dedicated | ELB - API Traffic - Authentication        |
+----------+---------------------+-------------------------------------------+
| 22/TCP   | Red Hat/Management  | Elastic IP - SSH Bastion                  |
+----------+---------------------+-------------------------------------------+

Communications internal to the nodes occur in the network address space defined by VPC subnets.

Platform View
-------------
The platform view describes the OCP architecture at the platform level.  This view abastracts out the AWS components and focuses primarily on the functional components of OCP.

PaaS Definition - NIST 800-145
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The capability provided to the consumer is to deploy onto the cloud infrastructure consumer-created or acquired applications created using programming languages, libraries, services, and tools supported by the provider.  The consumer does not manage or control the underlying cloud infrastructure including network, servers, operating systems, or storage, but has control over the deployed applications and possibly configuration settings for the application-hosting environment.

Description
~~~~~~~~~~~
The OpenShift Container Platform provides application developer's the ability to rappidly deploy applications in a variety of application frameworks.

Stakeholders
~~~~~~~~~~~~
**OCP Administrators** are responsible for the operations and proper function of the platform.  They have the ability to affect OCP security policies surrounding developer interaction and container function.

**Application Developers** have access to the OCP WebUI and CLI to deploy applications.

**Application Users** do not have a role at the platform level.

Diagram
~~~~~~~
The following diagram details the minimum highly-available configuration of OCP to meet FISMA high at the platform level.
|Platform View|

Components
~~~~~~~~~~
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Component           | Description                                                                                                                                                                                                                                                                                                       |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Master              | The OCP Master provides the API and WebUI entry points for Application Developers and OCP administrators. The OCP Master is also responsible for scheduling containers on each node.                                                                                                                              |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ETCD                | The ETCD servers are key-value stores used for maintaining information about the state of the OCP cluster.                                                                                                                                                                                                        |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Application Node    | The Application Nodes handle executing application containers.                                                                                                                                                                                                                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Infrastructure Node | In an OCP cluster, a containerized HA proxy routes application traffic.  A containerized integrated container registry in OCP is a mechanism in the automated build and deployment flow.  Both the application router and integrated container registry and only these components run on the Infrastructure Node. |
+---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Network Architecture
~~~~~~~~~~~~~~~~~~~~~
The network architecture in the platform view is broken into two parts.  The first is the internal networking from between the EC2 instances supporting the platorm.  The second is the software defined networking layer enabling multi-tenant deployment of container based applications.

The following diagram illustrates the internetworking of the platform components of OCP.

|Platform Network|

The following table describes the port information of the internal platform components.

+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| From                        | To                           | Port            | Notes                                                                                                                                                                                                                                      |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Application Traffic ELB     | OCP Infrastructure Node      | 443/TCP         |                                                                                                                                                                                                                                            |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| API Traffic ELB             | HA and Authentication Proxy  | 8443/TCP        |                                                                                                                                                                                                                                            |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HA and Authentication Proxy | OCP Master                   | 8443/TCP        |                                                                                                                                                                                                                                            |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OCP Master                  | OCP Master and Loop          | 8053/TCP        | Required for DNS resolution of clustered services.                                                                                                                                                                                         |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OCP Master                  | OCP Master and Loop          | 8053/UDP        | Required for DNS resolution of clustered services.                                                                                                                                                                                         |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OCP Master                  | OCP Master                   | 2379/TCP        | Used for standalone etcd (clustered) to accept changes in state.                                                                                                                                                                           |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OCP Master                  | OCP Master                   | 2380/TCP        | etcd requires this port be open between masters for leader election and peering connections when using standalone etcd (clustered).                                                                                                        |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OCP Master                  | OCP Node                     | 4789/UDP        | Required for SDN communication between pods on separate hosts.                                                                                                                                                                             |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OCP Master                  | OCP Node                     | 10250/TCP       | The master proxies to node hosts via the Kubelet for oc commands.                                                                                                                                                                          |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OCP Node                    | OCP Master                   | 4789/UDP        | Required for SDN communication between pods on separate hosts.                                                                                                                                                                             |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OCP Node                    | OCP Master                   | 8053/TCP        | Required for DNS resolution of clustered services.                                                                                                                                                                                         |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OCP Node                    | OCP Master                   | 8053/UDP        | Required for DNS resolution of clustered services.                                                                                                                                                                                         |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OCP Node                    | OCP Master                   | 8443/TCP        |                                                                                                                                                                                                                                            |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| All                         | Package Repository           | 443/TCP         |                                                                                                                                                                                                                                            |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OCP Node                    | Trusted Container Repository | 443/TCP         |                                                                                                                                                                                                                                            |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Bastion                     | All                          | 22/TCP          | SSH                                                                                                                                                                                                                                        |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ansible Tower               | All                          | 22/TCP          | SSH used during Ansible Plays                                                                                                                                                                                                              |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OCP Node                    | Gluster Node                 | 49152-49251/TCP | For client communication with Red Hat Gluster Storage 2.1 and for brick processes depending on the availability of the ports. The total number of ports required to be open depends on the total number of bricks exported on the machine. |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Gluster Node                | Gluster Node                 | 24007/TCP       | For glusterd (for management).                                                                                                                                                                                                             |
+-----------------------------+------------------------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

In order to achieve network traffic isolation between containers owned by different tenants running on the same node, the traffic must be encapsulated.  This capability is provided by OpenVSwitch which encapsulates the OSI L2 traffic from the containers in the L3 traffic between the nodes.  The packets are then tagged by an 24 bit value known as a VXLan Network Identifier (VNID).  A VNID corresponds to a project space in OCP and is transparent to both the **Application Developer** and **Application User**.  In order to utilize this option the *redhat/openshift-ovs-multitenant* must be selected during the installation.

The L3 traffic between nodes is sent as UDP packets to port 4789.

More information on the `software defined network`_ in OCP can be found in the online documentation.

Storage Architecture
~~~~~~~~~~~~~~~~~~~~
**Gluster**
Managing storage is a distinct problem from managing compute resources. OpenShift Container Platform leverages the Kubernetes persistent volume (PV) framework to allow administrators to provision persistent storage for a cluster. Using persistent volume claims (PVCs), developers can request PV resources without having specific knowledge of the underlying storage infrastructure.

In this reference architecture, storage services are provided through a managed storage tier, implemented by Red Hat Gluster Storage (Gluster).  Gluster provides a fault-tolerant and highly available network storage resource, efficiently rationed to tenant applications as PVs.  Since the storage interface to developers is managed by the Kubernetes PVC resource, the details of the underlying storage implementation are abstracted.

PVCs are specific to a project and are created and used by developers as a means to use a PV. PV resources on their own are not scoped to any single project; they can be shared across the entire OpenShift Container Platform cluster and claimed from any project. After a PV has been bound to a PVC, however, that PV cannot then be bound to additional PVCs. This has the effect of scoping a bound PV to a single namespace (that of the binding project).

The Gluster storage services are provided through a dedicated cluster of AWS instances within the scope of the platform VPC.  Administrators allocate storage resources, creating a pool of available PVs in standard sizes, and monitor the capacity of the underlying storage resources.  As PVs are released, administrators ensure the deletion and reclaimation of storage resources, returning capacity to the pool of available PVs.

Gluster complies with data protecture requirements through secure configuration of the storage resources and transport protols.  At rest, data is protected by LUKS encryption of the of the AWS EBS devices.  This ensures that access to EBS volumes or snapshots by unauthorized mechanisms are unable to extract any usable information from the storage tier.  During transit, information is protected through configuration of SSL connections, and enforcement of mutually authenticated TLS connections.

Application View
----------------
Definition
~~~~~~~~~~
Description
~~~~~~~~~~~
Actors
~~~~~~
Diagram
~~~~~~~
Architecture Rational
~~~~~~~~~~~~~~~~~~~~~

Container View
--------------
Definition
~~~~~~~~~~
Description
~~~~~~~~~~~
Actors
~~~~~~
Diagram
~~~~~~~
Architecture Rational
~~~~~~~~~~~~~~~~~~~~~

.. _NIST 800-145: http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf
.. _FISMA: http://csrc.nist.gov/drivers/documents/FISMA-final.pdf
.. _NIST 800-53: https://web.nvd.nist.gov/view/800-53/home
.. _software defined network: https://docs.openshift.com/container-platform/3.3/architecture/additional_concepts/sdn.html

.. |Infrastructure View| image:: /images/architecture/InfrastructureView.png
.. |Platform View| image:: /images/architecture/PlatformView.png
.. |Platform Network| image:: /images/architecture/PlatformNetwork.png
