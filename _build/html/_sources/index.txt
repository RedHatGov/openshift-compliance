.. _index:

##############################
The OpenShift Compliance Guide
##############################

********
Overview
********

OpenShift is a container management platform based on Docker_ containers and the
Kubernetes_ container cluster manager. OpenShift adds developer and operational
centric tools to enable rapid application development, easy deployment and
scaling, and long-term lifecycle maintenance for small and large teams and
applications.

Built atop Red Hat Enterprise Linux (RHEL_), OpenShift is very secure. For users
who must comply with the Federal Information Security Management Act (FISMA_),
there is additional configuration burden.

This guide can help you secure your OpenShift cluster to comply with the FISMA
moderate confidentiality, integrity, and availability requirements.

While the configurations and Security Control Traceability Matrix (SCTM)
documented in this guide could be implemented in any environment, the
:ref:`reference_architecture` is `Amazon Web Services`_.

*****************
Table of Contents
*****************
#. :ref:`fisma`
#. :ref:`reference_architecture`
#. :ref:`security_controls`
#. :ref:`ansible`
#. :ref:`continuous_compliance`
#. :ref:`ssp_template`
#. :ref:`template_poam`

**************************
Frequently Asked Questions
**************************

Have questions? Visit our :ref:`faq`.

************
Contributing
************

Security is an ongoing effort, and we appreciate any feedback or recommendations
 that you may have. Please use this project's `GitHub <https://github.com/jason-callaway/openshift-compliance>`_
 page to submit issues or pull requests.


.. _Docker: https://www.openshift.com/container-platform/containers.html
.. _Kubernetes: https://www.openshift.com/container-platform/kubernetes.html
.. _RHEL: https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux
.. _FISMA: https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act_of_2002
.. _`Amazon Web Services`: https://aws.amazon.com/
