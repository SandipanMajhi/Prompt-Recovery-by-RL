## **5 Test case mapping**


The Test Case Mapping Table (TCMT) maps test cases to specific requirements in the ICS. The IUT is
tested in all roles for which support is declared in the ICS document.


The columns for the TCMT are defined as follows:


**Item:** Contains a logical expression based on specific entries from the associated ICS document.
Contains a logical expression (using the operators AND, OR, NOT as needed) based on specific entries
from the applicable ICS document(s). The entries are in the form of y/x references, where y corresponds
to the table number and x corresponds to the feature number as defined in the ICS document for
Hands-Free Profile (HFP) [3].


If a test case is mandatory within the respective layer, then the y/x reference is omitted.


**Feature:** A brief, informal description of the feature being tested.


**Test Case(s):** The applicable test case identifiers are required for Bluetooth Qualification if the
corresponding y/x references defined in the Item column are supported. Further details about the function
of the TCMT are elaborated in [5].


For the purpose and structure of the ICS/IXIT, refer to [5].























|Item|Feature|Test Case(s)|
|---|---|---|
|HFP 2/1 AND<br>HFP 2/1a|AG reconnects to HF|HFP/AG/OOR/BV-01-C|
|HFP 3/1 AND NOT<br>HFP 3/22|HF reconnects to AG|HFP/HF/OOR/BV-01-C|
|HFP 2/1 AND NOT<br>HFP 2/22|AG reconnects to HF|HFP/AG/OOR/BV-02-C|
|HFP 3/1|HF reconnects to AG|HFP/HF/OOR/BV-02-C|
|HFP 2/2|Phone status information: Transfer of<br>registration status, signal strength,<br>battery level, and Operator selection|HFP/AG/TRS/BV-01-C<br>HFP/AG/PSI/BV-01-C<br>HFP/AG/PSI/BV-03-C<br>HFP/AG/PSI/BV-04-C|
|HFP 3/2a|Phone status information: Transfer of<br>registration status and Enhanced Call<br>Status|HFP/HF/TRS/BV-01-C<br>HFP/HF/ECS/BV-03-C|
|HFP 2/2 AND<br>HFP 2/6|Phone status information: Transfer of<br>call status|HFP/AG/TCA/BV-01-C<br>HFP/AG/TCA/BV-02-C<br>HFP/AG/TCA/BV-03-C<br>HFP/AG/TCA/BV-04-C|
|(HFP 3/2a OR<br>HFP 3/2b) AND<br>HFP 3/6|Phone status information: Transfer of<br>call status|HFP/HF/TCA/BV-01-C<br>HFP/HF/TCA/BV-02-C<br>HFP/HF/TCA/BV-03-C<br>HFP/HF/TCA/BV-04-C|
|HFP 3/2c|Phone status information: signal<br>strength|HFP/HF/PSI/BV-01-C|
|HFP 2/2 AND<br>HFP 2/25|Phone status information: roaming|HFP/AG/PSI/BV-02-C|
|HFP 3/2d|Phone status information: roaming|HFP/HF/PSI/BV-02-C|


Bluetooth SIG Proprietary Page **181 of 218**


