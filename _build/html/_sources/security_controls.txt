.. _security_controls:

*****************
Security Controls
*****************

A security control is any safeguard or countermeasure that minimizes the risk of
security incident. There are technical and non-technical controls. The latter
are outside the scope of this document.

NIST Special Publication 800-53
###############################

In Revision 4 of the `Security and Privacy Controls for Federal Information
Systems and Organizations <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>`_,
security controls are broken down into "Control Families." The following
sections detail control families with technical controls that can be implemeted
by OpenShift and its certified images.

Security Control Traceability Matrix
####################################

TODO: break down by control family... full matrix is 18MB


Access Control
**************

AC-2 Set Password Minimum Digit Characters
==========================================

AC-2 Set Password Minimum Lowercase Characters
==============================================

AC-2 Set Password Minimum Special Characters
============================================

AC-2 Set Password Minimum Uppercase Characters
==============================================

AC-2 Set Password Strength Minimum Different Characters
=======================================================

AC-2(2),AC-2(3) Set Account Expiration Following Inactivity
===========================================================

AC-2(5) Set SSH Idle Timeout Interval
=====================================

AC-3 Disable Interactive Boot
=============================

AC-3(10) Add Audit Rules
========================

AC-3, AC-17(2) Use Only Approved Ciphers
========================================

AC-3,AC-3(3),AC-4,AC-6 Enable SELinux
=====================================

AC-3,AC-3(3),AC-6 Ensure SELinux Not Disabled in /etc/grub.conf
===============================================================

AC-3,AC-3(3),AC-6 Ensure SELinux Not Disabled in /etc/grub2.conf
================================================================

AC-4 Disable Kernel Parameter for Accepting ICMP Redirects By Default
=====================================================================

AC-4 Disable Kernel Parameter for Accepting Secure Redirects By Default
=======================================================================

AC-4 Disable Kernel Parameter for Accepting Secure Redirects for All Interfaces
===============================================================================

AC-4 Disable Kernel Parameter for Accepting Source-Routed Packets By Default
============================================================================

AC-4 Disable Kernel Parameter for Sending ICMP Redirects by Default
===================================================================

AC-4 Enable Kernel Parameter to Use Reverse Path Filtering by Default
=====================================================================

AC-4 Enable Kernel Parameter to Use Reverse Path Filtering for All Interfaces
=============================================================================

AC-4 Enable Kernel Parameter to Use TCP Syncookies
==================================================

AC-6 Check ownership and permissions on /etc/group
==================================================

AC-6 Check ownership and permissions on /etc/passwd
===================================================

AC-6 Check ownership and permissions on /etc/shadow
===================================================

AC-6 Set Daemon Umask
=====================

AC-6 System Audit Logs Must Have Mode 0640 or Less Permissive
=============================================================

AC-6 Verify Only Root Has UID 0
===============================

AC-6 Verify that Shared Library Files Have Restrictive Permissions
==================================================================

AC-6 Verify that System Executables Have Restrictive Permissions
================================================================

AC-6 Verify that System Executables Have Root Ownership
=======================================================

AC-6(2) Restrict Serial Port Root Logins
========================================

AC-6(2) Restrict Virtual Console Root Logins
============================================

AC-6(8) Ensure that System Accounts Do Not Run a Shell Upon Login
=================================================================

AC-7(a) Set Deny, Lockout Time, and Interval Count For Failed Password Attempts in /etc/pam.d/password-auth
===========================================================================================================

AC-7(a) Set Deny, Lockout Time, and Interval Count For Failed Password Attempts in /etc/pam.d/system-auth
=========================================================================================================

AC-8(a),AC-8(b),AC-(c) Enable SSH Warning Banner
================================================

AC-8(a),AC-8(b),AC-(c) Modify the System Login Banner
=====================================================

AC-9 System Audit Logs Must Have Mode 0640 or Less Permissive
=============================================================

AC-10 Limit the Number of Concurrent Login Sessions Allowed Per User
====================================================================

AC-17 Install openswan or libreswan Package
===========================================

AC-17(2),68,2450
================

AC-17(7) Enable Kernel Parameter to Log Martian Packets
=======================================================

AC-17(8) Remove Rsh Trust Files
===============================

AC-17(8) Uninstall Unnecessary Package
======================================

