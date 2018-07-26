.. _crm:

******************************
Customer Responsibility Matrix
******************************

Overview
========

The following controls have been down-selected from the complete list
in :ref:`control`.

Procedural Generation
---------------------

Like the last chapter, this chapter is automatically generated from the `master_sctm.xlsx`_
spreadsheet on this project's `GitHub`_. Do not edit it directly. If you'd
like to change how this chapter is rendered, refer to the following:

+--------------------------+--------------------------------------------------+
| File                     | Description                                      |
+==========================+==================================================+
| `master_sctm_parser.py`_ | Python program that parses the master_sctm.xlsx  |
|                          | spreadsheet using the openpyxl module. Whe       |
|                          | editing this sheet do not change the existing    |
|                          | column headers. Column order does not matter.    |
|                          | New columns can be added. Only visible rows are  |
|                          | processed, so auto-filters can be used to modify |
|                          | which controls are rendered.                     |
+--------------------------+--------------------------------------------------+
| `security_control.j2`_   | `Jinja2`_ template that is used to render this   |
|                          | chapter.                                         |
+--------------------------+--------------------------------------------------+
| `crm.j2`_                | `Jinja2`_ template that is used to generate the  |
|                          | :ref:`crm`.                                      |
+--------------------------+--------------------------------------------------+




CM-8(4) - Information System Component Inventory | Accountability Information
==============================================================================================================================================================

:Requirement:
    INFORMATION SYSTEM COMPONENT INVENTORY | ACCOUNTABILITY INFORMATION The organization includes in the information system component inventory information, a means for identifying by [Selection (one or more): name; position; role], individuals responsible/accountable for administering those components.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

CM-8(4) What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM COMPONENT INVENTORY | ACCOUNTABILITY INFORMATION The organization includes in the information system component inventory information, a means for identifying by [Selection (one or more): name; position; role], individuals responsible/accountable for administering those components.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    Specified in the individual project / program's System Security Plan.








CP-10(2) - Information System Recovery And Reconstitution | Transaction Recovery
==============================================================================================================================================================

:Requirement:
    INFORMATION SYSTEM RECOVERY AND RECONSTITUTION | TRANSACTION RECOVERY The information system implements transaction recovery for systems that are transaction-based.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    Tenant SSP

CP-10(2) What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM RECOVERY AND RECONSTITUTION | TRANSACTION RECOVERY The information system implements transaction recovery for systems that are transaction-based.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined








DI-1 - Data Quality
==============================================================================================================================================================

:Requirement:
    DATA QUALITY Control: The organization: a. Confirms to the greatest extent practicable upon collection or creation of personally identifiable information (PII), the accuracy, relevance, timeliness, and completeness of that information; b. Collects PII directly from the individual to the greatest extent practicable; c. Checks for, and corrects as necessary, any inaccurate or outdated PII used by its programs or systems [Assignment: organization-defined frequency]; and d. Issues guidelines ensuring and maximizing the quality, utility, objectivity, and integrity of disseminated information.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

DI-1 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    DATA QUALITY Control: The organization: a. Confirms to the greatest extent practicable upon collection or creation of personally identifiable information (PII), the accuracy, relevance, timeliness, and completeness of that information;
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (c) and (e); Treasury and General Government Appropriations Act for Fiscal Year 2001 (P.L. 106-554), app C § 515, 114 Stat. 2763A-153-4; Paperwork Reduction Act, 44 U.S.C. § 3501; OMB Guidelines for Ensuring and Maximizing the Quality, Objectivity, Utility, and Integrity of Information Disseminated by Federal Agencies (October 2001); OMB M-07-16;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Collects PII directly from the individual to the greatest extent practicable;
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (c) and (e); Treasury and General Government Appropriations Act for Fiscal Year 2001 (P.L. 106-554), app C § 515, 114 Stat. 2763A-153-4; Paperwork Reduction Act, 44 U.S.C. § 3501; OMB Guidelines for Ensuring and Maximizing the Quality, Objectivity, Utility, and Integrity of Information Disseminated by Federal Agencies (October 2001); OMB M-07-16;




Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Checks for, and corrects as necessary, any inaccurate or outdated PII used by its programs or systems [Assignment: organization-defined frequency]; and
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (c) and (e); Treasury and General Government Appropriations Act for Fiscal Year 2001 (P.L. 106-554), app C § 515, 114 Stat. 2763A-153-4; Paperwork Reduction Act, 44 U.S.C. § 3501; OMB Guidelines for Ensuring and Maximizing the Quality, Objectivity, Utility, and Integrity of Information Disseminated by Federal Agencies (October 2001); OMB M-07-16;




Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Issues guidelines ensuring and maximizing the quality, utility, objectivity, and integrity of disseminated information.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (c) and (e); Treasury and General Government Appropriations Act for Fiscal Year 2001 (P.L. 106-554), app C § 515, 114 Stat. 2763A-153-4; Paperwork Reduction Act, 44 U.S.C. § 3501; OMB Guidelines for Ensuring and Maximizing the Quality, Objectivity, Utility, and Integrity of Information Disseminated by Federal Agencies (October 2001); OMB M-07-16;








DI-1(1) - Data Quality | Validate Pii
==============================================================================================================================================================