**Hands-Free Profile (HFP) /** Test Suite


































|Item|Feature|Test Case(s)|
|---|---|---|
|HFP 3/2e|Phone status information: battery<br>level|HFP/HF/PSI/BV-03-C|
|HFP 3/2f|Phone status information: Operator<br>selection|HFP/HF/PSI/BV-04-C|
|HFP 2/2 AND NOT<br>HFP 2/25|Phone status information: Roaming<br>not supported|HFP/AG/PSI/BV-05-C|
|HFP 2/3|Audio Connection handling (IUT is an<br>AG)|HFP/AG/ACR/BV-01-C<br>HFP/AG/ACR/BV-02-C<br>HFP/AG/ACS/BV-04-C<br>HFP/AG/ACS/BV-08-C<br>HFP/AG/ACS/BV-11-C<br>HFP/AG/ACS/BI-14-C|
|HFP 2/3a AND<br>HFP 2/3b|AG is IUT, AG Initiated, HF has eSCO|HFP/AG/ACS/BV-06-C|
|HFP 2/3a|AG is IUT, AG Initiated, HF is SCO<br>only or AG has eSCO allows only<br>SCO|HFP/AG/ACS/BV-02-C<br>HFP/AG/ACS/BV-10-C|
|HFP 3/3|Audio Connection handling (IUT is an<br>HF)|HFP/HF/ACR/BV-01-C<br>HFP/HF/ACR/BV-02-C<br>HFP/HF/ACS/BV-03-C<br>HFP/HF/ACS/BV-07-C<br>HFP/HF/ACS/BV-12-C<br>HFP/HF/ACS/BI-13-C|
|HFP 3/3a|HF is IUT, HF Initiated, AG is SCO<br>only or AG has eSCO allows only<br>SCO|HFP/HF/ACS/BV-01-C<br>HFP/HF/ACS/BV-09-C|
|HFP 3/3a AND<br>HFP 3/3b|HF is IUT, HF Initiated, AG has eSCO|HFP/HF/ACS/BV-05-C|
|HFP 2/4a OR<br>HFP 2/4b|Accept an Incoming Voice Call (AG)|HFP/AG/ICA/BV-06-C|
|HFP 3/4a OR<br>HFP 3/4b|Accept an Incoming Voice Call (AG)|HFP/HF/ICA/BV-06-C|
|HFP 2/4a|Accept an Incoming Voice Call (in-<br>band ring)|HFP/AG/ICA/BV-01-C|
|HFP 2/4a AND<br>HFP 2/4c|Accept an Incoming Voice Call (in-<br>band ring) and Capability to change<br>the “in-band ring” settings|HFP/AG/ICA/BV-02-C|
|HFP 3/4a|Accept an Incoming Voice Call (in-<br>band ring) and Capability to change<br>the “in-band ring” settings|HFP/HF/ICA/BV-01-C<br>HFP/HF/ICA/BV-02-C|
|HFP 3/4c|Accept an Incoming Voice Call<br>(muted in-band ring)|HFP/HF/ICA/BV-03-C|
|HFP 2/4b|Accept an Incoming Voice Call (no in-<br>band ring)|HFP/AG/ICA/BV-04-C|
|HFP 3/4b|Accept an Incoming Voice Call (no in-<br>band ring) and Audio Connection<br>establishment independent of call<br>processing|HFP/HF/ICA/BV-04-C<br>HFP/HF/ICA/BV-05-C|



Bluetooth SIG Proprietary Page **182 of 218**


**Hands-Free Profile (HFP) /** Test Suite
























|Item|Feature|Test Case(s)|
|---|---|---|
|HFP 2/3a AND<br>HFP 2/4b|Audio Connection establishment<br>independent of call processing|HFP/AG/ICA/BV-05-C|
|HFP 2/13|Caller ID|HFP/AG/CLI/BV-01-C|
|HFP 3/13|Caller ID|HFP/HF/CLI/BV-01-C|
|HFP 2/5|Reject an incoming call|HFP/AG/ICR/BV-01-C<br>HFP/AG/ICR/BV-02-C|
|HFP 3/5|Reject an incoming call|HFP/HF/ICR/BV-01-C<br>HFP/HF/ICR/BV-02-C|
|HFP 2/7|Audio Connection transfer|HFP/AG/ATA/BV-01-C<br>HFP/AG/ATH/BV-03-C<br>HFP/AG/ATH/BV-04-C<br>HFP/AG/ATH/BV-06-C|
|HFP 3/7|Audio Connection transfer|HFP/HF/ATA/BV-01-C<br>HFP/HF/ATH/BV-05-C<br>HFP/HF/ATH/BV-06-C|
|HFP 3/7a|Audio Connection transfer|HFP/HF/ATH/BV-04-C<br>HFP/HF/ATH/BV-03-C|
|HFP 2/7 AND<br>HFP 2/7a|Audio Connection transfer|HFP/AG/ATA/BV-02-C|
|HFP 3/7 AND<br>HFP 3/7a|Audio Connection transfer|HFP/HF/ATA/BV-02-C|
|HFP 2/7 AND<br>HFP 2/1a|Audio Connection transfer|HFP/AG/ATH/BV-05-C|
|HFP 2/8|Place call with the phone number<br>supplied by the HF|HFP/AG/OCN/BV-01-C|
|HFP 3/8|Place call with the phone number<br>supplied by the HF|HFP/HF/OCN/BV-01-C|
|HFP 2/9|Place call using memory dialing|HFP/AG/OCM/BV-01-C<br>HFP/AG/OCM/BV-02-C|
|HFP 3/9|Place call using memory dialing|HFP/HF/OCM/BV-01-C<br>HFP/HF/OCM/BV-02-C|
|HFP 2/10|Place call to the last number dialed|HFP/AG/OCL/BV-01-C<br>HFP/AG/OCL/BV-02-C|
|HFP 3/10|Place call to the last number dialed|HFP/HF/OCL/BV-01-C<br>HFP/HF/OCL/BV-02-C|
|HFP 2/11 AND<br>HFP 2/12a|Three-way calling|HFP/AG/TWC/BV-01-C|
|HFP 3/11 AND HFP<br>3/12 AND HFP 3/12a|Three-way calling|HFP/HF/TWC/BV-01-C|
|HFP 2/11 AND<br>HFP 2/12b|Three-way calling|HFP/AG/TWC/BV-02-C<br>HFP/AG/TWC/BV-03-C|
|HFP 3/11 AND HFP<br>3/12 AND HFP 3/12b|Three-way calling|HFP/HF/TWC/BV-02-C<br>HFP/HF/TWC/BV-03-C|
|HFP 2/11 AND<br>HFP 2/12c|Three-way calling|HFP/AG/TWC/BV-04-C|