AC-18(a),AC-18(d),AC-18(3) Disable Bluetooth Kernel Modules
===========================================================

AC-19(a), AC-19(d), AC-19(e) Disable Modprobe Loading of USB Storage Driver - Ensure usb-storage.conf is present
================================================================================================================

AC-19(a),AC-19(d),AC-19(e),AC-17(8)  Stop and disable services
==============================================================

Audit and Accountability
************************

AU-1(b), AU-2(a), AU-2(c), AU-2(d), AU-12(a), AU-12(c) Add Audit Rules
======================================================================

AU-1(b), AU-4, AU-5(b) Configure auditd admin_space_left Action on Low Disk Space
=================================================================================

AU-1(b), AU-4, AU-5(b) Configure auditd space_left Action on Low Disk Space
===========================================================================

AU-1(b), AU-9 System Audit Logs Must Have Mode 0640 or Less Permissive
======================================================================

AU-6,AU-1(b),AU-9 System Audit Logs Must Have Mode 0640 or Less Permissive
==========================================================================

AU-9 Enable SELinux
===================

AU-9 Ensure SELinux Not Disabled in /etc/grub{2}.conf
=====================================================


Configuration Management
************************

CM-2(1)(b), 366 Enable X11 Forwarding
=====================================

CM-3(d),CM-3(e),CM-6(d),CM-6(3) Copy AIDE Database
==================================================

CM-3(d),CM-3(e),CM-6(d),CM-6(3) Install AIDE
============================================

CM-3(d),CM-3(e),CM-6(d),CM-6(3) Schedule AIDE
=============================================

CM-7 Stop and disable rhnsd
===========================

CM-7 Add nodev, nosuid, noguid Options to /dev/sh
=================================================

CM-7 Disable Accepting IPv6 Redirects
=====================================

CM-7 Disable DCCP Support
=========================

CM-7 Disable IPv6 Networking Support Automatic Loading
======================================================

CM-7 Disable Kernel Parameter for Accepting ICMP Redirects By Default
=====================================================================

CM-7 Disable Kernel Parameter for Accepting ICMP Redirects for All Interfaces
=============================================================================

CM-7 Disable Kernel Parameter for Accepting Secure Redirects By Default
=======================================================================

CM-7 Disable Kernel Parameter for Accepting Secure Redirects for All Interfaces
===============================================================================

CM-7 Disable Kernel Parameter for Accepting Source-Routed Packets By Default
============================================================================

CM-7 Disable Kernel Parameter for Accepting Source-Routed Packets for All Interfaces
====================================================================================

CM-7 Disable Kernel Parameter for IP Forwarding
===============================================

CM-7 Disable Kernel Parameter for Sending ICMP Redirects by Default
===================================================================

CM-7 Disable Kernel Parameter for Sending ICMP Redirects for All Interfaces
===========================================================================

CM-7 Disable RDS Support
========================

CM-7 Disable SCTP Support
=========================

CM-7 Disable TIPC Support
=========================

CM-7 Enable Chrony Service (chrony)
===================================

CM-7 Enable Kernel Parameter to Ignore Bogus ICMP Error Responses
=================================================================

CM-7 Enable Kernel Parameter to Ignore ICMP Broadcast Echo Requests
===================================================================

CM-7 Enable Kernel Parameter to Log Martian Packets
===================================================

CM-7 Enable NTP Service (ntpd)
==============================

CM-7 Install Chrony Service
===========================

CM-7 Install NTP Service
========================

CM-7 Remove Rsh Trust Files - /etc/hosts.equiv
==============================================

CM-7 Remove Rsh Trust Files - ~/.rhosts
=======================================

CM-7 Set SELinux to Enforcing
=============================

CM-7 Stop and disable services
==============================

CM-7 Uninstall Unnecessary Packages
===================================


Identification and Authentication
*********************************

IA-2(1) Ensure that System Accounts Do Not Run a Shell Upon Login
=================================================================

IA-2(1) Require Authentication for Single User Mode
===================================================

IA-2(1) Verify Only Root Has UID 0
==================================

IA-5 Set Password Minimum Digit Characters
==========================================

IA-5 Set Password Minimum Lowercase Characters
==============================================

IA-5 Set Password Minimum Special Characters
============================================

IA-5 Set Password Minimum Uppercase Characters
==============================================

IA-5 Set Password Strength Minimum Different Characters
=======================================================