:Requirement:
    DATA QUALITY | VALIDATE PII The organization requests that the individual or individual’s authorized representative validate PII during the collection process.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

DI-1(1) What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    DATA QUALITY | VALIDATE PII The organization requests that the individual or individual’s authorized representative validate PII during the collection process.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined








DI-1(2) - Data Quality | Re-validate Pii
==============================================================================================================================================================

:Requirement:
    DATA QUALITY | RE-VALIDATE PII The organization requests that the individual or individual’s authorized representative revalidate that PII collected is still accurate [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

DI-1(2) What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    DATA QUALITY | RE-VALIDATE PII The organization requests that the individual or individual’s authorized representative revalidate that PII collected is still accurate [Assignment: organization-defined frequency].
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined








DI-2 - Data Integrity And Data Integrity Board
==============================================================================================================================================================

:Requirement:
    DATA INTEGRITY AND DATA INTEGRITY BOARD Control: The organization: a. Documents processes to ensure the integrity of personally identifiable information (PII) through existing security controls; and b. Establishes a Data Integrity Board when appropriate to oversee organizational Computer Matching Agreements123 and to ensure that those agreements comply with the computer matching provisions of the Privacy Act.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

DI-2 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    DATA INTEGRITY AND DATA INTEGRITY BOARD Control: The organization: a. Documents processes to ensure the integrity of personally identifiable information (PII) through existing security controls; and
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. §§ 552a (a)(8)(A), (o), (p), (u); OMB Circular A-130, Appendix I;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Establishes a Data Integrity Board when appropriate to oversee organizational Computer Matching Agreements123 and to ensure that those agreements comply with the computer matching provisions of the Privacy Act.
:Role:
    Organization
:Status:
    Inherited
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. §§ 552a (a)(8)(A), (o), (p), (u); OMB Circular A-130, Appendix I;








DM-1 - Minimization Of Personally Identifiable Information
==============================================================================================================================================================

:Requirement:
    MINIMIZATION OF PERSONALLY IDENTIFIABLE INFORMATION Control: The organization: a. Identifies the minimum personally identifiable information (PII) elements that are relevant and necessary to accomplish the legally authorized purpose of collection; b. Limits the collection and retention of PII to the minimum elements identified for the purposes described in the notice and for which the individual has provided consent; and c. Conducts an initial evaluation of PII holdings and establishes and follows a schedule for regularly reviewing those holdings [Assignment: organization-defined frequency, at least annually] to ensure that only PII identified in the notice is collected and retained, and that the PII continues to be necessary to accomplish the legally authorized purpose.


Control Summary Information
---------------------------

:Role:
    Organization
:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

DM-1 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    MINIMIZATION OF PERSONALLY IDENTIFIABLE INFORMATION Control: The organization: a. Identifies the minimum personally identifiable information (PII) elements that are relevant and necessary to accomplish the legally authorized purpose of collection;
:Role:
    Organization
:Status:
    Inherited
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. §552a (e); Section 208(b), E-Government Act of 2002 (P.L. 107-347); OMB M-03-22; OMB M-07-16;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Limits the collection and retention of PII to the minimum elements identified for the purposes described in the notice and for which the individual has provided consent; and
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. §552a (e); Section 208(b), E-Government Act of 2002 (P.L. 107-347); OMB M-03-22; OMB M-07-16;




Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Conducts an initial evaluation of PII holdings and establishes and follows a schedule for regularly reviewing those holdings [Assignment: organization-defined frequency, at least annually] to ensure that only PII identified in the notice is collected and retained, and that the PII continues to be necessary to accomplish the legally authorized purpose.
:Role:
    Organization
:Status:
    Inherited
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. §552a (e); Section 208(b), E-Government Act of 2002 (P.L. 107-347); OMB M-03-22; OMB M-07-16;








DM-2 - Data Retention And Disposal
==============================================================================================================================================================

:Requirement:
    DATA RETENTION AND DISPOSAL Control: The organization: a. Retains each collection of personally identifiable information (PII) for [Assignment: organization-defined time period] to fulfill the purpose(s) identified in the notice or as required by law; b. Disposes of, destroys, erases, and/or anonymizes the PII, regardless of the method of storage, in accordance with a NARA-approved record retention schedule and in a manner that prevents loss, theft, misuse, or unauthorized access; and c. Uses [Assignment: organization-defined techniques or methods] to ensure secure deletion or destruction of PII (including originals, copies, and archived records).


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

DM-2 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    DATA RETENTION AND DISPOSAL Control: The organization: a. Retains each collection of personally identifiable information (PII) for [Assignment: organization-defined time period] to fulfill the purpose(s) identified in the notice or as required by law;
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (e)(1), (c)(2); Section 208 (e), E-Government Act of 2002 (P.L. 107-347); 44 U.S.C. Chapters 29, 31, 33; OMB M-07-16; OMB Circular A-130; SP 800-88;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Disposes of, destroys, erases, and/or anonymizes the PII, regardless of the method of storage, in accordance with a NARA-approved record retention schedule and in a manner that prevents loss, theft, misuse, or unauthorized access; and
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (e)(1), (c)(2); Section 208 (e), E-Government Act of 2002 (P.L. 107-347); 44 U.S.C. Chapters 29, 31, 33; OMB M-07-16; OMB Circular A-130; SP 800-88;




Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Uses [Assignment: organization-defined techniques or methods] to ensure secure deletion or destruction of PII (including originals, copies, and archived records).
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (e)(1), (c)(2); Section 208 (e), E-Government Act of 2002 (P.L. 107-347); 44 U.S.C. Chapters 29, 31, 33; OMB M-07-16; OMB Circular A-130; SP 800-88;








DM-2(1) - Data Retention And Disposal | System Configuration
==============================================================================================================================================================

:Requirement:
    DATA RETENTION AND DISPOSAL | SYSTEM CONFIGURATION The organization, where feasible, configures its information systems to record the date PII is collected, created, or updated and when PII is to be deleted or archived under an approved record retention schedule.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

DM-2(1) What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    DATA RETENTION AND DISPOSAL | SYSTEM CONFIGURATION The organization, where feasible, configures its information systems to record the date PII is collected, created, or updated and when PII is to be deleted or archived under an approved record retention schedule.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined








DM-3 - Minimization Of Pii Used In Testing, Training, And Research
==============================================================================================================================================================

:Requirement:
    MINIMIZATION OF PII USED IN TESTING, TRAINING, AND RESEARCH Control: The organization: a. Develops policies and procedures that minimize the use of personally identifiable information (PII) for testing, training, and research; and b. Implements controls to protect PII used for testing, training, and research.


Control Summary Information
---------------------------

:Role:
    Organization
:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

DM-3 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    MINIMIZATION OF PII USED IN TESTING, TRAINING, AND RESEARCH Control: The organization: a. Develops policies and procedures that minimize the use of personally identifiable information (PII) for testing, training, and research; and
:Role:
    Organization
:Status:
    Inherited
:Details:
    undefined
:References:
    SP 800-122




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Implements controls to protect PII used for testing, training, and research.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    SP 800-122








IP-1 - Consent
==============================================================================================================================================================

:Requirement:
    CONSENT Control: The organization: a. Provides means, where feasible and appropriate, for individuals to authorize the collection, use, maintaining, and sharing of personally identifiable information (PII) prior to its collection; b. Provides appropriate means for individuals to understand the consequences of decisions to approve or decline the authorization of the collection, use, dissemination, and retention of PII; c. Obtains consent, where feasible and appropriate, from individuals prior to any new uses or disclosure of previously collected PII; and d. Ensures that individuals are aware of and, where feasible, consent to all uses of PII not initially described in the public notice that was in effect at the time the organization collected the PII.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

IP-1 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    CONSENT Control: The organization: a. Provides means, where feasible and appropriate, for individuals to authorize the collection, use, maintaining, and sharing of personally identifiable information (PII) prior to its collection;
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (b), (e)(3); Section 208(c), E-Government Act of 2002 (P.L. 107-347); OMB M-03-22; OMB M-10-22;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Provides appropriate means for individuals to understand the consequences of decisions to approve or decline the authorization of the collection, use, dissemination, and retention of PII;
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (b), (e)(3); Section 208(c), E-Government Act of 2002 (P.L. 107-347); OMB M-03-22; OMB M-10-22;




Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Obtains consent, where feasible and appropriate, from individuals prior to any new uses or disclosure of previously collected PII; and
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (b), (e)(3); Section 208(c), E-Government Act of 2002 (P.L. 107-347); OMB M-03-22; OMB M-10-22;




Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Ensures that individuals are aware of and, where feasible, consent to all uses of PII not initially described in the public notice that was in effect at the time the organization collected the PII.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (b), (e)(3); Section 208(c), E-Government Act of 2002 (P.L. 107-347); OMB M-03-22; OMB M-10-22;








IP-1(1) - Consent | Mechanisms Supporting Itemized Or Tiered Consent
==============================================================================================================================================================

:Requirement:
    CONSENT | MECHANISMS SUPPORTING ITEMIZED OR TIERED CONSENT The organization implements mechanisms to support itemized or tiered consent for specific uses of data.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

IP-1(1) What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    CONSENT | MECHANISMS SUPPORTING ITEMIZED OR TIERED CONSENT The organization implements mechanisms to support itemized or tiered consent for specific uses of data.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined








IP-2 - Individual Access
==============================================================================================================================================================

:Requirement:
    INDIVIDUAL ACCESS Control: The organization: a. Provides individuals the ability to have access to their personally identifiable information (PII) maintained in its system(s) of records; b. Publishes rules and regulations governing how individuals may request access to records maintained in a Privacy Act system of records; c. Publishes access procedures in System of Records Notices (SORNs); and d. Adheres to Privacy Act requirements and OMB policies and guidance for the proper processing of Privacy Act requests.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

IP-2 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INDIVIDUAL ACCESS Control: The organization: a. Provides individuals the ability to have access to their personally identifiable information (PII) maintained in its system(s) of records;
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. §§ 552a (c)(3), (d)(5), (e) (4), (j), (k), (t); OMB Circular A-130;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Publishes rules and regulations governing how individuals may request access to records maintained in a Privacy Act system of records;
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. §§ 552a (c)(3), (d)(5), (e) (4), (j), (k), (t); OMB Circular A-130;




Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Publishes access procedures in System of Records Notices (SORNs); and
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. §§ 552a (c)(3), (d)(5), (e) (4), (j), (k), (t); OMB Circular A-130;




Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Adheres to Privacy Act requirements and OMB policies and guidance for the proper processing of Privacy Act requests.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. §§ 552a (c)(3), (d)(5), (e) (4), (j), (k), (t); OMB Circular A-130;








IP-3 - Redress
==============================================================================================================================================================

:Requirement:
    REDRESS Control: The organization: a. Provides a process for individuals to have inaccurate personally identifiable information (PII) maintained by the organization corrected or amended, as appropriate; and b. Establishes a process for disseminating corrections or amendments of the PII to other authorized users of the PII, such as external information-sharing partners and, where feasible and appropriate, notifies affected individuals that their information has been corrected or amended.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

IP-3 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    REDRESS Control: The organization: a. Provides a process for individuals to have inaccurate personally identifiable information (PII) maintained by the organization corrected or amended, as appropriate; and
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (d), (c)(4); OMB Circular A-130;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Establishes a process for disseminating corrections or amendments of the PII to other authorized users of the PII, such as external information-sharing partners and, where feasible and appropriate, notifies affected individuals that their information has been corrected or amended.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (d), (c)(4); OMB Circular A-130;








IP-4 - Complaint Management
==============================================================================================================================================================

:Requirement:
    COMPLAINT MANAGEMENT Control: The organization implements a process for receiving and responding to complaints, concerns, or questions from individuals about the organizational privacy practices.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

IP-4 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    COMPLAINT MANAGEMENT Control: The organization implements a process for receiving and responding to complaints, concerns, or questions from individuals about the organizational privacy practices.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    OMB Circular A-130; OMB M-07-16; OMB M-08-09;








IP-4(1) - Complaint Management | Response Times
==============================================================================================================================================================

:Requirement:
    COMPLAINT MANAGEMENT | RESPONSE TIMES The organization responds to complaints, concerns, or questions from individuals within [Assignment: organization-defined time period].


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

IP-4(1) What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    COMPLAINT MANAGEMENT | RESPONSE TIMES The organization responds to complaints, concerns, or questions from individuals within [Assignment: organization-defined time period].
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined








MA-1 - System Maintenance Policy And Procedures
==============================================================================================================================================================

:Requirement:
    SYSTEM MAINTENANCE POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A system maintenance policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and 2. Procedures to facilitate the implementation of the system maintenance policy and associated system maintenance controls; and b. Reviews and updates the current: 1. System maintenance policy [Assignment: organization-defined frequency]; and 2. System maintenance procedures [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Origin:
    Tenant SSP

MA-1 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SYSTEM MAINTENANCE POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A system maintenance policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.
:References:
    SP 800-12; SP 800-100;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the system maintenance policy and associated system maintenance controls; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.
:References:
    SP 800-12; SP 800-100;




Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. System maintenance policy [Assignment: organization-defined frequency]; and
:Role:
    Organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization.
:References:
    SP 800-12; SP 800-100;




Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. System maintenance procedures [Assignment: organization-defined frequency].
:Role:
    Organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization.
:References:
    SP 800-12; SP 800-100;








PL-2 - System Security Plan
==============================================================================================================================================================

:Requirement:
    SYSTEM SECURITY PLAN Control: The organization: a. Develops a security plan for the information system that: 1. Is consistent with the organization’s enterprise architecture; 2. Explicitly defines the authorization boundary for the system; 3. Describes the operational context of the information system in terms of missions and business processes; 4. Provides the security categorization of the information system including supporting rationale; 5. Describes the operational environment for the information system and relationships with or connections to other information systems; 6. Provides an overview of the security requirements for the system; 7. Identifies any relevant overlays, if applicable; 8. Describes the security controls in place or planned for meeting those requirements including a rationale for the tailoring and supplementation decisions; and 9. Is reviewed and approved by the authorizing official or designated representative prior to plan implementation; b. Distributes copies of the security plan and communicates subsequent changes to the plan to [Assignment: organization-defined personnel or roles]; c. Reviews the security plan for the information system [Assignment: organization-defined frequency]; d. Updates the plan to address changes to the information system/environment of operation or problems identified during plan implementation or security control assessments; and e. Protects the security plan from unauthorized disclosure and modification.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Origin:
    Tenant SSP

PL-2 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SYSTEM SECURITY PLAN Control: The organization: a. Develops a security plan for the information system that: 1. Is consistent with the organization’s enterprise architecture;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    SP 800-18;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Explicitly defines the authorization boundary for the system;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    SP 800-18;




Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    3. Describes the operational context of the information system in terms of missions and business processes;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    SP 800-18;




Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    4. Provides the security categorization of the information system including supporting rationale;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    SP 800-18;




Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    5. Describes the operational environment for the information system and relationships with or connections to other information systems;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    SP 800-18;




Part f
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    6. Provides an overview of the security requirements for the system;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    SP 800-18;




Part g
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    7. Identifies any relevant overlays, if applicable;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    SP 800-18;




Part h
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    8. Describes the security controls in place or planned for meeting those requirements including a rationale for the tailoring and supplementation decisions; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    SP 800-18;




Part i
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    9. Is reviewed and approved by the authorizing official or designated representative prior to plan implementation;
:Role:
    Organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization.
:References:
    SP 800-18;




Part j
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Distributes copies of the security plan and communicates subsequent changes to the plan to [Assignment: organization-defined personnel or roles];
:Role:
    Organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization.
:References:
    SP 800-18;




Part k
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Reviews the security plan for the information system [Assignment: organization-defined frequency];
:Role:
    Organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization.
:References:
    SP 800-18;




Part l
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Updates the plan to address changes to the information system/environment of operation or problems identified during plan implementation or security control assessments; and
:Role:
    Organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization.
:References:
    SP 800-18;




Part m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    e. Protects the security plan from unauthorized disclosure and modification.
:Role:
    Organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization.
:References:
    SP 800-18;








RA-1 - Risk Assessment Policy And Procedures
==============================================================================================================================================================

:Requirement:
    RISK ASSESSMENT POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A risk assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and 2. Procedures to facilitate the implementation of the risk assessment policy and associated risk assessment controls; and b. Reviews and updates the current: 1. Risk assessment policy [Assignment: organization-defined frequency]; and 2. Risk assessment procedures [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Origin:
    Tenant SSP

RA-1 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    RISK ASSESSMENT POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A risk assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    SP 800-12; SP 800-30; SP 800-100;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the risk assessment policy and associated risk assessment controls; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    SP 800-12; SP 800-30; SP 800-100;




Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. Risk assessment policy [Assignment: organization-defined frequency]; and
:Role:
    Organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization.
:References:
    SP 800-12; SP 800-30; SP 800-100;




Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Risk assessment procedures [Assignment: organization-defined frequency].
:Role:
    Organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization.
:References:
    SP 800-12; SP 800-30; SP 800-100;








RA-3 - Risk Assessment
==============================================================================================================================================================

:Requirement:
    RISK ASSESSMENT Control: The organization: a. Conducts an assessment of risk, including the likelihood and magnitude of harm, from the unauthorized access, use, disclosure, disruption, modification, or destruction of the information system and the information it processes, stores, or transmits; b. Documents risk assessment results in [Selection: security plan; risk assessment report; [Assignment: organization-defined document]]; c. Reviews risk assessment results [Assignment: organization-defined frequency]; d. Disseminates risk assessment results to [Assignment: organization-defined personnel or roles]; and e. Updates the risk assessment [Assignment: organization-defined frequency] or whenever there are significant changes to the information system or environment of operation (including the identification of new threats and vulnerabilities), or other conditions that may impact the security state of the system.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Origin:
    Tenant SSP

RA-3 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    RISK ASSESSMENT Control: The organization: a. Conducts an assessment of risk, including the likelihood and magnitude of harm, from the unauthorized access, use, disclosure, disruption, modification, or destruction of the information system and the information it processes, stores, or transmits;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    OMB M-04-04; SP 800-30; SP 800-39; Web: idmanagement.gov;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Documents risk assessment results in [Selection: security plan; risk assessment report; [Assignment: organization-defined document]];
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    OMB M-04-04; SP 800-30; SP 800-39; Web: idmanagement.gov;




Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Reviews risk assessment results [Assignment: organization-defined frequency];
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    OMB M-04-04; SP 800-30; SP 800-39; Web: idmanagement.gov;




Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Disseminates risk assessment results to [Assignment: organization-defined personnel or roles]; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    OMB M-04-04; SP 800-30; SP 800-39; Web: idmanagement.gov;




Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    e. Updates the risk assessment [Assignment: organization-defined frequency] or whenever there are significant changes to the information system or environment of operation (including the identification of new threats and vulnerabilities), or other conditions that may impact the security state of the system.
:Role:
    Organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization.
:References:
    OMB M-04-04; SP 800-30; SP 800-39; Web: idmanagement.gov;








SA-11 - Developer Security Testing And Evaluation
==============================================================================================================================================================

:Requirement:
    DEVELOPER SECURITY TESTING AND EVALUATION Control: The organization requires the developer of the information system, system component, or information system service to: a. Create and implement a security assessment plan; b. Perform [Selection (one or more): unit; integration; system; regression] testing/evaluation at [Assignment: organization-defined depth and coverage]; c. Produce evidence of the execution of the security assessment plan and the results of the security testing/evaluation; d. Implement a verifiable flaw remediation process; and e. Correct flaws identified during security testing/evaluation.


Control Summary Information
---------------------------

:Role:
    Organization
:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SA-11 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    DEVELOPER SECURITY TESTING AND EVALUATION Control: The organization requires the developer of the information system, system component, or information system service to: a. Create and implement a security assessment plan;
:Role:
    Organization
:Status:
    Inherited
:Details:
    Documented in the project's System Test Plan.
:References:
    ISO/IEC 15408; SP 800-53A; Web: nvd.nist.gov, cwe.mitre.org, cve.mitre.org, capec.mitre.org;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Perform [Selection (one or more): unit; integration; system; regression] testing/evaluation at [Assignment: organization-defined depth and coverage];
:Role:
    Organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization.
:References:
    ISO/IEC 15408; SP 800-53A; Web: nvd.nist.gov, cwe.mitre.org, cve.mitre.org, capec.mitre.org;




Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Produce evidence of the execution of the security assessment plan and the results of the security testing/evaluation;
:Role:
    Organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization.
:References:
    ISO/IEC 15408; SP 800-53A; Web: nvd.nist.gov, cwe.mitre.org, cve.mitre.org, capec.mitre.org;




Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Implement a verifiable flaw remediation process; and
:Role:
    OpenShift Landlord, OpenShift Tenant
:Status:
    Planned
:Details:
    Documented in the POAM created as a result of vulnerability scanning.
:References:
    ISO/IEC 15408; SP 800-53A; Web: nvd.nist.gov, cwe.mitre.org, cve.mitre.org, capec.mitre.org;




Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    e. Correct flaws identified during security testing/evaluation.
:Role:
    OpenShift Landlord, OpenShift Tenant
:Status:
    Planned
:Details:
    Documented in the POAM created as a result of vulnerability scanning.
:References:
    ISO/IEC 15408; SP 800-53A; Web: nvd.nist.gov, cwe.mitre.org, cve.mitre.org, capec.mitre.org;








SA-3 - System Development Life Cycle
==============================================================================================================================================================

:Requirement:
    SYSTEM DEVELOPMENT LIFE CYCLE Control: The organization: a. Manages the information system using [Assignment: organization-defined system development life cycle] that incorporates information security considerations; b. Defines and documents information security roles and responsibilities throughout the system development life cycle; c. Identifies individuals having information security roles and responsibilities; and d. Integrates the organizational information security risk management process into system development life cycle activities.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Origin:
    Tenant SSP

SA-3 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SYSTEM DEVELOPMENT LIFE CYCLE Control: The organization: a. Manages the information system using [Assignment: organization-defined system development life cycle] that incorporates information security considerations;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    SP 800-37; SP 800-64;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Defines and documents information security roles and responsibilities throughout the system development life cycle;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    SP 800-37; SP 800-64;




Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Identifies individuals having information security roles and responsibilities; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    SP 800-37; SP 800-64;




Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Integrates the organizational information security risk management process into system development life cycle activities.
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.
:References:
    SP 800-37; SP 800-64;








SA-4(1) - Acquisition Process | Functional Properties Of Security Controls
==============================================================================================================================================================

:Requirement:
    ACQUISITION PROCESS | FUNCTIONAL PROPERTIES OF SECURITY CONTROLS The organization requires the developer of the information system, system component, or information system service to provide a description of the functional properties of the security controls to be employed.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Origin:
    Tenant SSP

SA-4(1) What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    ACQUISITION PROCESS | FUNCTIONAL PROPERTIES OF SECURITY CONTROLS The organization requires the developer of the information system, system component, or information system service to provide a description of the functional properties of the security controls to be employed.
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.








SA-4(2) - Acquisition Process | Design / Implementation Information For Security Controls
==============================================================================================================================================================

:Requirement:
    ACQUISITION PROCESS | DESIGN / IMPLEMENTATION INFORMATION FOR SECURITY CONTROLS The organization requires the developer of the information system, system component, or information system service to provide design and implementation information for the security controls to be employed that includes: [Selection (one or more): security-relevant external system interfaces; high-level design; low-level design; source code or hardware schematics; [Assignment: organization-defined design/implementation information]] at [Assignment: organization-defined level of detail].


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Origin:
    Tenant SSP

SA-4(2) What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    ACQUISITION PROCESS | DESIGN / IMPLEMENTATION INFORMATION FOR SECURITY CONTROLS The organization requires the developer of the information system, system component, or information system service to provide design and implementation information for the security controls to be employed that includes: [Selection (one or more): security-relevant external system interfaces; high-level design; low-level design; source code or hardware schematics; [Assignment: organization-defined design/implementation information]] at [Assignment: organization-defined level of detail].
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.








SE-1 - Inventory Of Personally Identifiable Information
==============================================================================================================================================================

:Requirement:
    INVENTORY OF PERSONALLY IDENTIFIABLE INFORMATION Control: The organization: a. Establishes, maintains, and updates [Assignment: organization-defined frequency] an inventory that contains a listing of all programs and information systems identified as collecting, using, maintaining, or sharing personally identifiable information (PII); and b. Provides each update of the PII inventory to the CIO or information security official [Assignment: organization-defined frequency] to support the establishment of information security requirements for all new or modified information systems containing PII.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

SE-1 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INVENTORY OF PERSONALLY IDENTIFIABLE INFORMATION Control: The organization: a. Establishes, maintains, and updates [Assignment: organization-defined frequency] an inventory that contains a listing of all programs and information systems identified as collecting, using, maintaining, or sharing personally identifiable information (PII); and
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (e) (10); Section 208(b)(2), E-Government Act of 2002 (P.L. 107-347); OMB M-03-22; OMB Circular A-130, Appendix I; FIPS Pub 199; SP 800-37; SP 800-122;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Provides each update of the PII inventory to the CIO or information security official [Assignment: organization-defined frequency] to support the establishment of information security requirements for all new or modified information systems containing PII.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (e) (10); Section 208(b)(2), E-Government Act of 2002 (P.L. 107-347); OMB M-03-22; OMB Circular A-130, Appendix I; FIPS Pub 199; SP 800-37; SP 800-122;








SI-1 - System And Information Integrity Policy And Procedures
==============================================================================================================================================================

:Requirement:
    SYSTEM AND INFORMATION INTEGRITY POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A system and information integrity policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and 2. Procedures to facilitate the implementation of the system and information integrity policy and associated system and information integrity controls; and b. Reviews and updates the current: 1. System and information integrity policy [Assignment: organization-defined frequency]; and 2. System and information integrity procedures [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Origin:
    Tenant SSP

SI-1 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SYSTEM AND INFORMATION INTEGRITY POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A system and information integrity policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.
:References:
    SP 800-12; SP 800-100;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the system and information integrity policy and associated system and information integrity controls; and
:Role:
    Shared
:Status:
    Shared
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.
:References:
    SP 800-12; SP 800-100;




Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. System and information integrity policy [Assignment: organization-defined frequency]; and
:Role:
    Shared
:Status:
    Shared
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.
:References:
    SP 800-12; SP 800-100;




Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. System and information integrity procedures [Assignment: organization-defined frequency].
:Role:
    Shared
:Status:
    Shared
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.
:References:
    SP 800-12; SP 800-100;








TR-1 - Privacy Notice
==============================================================================================================================================================

:Requirement:
    PRIVACY NOTICE Control: The organization: a. Provides effective notice to the public and to individuals regarding: (i) its activities that impact privacy, including its collection, use, sharing, safeguarding, maintenance, and disposal of personally identifiable information (PII); (ii) authority for collecting PII; (iii) the choices, if any, individuals may have regarding how the organization uses PII and the consequences of exercising or not exercising those choices; and (iv) the ability to access and have PII amended or corrected if necessary; b. Describes: (i) the PII the organization collects and the purpose(s) for which it collects that information; (ii) how the organization uses PII internally; (iii) whether the organization shares PII with external entities, the categories of those entities, and the purposes for such sharing; (iv) whether individuals have the ability to consent to specific uses or sharing of PII and how to exercise any such consent; (v) how individuals may obtain access to PII; and (vi) how the PII will be protected; and c. Revises its public notices to reflect changes in practice or policy that affect PII or changes in its activities that impact privacy, before or as soon as practicable after the change.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

TR-1 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    PRIVACY NOTICE Control: The organization: a. Provides effective notice to the public and to individuals regarding: (i) its activities that impact privacy, including its collection, use, sharing, safeguarding, maintenance, and disposal of personally identifiable information (PII); (ii) authority for collecting PII; (iii) the choices, if any, individuals may have regarding how the organization uses PII and the consequences of exercising or not exercising those choices; and (iv) the ability to access and have PII amended or corrected if necessary;
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (e)(3), (e)(4); Section 208(b), E-Government Act of 2002 (P.L. 107-347); OMB M-03-22; OMB M-07-16; OMB M-10-22; OMB M-10-23; ISE Privacy Guidelines;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Describes: (i) the PII the organization collects and the purpose(s) for which it collects that information; (ii) how the organization uses PII internally; (iii) whether the organization shares PII with external entities, the categories of those entities, and the purposes for such sharing; (iv) whether individuals have the ability to consent to specific uses or sharing of PII and how to exercise any such consent; (v) how individuals may obtain access to PII; and (vi) how the PII will be protected; and
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (e)(3), (e)(4); Section 208(b), E-Government Act of 2002 (P.L. 107-347); OMB M-03-22; OMB M-07-16; OMB M-10-22; OMB M-10-23; ISE Privacy Guidelines;




Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Revises its public notices to reflect changes in practice or policy that affect PII or changes in its activities that impact privacy, before or as soon as practicable after the change.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (e)(3), (e)(4); Section 208(b), E-Government Act of 2002 (P.L. 107-347); OMB M-03-22; OMB M-07-16; OMB M-10-22; OMB M-10-23; ISE Privacy Guidelines;








TR-1(1) - Privacy Notice | Real-time Or Layered Notice
==============================================================================================================================================================

:Requirement:
    PRIVACY NOTICE | REAL-TIME OR LAYERED NOTICE The organization provides real-time and/or layered notice when it collects PII.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

TR-1(1) What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    PRIVACY NOTICE | REAL-TIME OR LAYERED NOTICE The organization provides real-time and/or layered notice when it collects PII.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined








TR-2 - System Of Records Notices And Privacy Act Statements
==============================================================================================================================================================

:Requirement:
    SYSTEM OF RECORDS NOTICES AND PRIVACY ACT STATEMENTS Control: The organization: a. Publishes System of Records Notices (SORNs) in the Federal Register, subject to required oversight processes, for systems containing personally identifiable information (PII); b. Keeps SORNs current; and c. Includes Privacy Act Statements on its forms that collect PII, or on separate forms that can be retained by individuals, to provide additional formal notice to individuals from whom the information is being collected.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

TR-2 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SYSTEM OF RECORDS NOTICES AND PRIVACY ACT STATEMENTS Control: The organization: a. Publishes System of Records Notices (SORNs) in the Federal Register, subject to required oversight processes, for systems containing personally identifiable information (PII);
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (e)(3); OMB Circular A-130;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Keeps SORNs current; and
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (e)(3); OMB Circular A-130;




Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Includes Privacy Act Statements on its forms that collect PII, or on separate forms that can be retained by individuals, to provide additional formal notice to individuals from whom the information is being collected.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (e)(3); OMB Circular A-130;








TR-2(1) - System Of Records Notices And Privacy Act Statements | Public Website Publication
==============================================================================================================================================================

:Requirement:
    SYSTEM OF RECORDS NOTICES AND PRIVACY ACT STATEMENTS | PUBLIC WEBSITE PUBLICATION The organization publishes SORNs on its public website.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

TR-2(1) What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SYSTEM OF RECORDS NOTICES AND PRIVACY ACT STATEMENTS | PUBLIC WEBSITE PUBLICATION The organization publishes SORNs on its public website.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined








TR-3 - Dissemination Of Privacy Program Information
==============================================================================================================================================================

:Requirement:
    DISSEMINATION OF PRIVACY PROGRAM INFORMATION Control: The organization: a. Ensures that the public has access to information about its privacy activities and is able to communicate with its Senior Agency Official for Privacy (SAOP)/Chief Privacy Officer (CPO); and b. Ensures that its privacy practices are publicly available through organizational websites or otherwise.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

TR-3 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    DISSEMINATION OF PRIVACY PROGRAM INFORMATION Control: The organization: a. Ensures that the public has access to information about its privacy activities and is able to communicate with its Senior Agency Official for Privacy (SAOP)/Chief Privacy Officer (CPO); and
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a; Section 208, E-Government Act of 2002 (P.L. 107-347); OMB M-03-22; OMB M-10-23;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Ensures that its privacy practices are publicly available through organizational websites or otherwise.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a; Section 208, E-Government Act of 2002 (P.L. 107-347); OMB M-03-22; OMB M-10-23;








UL-1 - Internal Use
==============================================================================================================================================================

:Requirement:
    INTERNAL USE Control: The organization uses personally identifiable information (PII) internally only for the authorized purpose(s) identified in the Privacy Act and/or in public notices.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

UL-1 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INTERNAL USE Control: The organization uses personally identifiable information (PII) internally only for the authorized purpose(s) identified in the Privacy Act and/or in public notices.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (b)(1);








UL-2 - Information Sharing With Third Parties
==============================================================================================================================================================

:Requirement:
    INFORMATION SHARING WITH THIRD PARTIES Control: The organization: a. Shares personally identifiable information (PII) externally, only for the authorized purposes identified in the Privacy Act and/or described in its notice(s) or for a purpose that is compatible with those purposes; b. Where appropriate, enters into Memoranda of Understanding, Memoranda of Agreement, Letters of Intent, Computer Matching Agreements, or similar agreements, with third parties that specifically describe the PII covered and specifically enumerate the purposes for which the PII may be used; c. Monitors, audits, and trains its staff on the authorized sharing of PII with third parties and on the consequences of unauthorized use or sharing of PII; and d. Evaluates any proposed new instances of sharing PII with third parties to assess whether the sharing is authorized and whether additional or new public notice is required.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant
:Status:
    Planned
:Origin:
    OpenShift Tenant SSP

UL-2 What is the solution and how is it implemented?
-------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SHARING WITH THIRD PARTIES Control: The organization: a. Shares personally identifiable information (PII) externally, only for the authorized purposes identified in the Privacy Act and/or described in its notice(s) or for a purpose that is compatible with those purposes;
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (a)(7), (b), (c), (e)(3)(C), (o); ISE Privacy Guidelines;




Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Where appropriate, enters into Memoranda of Understanding, Memoranda of Agreement, Letters of Intent, Computer Matching Agreements, or similar agreements, with third parties that specifically describe the PII covered and specifically enumerate the purposes for which the PII may be used;
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (a)(7), (b), (c), (e)(3)(C), (o); ISE Privacy Guidelines;




Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Monitors, audits, and trains its staff on the authorized sharing of PII with third parties and on the consequences of unauthorized use or sharing of PII; and
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (a)(7), (b), (c), (e)(3)(C), (o); ISE Privacy Guidelines;




Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Evaluates any proposed new instances of sharing PII with third parties to assess whether the sharing is authorized and whether additional or new public notice is required.
:Role:
    OpenShift Tenant
:Status:
    Planned
:Details:
    undefined
:References:
    The Privacy Act of 1974, 5 U.S.C. § 552a (a)(7), (b), (c), (e)(3)(C), (o); ISE Privacy Guidelines;









.. _`NIST SP800-53r4`: http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf
.. _`master_sctm.xlsx`: https://github.com/jason-callaway/openshift-compliance/raw/master/master_sctm.xlsx
.. _`GitHub`: https://github.com/jason-callaway/openshift-compliance
.. _`FedRAMP SSP Template`: http://www.gsa.gov/graphics/staffoffices/System_Security_Plan_Template_072312_508.docx
.. _`master_sctm_parser.py`: https://github.com/jason-callaway/openshift-compliance/blob/master/master_sctm_parser.py
.. _`security_control.j2`: https://github.com/jason-callaway/openshift-compliance/blob/master/security_control.j2
.. _`crm.j2`: https://github.com/jason-callaway/openshift-compliance/blob/master/crm.j2
.. _`Jinja2`: http://jinja.pocoo.org/docs/dev/