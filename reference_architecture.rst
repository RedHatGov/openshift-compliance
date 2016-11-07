.. _reference_architecture:

*********************
Reference Architeture
*********************
Introduction
============
The reference architecture details, at various levels of abstraction, a
deployment of Red Hat's OpenShift Container Platform (OCP) deployed on Amazon Web Services (AWS).  The NIST *Definition of Cloud Computing* `NIST 800-145`_ succinctly describes different cloud service models and the attributes of a cloud platform.  The architecture described herein follows the definitions found in the NIST 800-145.  For example, Red Hat's OCP is a Platform-as-a-Service (PaaS) under NIST 800-145.  Similarly, AWS is an Infrastrucutre-as-a-Service (IaaS) per the NIST definition.

Security Standards
------------------
The Fedral Information Security Modernization Act (`FISMA`_), originally enacted in 2002, directs United States Federal Agencies to develop and implement programs to implement information and information systems security.  This reference architecture aims to describe an OCP deployment on AWS as FISMA high: high confidentiality, high integrity, high availability.

In order to demonstrate FISMA high, this architecture is traced to `NIST 800-53`_ *Security and Privacy Controls for Federal Information Systems and Organizations*.  The NIST 800-53 provides a catalog of controls accross multiple categories.  Many controls relate to organizational processes.  These controls will be mapped as appropriate.  The controls that are technical in nature are addressed by this architecture.

Architecture
============

Infrastructure View
-------------------

Platform View
-------------

Application View
----------------

.. _NIST 800-145: http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf
.. _FISMA: http://csrc.nist.gov/drivers/documents/FISMA-final.pdf
.. _NIST 800-53: https://web.nvd.nist.gov/view/800-53/home