IA-5(1)(c) Allow Only SSH Protocol 2
====================================

IA-5(1)(c),IA-7 Use Only Approved Ciphers
=========================================

IA-5(b),IA-5(c),IA-5(1)  Prevent Log In to Accounts With Empty Password - /etc/pam.d/system-auth
================================================================================================

IA-5(b),IA-5(c),IA-5(1)(a)  Set Password Strength - /etc/pam.d/password-auth
============================================================================

IA-5(b),IA-5(c),IA-5(1)(a) Prevent Log In to Accounts With Empty Password - /etc/pam.d/password-auth
====================================================================================================

IA-5(b),IA-5(c),IA-5(1)(a) Set Password Strength - /etc/pam.d/password-auth
===========================================================================

IA-5(b),IA-5(c),IA-5(1)(a) Set Password Strength - /etc/pam.d/system-auth
=========================================================================

IA-5(f) Set Password Warning Age
================================

IA-5(f), IA-5(1)(e) Limit Password Reuse
========================================

IA-5(f),IA-5(1)(a) Set Password Minimum Length
==============================================

IA-5(f),IA-5(1)(d) Set Password Minimum Age
===========================================

IA-5(f),IA-5(g),IA-5(1)(d) Set Password Maximum Age
===================================================

IA-5(h) Verify All Account Password Hashes are Shadowed - /etc/passwd
=====================================================================

IA-5(h) Verify All Account Password Hashes are Shadowed - /etc/shadow
=====================================================================

IA-5, 195 RHEL-07-010140
========================

IA-5, IA-5(c), 195 RHEL-07-010150
=================================

IA-5,IA-5(c),195 RHEL-07-010160
===============================

IR-5 Configure auditd admin_space_left Action on Low Disk Space
===============================================================

IR-5 Configure auditd space_left Action on Low Disk Space
=========================================================

IR-5 System Audit Logs Must Have Mode 0640 or Less Permissive
=============================================================


Maintenance
***********

MA-1(b) Ensure Red Hat GPG Key Installed
========================================

MA-1(b) Ensure gpgcheck Enabled For All Yum Package Repositories
================================================================

MA-1(b) Ensure gpgcheck Enabled In Main Yum Configuration
=========================================================

MA-4 Install openswan or libreswan Package
==========================================


Media Protection
****************

MP-2 Add nodev, nosuid, noguid Options to /dev/sh
=================================================


System and Communications Protection
************************************

SC-2 Disable Interactive Boot
=============================

SC-5 Disable Core Dumps for All Users
=====================================

SC-5 Disable Kernel Parameter for IP Forwarding
===============================================

SC-5 Enable Kernel Parameter to Ignore Bogus ICMP Error Responses
=================================================================

SC-5 Enable Kernel Parameter to Ignore ICMP Broadcast Echo Requests
===================================================================

SC-5(3) Enable Kernel Parameter to Log Martian Packets
======================================================

SC-5,SC-7 Disable Kernel Parameter for Accepting ICMP Redirects By Default
==========================================================================

SC-5,SC-7 Disable Kernel Parameter for Accepting Secure Redirects By Default
============================================================================

SC-5,SC-7 Disable Kernel Parameter for Accepting Source-Routed Packets By Default
=================================================================================

SC-5,SC-7 Disable Kernel Parameter for Sending ICMP Redirects by Default
========================================================================

SC-5,SC-7 Enable Kernel Parameter to Use Reverse Path Filtering by Default
==========================================================================

SC-5,SC-7 Enable Kernel Parameter to Use Reverse Path Filtering for All Interfaces
==================================================================================


System and Information Integrity
********************************

SI-7 Ensure Red Hat GPG Key Installed
=====================================

SI-7 Ensure gpgcheck Enabled For All Yum Package Repositories
=============================================================

SI-7 Ensure gpgcheck Enabled In Main Yum Configuration
======================================================

SI-7 Use Only Approved Ciphers
==============================

SI-11 Ensure System Log Files Have Correct Permissions
======================================================


System and Services Acquisition
*******************************

SA-8 Change cshell umask
========================

SA-8 Change default bash umask
==============================

SA-8 Change default umask
=========================

SA-8 Set SSH Idle Timeout Interval
==================================

SA-8 Set SSH Maximum Number of Client Connections
=================================================
