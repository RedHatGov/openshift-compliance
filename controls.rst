.. _control:

*****************
Security Controls
*****************

Overview
========

These security controls comply with FISMA High requirements as defined by `NIST SP800-53r4`_. Omitted controls are not required.

This chapter is automatically generated from the `master_sctm.xlsx`_ spreadsheet on this project's `GitHub`_.


AC-1 - Access Control Policy And Procedures
================================================================================

:Requirement:
    ACCESS CONTROL POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. An access control policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and 2. Procedures to facilitate the implementation of the access control policy and associated access controls; and b. Reviews and updates the current: 1. Access control policy [Assignment: organization-defined frequency]; and 2. Access control procedures [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    Shared

:Status:
    Implemented
:Origin:
    Inherited from pre-existing ATO

AC-1 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    ACCESS CONTROL POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. An access control policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    Shared
:Status:
    Implemented
:Details:
    Developed and maintained by the agency. The program will comply with the policy as published.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the access control policy and associated access controls; and
:Role:
    Shared
:Status:
    Implemented
:Details:
    Developed and maintained by the agency. The program will comply with the policy as published.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. Access control policy [Assignment: organization-defined frequency]; and
:Role:
    Shared
:Status:
    Implemented
:Details:
    Developed and maintained by the agency. The program will comply with the policy as published.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Access control procedures [Assignment: organization-defined frequency].
:Role:
    Shared
:Status:
    Implemented
:Details:
    Developed and maintained by the agency. The program will comply with the policy as published.







AC-10 - Concurrent Session Control
================================================================================

:Requirement:
    CONCURRENT SESSION CONTROL Control: The information system limits the number of concurrent sessions for each [Assignment: organization-defined account and/or account type] to [Assignment: organization-defined number].


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

AC-10 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    CONCURRENT SESSION CONTROL Control: The information system limits the number of concurrent sessions for each [Assignment: organization-defined account and/or account type] to [Assignment: organization-defined number].
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







AC-2(5) - Inactivity Logout
================================================================================

:Requirement:
    ACCOUNT MANAGEMENT | INACTIVITY LOGOUT The organization requires that users log out when [Assignment: organization-defined time-period of expected inactivity or description of when to log out].


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

AC-2(5) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    ACCOUNT MANAGEMENT | INACTIVITY LOGOUT The organization requires that users log out when [Assignment: organization-defined time-period of expected inactivity or description of when to log out].
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    undefined







AC-7 - Unsuccessful Logon Attempts
================================================================================

:Requirement:
    UNSUCCESSFUL LOGON ATTEMPTS Control: The information system: a. Enforces a limit of [Assignment: organization-defined number] consecutive invalid logon attempts by a user during a [Assignment: organization-defined time period]; and b. Automatically [Selection: locks the account/node for an [Assignment: organization-defined time period]; locks the account/node until released by an administrator; delays next logon prompt according to [Assignment: organization-defined delay algorithm]] when the maximum number of unsuccessful attempts is exceeded.


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Implemented
:Origin:
    OpenShift Landlord SSP

AC-7 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    UNSUCCESSFUL LOGON ATTEMPTS Control: The information system: a. Enforces a limit of [Assignment: organization-defined number] consecutive invalid logon attempts by a user during a [Assignment: organization-defined time period]; and
:Role:
    OpenShift Landlord
:Status:
    Implemented
:Details:
    Logins are done via PKI certificates and/or SSH keys. Invalid logins consist of the user not being authorized to login to the target gear, system or console and result in a rejected connection attempt. All rejected attempts are logged for review and provided to the continuous monitoring branch for review.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Automatically [Selection: locks the account/node for an [Assignment: organization-defined time period]; locks the account/node until released by an administrator; delays next logon prompt according to [Assignment: organization-defined delay algorithm]] when the maximum number of unsuccessful attempts is exceeded.
:Role:
    OpenShift Landlord
:Status:
    Implemented
:Details:
    See AC-7a







AT-1 - Security Awareness And Training Policy And Procedures
================================================================================

:Requirement:
    SECURITY AWARENESS AND TRAINING POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A security awareness and training policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and 2. Procedures to facilitate the implementation of the security awareness and training policy and associated security awareness and training controls; and b. Reviews and updates the current: 1. Security awareness and training policy [Assignment: organization-defined frequency]; and 2. Security awareness and training procedures [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

AT-1 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SECURITY AWARENESS AND TRAINING POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A security awareness and training policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the security awareness and training policy and associated security awareness and training controls; and
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. Security awareness and training policy [Assignment: organization-defined frequency]; and
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Security awareness and training procedures [Assignment: organization-defined frequency].
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







AT-2 - Security Awareness Training
================================================================================

:Requirement:
    SECURITY AWARENESS TRAINING Control: The organization provides basic security awareness training to information system users (including managers, senior executives, and contractors): a. As part of initial training for new users; b. When required by information system changes; and c. [Assignment: organization-defined frequency] thereafter.


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

AT-2 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SECURITY AWARENESS TRAINING Control: The organization provides basic security awareness training to information system users (including managers, senior executives, and contractors): a. As part of initial training for new users;
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. When required by information system changes; and
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. [Assignment: organization-defined frequency] thereafter.
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







AT-2(2) - Insider Threat
================================================================================

:Requirement:
    SECURITY AWARENESS | INSIDER THREAT The organization includes security awareness training on recognizing and reporting potential indicators of insider threat.


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

AT-2(2) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SECURITY AWARENESS | INSIDER THREAT The organization includes security awareness training on recognizing and reporting potential indicators of insider threat.
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







AT-3 - Role-based Security Training
================================================================================

:Requirement:
    ROLE-BASED SECURITY TRAINING Control: The organization provides role-based security training to personnel with assigned security roles and responsibilities: a. Before authorizing access to the information system or performing assigned duties; b. When required by information system changes; and c. [Assignment: organization-defined frequency] thereafter.


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

AT-3 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    ROLE-BASED SECURITY TRAINING Control: The organization provides role-based security training to personnel with assigned security roles and responsibilities: a. Before authorizing access to the information system or performing assigned duties;
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. When required by information system changes; and
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. [Assignment: organization-defined frequency] thereafter.
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







AT-3(2) - Physical Security Controls
================================================================================

:Requirement:
    SECURITY TRAINING | PHYSICAL SECURITY CONTROLS The organization provides [Assignment: organization-defined personnel or roles] with initial and [Assignment: organization-defined frequency] training in the employment and operation of physical security controls.


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

AT-3(2) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SECURITY TRAINING | PHYSICAL SECURITY CONTROLS The organization provides [Assignment: organization-defined personnel or roles] with initial and [Assignment: organization-defined frequency] training in the employment and operation of physical security controls.
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







AT-3(4) - Suspicious Communications And Anomalous System Behavior
================================================================================

:Requirement:
    SECURITY TRAINING | SUSPICIOUS COMMUNICATIONS AND ANOMALOUS SYSTEM BEHAVIOR The organization provides training to its personnel on [Assignment: organization-defined indicators of malicious code] to recognize suspicious communications and anomalous behavior in organizational information systems.


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

AT-3(4) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SECURITY TRAINING | SUSPICIOUS COMMUNICATIONS AND ANOMALOUS SYSTEM BEHAVIOR The organization provides training to its personnel on [Assignment: organization-defined indicators of malicious code] to recognize suspicious communications and anomalous behavior in organizational information systems.
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







AT-4 - Security Training Records
================================================================================

:Requirement:
    SECURITY TRAINING RECORDS Control: The organization: a. Documents and monitors individual information system security training activities including basic security awareness training and specific information system security training; and b. Retains individual training records for [Assignment: organization-defined time period].


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

AT-4 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SECURITY TRAINING RECORDS Control: The organization: a. Documents and monitors individual information system security training activities including basic security awareness training and specific information system security training; and
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Retains individual training records for [Assignment: organization-defined time period].
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







AU-1 - Audit And Accountability Policy And Procedures
================================================================================

:Requirement:
    AUDIT AND ACCOUNTABILITY POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. An audit and accountability policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and 2. Procedures to facilitate the implementation of the audit and accountability policy and associated audit and accountability controls; and b. Reviews and updates the current: 1. Audit and accountability policy [Assignment: organization-defined frequency]; and 2. Audit and accountability procedures [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

AU-1 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    AUDIT AND ACCOUNTABILITY POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. An audit and accountability policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Inherited from organizational audit policies.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the audit and accountability policy and associated audit and accountability controls; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    See AU-1a



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. Audit and accountability policy [Assignment: organization-defined frequency]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    See AU-1a



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Audit and accountability procedures [Assignment: organization-defined frequency].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    See AU-1a







AU-4(1) - Transfer To Alternate Storage
================================================================================

:Requirement:
    AUDIT STORAGE CAPACITY | TRANSFER TO ALTERNATE STORAGE The information system off-loads audit records [Assignment: organization-defined frequency] onto a different system or media than the system being audited.


Control Summary Information
---------------------------

:Role:
    Shared

:Status:
    Implemented
:Origin:
    OpenShift Landlord SSP

AU-4(1) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    AUDIT STORAGE CAPACITY | TRANSFER TO ALTERNATE STORAGE The information system off-loads audit records [Assignment: organization-defined frequency] onto a different system or media than the system being audited.
:Role:
    Shared
:Status:
    Implemented
:Details:
    Implemented by auditing subsystem and stored on system storage for the organizationally mandated length of time.







AU-9 - Protection Of Audit Information
================================================================================

:Requirement:
    PROTECTION OF AUDIT INFORMATION Control: The information system protects audit information and audit tools from unauthorized access, modification, and deletion.


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

AU-9 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    PROTECTION OF AUDIT INFORMATION Control: The information system protects audit information and audit tools from unauthorized access, modification, and deletion.
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







CA-1 - Security Assessment And Authorization Policy And Procedures
================================================================================

:Requirement:
    SECURITY ASSESSMENT AND AUTHORIZATION POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A security assessment and authorization policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and 2. Procedures to facilitate the implementation of the security assessment and authorization policy and associated security assessment and authorization controls; and b. Reviews and updates the current: 1. Security assessment and authorization policy [Assignment: organization-defined frequency]; and 2. Security assessment and authorization procedures [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

CA-1 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SECURITY ASSESSMENT AND AUTHORIZATION POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A security assessment and authorization policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Inherited from organizational IA policy.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the security assessment and authorization policy and associated security assessment and authorization controls; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Inherited from organizational IA policy.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. Security assessment and authorization policy [Assignment: organization-defined frequency]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Inherited from organizational IA policy.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Security assessment and authorization procedures [Assignment: organization-defined frequency].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Inherited from organizational IA policy.







CA-2 - Security Assessments
================================================================================

:Requirement:
    SECURITY ASSESSMENTS Control: The organization: a. Develops a security assessment plan that describes the scope of the assessment including: 1. Security controls and control enhancements under assessment; 2. Assessment procedures to be used to determine security control effectiveness; and 3. Assessment environment, assessment team, and assessment roles and responsibilities; b. Assesses the security controls in the information system and its environment of operation [Assignment: organization-defined frequency] to determine the extent to which the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting established security requirements; c. Produces a security assessment report that documents the results of the assessment; and d. Provides the results of the security control assessment to [Assignment: organization-defined individuals or roles].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

CA-2 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SECURITY ASSESSMENTS Control: The organization: a. Develops a security assessment plan that describes the scope of the assessment including: 1. Security controls and control enhancements under assessment;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Inherited from organizational IA policy.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Assessment procedures to be used to determine security control effectiveness; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Inherited from organizational IA policy.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    3. Assessment environment, assessment team, and assessment roles and responsibilities;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Inherited from organizational IA policy.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Assesses the security controls in the information system and its environment of operation [Assignment: organization-defined frequency] to determine the extent to which the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting established security requirements;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Inherited from organizational IA policy.



Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Produces a security assessment report that documents the results of the assessment; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Inherited from organizational IA policy.



Part f
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Provides the results of the security control assessment to [Assignment: organization-defined individuals or roles].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Inherited from organizational IA policy.







CA-2(1) - Independent Assessors
================================================================================

:Requirement:
    SECURITY ASSESSMENTS | INDEPENDENT ASSESSORS The organization employs assessors or assessment teams with [Assignment: organization-defined level of independence] to conduct security control assessments.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

CA-2(1) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SECURITY ASSESSMENTS | INDEPENDENT ASSESSORS The organization employs assessors or assessment teams with [Assignment: organization-defined level of independence] to conduct security control assessments.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    The security assessment is performed by the security assessor who is not part of the project team. The assessment and subsequent reports are generated by the assessor(s) with the cooperation and assistance as required from the project team.







CA-2(2) - Specialized Assessments
================================================================================

:Requirement:
    SECURITY ASSESSMENTS | SPECIALIZED ASSESSMENTS The organization includes as part of security control assessments, [Assignment: organization-defined frequency], [Selection: announced; unannounced], [Selection (one or more): in-depth monitoring; vulnerability scanning; malicious user testing; insider threat assessment; performance/load testing; [Assignment: organization-defined other forms of security assessment]].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

CA-2(2) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SECURITY ASSESSMENTS | SPECIALIZED ASSESSMENTS The organization includes as part of security control assessments, [Assignment: organization-defined frequency], [Selection: announced; unannounced], [Selection (one or more): in-depth monitoring; vulnerability scanning; malicious user testing; insider threat assessment; performance/load testing; [Assignment: organization-defined other forms of security assessment]].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    The framework will comply with the recommendations of the assessment by addressing the PoAMs created as a result of the assessment.







CA-5 - Plan Of Action And Milestones
================================================================================

:Requirement:
    PLAN OF ACTION AND MILESTONES Control: The organization: a. Develops a plan of action and milestones for the information system to document the organization’s planned remedial actions to correct weaknesses or deficiencies noted during the assessment of the security controls and to reduce or eliminate known vulnerabilities in the system; and b. Updates existing plan of action and milestones [Assignment: organization-defined frequency] based on the findings from security controls assessments, security impact analyses, and continuous monitoring activities.


Control Summary Information
---------------------------

:Role:
    Shared

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

CA-5 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    PLAN OF ACTION AND MILESTONES Control: The organization: a. Develops a plan of action and milestones for the information system to document the organization’s planned remedial actions to correct weaknesses or deficiencies noted during the assessment of the security controls and to reduce or eliminate known vulnerabilities in the system; and
:Role:
    Shared
:Status:
    Planned
:Details:
    Upon delivery of the report from the security assessor(s), a POAM document will be created and each item will be addressed with the: a) deficiency b) party responsible for remediation c) the estimated time to remediation and d) the current progress/status of the remediation.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Updates existing plan of action and milestones [Assignment: organization-defined frequency] based on the findings from security controls assessments, security impact analyses, and continuous monitoring activities.
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    The POAMs (as described in the response to CA-5a) will be updated as progress is made or on/before predetermined milestone.







CA-6 - Security Authorization
================================================================================

:Requirement:
    SECURITY AUTHORIZATION Control: The organization: a. Assigns a senior-level executive or manager as the authorizing official for the information system; b. Ensures that the authorizing official authorizes the information system for processing before commencing operations; and c. Updates the security authorization [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

CA-6 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SECURITY AUTHORIZATION Control: The organization: a. Assigns a senior-level executive or manager as the authorizing official for the information system;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Inherited from organizational IA policy.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Ensures that the authorizing official authorizes the information system for processing before commencing operations; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Inherited from organizational IA policy.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Updates the security authorization [Assignment: organization-defined frequency].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Inherited from organizational IA policy.







CA-7 - Continuous Monitoring
================================================================================

:Requirement:
    CONTINUOUS MONITORING Control: The organization develops a continuous monitoring strategy and implements a continuous monitoring program that includes: a. Establishment of [Assignment: organization-defined metrics] to be monitored; b. Establishment of [Assignment: organization-defined frequencies] for monitoring and [Assignment: organization-defined frequencies] for assessments supporting such monitoring; c. Ongoing security control assessments in accordance with the organizational continuous monitoring strategy; d. Ongoing security status monitoring of organization-defined metrics in accordance with the organizational continuous monitoring strategy; e. Correlation and analysis of security-related information generated by assessments and monitoring; f. Response actions to address results of the analysis of security-related information; and g. Reporting the security status of organization and the information system to [Assignment: organization-defined personnel or roles] [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

CA-7 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    CONTINUOUS MONITORING Control: The organization develops a continuous monitoring strategy and implements a continuous monitoring program that includes: a. Establishment of [Assignment: organization-defined metrics] to be monitored;
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Establishment of [Assignment: organization-defined frequencies] for monitoring and [Assignment: organization-defined frequencies] for assessments supporting such monitoring;
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Ongoing security control assessments in accordance with the organizational continuous monitoring strategy;
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Ongoing security status monitoring of organization-defined metrics in accordance with the organizational continuous monitoring strategy;
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    e. Correlation and analysis of security-related information generated by assessments and monitoring;
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part f
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    f. Response actions to address results of the analysis of security-related information; and
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part g
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    g. Reporting the security status of organization and the information system to [Assignment: organization-defined personnel or roles] [Assignment: organization-defined frequency].
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







CA-7(1) - Independent Assessment
================================================================================

:Requirement:
    CONTINUOUS MONITORING | INDEPENDENT ASSESSMENT The organization employs assessors or assessment teams with [Assignment: organization-defined level of independence] to monitor the security controls in the information system on an ongoing basis.


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

CA-7(1) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    CONTINUOUS MONITORING | INDEPENDENT ASSESSMENT The organization employs assessors or assessment teams with [Assignment: organization-defined level of independence] to monitor the security controls in the information system on an ongoing basis.
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







CP-1 - Contingency Planning Policy And Procedures
================================================================================

:Requirement:
    CONTINGENCY PLANNING POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A contingency planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and 2. Procedures to facilitate the implementation of the contingency planning policy and associated contingency planning controls; and b. Reviews and updates the current: 1. Contingency planning policy [Assignment: organization-defined frequency]; and 2. Contingency planning procedures [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

CP-1 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    CONTINGENCY PLANNING POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A contingency planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the contingency planning policy and associated contingency planning controls; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. Contingency planning policy [Assignment: organization-defined frequency]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Contingency planning procedures [Assignment: organization-defined frequency].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







CP-7 - Alternate Processing Site
================================================================================

:Requirement:
    ALTERNATE PROCESSING SITE Control: The organization: a. Establishes an alternate processing site including necessary agreements to permit the transfer and resumption of [Assignment: organization-defined information system operations] for essential missions/business functions within [Assignment: organization-defined time period consistent with recovery time and recovery point objectives] when the primary processing capabilities are unavailable; b. Ensures that equipment and supplies required to transfer and resume operations are available at the alternate processing site or contracts are in place to support delivery to the site within the organization-defined time period for transfer/resumption; and c. Ensures that the alternate processing site provides information security safeguards equivalent to that of the primary site.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

CP-7 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    ALTERNATE PROCESSING SITE Control: The organization: a. Establishes an alternate processing site including necessary agreements to permit the transfer and resumption of [Assignment: organization-defined information system operations] for essential missions/business functions within [Assignment: organization-defined time period consistent with recovery time and recovery point objectives] when the primary processing capabilities are unavailable;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Ensures that equipment and supplies required to transfer and resume operations are available at the alternate processing site or contracts are in place to support delivery to the site within the organization-defined time period for transfer/resumption; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Ensures that the alternate processing site provides information security safeguards equivalent to that of the primary site.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







CP-9 - Information System Backup
================================================================================

:Requirement:
    INFORMATION SYSTEM BACKUP Control: The organization: a. Conducts backups of user-level information contained in the information system [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives]; b. Conducts backups of system-level information contained in the information system [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives]; c. Conducts backups of information system documentation including security-related documentation [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives]; and d. Protects the confidentiality, integrity, and availability of backup information at storage locations.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

CP-9 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM BACKUP Control: The organization: a. Conducts backups of user-level information contained in the information system [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Conducts backups of system-level information contained in the information system [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Conducts backups of information system documentation including security-related documentation [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Protects the confidentiality, integrity, and availability of backup information at storage locations.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-1 - Incident Response Policy And Procedures
================================================================================

:Requirement:
    INCIDENT RESPONSE POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. An incident response policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and 2. Procedures to facilitate the implementation of the incident response policy and associated incident response controls; and b. Reviews and updates the current: 1. Incident response policy [Assignment: organization-defined frequency]; and 2. Incident response procedures [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-1 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT RESPONSE POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. An incident response policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the incident response policy and associated incident response controls; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. Incident response policy [Assignment: organization-defined frequency]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Incident response procedures [Assignment: organization-defined frequency].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-10 - Integrated Information Security Analysis Team
================================================================================

:Requirement:
    INTEGRATED INFORMATION SECURITY ANALYSIS TEAM Control: The organization establishes an integrated team of forensic/malicious code analysts, tool developers, and real-time operations personnel.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-10 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INTEGRATED INFORMATION SECURITY ANALYSIS TEAM Control: The organization establishes an integrated team of forensic/malicious code analysts, tool developers, and real-time operations personnel.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-2 - Incident Response Training
================================================================================

:Requirement:
    INCIDENT RESPONSE TRAINING Control: The organization provides incident response training to information system users consistent with assigned roles and responsibilities: a. Within [Assignment: organization-defined time period] of assuming an incident response role or responsibility; b. When required by information system changes; and c. [Assignment: organization-defined frequency] thereafter.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-2 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT RESPONSE TRAINING Control: The organization provides incident response training to information system users consistent with assigned roles and responsibilities: a. Within [Assignment: organization-defined time period] of assuming an incident response role or responsibility;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. When required by information system changes; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. [Assignment: organization-defined frequency] thereafter.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-2(1) - Simulated Events
================================================================================

:Requirement:
    INCIDENT RESPONSE TRAINING | SIMULATED EVENTS The organization incorporates simulated events into incident response training to facilitate effective response by personnel in crisis situations.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-2(1) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT RESPONSE TRAINING | SIMULATED EVENTS The organization incorporates simulated events into incident response training to facilitate effective response by personnel in crisis situations.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-3 - Incident Response Testing
================================================================================

:Requirement:
    INCIDENT RESPONSE TESTING Control: The organization tests the incident response capability for the information system [Assignment: organization-defined frequency] using [Assignment: organization-defined tests] to determine the incident response effectiveness and documents the results.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-3 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT RESPONSE TESTING Control: The organization tests the incident response capability for the information system [Assignment: organization-defined frequency] using [Assignment: organization-defined tests] to determine the incident response effectiveness and documents the results.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-3(2) - Coordination With Related Plans
================================================================================

:Requirement:
    INCIDENT RESPONSE TESTING | COORDINATION WITH RELATED PLANS The organization coordinates incident response testing with organizational elements responsible for related plans.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-3(2) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT RESPONSE TESTING | COORDINATION WITH RELATED PLANS The organization coordinates incident response testing with organizational elements responsible for related plans.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-4 - Incident Handling
================================================================================

:Requirement:
    INCIDENT HANDLING Control: The organization: a. Implements an incident handling capability for security incidents that includes preparation, detection and analysis, containment, eradication, and recovery; b. Coordinates incident handling activities with contingency planning activities; and c. Incorporates lessons learned from ongoing incident handling activities into incident response procedures, training, and testing/exercises, and implements the resulting changes accordingly.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-4 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT HANDLING Control: The organization: a. Implements an incident handling capability for security incidents that includes preparation, detection and analysis, containment, eradication, and recovery;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Coordinates incident handling activities with contingency planning activities; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Incorporates lessons learned from ongoing incident handling activities into incident response procedures, training, and testing/exercises, and implements the resulting changes accordingly.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-4(1) - Automated Incident Handling Processes
================================================================================

:Requirement:
    INCIDENT HANDLING | AUTOMATED INCIDENT HANDLING PROCESSES The organization employs automated mechanisms to support the incident handling process.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-4(1) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT HANDLING | AUTOMATED INCIDENT HANDLING PROCESSES The organization employs automated mechanisms to support the incident handling process.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-4(3) - Continuity Of Operations
================================================================================

:Requirement:
    INCIDENT HANDLING | CONTINUITY OF OPERATIONS The organization identifies [Assignment: organization-defined classes of incidents] and [Assignment: organization-defined actions to take in response to classes of incidents] to ensure continuation of organizational missions and business functions.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-4(3) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT HANDLING | CONTINUITY OF OPERATIONS The organization identifies [Assignment: organization-defined classes of incidents] and [Assignment: organization-defined actions to take in response to classes of incidents] to ensure continuation of organizational missions and business functions.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-4(4) - Information Correlation
================================================================================

:Requirement:
    INCIDENT HANDLING | INFORMATION CORRELATION The organization correlates incident information and individual incident responses to achieve an organization-wide perspective on incident awareness and response.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-4(4) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT HANDLING | INFORMATION CORRELATION The organization correlates incident information and individual incident responses to achieve an organization-wide perspective on incident awareness and response.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-4(6) - Insider Threats - Specific Capabilities
================================================================================

:Requirement:
    INCIDENT HANDLING | INSIDER THREATS - SPECIFIC CAPABILITIES The organization implements incident handling capability for insider threats.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-4(6) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT HANDLING | INSIDER THREATS - SPECIFIC CAPABILITIES The organization implements incident handling capability for insider threats.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-4(7) - Insider Threats - Intra-organization Coordination
================================================================================

:Requirement:
    INCIDENT HANDLING | INSIDER THREATS - INTRA-ORGANIZATION COORDINATION The organization coordinates incident handling capability for insider threats across [Assignment: organization-defined components or elements of the organization].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-4(7) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT HANDLING | INSIDER THREATS - INTRA-ORGANIZATION COORDINATION The organization coordinates incident handling capability for insider threats across [Assignment: organization-defined components or elements of the organization].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-4(8) - Correlation With External Organizations
================================================================================

:Requirement:
    INCIDENT HANDLING | CORRELATION WITH EXTERNAL ORGANIZATIONS The organization coordinates with [Assignment: organization-defined external organizations] to correlate and share [Assignment: organization-defined incident information] to achieve a cross-organization perspective on incident awareness and more effective incident responses.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-4(8) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT HANDLING | CORRELATION WITH EXTERNAL ORGANIZATIONS The organization coordinates with [Assignment: organization-defined external organizations] to correlate and share [Assignment: organization-defined incident information] to achieve a cross-organization perspective on incident awareness and more effective incident responses.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-5 - Incident Monitoring
================================================================================

:Requirement:
    INCIDENTMONITORING Control: The organization tracks and documents information system security incidents.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-5 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENTMONITORING Control: The organization tracks and documents information system security incidents.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-5(1) - Automated Tracking / Data Collection / Analysis
================================================================================

:Requirement:
    INCIDENT MONITORING | AUTOMATED TRACKING / DATA COLLECTION / ANALYSIS The organization employs automated mechanisms to assist in the tracking of security incidents and in the collection and analysis of incident information.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-5(1) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT MONITORING | AUTOMATED TRACKING / DATA COLLECTION / ANALYSIS The organization employs automated mechanisms to assist in the tracking of security incidents and in the collection and analysis of incident information.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-6 - Incident Reporting
================================================================================

:Requirement:
    INCIDENT REPORTING Control: The organization: a. Requires personnel to report suspected security incidents to the organizational incident response capability within [Assignment: organization-defined time period]; and b. Reports security incident information to [Assignment: organization-defined authorities].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-6 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT REPORTING Control: The organization: a. Requires personnel to report suspected security incidents to the organizational incident response capability within [Assignment: organization-defined time period]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reports security incident information to [Assignment: organization-defined authorities].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-6(1) - Automated Reporting
================================================================================

:Requirement:
    INCIDENT REPORTING | AUTOMATED REPORTING The organization employs automated mechanisms to assist in the reporting of security incidents.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-6(1) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT REPORTING | AUTOMATED REPORTING The organization employs automated mechanisms to assist in the reporting of security incidents.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-6(2) - Vulnerabilities Related To Incidents
================================================================================

:Requirement:
    INCIDENT REPORTING | VULNERABILITIES RELATED TO INCIDENTS The organization reports information system vulnerabilities associated with reported security incidents to [Assignment: organization-defined personnel or roles].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-6(2) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT REPORTING | VULNERABILITIES RELATED TO INCIDENTS The organization reports information system vulnerabilities associated with reported security incidents to [Assignment: organization-defined personnel or roles].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-7 - Incident Response Assistance
================================================================================

:Requirement:
    INCIDENT RESPONSE ASSISTANCE Control: The organization provides an incident response support resource, integral to the organizational incident response capability that offers advice and assistance to users of the information system for the handling and reporting of security incidents.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-7 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT RESPONSE ASSISTANCE Control: The organization provides an incident response support resource, integral to the organizational incident response capability that offers advice and assistance to users of the information system for the handling and reporting of security incidents.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-7(1) - Automation Support For Availability Of Information / Support
================================================================================

:Requirement:
    INCIDENT RESPONSE ASSISTANCE | AUTOMATION SUPPORT FOR AVAILABILITY OF INFORMATION / SUPPORT The organization employs automated mechanisms to increase the availability of incident response-related information and support.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-7(1) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT RESPONSE ASSISTANCE | AUTOMATION SUPPORT FOR AVAILABILITY OF INFORMATION / SUPPORT The organization employs automated mechanisms to increase the availability of incident response-related information and support.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-7(2) - Coordination With External Providers
================================================================================

:Requirement:
    INCIDENT RESPONSE ASSISTANCE | COORDINATION WITH EXTERNAL PROVIDERS The organization: (a) Establishes a direct, cooperative relationship between its incident response capability and external providers of information system protection capability; and (b) Identifies organizational incident response team members to the external providers.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-7(2) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT RESPONSE ASSISTANCE | COORDINATION WITH EXTERNAL PROVIDERS The organization: (a) Establishes a direct, cooperative relationship between its incident response capability and external providers of information system protection capability; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    (b) Identifies organizational incident response team members to the external providers.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







IR-8 - Incident Response Plan
================================================================================

:Requirement:
    INCIDENT RESPONSE PLAN Control: The organization: a. Develops an incident response plan that: 1. Provides the organization with a roadmap for implementing its incident response capability; 2. Describes the structure and organization of the incident response capability; 3. Provides a high-level approach for how the incident response capability fits into the overall organization; 4. Meets the unique requirements of the organization, which relate to mission, size, structure, and functions; 5. Defines reportable incidents; 6. Provides metrics for measuring the incident response capability within the organization; 7. Defines the resources and management support needed to effectively maintain and mature an incident response capability; and 8. Is reviewed and approved by [Assignment: organization-defined personnel or roles]; b. Distributes copies of the incident response plan to [Assignment: organization-defined incident response personnel (identified by name and/or by role) and organizational elements]; c. Reviews the incident response plan [Assignment: organization-defined frequency]; d. Updates the incident response plan to address system/organizational changes or problems encountered during plan implementation, execution, or testing; e. Communicates incident response plan changes to [Assignment: organization-defined incident response personnel (identified by name and/or by role) and organizational elements]; and f. Protects the incident response plan from unauthorized disclosure and modification.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

IR-8 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INCIDENT RESPONSE PLAN Control: The organization: a. Develops an incident response plan that: 1. Provides the organization with a roadmap for implementing its incident response capability;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Describes the structure and organization of the incident response capability;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    3. Provides a high-level approach for how the incident response capability fits into the overall organization;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    4. Meets the unique requirements of the organization, which relate to mission, size, structure, and functions;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    5. Defines reportable incidents;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part f
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    6. Provides metrics for measuring the incident response capability within the organization;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part g
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    7. Defines the resources and management support needed to effectively maintain and mature an incident response capability; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part h
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    8. Is reviewed and approved by [Assignment: organization-defined personnel or roles];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part i
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Distributes copies of the incident response plan to [Assignment: organization-defined incident response personnel (identified by name and/or by role) and organizational elements];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part j
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Reviews the incident response plan [Assignment: organization-defined frequency];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part k
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Updates the incident response plan to address system/organizational changes or problems encountered during plan implementation, execution, or testing;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part l
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    e. Communicates incident response plan changes to [Assignment: organization-defined incident response personnel (identified by name and/or by role) and organizational elements]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    f. Protects the incident response plan from unauthorized disclosure and modification.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







MA-1 - System Maintenance Policy And Procedures
================================================================================

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
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SYSTEM MAINTENANCE POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A system maintenance policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the system maintenance policy and associated system maintenance controls; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. System maintenance policy [Assignment: organization-defined frequency]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. System maintenance procedures [Assignment: organization-defined frequency].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







MA-2 - Controlled Maintenance
================================================================================

:Requirement:
    CONTROLLED MAINTENANCE Control: The organization: a. Schedules, performs, documents, and reviews records of maintenance and repairs on information system components in accordance with manufacturer or vendor specifications and/or organizational requirements; b. Approves and monitors all maintenance activities, whether performed on site or remotely and whether the equipment is serviced on site or removed to another location; c. Requires that [Assignment: organization-defined personnel or roles] explicitly approve the removal of the information system or system components from organizational facilities for off-site maintenance or repairs; d. Sanitizes equipment to remove all information from associated media prior to removal from organizational facilities for off-site maintenance or repairs; e. Checks all potentially impacted security controls to verify that the controls are still functioning properly following maintenance or repair actions; and f. Includes [Assignment: organization-defined maintenance-related information] in organizational maintenance records.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

MA-2 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    CONTROLLED MAINTENANCE Control: The organization: a. Schedules, performs, documents, and reviews records of maintenance and repairs on information system components in accordance with manufacturer or vendor specifications and/or organizational requirements;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Approves and monitors all maintenance activities, whether performed on site or remotely and whether the equipment is serviced on site or removed to another location;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Requires that [Assignment: organization-defined personnel or roles] explicitly approve the removal of the information system or system components from organizational facilities for off-site maintenance or repairs;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Sanitizes equipment to remove all information from associated media prior to removal from organizational facilities for off-site maintenance or repairs;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    e. Checks all potentially impacted security controls to verify that the controls are still functioning properly following maintenance or repair actions; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part f
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    f. Includes [Assignment: organization-defined maintenance-related information] in organizational maintenance records.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







MA-2(2) - Automated Maintenance Activities
================================================================================

:Requirement:
    CONTROLLED MAINTENANCE | AUTOMATED MAINTENANCE ACTIVITIES The organization: (a) Employs automated mechanisms to schedule, conduct, and document maintenance and repairs; and (b) Produces up-to date, accurate, and complete records of all maintenance and repair actions requested, scheduled, in process, and completed.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

MA-2(2) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    CONTROLLED MAINTENANCE | AUTOMATED MAINTENANCE ACTIVITIES The organization: (a) Employs automated mechanisms to schedule, conduct, and document maintenance and repairs; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    (b) Produces up-to date, accurate, and complete records of all maintenance and repair actions requested, scheduled, in process, and completed.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







MA-5 - Maintenance Personnel
================================================================================

:Requirement:
    MAINTENANCE PERSONNEL Control: The organization: a. Establishes a process for maintenance personnel authorization and maintains a list of authorized maintenance organizations or personnel; b. Ensures that non-escorted personnel performing maintenance on the information system have required access authorizations; and c. Designates organizational personnel with required access authorizations and technical competence to supervise the maintenance activities of personnel who do not possess the required access authorizations.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

MA-5 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    MAINTENANCE PERSONNEL Control: The organization: a. Establishes a process for maintenance personnel authorization and maintains a list of authorized maintenance organizations or personnel;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Ensures that non-escorted personnel performing maintenance on the information system have required access authorizations; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Designates organizational personnel with required access authorizations and technical competence to supervise the maintenance activities of personnel who do not possess the required access authorizations.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







MA-5(1) - Individuals Without Appropriate Access
================================================================================

:Requirement:
    MAINTENANCE PERSONNEL | INDIVIDUALS WITHOUT APPROPRIATE ACCESS The organization: (a) Implements procedures for the use of maintenance personnel that lack appropriate security clearances or are not U.S. citizens, that include the following requirements: (1) Maintenance personnel who do not have needed access authorizations, clearances, or formal access approvals are escorted and supervised during the performance of maintenance and diagnostic activities on the information system by approved organizational personnel who are fully cleared, have appropriate access authorizations, and are technically qualified; (2) Prior to initiating maintenance or diagnostic activities by personnel who do not have needed access authorizations, clearances or formal access approvals, all volatile information storage components within the information system are sanitized and all nonvolatile storage media are removed or physically disconnected from the system and secured; and (b) Develops and implements alternate security safeguards in the event an information system component cannot be sanitized, removed, or disconnected from the system.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

MA-5(1) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    MAINTENANCE PERSONNEL | INDIVIDUALS WITHOUT APPROPRIATE ACCESS The organization: (a) Implements procedures for the use of maintenance personnel that lack appropriate security clearances or are not U.S. citizens, that include the following requirements: (1) Maintenance personnel who do not have needed access authorizations, clearances, or formal access approvals are escorted and supervised during the performance of maintenance and diagnostic activities on the information system by approved organizational personnel who are fully cleared, have appropriate access authorizations, and are technically qualified;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    (2) Prior to initiating maintenance or diagnostic activities by personnel who do not have needed access authorizations, clearances or formal access approvals, all volatile information storage components within the information system are sanitized and all nonvolatile storage media are removed or physically disconnected from the system and secured; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    (b) Develops and implements alternate security safeguards in the event an information system component cannot be sanitized, removed, or disconnected from the system.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PE-1 - Physical And Environmental Protection Policy And Procedures
================================================================================

:Requirement:
    PHYSICAL AND ENVIRONMENTAL PROTECTION POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A physical and environmental protection policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and 2. Procedures to facilitate the implementation of the physical and environmental protection policy and associated physical and environmental protection controls; and b. Reviews and updates the current: 1. Physical and environmental protection policy [Assignment: organization-defined frequency]; and 2. Physical and environmental protection procedures [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PE-1 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    PHYSICAL AND ENVIRONMENTAL PROTECTION POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A physical and environmental protection policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the physical and environmental protection policy and associated physical and environmental protection controls; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. Physical and environmental protection policy [Assignment: organization-defined frequency]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Physical and environmental protection procedures [Assignment: organization-defined frequency].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PE-16 - Delivery And Removal
================================================================================

:Requirement:
    DELIVERY AND REMOVAL Control: The organization authorizes, monitors, and controls [Assignment: organization-defined types of information system components] entering and exiting the facility and maintains records of those items.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PE-16 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    DELIVERY AND REMOVAL Control: The organization authorizes, monitors, and controls [Assignment: organization-defined types of information system components] entering and exiting the facility and maintains records of those items.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PE-17 - Alternate Work Site
================================================================================

:Requirement:
    ALTERNATE WORK SITE Control: The organization: a. Employs [Assignment: organization-defined security controls] at alternate work sites; b. Assesses as feasible, the effectiveness of security controls at alternate work sites; and c. Provides a means for employees to communicate with information security personnel in case of security incidents or problems.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PE-17 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    ALTERNATE WORK SITE Control: The organization: a. Employs [Assignment: organization-defined security controls] at alternate work sites;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Assesses as feasible, the effectiveness of security controls at alternate work sites; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Provides a means for employees to communicate with information security personnel in case of security incidents or problems.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PE-2 - Physical Access Authorizations
================================================================================

:Requirement:
    PHYSICAL ACCESS AUTHORIZATIONS Control: The organization: a. Develops, approves, and maintains a list of individuals with authorized access to the facility where the information system resides; b. Issues authorization credentials for facility access; c. Reviews the access list detailing authorized facility access by individuals [Assignment: organization-defined frequency]; and d. Removes individuals from the facility access list when access is no longer required.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PE-2 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    PHYSICAL ACCESS AUTHORIZATIONS Control: The organization: a. Develops, approves, and maintains a list of individuals with authorized access to the facility where the information system resides;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Issues authorization credentials for facility access;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Reviews the access list detailing authorized facility access by individuals [Assignment: organization-defined frequency]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Removes individuals from the facility access list when access is no longer required.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PE-3 - Physical Access Control
================================================================================

:Requirement:
    PHYSICAL ACCESS CONTROL Control: The organization: a. Enforces physical access authorizations at [Assignment: organization-defined entry/exit points to the facility where the information system resides] by; 1. Verifying individual access authorizations before granting access to the facility; and 2. Controlling ingress/egress to the facility using [Selection (one or more): [Assignment: organization-defined physical access control systems/devices]; guards]; b. Maintains physical access audit logs for [Assignment: organization-defined entry/exit points]; c. Provides [Assignment: organization-defined security safeguards] to control access to areas within the facility officially designated as publicly accessible; d. Escorts visitors and monitors visitor activity [Assignment: organization-defined circumstances requiring visitor escorts and monitoring]; e. Secures keys, combinations, and other physical access devices; f. Inventories [Assignment: organization-defined physical access devices] every [Assignment: organization-defined frequency]; and g. Changes combinations and keys [Assignment: organization-defined frequency] and/or when keys are lost, combinations are compromised, or individuals are transferred or terminated.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PE-3 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    PHYSICAL ACCESS CONTROL Control: The organization: a. Enforces physical access authorizations at [Assignment: organization-defined entry/exit points to the facility where the information system resides] by; 1. Verifying individual access authorizations before granting access to the facility; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Controlling ingress/egress to the facility using [Selection (one or more): [Assignment: organization-defined physical access control systems/devices]; guards];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Maintains physical access audit logs for [Assignment: organization-defined entry/exit points];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Provides [Assignment: organization-defined security safeguards] to control access to areas within the facility officially designated as publicly accessible;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Escorts visitors and monitors visitor activity [Assignment: organization-defined circumstances requiring visitor escorts and monitoring];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part f
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    e. Secures keys, combinations, and other physical access devices;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part g
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    f. Inventories [Assignment: organization-defined physical access devices] every [Assignment: organization-defined frequency]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part h
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    g. Changes combinations and keys [Assignment: organization-defined frequency] and/or when keys are lost, combinations are compromised, or individuals are transferred or terminated.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PE-6 - Monitoring Physical Access
================================================================================

:Requirement:
    MONITORING PHYSICAL ACCESS Control: The organization: a. Monitors physical access to the facility where the information system resides to detect and respond to physical security incidents; b. Reviews physical access logs [Assignment: organization-defined frequency] and upon occurrence of [Assignment: organization-defined events or potential indications of events]; and c. Coordinates results of reviews and investigations with the organizational incident response capability.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PE-6 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    MONITORING PHYSICAL ACCESS Control: The organization: a. Monitors physical access to the facility where the information system resides to detect and respond to physical security incidents;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews physical access logs [Assignment: organization-defined frequency] and upon occurrence of [Assignment: organization-defined events or potential indications of events]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Coordinates results of reviews and investigations with the organizational incident response capability.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PE-6(1) - Intrusion Alarms / Surveillance Equipment
================================================================================

:Requirement:
    MONITORING PHYSICAL ACCESS | INTRUSION ALARMS / SURVEILLANCE EQUIPMENT The organization monitors physical intrusion alarms and surveillance equipment.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PE-6(1) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    MONITORING PHYSICAL ACCESS | INTRUSION ALARMS / SURVEILLANCE EQUIPMENT The organization monitors physical intrusion alarms and surveillance equipment.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PE-6(4) - Monitoring Physical Access To Information Systems
================================================================================

:Requirement:
    MONITORING PHYSICAL ACCESS | MONITORING PHYSICAL ACCESS TO INFORMATION SYSTEMS The organization monitors physical access to the information system in addition to the physical access monitoring of the facility as [Assignment: organization-defined physical spaces containing one or more components of the information system].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PE-6(4) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    MONITORING PHYSICAL ACCESS | MONITORING PHYSICAL ACCESS TO INFORMATION SYSTEMS The organization monitors physical access to the information system in addition to the physical access monitoring of the facility as [Assignment: organization-defined physical spaces containing one or more components of the information system].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PE-8 - Visitor Access Records
================================================================================

:Requirement:
    VISITOR ACCESS RECORDS Control: The organization: a. Maintains visitor access records to the facility where the information system resides for [Assignment: organization-defined time period]; and b. Reviews visitor access records [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PE-8 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    VISITOR ACCESS RECORDS Control: The organization: a. Maintains visitor access records to the facility where the information system resides for [Assignment: organization-defined time period]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews visitor access records [Assignment: organization-defined frequency].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PL-1 - Security Planning Policy And Procedures
================================================================================

:Requirement:
    SECURITY PLANNING POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A security planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and 2. Procedures to facilitate the implementation of the security planning policy and associated security planning controls; and b. Reviews and updates the current: 1. Security planning policy [Assignment: organization-defined frequency]; and 2. Security planning procedures [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PL-1 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SECURITY PLANNING POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A security planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the security planning policy and associated security planning controls; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. Security planning policy [Assignment: organization-defined frequency]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Security planning procedures [Assignment: organization-defined frequency].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PL-2 - System Security Plan
================================================================================

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
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SYSTEM SECURITY PLAN Control: The organization: a. Develops a security plan for the information system that: 1. Is consistent with the organization’s enterprise architecture;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Explicitly defines the authorization boundary for the system;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    3. Describes the operational context of the information system in terms of missions and business processes;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    4. Provides the security categorization of the information system including supporting rationale;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    5. Describes the operational environment for the information system and relationships with or connections to other information systems;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part f
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    6. Provides an overview of the security requirements for the system;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part g
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    7. Identifies any relevant overlays, if applicable;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part h
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    8. Describes the security controls in place or planned for meeting those requirements including a rationale for the tailoring and supplementation decisions; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part i
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    9. Is reviewed and approved by the authorizing official or designated representative prior to plan implementation;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part j
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Distributes copies of the security plan and communicates subsequent changes to the plan to [Assignment: organization-defined personnel or roles];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part k
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Reviews the security plan for the information system [Assignment: organization-defined frequency];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part l
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Updates the plan to address changes to the information system/environment of operation or problems identified during plan implementation or security control assessments; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    e. Protects the security plan from unauthorized disclosure and modification.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PL-2(3) - Plan / Coordinate With Other Organizational Entities
================================================================================

:Requirement:
    SYSTEM SECURITY PLAN | PLAN / COORDINATE WITH OTHER ORGANIZATIONAL ENTITIES The organization plans and coordinates security-related activities affecting the information system with [Assignment: organization-defined individuals or groups] before conducting such activities in order to reduce the impact on other organizational entities.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PL-2(3) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SYSTEM SECURITY PLAN | PLAN / COORDINATE WITH OTHER ORGANIZATIONAL ENTITIES The organization plans and coordinates security-related activities affecting the information system with [Assignment: organization-defined individuals or groups] before conducting such activities in order to reduce the impact on other organizational entities.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PL-4 - Rules Of Behavior
================================================================================

:Requirement:
    RULES OF BEHAVIOR Control: The organization: a. Establishes and makes readily available to individuals requiring access to the information system, the rules that describe their responsibilities and expected behavior with regard to information and information system usage; b. Receives a signed acknowledgment from such individuals, indicating that they have read, understand, and agree to abide by the rules of behavior, before authorizing access to information and the information system; c. Reviews and updates the rules of behavior [Assignment: organization-defined frequency]; and d. Requires individuals who have signed a previous version of the rules of behavior to read and resign when the rules of behavior are revised/updated.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PL-4 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    RULES OF BEHAVIOR Control: The organization: a. Establishes and makes readily available to individuals requiring access to the information system, the rules that describe their responsibilities and expected behavior with regard to information and information system usage;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Receives a signed acknowledgment from such individuals, indicating that they have read, understand, and agree to abide by the rules of behavior, before authorizing access to information and the information system;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Reviews and updates the rules of behavior [Assignment: organization-defined frequency]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Requires individuals who have signed a previous version of the rules of behavior to read and resign when the rules of behavior are revised/updated.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PL-8 - Information Security Architecture
================================================================================

:Requirement:
    INFORMATION SECURITY ARCHITECTURE Control: The organization: a. Develops an information security architecture for the information system that: 1. Describes the overall philosophy, requirements, and approach to be taken with regard to protecting the confidentiality, integrity, and availability of organizational information; 2. Describes how the information security architecture is integrated into and supports the enterprise architecture; and 3. Describes any information security assumptions about, and dependencies on, external services; b. Reviews and updates the information security architecture [Assignment: organization-defined frequency] to reflect updates in the enterprise architecture; and c. Ensures that planned information security architecture changes are reflected in the security plan, the security Concept of Operations (CONOPS), and organizational procurements/acquisitions.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant

:Status:
    Not implemented
:Origin:
    Tenant SSP

PL-8 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SECURITY ARCHITECTURE Control: The organization: a. Develops an information security architecture for the information system that: 1. Describes the overall philosophy, requirements, and approach to be taken with regard to protecting the confidentiality, integrity, and availability of organizational information;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Describes how the information security architecture is integrated into and supports the enterprise architecture; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    3. Describes any information security assumptions about, and dependencies on, external services;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the information security architecture [Assignment: organization-defined frequency] to reflect updates in the enterprise architecture; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Ensures that planned information security architecture changes are reflected in the security plan, the security Concept of Operations (CONOPS), and organizational procurements/acquisitions.
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.







PL-8(1) - Defense-in-depth
================================================================================

:Requirement:
    INFORMATION SECURITY ARCHITECTURE | DEFENSE-IN-DEPTH The organization designs its security architecture using a defense-in-depth approach that: (a) Allocates [Assignment: organization-defined security safeguards] to [Assignment: organization-defined locations and architectural layers]; and (b) Ensures that the allocated security safeguards operate in a coordinated and mutually reinforcing manner.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PL-8(1) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SECURITY ARCHITECTURE | DEFENSE-IN-DEPTH The organization designs its security architecture using a defense-in-depth approach that: (a) Allocates [Assignment: organization-defined security safeguards] to [Assignment: organization-defined locations and architectural layers]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    (b) Ensures that the allocated security safeguards operate in a coordinated and mutually reinforcing manner.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PL-8(2) - Supplier Diversity
================================================================================

:Requirement:
    INFORMATION SECURITY ARCHITECTURE | SUPPLIER DIVERSITY The organization requires that [Assignment: organization-defined security safeguards] allocated to [Assignment: organization-defined locations and architectural layers] are obtained from different suppliers.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PL-8(2) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SECURITY ARCHITECTURE | SUPPLIER DIVERSITY The organization requires that [Assignment: organization-defined security safeguards] allocated to [Assignment: organization-defined locations and architectural layers] are obtained from different suppliers.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PS-1 - Personnel Security Policy And Procedures
================================================================================

:Requirement:
    PERSONNEL SECURITY POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A personnel security policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and 2. Procedures to facilitate the implementation of the personnel security policy and associated personnel security controls; and b. Reviews and updates the current: 1. Personnel security policy [Assignment: organization-defined frequency]; and 2. Personnel security procedures [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PS-1 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    PERSONNEL SECURITY POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A personnel security policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the personnel security policy and associated personnel security controls; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. Personnel security policy [Assignment: organization-defined frequency]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Personnel security procedures [Assignment: organization-defined frequency].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PS-2 - Position Risk Designation
================================================================================

:Requirement:
    POSITION RISK DESIGNATION Control: The organization: a. Assigns a risk designation to all organizational positions; b. Establishes screening criteria for individuals filling those positions; and c. Reviews and updates position risk designations [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PS-2 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    POSITION RISK DESIGNATION Control: The organization: a. Assigns a risk designation to all organizational positions;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Establishes screening criteria for individuals filling those positions; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Reviews and updates position risk designations [Assignment: organization-defined frequency].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PS-4 - Personnel Termination
================================================================================

:Requirement:
    PERSONNEL TERMINATION Control: The organization, upon termination of individual employment: a. Disables information system access within [Assignment: organization-defined time period]; b. Terminates/revokes any authenticators/credentials associated with the individual; c. Conducts exit interviews that include a discussion of [Assignment: organization-defined information security topics]; d. Retrieves all security-related organizational information system-related property; e. Retains access to organizational information and information systems formerly controlled by terminated individual; and f. Notifies [Assignment: organization-defined personnel or roles] within [Assignment: organization-defined time period].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PS-4 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    PERSONNEL TERMINATION Control: The organization, upon termination of individual employment: a. Disables information system access within [Assignment: organization-defined time period];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Terminates/revokes any authenticators/credentials associated with the individual;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Conducts exit interviews that include a discussion of [Assignment: organization-defined information security topics];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Retrieves all security-related organizational information system-related property;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    e. Retains access to organizational information and information systems formerly controlled by terminated individual; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part f
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    f. Notifies [Assignment: organization-defined personnel or roles] within [Assignment: organization-defined time period].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PS-4(2) - Automated Notification
================================================================================

:Requirement:
    PERSONNEL TERMINATION | AUTOMATED NOTIFICATION The organization employs automated mechanisms to notify [Assignment: organization-defined personnel or roles] upon termination of an individual.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PS-4(2) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    PERSONNEL TERMINATION | AUTOMATED NOTIFICATION The organization employs automated mechanisms to notify [Assignment: organization-defined personnel or roles] upon termination of an individual.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PS-5 - Personnel Transfer
================================================================================

:Requirement:
    PERSONNEL TRANSFER Control: The organization: a. Reviews and confirms ongoing operational need for current logical and physical access authorizations to information systems/facilities when individuals are reassigned or transferred to other positions within the organization; b. Initiates [Assignment: organization-defined transfer or reassignment actions] within [Assignment: organization-defined time period following the formal transfer action]; c. Modifies access authorization as needed to correspond with any changes in operational need due to reassignment or transfer; and d. Notifies [Assignment: organization-defined personnel or roles] within [Assignment: organization-defined time period].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PS-5 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    PERSONNEL TRANSFER Control: The organization: a. Reviews and confirms ongoing operational need for current logical and physical access authorizations to information systems/facilities when individuals are reassigned or transferred to other positions within the organization;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Initiates [Assignment: organization-defined transfer or reassignment actions] within [Assignment: organization-defined time period following the formal transfer action];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Modifies access authorization as needed to correspond with any changes in operational need due to reassignment or transfer; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Notifies [Assignment: organization-defined personnel or roles] within [Assignment: organization-defined time period].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







PS-8 - Personnel Sanctions
================================================================================

:Requirement:
    PERSONNEL SANCTIONS Control: The organization: a. Employs a formal sanctions process for individuals failing to comply with established information security policies and procedures; and b. Notifies [Assignment: organization-defined personnel or roles] within [Assignment: organization-defined time period] when a formal employee sanctions process is initiated, identifying the individual sanctioned and the reason for the sanction.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

PS-8 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    PERSONNEL SANCTIONS Control: The organization: a. Employs a formal sanctions process for individuals failing to comply with established information security policies and procedures; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Notifies [Assignment: organization-defined personnel or roles] within [Assignment: organization-defined time period] when a formal employee sanctions process is initiated, identifying the individual sanctioned and the reason for the sanction.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







RA-1 - Risk Assessment Policy And Procedures
================================================================================

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
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    RISK ASSESSMENT POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A risk assessment policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the risk assessment policy and associated risk assessment controls; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. Risk assessment policy [Assignment: organization-defined frequency]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Risk assessment procedures [Assignment: organization-defined frequency].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







RA-2 - Security Categorization
================================================================================

:Requirement:
    SECURITY CATEGORIZATION Control: The organization: a. Categorizes information and the information system in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance; b. Documents the security categorization results (including supporting rationale) in the security plan for the information system; and c. Ensures that the security categorization decision is reviewed and approved by the authorizing official or authorizing official designated representative.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

RA-2 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SECURITY CATEGORIZATION Control: The organization: a. Categorizes information and the information system in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Documents the security categorization results (including supporting rationale) in the security plan for the information system; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Ensures that the security categorization decision is reviewed and approved by the authorizing official or authorizing official designated representative.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







RA-3 - Risk Assessment
================================================================================

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
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    RISK ASSESSMENT Control: The organization: a. Conducts an assessment of risk, including the likelihood and magnitude of harm, from the unauthorized access, use, disclosure, disruption, modification, or destruction of the information system and the information it processes, stores, or transmits;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Documents risk assessment results in [Selection: security plan; risk assessment report; [Assignment: organization-defined document]];
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Reviews risk assessment results [Assignment: organization-defined frequency];
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Disseminates risk assessment results to [Assignment: organization-defined personnel or roles]; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    e. Updates the risk assessment [Assignment: organization-defined frequency] or whenever there are significant changes to the information system or environment of operation (including the identification of new threats and vulnerabilities), or other conditions that may impact the security state of the system.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







RA-5 - Vulnerability Scanning
================================================================================

:Requirement:
    VULNERABILITY SCANNING Control: The organization: a. Scans for vulnerabilities in the information system and hosted applications [Assignment: organization-defined frequency and/or randomly in accordance with organization-defined process] and when new vulnerabilities potentially affecting the system/applications are identified and reported; b. Employs vulnerability scanning tools and techniques that facilitate interoperability among tools and automate parts of the vulnerability management process by using standards for: 1. Enumerating platforms, software flaws, and improper configurations; 2. Formatting checklists and test procedures; and 3. Measuring vulnerability impact; c. Analyzes vulnerability scan reports and results from security control assessments; d. Remediates legitimate vulnerabilities [Assignment: organization-defined response times] in accordance with an organizational assessment of risk; and e. Shares information obtained from the vulnerability scanning process and security control assessments with [Assignment: organization-defined personnel or roles] to help eliminate similar vulnerabilities in other information systems (i.e., systemic weaknesses or deficiencies).


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

RA-5 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    VULNERABILITY SCANNING Control: The organization: a. Scans for vulnerabilities in the information system and hosted applications [Assignment: organization-defined frequency and/or randomly in accordance with organization-defined process] and when new vulnerabilities potentially affecting the system/applications are identified and reported;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Employs vulnerability scanning tools and techniques that facilitate interoperability among tools and automate parts of the vulnerability management process by using standards for: 1. Enumerating platforms, software flaws, and improper configurations;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Formatting checklists and test procedures; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    3. Measuring vulnerability impact;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Analyzes vulnerability scan reports and results from security control assessments;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part f
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Remediates legitimate vulnerabilities [Assignment: organization-defined response times] in accordance with an organizational assessment of risk; and
:Role:
    Shared
:Status:
    Not implemented
:Details:
    Documented in the POAM created as a result of vulnerability scanning.



Part g
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    e. Shares information obtained from the vulnerability scanning process and security control assessments with [Assignment: organization-defined personnel or roles] to help eliminate similar vulnerabilities in other information systems (i.e., systemic weaknesses or deficiencies).
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







RA-5(1) - Update Tool Capability
================================================================================

:Requirement:
    VULNERABILITY SCANNING | UPDATE TOOL CAPABILITY The organization employs vulnerability scanning tools that include the capability to readily update the information system vulnerabilities to be scanned.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

RA-5(1) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    VULNERABILITY SCANNING | UPDATE TOOL CAPABILITY The organization employs vulnerability scanning tools that include the capability to readily update the information system vulnerabilities to be scanned.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







RA-5(10) - Correlate Scanning Information
================================================================================

:Requirement:
    VULNERABILITY SCANNING | CORRELATE SCANNING INFORMATION The organization correlates the output from vulnerability scanning tools to determine the presence of multi-vulnerability/multi-hop attack vectors.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

RA-5(10) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    VULNERABILITY SCANNING | CORRELATE SCANNING INFORMATION The organization correlates the output from vulnerability scanning tools to determine the presence of multi-vulnerability/multi-hop attack vectors.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







RA-5(2) - Update By Frequency / Prior To New Scan / When Identified
================================================================================

:Requirement:
    VULNERABILITY SCANNING | UPDATE BY FREQUENCY / PRIOR TO NEW SCAN / WHEN IDENTIFIED The organization updates the information system vulnerabilities scanned [Selection (one or more): [Assignment: organization-defined frequency]; prior to a new scan; when new vulnerabilities are identified and reported].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

RA-5(2) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    VULNERABILITY SCANNING | UPDATE BY FREQUENCY / PRIOR TO NEW SCAN / WHEN IDENTIFIED The organization updates the information system vulnerabilities scanned [Selection (one or more): [Assignment: organization-defined frequency]; prior to a new scan; when new vulnerabilities are identified and reported].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







RA-5(4) - Discoverable Information
================================================================================

:Requirement:
    VULNERABILITY SCANNING | DISCOVERABLE INFORMATION The organization determines what information about the information system is discoverable by adversaries and subsequently takes [Assignment: organization-defined corrective actions].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

RA-5(4) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    VULNERABILITY SCANNING | DISCOVERABLE INFORMATION The organization determines what information about the information system is discoverable by adversaries and subsequently takes [Assignment: organization-defined corrective actions].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







RA-5(5) - Privileged Access
================================================================================

:Requirement:
    VULNERABILITY SCANNING | PRIVILEGED ACCESS The information system implements privileged access authorization to [Assignment: organization-identified information system components] for selected [Assignment: organization-defined vulnerability scanning activities].


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

RA-5(5) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    VULNERABILITY SCANNING | PRIVILEGED ACCESS The information system implements privileged access authorization to [Assignment: organization-identified information system components] for selected [Assignment: organization-defined vulnerability scanning activities].
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







SA-1 - System And Services Acquisition Policy And Procedures
================================================================================

:Requirement:
    SYSTEM AND SERVICES ACQUISITION POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A system and services acquisition policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and 2. Procedures to facilitate the implementation of the system and services acquisition policy and associated system and services acquisition controls; and b. Reviews and updates the current: 1. System and services acquisition policy [Assignment: organization-defined frequency]; and 2. System and services acquisition procedures [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SA-1 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SYSTEM AND SERVICES ACQUISITION POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A system and services acquisition policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the system and services acquisition policy and associated system and services acquisition controls; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. System and services acquisition policy [Assignment: organization-defined frequency]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. System and services acquisition procedures [Assignment: organization-defined frequency].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SA-11 - Developer Security Testing And Evaluation
================================================================================

:Requirement:
    DEVELOPER SECURITY TESTING AND EVALUATION Control: The organization requires the developer of the information system, system component, or information system service to: a. Create and implement a security assessment plan; b. Perform [Selection (one or more): unit; integration; system; regression] testing/evaluation at [Assignment: organization-defined depth and coverage]; c. Produce evidence of the execution of the security assessment plan and the results of the security testing/evaluation; d. Implement a verifiable flaw remediation process; and e. Correct flaws identified during security testing/evaluation.


Control Summary Information
---------------------------

:Role:
    Shared

:Status:
    Not implemented
:Origin:
    OpenShift Landlord SSP and OpenShift Tenant SSP

SA-11 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    DEVELOPER SECURITY TESTING AND EVALUATION Control: The organization requires the developer of the information system, system component, or information system service to: a. Create and implement a security assessment plan;
:Role:
    Shared
:Status:
    Not implemented
:Details:
    Documented in the project's System Test Plan.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Perform [Selection (one or more): unit; integration; system; regression] testing/evaluation at [Assignment: organization-defined depth and coverage];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Produce evidence of the execution of the security assessment plan and the results of the security testing/evaluation;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Implement a verifiable flaw remediation process; and
:Role:
    Shared
:Status:
    Not implemented
:Details:
    Documented in the POAM created as a result of vulnerability scanning.



Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    e. Correct flaws identified during security testing/evaluation.
:Role:
    Shared
:Status:
    Not implemented
:Details:
    Documented in the POAM created as a result of vulnerability scanning.







SA-12 - Supply Chain Protection
================================================================================

:Requirement:
    SUPPLY CHAIN PROTECTION Control: The organization protects against supply chain threats to the information system, system component, or information system service by employing [Assignment: organization-defined security safeguards] as part of a comprehensive, defense-in-breadth information security strategy.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SA-12 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SUPPLY CHAIN PROTECTION Control: The organization protects against supply chain threats to the information system, system component, or information system service by employing [Assignment: organization-defined security safeguards] as part of a comprehensive, defense-in-breadth information security strategy.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SA-12(1) - Acquisition Strategies / Tools / Methods
================================================================================

:Requirement:
    SUPPLY CHAIN PROTECTION | ACQUISITION STRATEGIES / TOOLS / METHODS The organization employs [Assignment: organization-defined tailored acquisition strategies, contract tools, and procurement methods] for the purchase of the information system, system component, or information system service from suppliers.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SA-12(1) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SUPPLY CHAIN PROTECTION | ACQUISITION STRATEGIES / TOOLS / METHODS The organization employs [Assignment: organization-defined tailored acquisition strategies, contract tools, and procurement methods] for the purchase of the information system, system component, or information system service from suppliers.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SA-12(11) - Penetration Testing / Analysis Of Elements, Processes, And Actors
================================================================================

:Requirement:
    SUPPLY CHAIN PROTECTION | PENETRATION TESTING / ANALYSIS OF ELEMENTS, PROCESSES, AND ACTORS The organization employs [Selection (one or more): organizational analysis, independent third-party analysis, organizational penetration testing, independent third-party penetration testing] of [Assignment: organization-defined supply chain elements, processes, and actors] associated with the information system, system component, or information system service.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SA-12(11) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SUPPLY CHAIN PROTECTION | PENETRATION TESTING / ANALYSIS OF ELEMENTS, PROCESSES, AND ACTORS The organization employs [Selection (one or more): organizational analysis, independent third-party analysis, organizational penetration testing, independent third-party penetration testing] of [Assignment: organization-defined supply chain elements, processes, and actors] associated with the information system, system component, or information system service.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SA-12(5) - Limitation Of Harm
================================================================================

:Requirement:
    SUPPLY CHAIN PROTECTION | LIMITATION OF HARM The organization employs [Assignment: organization-defined security safeguards] to limit harm from potential adversaries identifying and targeting the organizational supply chain.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SA-12(5) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SUPPLY CHAIN PROTECTION | LIMITATION OF HARM The organization employs [Assignment: organization-defined security safeguards] to limit harm from potential adversaries identifying and targeting the organizational supply chain.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SA-12(8) - Use Of All-source Intelligence
================================================================================

:Requirement:
    SUPPLY CHAIN PROTECTION | USE OF ALL-SOURCE INTELLIGENCE The organization uses all-source intelligence analysis of suppliers and potential suppliers of the information system, system component, or information system service.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SA-12(8) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SUPPLY CHAIN PROTECTION | USE OF ALL-SOURCE INTELLIGENCE The organization uses all-source intelligence analysis of suppliers and potential suppliers of the information system, system component, or information system service.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SA-12(9) - Operations Security
================================================================================

:Requirement:
    SUPPLY CHAIN PROTECTION | OPERATIONS SECURITY The organization employs [Assignment: organization-defined Operations Security (OPSEC) safeguards] in accordance with classification guides to protect supply chain-related information for the information system, system component, or information system service.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SA-12(9) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SUPPLY CHAIN PROTECTION | OPERATIONS SECURITY The organization employs [Assignment: organization-defined Operations Security (OPSEC) safeguards] in accordance with classification guides to protect supply chain-related information for the information system, system component, or information system service.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SA-14 - Criticality Analysis
================================================================================

:Requirement:
    CRITICALITY ANALYSIS Control: The organization identifies critical information system components and functions by performing a criticality analysis for [Assignment: organization-defined information systems, information system components, or information system services] at [Assignment: organization-defined decision points in the system development life cycle].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SA-14 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    CRITICALITY ANALYSIS Control: The organization identifies critical information system components and functions by performing a criticality analysis for [Assignment: organization-defined information systems, information system components, or information system services] at [Assignment: organization-defined decision points in the system development life cycle].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SA-15 - Development Process, Standards, And Tools
================================================================================

:Requirement:
    DEVELOPMENT PROCESS, STANDARDS, AND TOOLS Control: The organization: a. Requires the developer of the information system, system component, or information system service to follow a documented development process that: 1. Explicitly addresses security requirements; 2. Identifies the standards and tools used in the development process; 3. Documents the specific tool options and tool configurations used in the development process; and 4. Documents, manages, and ensures the integrity of changes to the process and/or tools used in development; and b. Reviews the development process, standards, tools, and tool options/configurations [Assignment: organization-defined frequency] to determine if the process, standards, tools, and tool options/configurations selected and employed can satisfy [Assignment: organization-defined security requirements].


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant

:Status:
    Not implemented
:Origin:
    Tenant SSP

SA-15 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    DEVELOPMENT PROCESS, STANDARDS, AND TOOLS Control: The organization: a. Requires the developer of the information system, system component, or information system service to follow a documented development process that: 1. Explicitly addresses security requirements;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Identifies the standards and tools used in the development process;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    3. Documents the specific tool options and tool configurations used in the development process; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    4. Documents, manages, and ensures the integrity of changes to the process and/or tools used in development; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.



Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews the development process, standards, tools, and tool options/configurations [Assignment: organization-defined frequency] to determine if the process, standards, tools, and tool options/configurations selected and employed can satisfy [Assignment: organization-defined security requirements].
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.







SA-15(3) - Criticality Analysis
================================================================================

:Requirement:
    DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | CRITICALITY ANALYSIS The organization requires the developer of the information system, system component, or information system service to perform a criticality analysis at [Assignment: organization-defined breadth/depth] and at [Assignment: organization-defined decision points in the system development life cycle].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SA-15(3) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | CRITICALITY ANALYSIS The organization requires the developer of the information system, system component, or information system service to perform a criticality analysis at [Assignment: organization-defined breadth/depth] and at [Assignment: organization-defined decision points in the system development life cycle].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SA-15(4) - Threat Modeling / Vulnerability Analysis
================================================================================

:Requirement:
    DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | THREAT MODELING / VULNERABILITY ANALYSIS The organization requires that developers perform threat modeling and a vulnerability analysis for the information system at [Assignment: organization-defined breadth/depth] that: (a) Uses [Assignment: organization-defined information concerning impact, environment of operations, known or assumed threats, and acceptable risk levels]; (b) Employs [Assignment: organization-defined tools and methods]; and (c) Produces evidence that meets [Assignment: organization-defined acceptance criteria].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SA-15(4) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    DEVELOPMENT PROCESS, STANDARDS, AND TOOLS | THREAT MODELING / VULNERABILITY ANALYSIS The organization requires that developers perform threat modeling and a vulnerability analysis for the information system at [Assignment: organization-defined breadth/depth] that: (a) Uses [Assignment: organization-defined information concerning impact, environment of operations, known or assumed threats, and acceptable risk levels];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    (b) Employs [Assignment: organization-defined tools and methods]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    (c) Produces evidence that meets [Assignment: organization-defined acceptance criteria].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SA-16 - Developer-provided Training
================================================================================

:Requirement:
    DEVELOPER-PROVIDED TRAINING Control: The organization requires the developer of the information system, system component, or information system service to provide [Assignment: organization-defined training] on the correct use and operation of the implemented security functions, controls, and/or mechanisms.


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

SA-16 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    DEVELOPER-PROVIDED TRAINING Control: The organization requires the developer of the information system, system component, or information system service to provide [Assignment: organization-defined training] on the correct use and operation of the implemented security functions, controls, and/or mechanisms.
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







SA-17 - Developer Security Architecture And Design
================================================================================

:Requirement:
    DEVELOPER SECURITY ARCHITECTURE AND DESIGN Control: The organization requires the developer of the information system, system component, or information system service to produce a design specification and security architecture that: a. Is consistent with and supportive of the organization’s security architecture which is established within and is an integrated part of the organization’s enterprise architecture; b. Accurately and completely describes the required security functionality, and the allocation of security controls among physical and logical components; and c. Expresses how individual security functions, mechanisms, and services work together to provide required security capabilities and a unified approach to protection.


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

SA-17 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    DEVELOPER SECURITY ARCHITECTURE AND DESIGN Control: The organization requires the developer of the information system, system component, or information system service to produce a design specification and security architecture that: a. Is consistent with and supportive of the organization’s security architecture which is established within and is an integrated part of the organization’s enterprise architecture;
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Accurately and completely describes the required security functionality, and the allocation of security controls among physical and logical components; and
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Expresses how individual security functions, mechanisms, and services work together to provide required security capabilities and a unified approach to protection.
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







SA-2 - Allocation Of Resources
================================================================================

:Requirement:
    ALLOCATION OF RESOURCES Control: The organization: a. Determines information security requirements for the information system or information system service in mission/business process planning; b. Determines, documents, and allocates the resources required to protect the information system or information system service as part of its capital planning and investment control process; and c. Establishes a discrete line item for information security in organizational programming and budgeting documentation.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SA-2 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    ALLOCATION OF RESOURCES Control: The organization: a. Determines information security requirements for the information system or information system service in mission/business process planning;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Determines, documents, and allocates the resources required to protect the information system or information system service as part of its capital planning and investment control process; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Establishes a discrete line item for information security in organizational programming and budgeting documentation.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SA-22 - Unsupported System Components
================================================================================

:Requirement:
    UNSUPPORTED SYSTEM COMPONENTS Control: The organization: a. Replaces information system components when support for the components is no longer available from the developer, vendor, or manufacturer; and b. Provides justification and documents approval for the continued use of unsupported system components required to satisfy mission/business needs.


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

SA-22 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    UNSUPPORTED SYSTEM COMPONENTS Control: The organization: a. Replaces information system components when support for the components is no longer available from the developer, vendor, or manufacturer; and
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Provides justification and documents approval for the continued use of unsupported system components required to satisfy mission/business needs.
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







SA-3 - System Development Life Cycle
================================================================================

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
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SYSTEM DEVELOPMENT LIFE CYCLE Control: The organization: a. Manages the information system using [Assignment: organization-defined system development life cycle] that incorporates information security considerations;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Defines and documents information security roles and responsibilities throughout the system development life cycle;
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Identifies individuals having information security roles and responsibilities; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Integrates the organizational information security risk management process into system development life cycle activities.
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Security Plan.







SA-4 - Acquisition Process
================================================================================

:Requirement:
    ACQUISITION PROCESS Control: The organization includes the following requirements, descriptions, and criteria, explicitly or by reference, in the acquisition contract for the information system, system component, or information system service in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, guidelines, and organizational mission/business needs: a. Security functional requirements; b. Security strength requirements; c. Security assurance requirements; d. Security-related documentation requirements; e. Requirements for protecting security-related documentation; f. Description of the information system development environment and environment in which the system is intended to operate; and g. Acceptance criteria.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SA-4 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    ACQUISITION PROCESS Control: The organization includes the following requirements, descriptions, and criteria, explicitly or by reference, in the acquisition contract for the information system, system component, or information system service in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, guidelines, and organizational mission/business needs: a. Security functional requirements;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Security strength requirements;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Security assurance requirements;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Security-related documentation requirements;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    e. Requirements for protecting security-related documentation;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part f
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    f. Description of the information system development environment and environment in which the system is intended to operate; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part g
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    g. Acceptance criteria.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SA-4(1) - Functional Properties Of Security Controls
================================================================================

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
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    ACQUISITION PROCESS | FUNCTIONAL PROPERTIES OF SECURITY CONTROLS The organization requires the developer of the information system, system component, or information system service to provide a description of the functional properties of the security controls to be employed.
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.







SA-4(2) - Design / Implementation Information For Security Controls
================================================================================

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
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    ACQUISITION PROCESS | DESIGN / IMPLEMENTATION INFORMATION FOR SECURITY CONTROLS The organization requires the developer of the information system, system component, or information system service to provide design and implementation information for the security controls to be employed that includes: [Selection (one or more): security-relevant external system interfaces; high-level design; low-level design; source code or hardware schematics; [Assignment: organization-defined design/implementation information]] at [Assignment: organization-defined level of detail].
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.







SA-4(9) - Functions / Ports / Protocols / Services In Use
================================================================================

:Requirement:
    ACQUISITION PROCESS | FUNCTIONS / PORTS / PROTOCOLS / SERVICES IN USE The organization requires the developer of the information system, system component, or information system service to identify early in the system development life cycle, the functions, ports, protocols, and services intended for organizational use.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant

:Status:
    Not implemented
:Origin:
    Tenant SSP

SA-4(9) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    ACQUISITION PROCESS | FUNCTIONS / PORTS / PROTOCOLS / SERVICES IN USE The organization requires the developer of the information system, system component, or information system service to identify early in the system development life cycle, the functions, ports, protocols, and services intended for organizational use.
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.







SA-5 - Information System Documentation
================================================================================

:Requirement:
    INFORMATION SYSTEM DOCUMENTATION Control: The organization: a. Obtains administrator documentation for the information system, system component, or information system service that describes: 1. Secure configuration, installation, and operation of the system, component, or service; 2. Effective use and maintenance of security functions/mechanisms; and 3. Known vulnerabilities regarding configuration and use of administrative (i.e., privileged) functions; b. Obtains user documentation for the information system, system component, or information system service that describes: 1. User-accessible security functions/mechanisms and how to effectively use those security functions/mechanisms; 2. Methods for user interaction, which enables individuals to use the system, component, or service in a more secure manner; and 3. User responsibilities in maintaining the security of the system, component, or service; c. Documents attempts to obtain information system, system component, or information system service documentation when such documentation is either unavailable or nonexistent and [Assignment: organization-defined actions] in response; d. Protects documentation as required, in accordance with the risk management strategy; and e. Distributes documentation to [Assignment: organization-defined personnel or roles].


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Inplemented
:Origin:
    OpenShift SSP

SA-5 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM DOCUMENTATION Control: The organization: a. Obtains administrator documentation for the information system, system component, or information system service that describes: 1. Secure configuration, installation, and operation of the system, component, or service;
:Role:
    OpenShift Landlord
:Status:
    Inplemented
:Details:
    Documentation available from the OSE vendor, Red Hat.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Effective use and maintenance of security functions/mechanisms; and
:Role:
    OpenShift Landlord
:Status:
    Inplemented
:Details:
    Documentation available from the OSE vendor, Red Hat.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    3. Known vulnerabilities regarding configuration and use of administrative (i.e., privileged) functions;
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Obtains user documentation for the information system, system component, or information system service that describes: 1. User-accessible security functions/mechanisms and how to effectively use those security functions/mechanisms;
:Role:
    OpenShift Landlord
:Status:
    Inplemented
:Details:
    Documentation available from the OSE vendor, Red Hat.



Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Methods for user interaction, which enables individuals to use the system, component, or service in a more secure manner; and
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part f
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    3. User responsibilities in maintaining the security of the system, component, or service;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part g
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Documents attempts to obtain information system, system component, or information system service documentation when such documentation is either unavailable or nonexistent and [Assignment: organization-defined actions] in response;
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS



Part h
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Protects documentation as required, in accordance with the risk management strategy; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part i
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    e. Distributes documentation to [Assignment: organization-defined personnel or roles].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SA-8 - Security Engineering Principles
================================================================================

:Requirement:
    SECURITY ENGINEERING PRINCIPLES Control: The organization applies information system security engineering principles in the specification, design, development, implementation, and modification of the information system.


Control Summary Information
---------------------------

:Role:
    OpenShift Tenant

:Status:
    Not implemented
:Origin:
    Tenant SSP

SA-8 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SECURITY ENGINEERING PRINCIPLES Control: The organization applies information system security engineering principles in the specification, design, development, implementation, and modification of the information system.
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.







SA-9 - External Information System Services
================================================================================

:Requirement:
    EXTERNAL INFORMATION SYSTEM SERVICES Control: The organization: a. Requires that providers of external information system services comply with organizational information security requirements and employ [Assignment: organization-defined security controls] in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance; b. Defines and documents government oversight and user roles and responsibilities with regard to external information system services; and c. Employs [Assignment: organization-defined processes, methods, and techniques] to monitor security control compliance by external service providers on an ongoing basis.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SA-9 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    EXTERNAL INFORMATION SYSTEM SERVICES Control: The organization: a. Requires that providers of external information system services comply with organizational information security requirements and employ [Assignment: organization-defined security controls] in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Defines and documents government oversight and user roles and responsibilities with regard to external information system services; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Employs [Assignment: organization-defined processes, methods, and techniques] to monitor security control compliance by external service providers on an ongoing basis.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SA-9(2) - Identification Of Functions / Ports / Protocols / Services
================================================================================

:Requirement:
    EXTERNAL INFORMATION SYSTEMS | IDENTIFICATION OF FUNCTIONS / PORTS / PROTOCOLS / SERVICES The organization requires providers of [Assignment: organization-defined external information system services] to identify the functions, ports, protocols, and other services required for the use of such services.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SA-9(2) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    EXTERNAL INFORMATION SYSTEMS | IDENTIFICATION OF FUNCTIONS / PORTS / PROTOCOLS / SERVICES The organization requires providers of [Assignment: organization-defined external information system services] to identify the functions, ports, protocols, and other services required for the use of such services.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SC-1 - System And Communications Protection Policy And Procedures
================================================================================

:Requirement:
    SYSTEM AND COMMUNICATIONS PROTECTION POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A system and communications protection policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and 2. Procedures to facilitate the implementation of the system and communications protection policy and associated system and communications protection controls; and b. Reviews and updates the current: 1. System and communications protection policy [Assignment: organization-defined frequency]; and 2. System and communications protection procedures [Assignment: organization-defined frequency].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SC-1 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SYSTEM AND COMMUNICATIONS PROTECTION POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A system and communications protection policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the system and communications protection policy and associated system and communications protection controls; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. System and communications protection policy [Assignment: organization-defined frequency]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. System and communications protection procedures [Assignment: organization-defined frequency].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SC-19 - Voice Over Internet Protocol
================================================================================

:Requirement:
    VOICE OVER INTERNET PROTOCOL Control: The organization: a. Establishes usage restrictions and implementation guidance for Voice over Internet Protocol (VoIP) technologies based on the potential to cause damage to the information system if used maliciously; and b. Authorizes, monitors, and controls the use of VoIP within the information system.


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Not implemented
:Origin:
    OpenShift Landlord SSP

SC-19 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    VOICE OVER INTERNET PROTOCOL Control: The organization: a. Establishes usage restrictions and implementation guidance for Voice over Internet Protocol (VoIP) technologies based on the potential to cause damage to the information system if used maliciously; and
:Role:
    OpenShift Landlord
:Status:
    Not implemented
:Details:
    Tailored out: OSE systems do not utilize VoIP.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Authorizes, monitors, and controls the use of VoIP within the information system.
:Role:
    OpenShift Landlord
:Status:
    Not implemented
:Details:
    Tailored out: OSE systems do not utilize VoIP.







SC-22 - Architecture And Provisioning For Name / Address Resolution Service
================================================================================

:Requirement:
    ARCHITECTURE AND PROVISIONING FOR NAME / ADDRESS RESOLUTION SERVICE Control: The information systems that collectively provide name/address resolution service for an organization are fault-tolerant and implement internal/external role separation.


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Not implemented
:Origin:
    OpenShift Landlord SSP

SC-22 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    ARCHITECTURE AND PROVISIONING FOR NAME / ADDRESS RESOLUTION SERVICE Control: The information systems that collectively provide name/address resolution service for an organization are fault-tolerant and implement internal/external role separation.
:Role:
    OpenShift Landlord
:Status:
    Not implemented
:Details:
    OSE systems are clients of DNS services and do not provide name resolution capabilities.







SC-38 - Operations Security
================================================================================

:Requirement:
    OPERATIONS SECURITY Control: The organization employs [Assignment: organization-defined operations security safeguards] to protect key organizational information throughout the system development life cycle.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SC-38 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    OPERATIONS SECURITY Control: The organization employs [Assignment: organization-defined operations security safeguards] to protect key organizational information throughout the system development life cycle.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SC-7(12) - Host-based Protection
================================================================================

:Requirement:
    BOUNDARY PROTECTION | HOST-BASED PROTECTION The organization implements [Assignment: organization-defined host-based boundary protection mechanisms] at [Assignment: organization-defined information system components].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SC-7(12) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    BOUNDARY PROTECTION | HOST-BASED PROTECTION The organization implements [Assignment: organization-defined host-based boundary protection mechanisms] at [Assignment: organization-defined information system components].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SC-7(18) - Fail Secure
================================================================================

:Requirement:
    BOUNDARY PROTECTION | FAIL SECURE The information system fails securely in the event of an operational failure of a boundary protection device.


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

SC-7(18) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    BOUNDARY PROTECTION | FAIL SECURE The information system fails securely in the event of an operational failure of a boundary protection device.
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







SI-1 - System And Information Integrity Policy And Procedures
================================================================================

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
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    SYSTEM AND INFORMATION INTEGRITY POLICY AND PROCEDURES Control: The organization: a. Develops, documents, and disseminates to [Assignment: organization-defined personnel or roles]: 1. A system and information integrity policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
:Role:
    OpenShift Tenant
:Status:
    Not implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Procedures to facilitate the implementation of the system and information integrity policy and associated system and information integrity controls; and
:Role:
    Shared
:Status:
    Implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Reviews and updates the current: 1. System and information integrity policy [Assignment: organization-defined frequency]; and
:Role:
    Shared
:Status:
    Implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. System and information integrity procedures [Assignment: organization-defined frequency].
:Role:
    Shared
:Status:
    Implemented
:Details:
    Documented in the individual project / program's System Design Specification document and System Security Plan.







SI-4 - Information System Monitoring
================================================================================

:Requirement:
    INFORMATION SYSTEM MONITORING Control: The organization: a. Monitors the information system to detect: 1. Attacks and indicators of potential attacks in accordance with [Assignment: organization-defined monitoring objectives]; and 2. Unauthorized local, network, and remote connections; b. Identifies unauthorized use of the information system through [Assignment: organization-defined techniques and methods]; c. Deploys monitoring devices: (i) strategically within the information system to collect organization-determined essential information; and (ii) at ad hoc locations within the system to track specific types of transactions of interest to the organization; d. Protects information obtained from intrusion-monitoring tools from unauthorized access, modification, and deletion; e. Heightens the level of information system monitoring activity whenever there is an indication of increased risk to organizational operations and assets, individuals, other organizations, or the Nation based on law enforcement information, intelligence information, or other credible sources of information; f. Obtains legal opinion with regard to information system monitoring activities in accordance with applicable federal laws, Executive Orders, directives, policies, or regulations; and g. Provides [Assignment: organization-defined information system monitoring information] to [Assignment: organization-defined personnel or roles] [Selection (one or more): as needed; [Assignment: organization-defined frequency]].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SI-4 What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM MONITORING Control: The organization: a. Monitors the information system to detect: 1. Attacks and indicators of potential attacks in accordance with [Assignment: organization-defined monitoring objectives]; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part b
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    2. Unauthorized local, network, and remote connections;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    b. Identifies unauthorized use of the information system through [Assignment: organization-defined techniques and methods];
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part d
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    c. Deploys monitoring devices: (i) strategically within the information system to collect organization-determined essential information; and (ii) at ad hoc locations within the system to track specific types of transactions of interest to the organization;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part e
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    d. Protects information obtained from intrusion-monitoring tools from unauthorized access, modification, and deletion;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part f
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    e. Heightens the level of information system monitoring activity whenever there is an indication of increased risk to organizational operations and assets, individuals, other organizations, or the Nation based on law enforcement information, intelligence information, or other credible sources of information;
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part g
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    f. Obtains legal opinion with regard to information system monitoring activities in accordance with applicable federal laws, Executive Orders, directives, policies, or regulations; and
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.



Part h
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    g. Provides [Assignment: organization-defined information system monitoring information] to [Assignment: organization-defined personnel or roles] [Selection (one or more): as needed; [Assignment: organization-defined frequency]].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SI-4(1) - System-wide Intrusion Detection System
================================================================================

:Requirement:
    INFORMATION SYSTEM MONITORING | SYSTEM-WIDE INTRUSION DETECTION SYSTEM The organization connects and configures individual intrusion detection tools into an information system-wide intrusion detection system.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SI-4(1) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM MONITORING | SYSTEM-WIDE INTRUSION DETECTION SYSTEM The organization connects and configures individual intrusion detection tools into an information system-wide intrusion detection system.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SI-4(10) - Visibility Of Encrypted Communications
================================================================================

:Requirement:
    INFORMATION SYSTEM MONITORING | VISIBILITY OF ENCRYPTED COMMUNICATIONS The organization makes provisions so that [Assignment: organization-defined encrypted communications traffic] is visible to [Assignment: organization-defined information system monitoring tools].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SI-4(10) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM MONITORING | VISIBILITY OF ENCRYPTED COMMUNICATIONS The organization makes provisions so that [Assignment: organization-defined encrypted communications traffic] is visible to [Assignment: organization-defined information system monitoring tools].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SI-4(11) - Analyze Communications Traffic Anomalies
================================================================================

:Requirement:
    INFORMATION SYSTEM MONITORING | ANALYZE COMMUNICATIONS TRAFFIC ANOMALIES The organization analyzes outbound communications traffic at the external boundary of the information system and selected [Assignment: organization-defined interior points within the system (e.g., subnetworks, subsystems)] to discover anomalies.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SI-4(11) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM MONITORING | ANALYZE COMMUNICATIONS TRAFFIC ANOMALIES The organization analyzes outbound communications traffic at the external boundary of the information system and selected [Assignment: organization-defined interior points within the system (e.g., subnetworks, subsystems)] to discover anomalies.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SI-4(12) - Automated Alerts
================================================================================

:Requirement:
    INFORMATION SYSTEM MONITORING | AUTOMATED ALERTS The organization employs automated mechanisms to alert security personnel of the following inappropriate or unusual activities with security implications: [Assignment: organization-defined activities that trigger alerts].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SI-4(12) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM MONITORING | AUTOMATED ALERTS The organization employs automated mechanisms to alert security personnel of the following inappropriate or unusual activities with security implications: [Assignment: organization-defined activities that trigger alerts].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SI-4(14) - Wireless Intrusion Detection
================================================================================

:Requirement:
    INFORMATION SYSTEM MONITORING | WIRELESS INTRUSION DETECTION The organization employs a wireless intrusion detection system to identify rogue wireless devices and to detect attack attempts and potential compromises/breaches to the information system.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SI-4(14) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM MONITORING | WIRELESS INTRUSION DETECTION The organization employs a wireless intrusion detection system to identify rogue wireless devices and to detect attack attempts and potential compromises/breaches to the information system.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SI-4(15) - Wireless To Wireline Communications
================================================================================

:Requirement:
    INFORMATION SYSTEM MONITORING | WIRELESS TO WIRELINE COMMUNICATIONS The organization employs an intrusion detection system to monitor wireless communications traffic as the traffic passes from wireless to wireline networks.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SI-4(15) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM MONITORING | WIRELESS TO WIRELINE COMMUNICATIONS The organization employs an intrusion detection system to monitor wireless communications traffic as the traffic passes from wireless to wireline networks.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SI-4(16) - Correlate Monitoring Information
================================================================================

:Requirement:
    INFORMATION SYSTEM MONITORING | CORRELATE MONITORING INFORMATION The organization correlates information from monitoring tools employed throughout the information system.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SI-4(16) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM MONITORING | CORRELATE MONITORING INFORMATION The organization correlates information from monitoring tools employed throughout the information system.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SI-4(19) - Individuals Posing Greater Risk
================================================================================

:Requirement:
    INFORMATION SYSTEM MONITORING | INDIVIDUALS POSING GREATER RISK The organization implements [Assignment: organization-defined additional monitoring] of individuals who have been identified by [Assignment: organization-defined sources] as posing an increased level of risk.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SI-4(19) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM MONITORING | INDIVIDUALS POSING GREATER RISK The organization implements [Assignment: organization-defined additional monitoring] of individuals who have been identified by [Assignment: organization-defined sources] as posing an increased level of risk.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SI-4(2) - Automated Tools For Real-time Analysis
================================================================================

:Requirement:
    INFORMATION SYSTEM MONITORING | AUTOMATED TOOLS FOR REAL-TIME ANALYSIS The organization employs automated tools to support near real-time analysis of events.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SI-4(2) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM MONITORING | AUTOMATED TOOLS FOR REAL-TIME ANALYSIS The organization employs automated tools to support near real-time analysis of events.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SI-4(20) - Privileged Users
================================================================================

:Requirement:
    INFORMATION SYSTEM MONITORING | PRIVILEGED USER The organization implements [Assignment: organization-defined additional monitoring] of privileged users.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SI-4(20) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM MONITORING | PRIVILEGED USER The organization implements [Assignment: organization-defined additional monitoring] of privileged users.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SI-4(22) - Unauthorized Network Services
================================================================================

:Requirement:
    INFORMATION SYSTEM MONITORING | UNAUTHORIZED NETWORK SERVICES The information system detects network services that have not been authorized or approved by [Assignment: organization-defined authorization or approval processes] and [Selection (one or more): audits; alerts [Assignment: organization-defined personnel or roles]].


Control Summary Information
---------------------------

:Role:
    OpenShift Landlord

:Status:
    Planned
:Origin:
    OpenShift Landlord SSP

SI-4(22) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM MONITORING | UNAUTHORIZED NETWORK SERVICES The information system detects network services that have not been authorized or approved by [Assignment: organization-defined authorization or approval processes] and [Selection (one or more): audits; alerts [Assignment: organization-defined personnel or roles]].
:Role:
    OpenShift Landlord
:Status:
    Planned
:Details:
    NEED TO ADDRESS







SI-4(23) - Host-based Devices
================================================================================

:Requirement:
    INFORMATION SYSTEM MONITORING | HOST-BASED DEVICES The organization implements [Assignment: organization-defined host-based monitoring mechanisms] at [Assignment: organization-defined information system components].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SI-4(23) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM MONITORING | HOST-BASED DEVICES The organization implements [Assignment: organization-defined host-based monitoring mechanisms] at [Assignment: organization-defined information system components].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SI-4(4) - Inbound And Outbound Communications Traffic
================================================================================

:Requirement:
    INFORMATION SYSTEM MONITORING | INBOUND AND OUTBOUND COMMUNICATIONS TRAFFIC The information system monitors inbound and outbound communications traffic [Assignment: organization-defined frequency] for unusual or unauthorized activities or conditions.


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SI-4(4) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM MONITORING | INBOUND AND OUTBOUND COMMUNICATIONS TRAFFIC The information system monitors inbound and outbound communications traffic [Assignment: organization-defined frequency] for unusual or unauthorized activities or conditions.
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.







SI-4(5) - System-generated Alerts
================================================================================

:Requirement:
    INFORMATION SYSTEM MONITORING | SYSTEM-GENERATED ALERTS The information system alerts [Assignment: organization-defined personnel or roles] when the following indications of compromise or potential compromise occur: [Assignment: organization-defined compromise indicators].


Control Summary Information
---------------------------

:Role:
    Parent organization

:Status:
    Inherited
:Origin:
    Inherited from pre-existing ATO

SI-4(5) What is the solution and how is it implemented?
--------------------------------------------------------------------------------



Part a
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Requirement:
    INFORMATION SYSTEM MONITORING | SYSTEM-GENERATED ALERTS The information system alerts [Assignment: organization-defined personnel or roles] when the following indications of compromise or potential compromise occur: [Assignment: organization-defined compromise indicators].
:Role:
    Parent organization
:Status:
    Inherited
:Details:
    Dependent on implementing organization / agency.








.. _`NIST SP800-53r4`: http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf
.. _`master_sctm.xlsx`: https://github.com/jason-callaway/openshift-compliance/raw/master/master_sctm.xlsx
.. _`GitHub`: https://github.com/jason-callaway/openshift-compliance