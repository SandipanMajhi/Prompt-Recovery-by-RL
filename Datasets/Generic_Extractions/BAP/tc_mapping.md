## **5 Test case mapping**


The Test Case Mapping Table (TCMT) maps test cases to specific requirements in the ICS. The IUT is
tested in all roles for which support is declared in the ICS document.


The columns for the TCMT are defined as follows:


**Item:** Contains a logical expression based on specific entries from the associated ICS document.
Contains a logical expression (using the operators AND, OR, NOT as needed) based on specific entries
from the applicable ICS document(s). The entries are in the form of y/x references, where y corresponds
to the table number and x corresponds to the feature number as defined in the ICS document for BAP [4].


If a test case is mandatory within the respective layer, then the y/x reference is omitted.


**Feature:** A brief, informal description of the feature being tested.


**Test Case(s):** The applicable test case identifiers are required for Bluetooth Qualification if the
corresponding y/x references defined in the Item column are supported. Further details about the function
of the TCMT are elaborated in [2].


For the purpose and structure of the ICS/IXIT, refer to [2].


























|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 28/3 OR BAP 28/4 OR<br>BAP 85/3 OR BAP 85/4|Published Audio Capabilities<br>Service|BAP/CL/CGGIT/SER/BV-01-C|
|BAP 32/1 OR BAP 87/1|Sink PAC Characteristic|BAP/CL/CGGIT/CHA/BV-01-C|
|BAP 32/2 OR BAP 87/2|Sink Audio Locations<br>Characteristic|BAP/CL/CGGIT/CHA/BV-02-C|
|BAP 33/3|Source PAC Characteristic|BAP/CL/CGGIT/CHA/BV-03-C|
|BAP 33/4|Source Audio Locations<br>Characteristic|BAP/CL/CGGIT/CHA/BV-04-C|
|BAP 32/5|Available Audio Contexts<br>Characteristic|BAP/CL/CGGIT/CHA/BV-05-C|
|BAP 32/6|Supported Audio Contexts<br>Characteristic|BAP/CL/CGGIT/CHA/BV-06-C|
|BAP 28/1 OR BAP 28/2|Audio Stream Control Service|BAP/UCL/CGGIT/SER/BV-01-C|
|BAP 31/1|Sink ASE Characteristic|BAP/UCL/CGGIT/CHA/BV-01-C|
|BAP 31/2|Source ASE Characteristic|BAP/UCL/CGGIT/CHA/BV-02-C|
|BAP 31/3|ASE Control Point Characteristic|BAP/UCL/CGGIT/CHA/BV-03-C|
|BAP 85/1 OR BAP 85/2|Broadcast Audio Scan Service|BAP/BA/CGGIT/SER/BV-01-C|
|BAP 86/1|Broadcast Audio Scan Control<br>Point Characteristic|BAP/BA/CGGIT/CHA/BV-01-C|
|BAP 86/2|Broadcast Receive State<br>Characteristic|BAP/BA/CGGIT/CHA/BV-02-C|
|**Unicast Client – Discovery and Advertising**|**Unicast Client – Discovery and Advertising**|**Unicast Client – Discovery and Advertising**|
|BAP 29/2|Unicast Client – Discover Audio<br>Sink Capabilities|BAP/UCL/DISC/BV-01-C|
|BAP 29/1|Unicast Client – Discover Audio<br>Source Capabilities|BAP/UCL/DISC/BV-02-C|
|BAP 31/6|Unicast Client – Discover Sink<br>ASE_ID|BAP/UCL/DISC/BV-03-C|



Bluetooth SIG Proprietary Page **201 of 270**


**Basic Audio Profile (BAP) /** Test Suite












|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 31/7|Unicast Client – Discover Source<br>ASE_ID|BAP/UCL/DISC/BV-04-C|
|BAP 32/9|Unicast Client performs<br>Supported Audio Contexts<br>Discovery|BAP/UCL/DISC/BV-05-C|
|BAP 32/10|Unicast Client performs Available<br>Audio Contexts Discovery|BAP/UCL/DISC/BV-06-C<br>BAP/UCL/ADV/BV-01-C|
|BAP 29/2|Unicast Client Behavior – Sink<br>Role|BAP/UCL/PD/BV-03-C|
|BAP 29/1|Unicast Client Behavior – Source<br>Role|BAP/UCL/PD/BV-04-C|
|BAP 29/2 AND BAP 30/1|Presentation Delay with multiple<br>servers - Sink|BAP/UCL/PD/BV-01-C|
|BAP 29/1 AND BAP 30/1|Presentation Delay with multiple<br>servers - Source|BAP/UCL/PD/BV-02-C|
|**Discovery and Advertising**|**Discovery and Advertising**|**Discovery and Advertising**|
|BAP 8/1|Unicast Server – Expose Audio<br>Sink Capabilities|BAP/USR/DISC/BV-01-C|
|BAP 8/2|Unicast Server – Expose Audio<br>Source Capabilities|BAP/USR/DISC/BV-02-C|
|BAP 8/1 AND NOT BAP 8/2|Unicast Server – Expose Sink<br>ASE_ID|BAP/USR/DISC/BV-03-C|
|BAP 8/2 AND NOT BAP 8/1|Unicast Server – Expose Source<br>ASE_ID|BAP/USR/DISC/BV-04-C|
|BAP 8/1 AND BAP 8/2|Unicast Server – Expose Sink<br>and Source ASE_ID|BAP/USR/DISC/BV-05-C|
|BAP 9/5|Unicast Server – Expose<br>Available Audio Contexts|BAP/USR/DISC/BV-06-C|
|BAP 9/6|Unicast Server – Expose<br>Supported Audio Contexts|BAP/USR/DISC/BV-07-C|
|BAP 25/2 AND NOT BAP 3/2<br>AND BAP 7/9|Unicast Server General<br>Advertisements|BAP/USR/ADV/BV-01-C|
|BAP 25/2 AND BAP 3/2 AND<br>BAP 23/12 AND BAP 7/9|Unicast Server LE Extended<br>Advertising – BR/EDR/LE,<br>General Advertisements|BAP/USR/ADV/BV-02-C|
|BAP 25/2 AND BAP 3/2 AND<br>BAP 23/12 AND BAP 7/10|Unicast Server LE Extended<br>Advertising – BR/EDR/LE,<br>Targeted Advertisements|BAP/USR/ADV/BV-05-C|
|BAP 25/2 AND BAP 3/2 AND<br>NOT BAP 23/12 AND BAP<br>7/9|Unicast Server LE Extended<br>Advertising – No CTKD, General<br>Advertisements|BAP/USR/ADV/BV-03-C|
|BAP 25/2 AND BAP 3/2 AND<br>NOT BAP 23/12 AND<br>BAP 7/10|Unicast Server LE Extended<br>Advertising – No CTKD, Targeted<br>Advertisements|BAP/USR/ADV/BV-06-C|
|BAP 25/2 AND NOT BAP 3/2<br>AND BAP 7/10|Unicast Server Targeted<br>Advertisements|BAP/USR/ADV/BV-04-C|
|BAP 1/1 AND BAP 23/13<br>AND BAP 3/2|Unicast Server - CoD|BAP/USR/DEVD/BV-01-C|



Bluetooth SIG Proprietary Page **202 of 270**


**Basic Audio Profile (BAP) /** Test Suite










|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 1/4 AND BAP 74/18<br>AND BAP 3/2|Broadcast Sink - CoD|BAP/BSNK/DEVD/BV-01-C|
|BAP 1/5 AND BAP 80/19<br>AND BAP 3/2|Scan Delegator - CoD|BAP/SDE/DEVD/BV-01-C|
|BAP 1/3 AND BAP 60/5 AND<br>BAP 3/2|Broadcast Source - CoD|BAP/BSRC/DEVD/BV-01-C|
|BAP 1/6 AND BAP 90/18<br>AND BAP 3/2|Broadcast Assistant - CoD|BAP/BA/DEVD/BV-01-C|
|**Unicast Client – Generic**|**Unicast Client – Generic**|**Unicast Client – Generic**|
|**AC.1, 2, 4, 10**|**AC.1, 2, 4, 10**|**AC.1, 2, 4, 10**|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>BAP 44/2 AND BAP 33a/7|UCL Streaming – A.C.2: Generic|BAP/UCL/STR/BV-535-C<br>BAP/UCL/STR/BV-552-C<br>BAP/UCL/STR/BV-553-C<br>BAP/UCL/STR/BV-554-C<br>BAP/UCL/STR/BV-555-C<br>BAP/UCL/STR/BV-569-C|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12|UCL Streaming – A.C.2: Generic<br>w/ No A.C.10|BAP/UCL/STR/BV-568-C<br>BAP/UCL/STR/BV-570-C|



Bluetooth SIG Proprietary Page **203 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/2 AND BAP 33a/7<br>AND NOT BAP 44/14|||
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>BAP 44/2 AND BAP 33a/8|UCL Streaming – A.C.2: Generic,<br>QoS Config|BAP/UCL/STR/BV-539-C<br>BAP/UCL/STR/BV-560-C<br>BAP/UCL/STR/BV-561-C<br>BAP/UCL/STR/BV-562-C<br>BAP/UCL/STR/BV-563-C<br>BAP/UCL/STR/BV-581-C<br>|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR|UCL Streaming – A.C.2: Generic<br>w/ No A.C.10, QoS Config|BAP/UCL/STR/BV-580-C<br>BAP/UCL/STR/BV-582-C|



Bluetooth SIG Proprietary Page **204 of 270**


**Basic Audio Profile (BAP) /** Test Suite










|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/2 AND BAP 33a/8<br>AND NOT BAP 44/14|||
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>BAP 44/14 AND BAP 33a/7|UCL Streaming – A.C.10:<br>Generic|BAP/UCL/STR/BV-536-C<br>BAP/UCL/STR/BV-571-C<br>BAP/UCL/STR/BV-572-C<br>BAP/UCL/STR/BV-573-C|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>BAP 44/14 AND BAP 33a/8|UCL Streaming – A.C.10:<br>Generic, QoS Config|BAP/UCL/STR/BV-540-C<br>BAP/UCL/STR/BV-583-C<br>BAP/UCL/STR/BV-584-C<br>BAP/UCL/STR/BV-585-C|
|(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR|UCL Streaming – A.C.1: Generic|BAP/UCL/STR/BV-537-C<br>BAP/UCL/STR/BV-556-C|



Bluetooth SIG Proprietary Page **205 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/1 AND BAP 33a/3||BAP/UCL/STR/BV-557-C<br>BAP/UCL/STR/BV-558-C<br>BAP/UCL/STR/BV-559-C<br>BAP/UCL/STR/BV-575-C<br>|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/1 AND BAP 33a/3<br>AND NOT BAP 44/4|UCL Streaming – A.C.1: Generic<br>w/ No A.C.4|BAP/UCL/STR/BV-574-C<br>BAP/UCL/STR/BV-576-C|
|(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR|UCL Streaming – A.C.1: Generic,<br>QoS Config|BAP/UCL/STR/BV-541-C<br>BAP/UCL/STR/BV-564-C|



Bluetooth SIG Proprietary Page **206 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/1 AND BAP 33a/6||BAP/UCL/STR/BV-565-C<br>BAP/UCL/STR/BV-566-C<br>BAP/UCL/STR/BV-567-C<br>BAP/UCL/STR/BV-587-C<br>|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/1 AND BAP 33a/6<br>AND NOT BAP 44/4|UCL Streaming – A.C.1: Generic,<br>QoS Config w/ No A.C.4|BAP/UCL/STR/BV-586-C<br>BAP/UCL/STR/BV-588-C|



Bluetooth SIG Proprietary Page **207 of 270**


**Basic Audio Profile (BAP) /** Test Suite












|Item|Feature|Test Case(s)|
|---|---|---|
|(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/4 AND BAP 33a/3|UCL Streaming – A.C.4: Generic|BAP/UCL/STR/BV-538-C<br>BAP/UCL/STR/BV-577-C<br>BAP/UCL/STR/BV-578-C<br>BAP/UCL/STR/BV-579-C|
|(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/4 AND BAP 33a/6|UCL Streaming – A.C.4: Generic,<br>QoS Config|BAP/UCL/STR/BV-542-C<br>BAP/UCL/STR/BV-589-C<br>BAP/UCL/STR/BV-590-C<br>BAP/UCL/STR/BV-591-C|
|**A.C. 3, 5, 7(i)**|**A.C. 3, 5, 7(i)**|**A.C. 3, 5, 7(i)**|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR|UCL Streaming – A.C.3: Generic|BAP/UCL/STR/BV-523-C|



Bluetooth SIG Proprietary Page **208 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/3 AND BAP 33a/1|||
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15|UCL Streaming – A.C.3: Generic,<br>Enable, QoS|BAP/UCL/STR/BV-543-C|



Bluetooth SIG Proprietary Page **209 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|OR BAP 41/16) AND<br>BAP 44/3 AND BAP 33a/2|||
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/3 AND BAP 33a/4|UCL Streaming – A.C.3: Generic,<br>QoS, Enable|BAP/UCL/STR/BV-546-C|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15|UCL Streaming – A.C.3: Generic,<br>QoS, QoS|BAP/UCL/STR/BV-549-C|



Bluetooth SIG Proprietary Page **210 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/3 AND BAP 33a/5|||
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/5 OR<br>BAP 39/6 OR BAP 39/8 OR<br>BAP 39/7 OR BAP 39/9 OR<br>BAP 39/10 OR BAP 39/11<br>OR BAP 39/12 OR<br>BAP 39/13 OR BAP 39/14<br>OR BAP 39/15 OR<br>BAP 39/16 OR BAP 41/1 OR<br>BAP 41/2 OR BAP 41/3 OR<br>BAP 41/5 OR BAP 41/6 OR<br>BAP 41/7 OR BAP 41/8 OR<br>BAP 41/9 OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/5 AND BAP 33a/1|UCL Streaming – A.C.5: Generic|BAP/UCL/STR/BV-524-C|



Bluetooth SIG Proprietary Page **211 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/5 OR<br>BAP 39/6 OR BAP 39/8 OR<br>BAP 39/7 OR BAP 39/9 OR<br>BAP 39/10 OR BAP 39/11<br>OR BAP 39/12 OR<br>BAP 39/13 OR BAP 39/14<br>OR BAP 39/15 OR<br>BAP 39/16 OR BAP 41/1 OR<br>BAP 41/2 OR BAP 41/3 OR<br>BAP 41/5 OR BAP 41/6 OR<br>BAP 41/7 OR BAP 41/8 OR<br>BAP 41/9 OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/5 AND BAP 33a/2|UCL Streaming – A.C.5: Generic,<br>Enable, QoS|BAP/UCL/STR/BV-544-C|



Bluetooth SIG Proprietary Page **212 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/5 OR<br>BAP 39/6 OR BAP 39/8 OR<br>BAP 39/7 OR BAP 39/9 OR<br>BAP 39/10 OR BAP 39/11<br>OR BAP 39/12 OR<br>BAP 39/13 OR BAP 39/14<br>OR BAP 39/15 OR<br>BAP 39/16 OR BAP 41/1 OR<br>BAP 41/2 OR BAP 41/3 OR<br>BAP 41/5 OR BAP 41/6 OR<br>BAP 41/7 OR BAP 41/8 OR<br>BAP 41/9 OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/5 AND BAP 33a/4|UCL Streaming – A.C.5: Generic,<br>QoS, Enable|BAP/UCL/STR/BV-547-C|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/5 OR|UCL Streaming – A.C.5: Generic,<br>QoS, QoS|BAP/UCL/STR/BV-550-C|



Bluetooth SIG Proprietary Page **213 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 39/6 OR BAP 39/8 OR<br>BAP 39/7 OR BAP 39/9 OR<br>BAP 39/10 OR BAP 39/11<br>OR BAP 39/12 OR<br>BAP 39/13 OR BAP 39/14<br>OR BAP 39/15 OR<br>BAP 39/16 OR BAP 41/1 OR<br>BAP 41/2 OR BAP 41/3 OR<br>BAP 41/5 OR BAP 41/6 OR<br>BAP 41/7 OR BAP 41/8 OR<br>BAP 41/9 OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/5 AND BAP 33a/5|||
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/8 AND BAP 33a/1|UCL Streaming – A.C.7(i):<br>Generic|BAP/UCL/STR/BV-525-C|



Bluetooth SIG Proprietary Page **214 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/8 AND BAP 33a/2|UCL Streaming – A.C.7(i):<br>Generic, Enable, QoS|BAP/UCL/STR/BV-545-C|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR|UCL Streaming – A.C.7(i):<br>Generic, QoS, Enable|BAP/UCL/STR/BV-548-C|



Bluetooth SIG Proprietary Page **215 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/8 AND BAP 33a/4|||
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/8 AND BAP 33a/5|UCL Streaming – A.C.7(i):<br>Generic, QoS, QoS|BAP/UCL/STR/BV-551-C|



Bluetooth SIG Proprietary Page **216 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|**Other A.C. Config**|**Other A.C. Config**|**Other A.C. Config**|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR BAP<br>38/14 OR BAP 38/15 OR<br>BAP 38/16 OR BAP 40/1 OR<br>BAP 40/2 OR BAP 40/3 OR<br>BAP 40/4 OR BAP 40/5 OR<br>BAP 40/6 OR BAP 40/7 OR<br>BAP 40/8 OR BAP 40/9 OR<br>BAP 40/10 OR BAP 40/11<br>OR BAP 40/12 OR BAP<br>40/13 OR BAP 40/14 OR<br>BAP 40/15 OR BAP 40/16)<br>AND (BAP 39/1 OR BAP 39/2<br>OR BAP 39/3 OR BAP 39/4<br>OR BAP 39/5 OR BAP 39/6<br>OR BAP 39/8 OR BAP 39/7<br>OR BAP 39/9 OR BAP 39/10<br>OR BAP 39/11 OR BAP<br>39/12 OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR BAP<br>41/11 OR BAP 41/12 OR<br>BAP 41/13 OR BAP 41/14<br>OR BAP 41/15 OR BAP<br>41/16) AND BAP 44/9|UCL Streaming – A.C.7(ii):<br>Generic|BAP/UCL/STR/BV-526-C|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR BAP<br>38/14 OR BAP 38/15 OR<br>BAP 38/16 OR BAP 40/1 OR<br>BAP 40/2 OR BAP 40/3 OR<br>BAP 40/4 OR BAP 40/5 OR<br>BAP 40/6 OR BAP 40/7 OR<br>BAP 40/8 OR BAP 40/9 OR<br>BAP 40/10 OR BAP 40/11<br>OR BAP 40/12 OR BAP<br>40/13 OR BAP 40/14 OR<br>BAP 40/15 OR BAP 40/16)<br>AND (BAP 39/1 OR BAP 39/2<br>OR BAP 39/3 OR BAP 39/4<br>OR BAP 39/5 OR BAP 39/6|UCL Streaming – A.C.8(i):<br>Generic|BAP/UCL/STR/BV-531-C|



Bluetooth SIG Proprietary Page **217 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|OR BAP 39/8 OR BAP 39/7<br>OR BAP 39/9 OR BAP 39/10<br>OR BAP 39/11 OR BAP<br>39/12 OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR BAP<br>41/11 OR BAP 41/12 OR<br>BAP 41/13 OR BAP 41/14<br>OR BAP 41/15 OR BAP<br>41/16) AND BAP 44/10|||
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/11|UCL Streaming – A.C.8(ii):<br>Generic|BAP/UCL/STR/BV-532-C|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR|UCL Streaming – A.C.11(i):<br>Generic|BAP/UCL/STR/BV-533-C|



Bluetooth SIG Proprietary Page **218 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/15|||
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR|UCL Streaming – A.C.11(ii):<br>Generic|BAP/UCL/STR/BV-534-C|



Bluetooth SIG Proprietary Page **219 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/16|||
|**Sink Only**|**Sink Only**|**Sink Only**|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>BAP 44/6|UCL Streaming – A.C.6(i):<br>Generic|BAP/UCL/STR/BV-527-C|
|(BAP 38/1 OR BAP 38/2 OR<br>BAP 38/3 OR BAP 38/4 OR<br>BAP 38/5 OR BAP 38/6 OR<br>BAP 38/7 OR BAP 38/8 OR<br>BAP 38/9 OR BAP 38/10 OR<br>BAP 38/11 OR BAP 38/12<br>OR BAP 38/13 OR<br>BAP 38/14 OR BAP 38/15<br>OR BAP 38/16 OR BAP 40/1<br>OR BAP 40/2 OR BAP 40/3<br>OR BAP 40/4 OR BAP 40/5<br>OR BAP 40/6 OR BAP 40/7<br>OR BAP 40/8 OR BAP 40/9<br>OR BAP 40/10 OR<br>BAP 40/11 OR BAP 40/12<br>OR BAP 40/13 OR<br>BAP 40/14 OR BAP 40/15<br>OR BAP 40/16) AND<br>BAP 44/7|UCL Streaming – A.C.6(ii):<br>Generic|BAP/UCL/STR/BV-528-C|



Bluetooth SIG Proprietary Page **220 of 270**


**Basic Audio Profile (BAP) /** Test Suite










|Item|Feature|Test Case(s)|
|---|---|---|
|**Source Only**|**Source Only**|**Source Only**|
|(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/12|UCL Streaming – A.C.9(i):<br>Generic|BAP/UCL/STR/BV-529-C|
|(BAP 39/1 OR BAP 39/2 OR<br>BAP 39/3 OR BAP 39/4 OR<br>BAP 39/5 OR BAP 39/6 OR<br>BAP 39/8 OR BAP 39/7 OR<br>BAP 39/9 OR BAP 39/10 OR<br>BAP 39/11 OR BAP 39/12<br>OR BAP 39/13 OR<br>BAP 39/14 OR BAP 39/15<br>OR BAP 39/16 OR BAP 41/1<br>OR BAP 41/2 OR BAP 41/3<br>OR BAP 41/4 OR BAP 41/5<br>OR BAP 41/6 OR BAP 41/7<br>OR BAP 41/8 OR BAP 41/9<br>OR BAP 41/10 OR<br>BAP 41/11 OR BAP 41/12<br>OR BAP 41/13 OR<br>BAP 41/14 OR BAP 41/15<br>OR BAP 41/16) AND<br>BAP 44/13|UCL Streaming – A.C.9(ii):<br>Generic|BAP/UCL/STR/BV-530-C|
|**Unicast Client – LC3 8_1**|**Unicast Client – LC3 8_1**|**Unicast Client – LC3 8_1**|
|BAP 36/1|Unicast Client as Audio Sink<br>Initiates Config Codec – LC3 8_1|BAP/UCL/SCC/BV-017-C|
|BAP 38/1|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 8_1_1|BAP/UCL/SCC/BV-051-C|
|BAP 40/1|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 8_1_2|BAP/UCL/SCC/BV-083-C|
|BAP 37/1|Unicast Client as Audio Source<br>initiates Config Codec – LC3 8_1|BAP/UCL/SCC/BV-001-C|



Bluetooth SIG Proprietary Page **221 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 39/1|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 8_1_1|BAP/UCL/SCC/BV-035-C|
|BAP 41/1|QoS Configuration – Unicast<br>Client as Audio Source - LC3 –<br>High Reliability – 8_1_2|BAP/UCL/SCC/BV-067-C|
|**Unicast Client – LC3 8_2**|**Unicast Client – LC3 8_2**|**Unicast Client – LC3 8_2**|
|BAP 36/2|Unicast Client as Audio Sink<br>Initiates Config Codec – LC3 8_2|BAP/UCL/SCC/BV-018-C|
|BAP 38/2|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 8_2_1|BAP/UCL/SCC/BV-052-C|
|BAP 40/2|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 8_2_2|BAP/UCL/SCC/BV-084-C|
|BAP 37/2|Unicast Client as Audio Source<br>initiates Config Codec – LC3 8_2|BAP/UCL/SCC/BV-002-C|
|BAP 39/2|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 8_2_1|BAP/UCL/SCC/BV-036-C|
|BAP 41/2|QoS Configuration – Unicast<br>Client as Audio Source - LC3 –<br>High Reliability – 8_2_2|BAP/UCL/SCC/BV-068-C|
|**Unicast Client – LC3 16_1**|**Unicast Client – LC3 16_1**|**Unicast Client – LC3 16_1**|
|BAP 36/3|Unicast Client as Audio Sink<br>Initiates Config Codec – LC3<br>16_1|BAP/UCL/SCC/BV-019-C|
|BAP 38/3|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 16_1_1|BAP/UCL/SCC/BV-053-C|
|BAP 40/3|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 16_1_2|BAP/UCL/SCC/BV-085-C|
|BAP 37/3|Unicast Client as Audio Source<br>initiates Config Codec – LC3<br>16_1|BAP/UCL/SCC/BV-003-C|
|BAP 39/3|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 16_1_1|BAP/UCL/SCC/BV-037-C|
|BAP 41/3|QoS Configuration – Unicast<br>Client as Audio Source - LC3 –<br>High Reliability – 16_1_2|BAP/UCL/SCC/BV-069-C|
|**Unicast Client – LC3 16_2**|**Unicast Client – LC3 16_2**|**Unicast Client – LC3 16_2**|
|BAP 36/4|Unicast Client as Audio Sink<br>Initiates Config Codec – LC3<br>16_2|BAP/UCL/SCC/BV-020-C|
|BAP 38/4|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 16_2_1|BAP/UCL/SCC/BV-054-C|



Bluetooth SIG Proprietary Page **222 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 40/4|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 16_2_2|BAP/UCL/SCC/BV-086-C|
|BAP 37/4|Unicast Client as Audio Source<br>initiates Config Codec – LC3<br>16_2|BAP/UCL/SCC/BV-004-C|
|BAP 39/4|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 16_2_1|BAP/UCL/SCC/BV-038-C|
|BAP 41/4|QoS Configuration – Unicast<br>Client as Audio Source - LC3 –<br>High Reliability – 16_2_2|BAP/UCL/SCC/BV-070-C|
|**Unicast Client – LC3 24_1**|**Unicast Client – LC3 24_1**|**Unicast Client – LC3 24_1**|
|BAP 36/5|Unicast Client as Audio Sink<br>Initiates Config Codec – LC3<br>24_1|BAP/UCL/SCC/BV-021-C|
|BAP 38/5|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 24_1_1|BAP/UCL/SCC/BV-055-C|
|BAP 41/5|QoS Configuration – Unicast<br>Client as Audio Source - LC3 -<br>High Reliability - 24_1_2|BAP/UCL/SCC/BV-071-C|
|BAP 37/5|Unicast Client as Audio Source<br>initiates Config Codec – LC3<br>24_1|BAP/UCL/SCC/BV-005-C|
|BAP 39/5|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 24_1_1|BAP/UCL/SCC/BV-039-C|
|BAP 40/5|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 24_1_2|BAP/UCL/SCC/BV-087-C|
|**Unicast Client – LC3 24_2**|**Unicast Client – LC3 24_2**|**Unicast Client – LC3 24_2**|
|BAP 36/6|Unicast Client as Audio Sink<br>Initiates Config Codec – LC3<br>24_2|BAP/UCL/SCC/BV-022-C|
|BAP 38/6|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 24_2_1|BAP/UCL/SCC/BV-056-C|
|BAP 40/6|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 24_2_2|BAP/UCL/SCC/BV-088-C|
|BAP 37/6|Unicast Client as Audio Source<br>initiates Config Codec – LC3<br>24_2|BAP/UCL/SCC/BV-006-C|



Bluetooth SIG Proprietary Page **223 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 39/6|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 24_2_1|BAP/UCL/SCC/BV-040-C|
|BAP 41/6|QoS Configuration – Unicast<br>Client as Audio Source - LC3 –<br>High Reliability – 24_2_2|BAP/UCL/SCC/BV-072-C|
|**Unicast Client – LC3 32_1**|**Unicast Client – LC3 32_1**|**Unicast Client – LC3 32_1**|
|BAP 36/7|Unicast Client as Audio Sink<br>Initiates Config Codec with LC3<br>32_1|BAP/UCL/SCC/BV-023-C|
|BAP 38/7|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 32_1_1|BAP/UCL/SCC/BV-057-C|
|BAP 40/7|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 32_1_2|BAP/UCL/SCC/BV-089-C|
|BAP 37/7|Unicast Client as Audio Source<br>initiates Config Codec – LC3<br>32_1|BAP/UCL/SCC/BV-007-C|
|BAP 39/7|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 32_1_1|BAP/UCL/SCC/BV-041-C|
|BAP 41/7|QoS – Unicast Client as Audio<br>Source - LC3 – High Reliability –<br>32_1_2|BAP/UCL/SCC/BV-073-C|
|**Unicast Client – LC3 32_2**|**Unicast Client – LC3 32_2**|**Unicast Client – LC3 32_2**|
|BAP 36/8|Unicast Client as Audio Sink<br>Initiates Config Codec with LC3<br>32_2|BAP/UCL/SCC/BV-024-C|
|BAP 38/8|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 32_2_1|BAP/UCL/SCC/BV-058-C|
|BAP 40/8|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 32_2_2|BAP/UCL/SCC/BV-090-C|
|BAP 37/8|Unicast Client as Audio Source<br>initiates Config Codec – LC3<br>32_2|BAP/UCL/SCC/BV-008-C|
|BAP 39/8|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 32_2_1|BAP/UCL/SCC/BV-042-C|
|BAP 41/8|QoS Configuration – Unicast<br>Client as Audio Source - LC3 –<br>High Reliability – 32_2_2|BAP/UCL/SCC/BV-074-C|



Bluetooth SIG Proprietary Page **224 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|**Unicast Client – LC3 441_1**|**Unicast Client – LC3 441_1**|**Unicast Client – LC3 441_1**|
|BAP 36/9|Unicast Client as Audio Sink<br>Initiates Config Codec with LC3<br>441_1|BAP/UCL/SCC/BV-025-C|
|BAP 38/9|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 441_1_1|BAP/UCL/SCC/BV-059-C|
|BAP 40/9|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 441_1_2|BAP/UCL/SCC/BV-091-C|
|BAP 37/9|Unicast Client as Audio Source<br>initiates Config Codec – LC3<br>441_1|BAP/UCL/SCC/BV-009-C|
|BAP 39/9|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 441_1_1|BAP/UCL/SCC/BV-043-C|
|BAP 41/9|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>High Reliability – 441_1_2|BAP/UCL/SCC/BV-075-C|
|**Unicast Client – LC3 441_2**|**Unicast Client – LC3 441_2**|**Unicast Client – LC3 441_2**|
|BAP 36/10|Unicast Client as Audio Sink<br>Initiates Config Codec with LC3<br>441_2|BAP/UCL/SCC/BV-026-C|
|BAP 38/10|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 441_2_1|BAP/UCL/SCC/BV-060-C|
|BAP 40/10|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 441_2_2|BAP/UCL/SCC/BV-092-C|
|BAP 37/10|Unicast Client as Audio Source<br>initiates Config Codec – LC3<br>441_2|BAP/UCL/SCC/BV-010-C|
|BAP 39/10|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 441_2_1|BAP/UCL/SCC/BV-044-C|
|BAP 41/10|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>High Reliability – 441_2_2|BAP/UCL/SCC/BV-076-C|
|**Unicast Client – LC3 48_1**|**Unicast Client – LC3 48_1**|**Unicast Client – LC3 48_1**|
|BAP 36/11|Unicast Client as Audio Sink<br>Initiates Config Codec with LC3<br>48_1|BAP/UCL/SCC/BV-027-C|
|BAP 38/11|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 48_1_1|BAP/UCL/SCC/BV-061-C|
|BAP 40/11|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 48_1_2|BAP/UCL/SCC/BV-093-C|



Bluetooth SIG Proprietary Page **225 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 37/11|Unicast Client as Audio Source<br>initiates Config Codec – LC3<br>48_1|BAP/UCL/SCC/BV-011-C|
|BAP 39/11|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 48_1_1|BAP/UCL/SCC/BV-045-C|
|BAP 41/11|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>High Reliability – 48_1_2|BAP/UCL/SCC/BV-077-C|
|**Unicast Client – LC3 48_2**|**Unicast Client – LC3 48_2**|**Unicast Client – LC3 48_2**|
|BAP 36/12|Unicast Client as Audio Sink<br>Initiates Config Codec with LC3<br>48_2|BAP/UCL/SCC/BV-028-C|
|BAP 38/12|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 48_2_1|BAP/UCL/SCC/BV-062-C|
|BAP 40/12|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 48_2_2|BAP/UCL/SCC/BV-094-C|
|BAP 37/12|Unicast Client as Audio Source<br>initiates Config Codec – LC3<br>48_2|BAP/UCL/SCC/BV-012-C|
|BAP 39/12|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 48_2_1|BAP/UCL/SCC/BV-046-C|
|BAP 41/12|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>High Reliability – 48_2_2|BAP/UCL/SCC/BV-078-C|
|**Unicast Client – LC3 48_3**|**Unicast Client – LC3 48_3**|**Unicast Client – LC3 48_3**|
|BAP 36/13|Unicast Client as Audio Sink<br>Initiates Config Codec with LC3<br>48_3|BAP/UCL/SCC/BV-029-C|
|BAP 38/13|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 48_3_1|BAP/UCL/SCC/BV-063-C|
|BAP 40/13|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 48_3_2|BAP/UCL/SCC/BV-095-C|
|BAP 37/13|Unicast Client as Audio Source<br>initiates Config Codec – LC3<br>48_3|BAP/UCL/SCC/BV-013-C|
|BAP 39/13|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 48_3_1|BAP/UCL/SCC/BV-047-C|
|BAP 41/13|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>High Reliability – 48_3_2|BAP/UCL/SCC/BV-079-C|



Bluetooth SIG Proprietary Page **226 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|**Unicast Client – LC3 48_4**|**Unicast Client – LC3 48_4**|**Unicast Client – LC3 48_4**|
|BAP 36/14|Unicast Client as Audio Sink<br>Initiates Config Codec with LC3<br>48_4|BAP/UCL/SCC/BV-030-C|
|BAP 38/14|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 48_4_1|BAP/UCL/SCC/BV-064-C|
|BAP 40/14|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 48_4_2|BAP/UCL/SCC/BV-096-C|
|BAP 37/14|Unicast Client as Audio Source<br>initiates Config Codec – LC3<br>48_4|BAP/UCL/SCC/BV-014-C|
|BAP 39/14|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 48_4_1|BAP/UCL/SCC/BV-048-C|
|BAP 41/14|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>High Reliability – 48_4_2|BAP/UCL/SCC/BV-080-C|
|**Unicast Client – LC3 48_5**|**Unicast Client – LC3 48_5**|**Unicast Client – LC3 48_5**|
|BAP 36/15|Unicast Client as Audio Sink<br>Initiates Config Codec LC3<br>Setting 48_5|BAP/UCL/SCC/BV-031-C|
|BAP 38/15|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 48_5_1|BAP/UCL/SCC/BV-065-C|
|BAP 40/15|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 48_5_2|BAP/UCL/SCC/BV-097-C|
|BAP 37/15|Unicast Client as Audio Source<br>initiates Config Codec – LC3<br>48_5|BAP/UCL/SCC/BV-015-C|
|BAP 39/15|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 48_5_1|BAP/UCL/SCC/BV-049-C|
|BAP 41/15|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>High Reliability – 48_5_2|BAP/UCL/SCC/BV-081-C|
|**Unicast Client – LC3 48_6**|**Unicast Client – LC3 48_6**|**Unicast Client – LC3 48_6**|
|BAP 36/16|Unicast Client as Audio Sink<br>Initiates Config Codec – LC3<br>Setting 48_6|BAP/UCL/SCC/BV-032-C|
|BAP 38/16|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 – Low<br>Latency - 48_6_1|BAP/UCL/SCC/BV-066-C|
|BAP 40/16|QoS Configuration – Unicast<br>Client as Audio Sink – LC3 –<br>High Reliability – 48_6_2|BAP/UCL/SCC/BV-098-C|



Bluetooth SIG Proprietary Page **227 of 270**


**Basic Audio Profile (BAP) /** Test Suite










|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 37/16|Unicast Client as Audio Source<br>initiates Config Codec – LC3<br>48_6|BAP/UCL/SCC/BV-016-C|
|BAP 39/16|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>Low Latency - 48_6_1|BAP/UCL/SCC/BV-050-C|
|BAP 41/16|QoS Configuration – Unicast<br>Client as Audio Source – LC3 –<br>High Reliability – 48_6_1|BAP/UCL/SCC/BV-082-C|
|**Unicast Client – Vendor Specific**|**Unicast Client – Vendor Specific**|**Unicast Client – Vendor Specific**|
|BAP 37/17|Unicast Client as Audio Source –<br>Config Codec – Vendor-Specific<br>Codec Setting|BAP/UCL/SCC/BV-033-C|
|BAP 43/1|QoS Configuration – Unicast<br>Client as Audio Source – Vendor-<br>Specific Codec Settings|BAP/UCL/SCC/BV-100-C|
|BAP 36/17|Unicast Client is Audio Sink –<br>Config Codec – Vendor-Specific<br>Codec Setting|BAP/UCL/SCC/BV-034-C|
|BAP 42/1|QoS Configuration – Unicast<br>Client as Audio Sink – Vendor-<br>Specific Codec Settings|BAP/UCL/SCC/BV-099-C|
|BAP 36/17 AND BAP 44/1|UCL Source Streaming A.C.1 - 1<br>Server 1 Stream 1 Channel – VS<br>Codec|BAP/UCL/STR/BV-129-C|
|BAP 36/17 AND BAP 44/4|UCL Source Streaming A.C.4 - 1<br>Server 1 Stream 2 Channels –<br>VS Codec|BAP/UCL/STR/BV-130-C|
|BAP 37/17 AND BAP 44/2|UCL Sink Streaming A.C.2 - 1<br>Server 1 Stream 1 Channel – VS<br>Codec|BAP/UCL/STR/BV-131-C|
|BAP 37/17 AND BAP 44/14|UCL Sink Streaming A.C.10 - 1<br>Server 1 Stream 2 Channels –<br>VS Codec|BAP/UCL/STR/BV-132-C|
|BAP 42/1 AND BAP 43/1<br>AND BAP 44/3|UCL Streaming – A.C.3: 1<br>Server, 1 Sink ASE, 1 Source<br>ASE, 2 Sink Channels, 2 Streams<br>Vendor-specific Codec Settings|BAP/UCL/STR/BV-229-C|
|BAP 42/1 AND BAP 43/1<br>AND BAP 44/5|UCL Streaming A.C.5 - 1 Server<br>2 Streams 1 Sink 1 Source – VS<br>Codec|BAP/UCL/STR/BV-230-C|
|BAP 42/1 AND BAP 43/1<br>AND BAP 44/8|UCL Streaming A.C.7(i) 1 Server<br>2 Streams 1 Sink 1 Source – VS<br>Codec|BAP/UCL/STR/BV-231-C|
|BAP 42/1 AND BAP 43/1<br>AND BAP 44/6|UCL Streaming – A.C.6(i): 1<br>Server, 2 Sink ASEs, 2 CISes, 2<br>Streams – VS Codec|BAP/UCL/STR/BV-296-C|



Bluetooth SIG Proprietary Page **228 of 270**


**Basic Audio Profile (BAP) /** Test Suite














|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 42/1 AND BAP 43/1<br>AND BAP 44/7|UCL Streaming – A.C.6(ii): 2<br>Server, 2 Source ASEs, 2 CISes,<br>2 Streams – VS Codec|BAP/UCL/STR/BV-329-C|
|BAP 42/1 AND BAP 43/1<br>AND BAP 44/16|UCL Streaming – A.C.11(ii): 2<br>Servers, 2 CISes, 4 streams – VS<br>Codec|BAP/UCL/STR/BV-522-C|
|**Unicast Server**|**Unicast Server**|**Unicast Server**|
|**Unicast Server - Generic**|**Unicast Server - Generic**|**Unicast Server - Generic**|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6<br>OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/5 OR BAP 17/6<br>OR BAP 17/7 OR BAP 17/8<br>OR BAP 17/9 OR BAP 17/10<br>OR BAP 17/11 OR BAP<br>17/12 OR BAP 17/13 OR<br>BAP 17/14 OR BAP 17/15<br>OR BAP 17/16) AND BAP<br>20/1 AND BAP 9a/3|USR Streaming – A.C.1: Generic|BAP/USR/STR/BV-367-C|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR|USR Streaming – A.C.1: Generic,<br>QoS|BAP/USR/STR/BV-371-C|



Bluetooth SIG Proprietary Page **229 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6<br>OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/5 OR BAP 17/6<br>OR BAP 17/7 OR BAP 17/8<br>OR BAP 17/9 OR BAP 17/10<br>OR BAP 17/11 OR BAP<br>17/12 OR BAP 17/13 OR<br>BAP 17/14 OR BAP 17/15<br>OR BAP 17/16) AND BAP<br>20/1 AND BAP 9a/6|||
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/5<br>OR BAP 15/6 OR BAP 15/7<br>OR BAP 15/8 OR BAP 15/9<br>OR BAP 15/10 OR BAP<br>15/11 OR BAP 15/12 OR<br>BAP 15/13 OR BAP 15/14<br>OR BAP 15/15 OR BAP<br>15/16 OR BAP 17/1 OR BAP<br>17/2 OR BAP 17/3 OR BAP<br>17/4 OR BAP 17/5 OR BAP<br>17/6 OR BAP 17/7 OR BAP<br>17/8 OR BAP 17/9 OR BAP<br>17/10 OR BAP 17/11 OR<br>BAP 17/12 OR BAP 17/13|USR Streaming – A.C.4: Generic|BAP/USR/STR/BV-368-C|



Bluetooth SIG Proprietary Page **230 of 270**


**Basic Audio Profile (BAP) /** Test Suite










|Item|Feature|Test Case(s)|
|---|---|---|
|OR BAP 17/14 OR BAP<br>17/15 OR BAP 17/16) AND<br>BAP 20/4 AND BAP 9a/3|||
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/5<br>OR BAP 15/6 OR BAP 15/7<br>OR BAP 15/8 OR BAP 15/9<br>OR BAP 15/10 OR BAP<br>15/11 OR BAP 15/12 OR<br>BAP 15/13 OR BAP 15/14<br>OR BAP 15/15 OR BAP<br>15/16 OR BAP 17/1 OR BAP<br>17/2 OR BAP 17/3 OR BAP<br>17/4 OR BAP 17/5 OR BAP<br>17/6 OR BAP 17/7 OR BAP<br>17/8 OR BAP 17/9 OR BAP<br>17/10 OR BAP 17/11 OR<br>BAP 17/12 OR BAP 17/13<br>OR BAP 17/14 OR BAP<br>17/15 OR BAP 17/16) AND<br>BAP 20/4 AND BAP 9a/6|USR Streaming – A.C.4: Generic,<br>QoS|BAP/USR/STR/BV-372-C|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2|USR Streaming – A.C.2: Generic|BAP/USR/STR/BV-369-C|



Bluetooth SIG Proprietary Page **231 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|OR BAP 15/3 OR BAP 16/4<br>OR BAP 15/5 OR BAP 15/6<br>OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/2 AND<br>BAP 9a/7|||
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 16/4<br>OR BAP 15/5 OR BAP 15/6<br>OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/2 AND<br>BAP 9a/8|USR Streaming – A.C.2: Generic,<br>QoS|BAP/USR/STR/BV-373-C|



Bluetooth SIG Proprietary Page **232 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6<br>OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/10 AND<br>BAP 9a/7|USR Streaming – A.C.10:<br>Generic|BAP/USR/STR/BV-370-C|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6|USR Streaming – A.C.10:<br>Generic, QoS|BAP/USR/STR/BV-374-C|



Bluetooth SIG Proprietary Page **233 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/10 AND<br>BAP 9a/8|||
|**A.C. 3, 5, and 7(i)**|**A.C. 3, 5, and 7(i)**|**A.C. 3, 5, and 7(i)**|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6<br>OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/3 AND<br>BAP 9a/1|USR Streaming – A.C.3: Generic|BAP/USR/STR/BV-360-C|



Bluetooth SIG Proprietary Page **234 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6<br>OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/3 AND<br>BAP 9a/2|USR Streaming – A.C.3: Generic,<br>Enable, QoS|BAP/USR/STR/BV-375-C|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6|USR Streaming – A.C.3: Generic,<br>QoS, Enable|BAP/USR/STR/BV-378-C|



Bluetooth SIG Proprietary Page **235 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/3 AND<br>BAP 9a/4|||
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6<br>OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/3 AND<br>BAP 9a/5|USR Streaming – A.C.3: Generic,<br>QoS, QoS|BAP/USR/STR/BV-381-C|



Bluetooth SIG Proprietary Page **236 of 270**


**Basic Audio Profile (BAP) /** Test Suite










|Item|Feature|Test Case(s)|
|---|---|---|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6<br>OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/5 AND<br>BAP 9a/1|USR Streaming – A.C.5: Generic|BAP/USR/STR/BV-361-C|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6|USR Streaming – A.C.5: Generic,<br>Enable, QoS|BAP/USR/STR/BV-376-C|



Bluetooth SIG Proprietary Page **237 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/5 AND<br>BAP 9a/2|||
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6<br>OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/5 AND<br>BAP 9a/4|USR Streaming – A.C.5: Generic,<br>QoS, Enable|BAP/USR/STR/BV-379-C|



Bluetooth SIG Proprietary Page **238 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6<br>OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/5 AND<br>BAP 9a/5|USR Streaming – A.C.5: Generic,<br>QoS, QoS|BAP/USR/STR/BV-382-C|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6|USR Streaming – A.C.7(i):<br>Generic|BAP/USR/STR/BV-362-C|



Bluetooth SIG Proprietary Page **239 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/7 AND<br>BAP 9a/1|||
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6<br>OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/7 AND<br>BAP 9a/2|USR Streaming – A.C.7(i):<br>Generic, Enable, QoS|BAP/USR/STR/BV-377-C|



Bluetooth SIG Proprietary Page **240 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6<br>OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/7 AND<br>BAP 9a/4|USR Streaming – A.C.7(i):<br>Generic, QoS, Enable|BAP/USR/STR/BV-380-C|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6|USR Streaming – A.C.7(i):<br>Generic, QoS, QoS|BAP/USR/STR/BV-383-C|



Bluetooth SIG Proprietary Page **241 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/7 AND<br>BAP 9a/5|||
|**Other A.C.s**|**Other A.C.s**|**Other A.C.s**|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6<br>OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/8|USR Streaming – A.C.8(i):<br>Generic|BAP/USR/STR/BV-364-C|



Bluetooth SIG Proprietary Page **242 of 270**


**Basic Audio Profile (BAP) /** Test Suite








|Item|Feature|Test Case(s)|
|---|---|---|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND (BAP 15/1 OR BAP 15/2<br>OR BAP 15/3 OR BAP 15/4<br>OR BAP 15/5 OR BAP 15/6<br>OR BAP 15/7 OR BAP 15/8<br>OR BAP 15/9 OR BAP 15/10<br>OR BAP 15/11 OR BAP<br>15/12 OR BAP 15/13 OR<br>BAP 15/14 OR BAP 15/15<br>OR BAP 15/16 OR BAP 17/1<br>OR BAP 17/2 OR BAP 17/3<br>OR BAP 17/4 OR BAP 17/5<br>OR BAP 17/6 OR BAP 17/7<br>OR BAP 17/8 OR BAP 17/9<br>OR BAP 17/10 OR BAP<br>17/11 OR BAP 17/12 OR<br>BAP 17/13 OR BAP 17/14<br>OR BAP 17/15 OR BAP<br>17/16) AND BAP 20/11|USR Streaming – A.C.11(i):<br>Generic|BAP/USR/STR/BV-366-C|
|**Sink Only**|**Sink Only**|**Sink Only**|
|(BAP 14/1 OR BAP 14/2 OR<br>BAP 14/3 OR BAP 14/4 OR<br>BAP 14/5 OR BAP 14/6 OR<br>BAP 14/7 OR BAP 14/8 OR<br>BAP 14/9 OR BAP 14/10 OR<br>BAP 14/11 OR BAP 14/12<br>OR BAP 14/13 OR BAP<br>14/14 OR BAP 14/15 OR<br>BAP 14/16 OR BAP 16/1 OR<br>BAP 16/2 OR BAP 16/3 OR<br>BAP 16/4 OR BAP 16/5 OR<br>BAP 16/6 OR BAP 16/7 OR<br>BAP 16/8 OR BAP 16/9 OR<br>BAP 16/10 OR BAP 16/11<br>OR BAP 16/12 OR BAP<br>16/13 OR BAP 16/14 OR<br>BAP 16/15 OR BAP 16/16)<br>AND BAP 20/6|USR Streaming – A.C.6(i):<br>Generic|BAP/USR/STR/BV-363-C|



Bluetooth SIG Proprietary Page **243 of 270**


**Basic Audio Profile (BAP) /** Test Suite










|Item|Feature|Test Case(s)|
|---|---|---|
|**Source Only**|**Source Only**|**Source Only**|
|(BAP 15/1 OR BAP 15/2 OR<br>BAP 15/3 OR BAP 15/4 OR<br>BAP 15/5 OR BAP 15/6 OR<br>BAP 15/7 OR BAP 15/8 OR<br>BAP 15/9 OR BAP 15/10 OR<br>BAP 15/11 OR BAP 15/12<br>OR BAP 15/13 OR BAP<br>15/14 OR BAP 15/15 OR<br>BAP 15/16 OR BAP 17/1 OR<br>BAP 17/2 OR BAP 17/3 OR<br>BAP 17/4 OR BAP 17/5 OR<br>BAP 17/6 OR BAP 17/7 OR<br>BAP 17/8 OR BAP 17/9 OR<br>BAP 17/10 OR BAP 17/11<br>OR BAP 17/12 OR BAP<br>17/13 OR BAP 17/14 OR<br>BAP 17/15 OR BAP 17/16)<br>AND BAP 20/9|USR Streaming – A.C.9(i):<br>Generic|BAP/USR/STR/BV-365-C|
|**Unicast Server – LC3 – 8_1**|**Unicast Server – LC3 – 8_1**|**Unicast Server – LC3 – 8_1**|
|BAP 12/1|Unicast Server – Server as Audio<br>Sink – LC3 Setting 8_1|BAP/USR/SCC/BV-001-C|
|BAP 12/1 AND BAP 7/4|Unicast Server – Server as Audio<br>Sink – LC3 Setting 8_1<br>Autonomous|BAP/USR/SCC/BV-035-C|
|BAP 14/1|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 -Low<br>Latency - 8_1_1|BAP/USR/SCC/BV-069-C|
|BAP 16/1|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - High<br>Reliability - 8_1_2|BAP/USR/SCC/BV-101-C|
|BAP 13/1|Unicast Server – Server as Audio<br>Source – LC3 Setting 8_1|BAP/USR/SCC/BV-017-C|
|BAP 13/1 AND BAP 7/4|Unicast Server – Server as Audio<br>Source – LC3 Setting 8_1<br>Autonomous|BAP/USR/SCC/BV-051-C|
|BAP 15/1|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 8_1_1|BAP/USR/SCC/BV-085-C|
|BAP 17/1|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 8_1_2|BAP/USR/SCC/BV-117-C|
|**Unicast Server – LC3 – 8_2**|**Unicast Server – LC3 – 8_2**|**Unicast Server – LC3 – 8_2**|
|BAP 12/2|Unicast Server - Server Is Sink -<br>LC3 Setting 8_2|BAP/USR/SCC/BV-002-C|
|BAP 12/2 AND BAP 7/4|Unicast Server - Server Is Sink -<br>LC3 Setting 8_2 Autonomous|BAP/USR/SCC/BV-036-C|
|BAP 14/2|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - Low<br>Latency - 8_2_1|BAP/USR/SCC/BV-070-C|



Bluetooth SIG Proprietary Page **244 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 16/2|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - High<br>Reliability - 8_2_2|BAP/USR/SCC/BV-102-C|
|BAP 13/2|Unicast Server - Server as Audio<br>Source - LC3 Setting 8_2|BAP/USR/SCC/BV-018-C|
|BAP 13/2 AND BAP 7/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 8_2<br>Autonomous|BAP/USR/SCC/BV-052-C|
|BAP 15/2|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 8_2_1|BAP/USR/SCC/BV-086-C|
|BAP 17/2|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 8_2_2|BAP/USR/SCC/BV-118-C|
|**Unicast Server – LC3 – 16_1**|**Unicast Server – LC3 – 16_1**|**Unicast Server – LC3 – 16_1**|
|BAP 12/3|Unicast Server - Server as Audio<br>Sink - LC3 Setting 16_1|BAP/USR/SCC/BV-003-C|
|BAP 12/3 AND BAP 7/4|Unicast Server - Server as Audio<br>Sink - LC3 Setting 16_1<br>Autonomous|BAP/USR/SCC/BV-037-C|
|BAP 14/3|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - Low<br>Latency - 16_1_1|BAP/USR/SCC/BV-071-C|
|BAP 16/3|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - High<br>Reliability - 16_1_2|BAP/USR/SCC/BV-103-C|
|BAP 13/3|Unicast Server - Server as Audio<br>Source - LC3 Setting 16_1|BAP/USR/SCC/BV-019-C|
|BAP 13/3 AND BAP 7/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 16_1<br>Autonomous|BAP/USR/SCC/BV-053-C|
|BAP 15/3|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 16_1_1|BAP/USR/SCC/BV-087-C|
|BAP 17/3|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 16_1_2|BAP/USR/SCC/BV-119-C|
|**Unicast Server – LC3 – 16_2**|**Unicast Server – LC3 – 16_2**|**Unicast Server – LC3 – 16_2**|
|BAP 12/4|Unicast Server - Server as Audio<br>Sink - LC3 Setting 16_2|BAP/USR/SCC/BV-004-C|
|BAP 12/4 AND BAP 7/4|Unicast Server - Server as Audio<br>Sink - LC3 Setting 16_2<br>Autonomous|BAP/USR/SCC/BV-038-C|
|BAP 14/4|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - Low<br>Latency - 16_2_1|BAP/USR/SCC/BV-072-C|
|BAP 16/4|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - High<br>Reliability - 16_2_2|BAP/USR/SCC/BV-104-C|



Bluetooth SIG Proprietary Page **245 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 13/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 16_2|BAP/USR/SCC/BV-020-C|
|BAP 13/4 AND BAP 7/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 16_2<br>Autonomous|BAP/USR/SCC/BV-054-C|
|BAP 15/4|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 16_2_1|BAP/USR/SCC/BV-088-C|
|BAP 17/4|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 16_2_2|BAP/USR/SCC/BV-120-C|
|**Unicast Server – LC3 – 24_1**|**Unicast Server – LC3 – 24_1**|**Unicast Server – LC3 – 24_1**|
|BAP 12/5|Unicast Server - Server as Audio<br>Sink - LC3 Setting 24_1|BAP/USR/SCC/BV-005-C|
|BAP 12/5 AND BAP 7/4|Unicast Server - Server as Audio<br>Sink - LC3 Setting 24_1<br>Autonomous|BAP/USR/SCC/BV-039-C|
|BAP 14/5|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - Low<br>Latency - 24_1_1|BAP/USR/SCC/BV-073-C|
|BAP 16/5|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - High<br>Reliability - 24_1_2|BAP/USR/SCC/BV-105-C|
|BAP 13/5|Unicast Server - Server as Audio<br>Source - LC3 Setting 24_1|BAP/USR/SCC/BV-021-C|
|BAP 13/5 AND BAP 7/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 24_1<br>Autonomous|BAP/USR/SCC/BV-055-C|
|BAP 15/5|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 24_1_1|BAP/USR/SCC/BV-089-C|
|BAP 17/5|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 24_1_2|BAP/USR/SCC/BV-121-C|
|**Unicast Server – LC3 – 24_2**|**Unicast Server – LC3 – 24_2**|**Unicast Server – LC3 – 24_2**|
|BAP 12/6|Unicast Server - Server as Audio<br>Sink - LC3 Setting 24_2|BAP/USR/SCC/BV-006-C|
|BAP 12/6 AND BAP 7/4|Unicast Server - Server as Audio<br>Sink - LC3 Setting 24_2<br>Autonomous|BAP/USR/SCC/BV-040-C|
|BAP 14/6|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - Low<br>Latency - 24_2_1|BAP/USR/SCC/BV-074-C|
|BAP 16/6|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - High<br>Reliability - 24_2_2|BAP/USR/SCC/BV-106-C|
|BAP 13/6|Unicast Server - Server as Audio<br>Source - LC3 Setting 24_2|BAP/USR/SCC/BV-022-C|



Bluetooth SIG Proprietary Page **246 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 13/6 AND BAP 7/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 24_2<br>Autonomous|BAP/USR/SCC/BV-056-C|
|BAP 15/6|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 24_2_1|BAP/USR/SCC/BV-090-C|
|BAP 17/6|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 24_2_2|BAP/USR/SCC/BV-122-C|
|**Unicast Server – LC3 – 32_1**|**Unicast Server – LC3 – 32_1**|**Unicast Server – LC3 – 32_1**|
|BAP 12/7|Unicast Server - Server as Audio<br>Sink - LC3 Setting 32_1|BAP/USR/SCC/BV-007-C|
|BAP 12/7 AND BAP 7/4|Unicast Server - Server as Audio<br>Sink - LC3 Setting 32_1<br>Autonomous|BAP/USR/SCC/BV-041-C|
|BAP 14/7|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - Low<br>Latency - 32_1_1|BAP/USR/SCC/BV-075-C|
|BAP 16/7|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - High<br>Reliability - 32_1_2|BAP/USR/SCC/BV-107-C|
|BAP 13/7|Unicast Server - Server as Audio<br>Source - LC3 Setting 32_1|BAP/USR/SCC/BV-023-C|
|BAP 13/7 AND BAP 7/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 32_1<br>Autonomous|BAP/USR/SCC/BV-057-C|
|BAP 15/7|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 32_1_1|BAP/USR/SCC/BV-091-C|
|BAP 17/7|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 32_1_2|BAP/USR/SCC/BV-123-C|
|**Unicast Server – LC3 – 32_2**|**Unicast Server – LC3 – 32_2**|**Unicast Server – LC3 – 32_2**|
|BAP 12/8|Unicast Server - Server as Audio<br>Sink - LC3 Setting 32_2|BAP/USR/SCC/BV-008-C|
|BAP 12/8 AND BAP 7/4|Unicast Server - Server as Audio<br>Sink - LC3 Setting 32_2<br>Autonomous|BAP/USR/SCC/BV-042-C|
|BAP 14/8|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - Low<br>Latency - 32_2_1|BAP/USR/SCC/BV-076-C|
|BAP 16/8|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - High<br>Reliability - 32_2_2|BAP/USR/SCC/BV-108-C|
|BAP 13/8|Unicast Server - Server as Audio<br>Source - LC3 Setting 32_2|BAP/USR/SCC/BV-024-C|
|BAP 13/8 AND BAP 7/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 32_2<br>Autonomous|BAP/USR/SCC/BV-058-C|



Bluetooth SIG Proprietary Page **247 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 15/8|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 32_2_1|BAP/USR/SCC/BV-092-C|
|BAP 17/8|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 32_2_2|BAP/USR/SCC/BV-124-C|
|**Unicast Server – LC3 – 441_1**|**Unicast Server – LC3 – 441_1**|**Unicast Server – LC3 – 441_1**|
|BAP 12/9|Unicast Server - Server as Audio<br>Sink - LC3 Setting 441_1|BAP/USR/SCC/BV-009-C|
|BAP 12/9 AND BAP 7/4|Unicast Server - Server as Audio<br>Sink - LC3 Setting 441_1<br>Autonomous|BAP/USR/SCC/BV-043-C|
|BAP 14/9|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - Low<br>Latency - 441_1_1|BAP/USR/SCC/BV-077-C|
|BAP 16/9|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - High<br>Reliability - 441_1_2|BAP/USR/SCC/BV-109-C|
|BAP 13/9|Unicast Server - Server as Audio<br>Source - LC3 Setting 441_1|BAP/USR/SCC/BV-025-C|
|BAP 13/9 AND BAP 7/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 441_1<br>Autonomous|BAP/USR/SCC/BV-059-C|
|BAP 15/9|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 441_1_1|BAP/USR/SCC/BV-093-C|
|BAP 17/9|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 441_1_2|BAP/USR/SCC/BV-125-C|
|**Unicast Server – LC3 – 441_2**|**Unicast Server – LC3 – 441_2**|**Unicast Server – LC3 – 441_2**|
|BAP 12/10|Unicast Server - Server as Audio<br>Sink - LC3 Setting 441_2|BAP/USR/SCC/BV-010-C|
|BAP 12/10 AND BAP 7/4|Unicast Server - Server as Audio<br>Sink - LC3 Setting 441_2<br>Autonomous|BAP/USR/SCC/BV-044-C|
|BAP 14/10|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - Low<br>Latency - 441_2_1|BAP/USR/SCC/BV-078-C|
|BAP 16/10|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - High<br>Reliability - 441_2_2|BAP/USR/SCC/BV-110-C|
|BAP 13/10|Unicast Server - Server as Audio<br>Source - LC3 Setting 441_2|BAP/USR/SCC/BV-026-C|
|BAP 13/10 AND BAP 7/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 441_2<br>Autonomous|BAP/USR/SCC/BV-060-C|



Bluetooth SIG Proprietary Page **248 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 15/10|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 441_2_1|BAP/USR/SCC/BV-094-C|
|BAP 17/10|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 441_2_2|BAP/USR/SCC/BV-126-C|
|**Unicast Server – LC3 – 48_1**|**Unicast Server – LC3 – 48_1**|**Unicast Server – LC3 – 48_1**|
|BAP 12/11|Unicast Server - Server as Audio<br>Sink - LC3 Setting 48_1|BAP/USR/SCC/BV-011-C|
|BAP 12/11 AND BAP 7/4|Unicast Server - Server as Audio<br>Sink - LC3 Setting 48_1<br>Autonomous|BAP/USR/SCC/BV-045-C|
|BAP 14/11|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - Low<br>Latency - 48_1_1|BAP/USR/SCC/BV-079-C|
|BAP 16/11|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - High<br>Reliability - 48_1_2|BAP/USR/SCC/BV-111-C|
|BAP 13/11|Unicast Server - Server as Audio<br>Source - LC3 Setting 48_1|BAP/USR/SCC/BV-027-C|
|BAP 13/11 AND BAP 7/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 48_1<br>Autonomous|BAP/USR/SCC/BV-061-C|
|BAP 15/11|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 48_1_1|BAP/USR/SCC/BV-095-C|
|BAP 17/11|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 48_1_2|BAP/USR/SCC/BV-127-C|
|**Unicast Server – LC3 – 48_2**|**Unicast Server – LC3 – 48_2**|**Unicast Server – LC3 – 48_2**|
|BAP 12/12|Unicast Server - Server as Audio<br>Sink - LC3 Setting 48_2|BAP/USR/SCC/BV-012-C|
|BAP 12/12 AND BAP 7/4|Unicast Server - Server as Audio<br>Sink - LC3 Setting 48_2<br>Autonomous|BAP/USR/SCC/BV-046-C|
|BAP 14/12|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - Low<br>Latency - 48_2_1|BAP/USR/SCC/BV-080-C|
|BAP 16/12|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - High<br>Reliability - 48_2_2|BAP/USR/SCC/BV-112-C|
|BAP 13/12|Unicast Server - Server as Audio<br>Source - LC3 Setting 48_2|BAP/USR/SCC/BV-028-C|
|BAP 13/12 AND BAP 7/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 48_2<br>Autonomous|BAP/USR/SCC/BV-062-C|



Bluetooth SIG Proprietary Page **249 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 15/12|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 48_2_1|BAP/USR/SCC/BV-096-C|
|BAP 17/12|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 48_2_2|BAP/USR/SCC/BV-128-C|
|**Unicast Server – LC3 – 48_3**|**Unicast Server – LC3 – 48_3**|**Unicast Server – LC3 – 48_3**|
|BAP 12/13|Unicast Server - Server Is Sink -<br>LC3 Setting 48_3|BAP/USR/SCC/BV-013-C|
|BAP 12/13 AND BAP 7/4|Unicast Server - Server Is Sink -<br>LC3 Setting 48_3 Autonomous|BAP/USR/SCC/BV-047-C|
|BAP 14/13|QoS Configuration – Unicast<br>Server Is Sink - LC3 - Low<br>Latency - 48_3_1|BAP/USR/SCC/BV-081-C|
|BAP 16/13|QoS Configuration – Unicast<br>Server Is Sink - LC3 - High<br>Reliability - 48_3_2|BAP/USR/SCC/BV-113-C|
|BAP 13/13|Unicast Server - Server as Audio<br>Source - LC3 Setting 48_3|BAP/USR/SCC/BV-029-C|
|BAP 13/13 AND BAP 7/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 48_3<br>Autonomous|BAP/USR/SCC/BV-063-C|
|BAP 15/13|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 48_3_1|BAP/USR/SCC/BV-097-C|
|BAP 17/13|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 48_3_2|BAP/USR/SCC/BV-129-C|
|**Unicast Server – LC3 – 48_4**|**Unicast Server – LC3 – 48_4**|**Unicast Server – LC3 – 48_4**|
|BAP 12/14|Unicast Server - Server as Audio<br>Sink - LC3 Setting 48_4|BAP/USR/SCC/BV-014-C|
|BAP 12/14 AND BAP 7/4|Unicast Server - Server as Audio<br>Sink - LC3 Setting 48_4<br>Autonomous|BAP/USR/SCC/BV-048-C|
|BAP 14/14|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - Low<br>Latency - 48_4_1|BAP/USR/SCC/BV-082-C|
|BAP 16/14|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - High<br>Reliability - 48_4_2|BAP/USR/SCC/BV-114-C|
|BAP 13/14|Unicast Server - Server as Audio<br>Source - LC3 Setting 48_4|BAP/USR/SCC/BV-030-C|
|BAP 13/14 AND BAP 7/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 48_4<br>Autonomous|BAP/USR/SCC/BV-064-C|
|BAP 15/14|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 48_4_1|BAP/USR/SCC/BV-098-C|



Bluetooth SIG Proprietary Page **250 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 17/14|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 48_4_2|BAP/USR/SCC/BV-130-C|
|**Unicast Server – LC3 – 48_5**|**Unicast Server – LC3 – 48_5**|**Unicast Server – LC3 – 48_5**|
|BAP 12/15|Unicast Server - Server as Audio<br>Sink - LC3 Setting 48_5|BAP/USR/SCC/BV-015-C|
|BAP 12/15 AND BAP 7/4|Unicast Server - Server as Audio<br>Sink - LC3 Setting 48_5<br>Autonomous|BAP/USR/SCC/BV-049-C|
|BAP 14/15|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - Low<br>Latency - 48_5_1|BAP/USR/SCC/BV-083-C|
|BAP 16/15|QoS Configuration – Unicast<br>Server as Audio Sink - LC3 - High<br>Reliability - 48_5_2|BAP/USR/SCC/BV-115-C|
|BAP 13/15|Unicast Server - Server as Audio<br>Source - LC3 Setting 48_5|BAP/USR/SCC/BV-031-C|
|BAP 13/15 AND BAP 7/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 48_5<br>Autonomous|BAP/USR/SCC/BV-065-C|
|BAP 15/15|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 48_5_1|BAP/USR/SCC/BV-099-C|
|BAP 17/15|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 48_5_2|BAP/USR/SCC/BV-131-C|
|**Unicast Server – LC3 – 48_6**|**Unicast Server – LC3 – 48_6**|**Unicast Server – LC3 – 48_6**|
|BAP 12/16|Unicast Server - Server Is Sink -<br>LC3 Setting 48_6|BAP/USR/SCC/BV-016-C|
|BAP 12/16 AND BAP 7/4|Unicast Server - Server Is Sink -<br>LC3 Setting 48_6 Autonomous|BAP/USR/SCC/BV-050-C|
|BAP 14/16|QoS Configuration – Unicast<br>Server Is Sink - LC3 - Low<br>Latency - 48_6_1|BAP/USR/SCC/BV-084-C|
|BAP 16/16|QoS Configuration – Unicast<br>Server Is Sink - LC3 - High<br>Reliability - 48_6_2|BAP/USR/SCC/BV-116-C|
|BAP 13/16|Unicast Server - Server as Audio<br>Source - LC3 Setting 48_6|BAP/USR/SCC/BV-032-C|
|BAP 13/16 AND BAP 7/4|Unicast Server - Server as Audio<br>Source - LC3 Setting 48_6<br>Autonomous|BAP/USR/SCC/BV-066-C|
|BAP 15/16|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>Low Latency - 48_6_1|BAP/USR/SCC/BV-100-C|
|BAP 17/16|QoS Configuration – Unicast<br>Server as Audio Source - LC3 -<br>High Reliability - 48_6_2|BAP/USR/SCC/BV-132-C|



Bluetooth SIG Proprietary Page **251 of 270**


**Basic Audio Profile (BAP) /** Test Suite










|Item|Feature|Test Case(s)|
|---|---|---|
|**Unicast Server – Vendor Specific**|**Unicast Server – Vendor Specific**|**Unicast Server – Vendor Specific**|
|BAP 12/17|Unicast Server - Server Is Sink –<br>Vendor-Specific Codec Setting|BAP/USR/SCC/BV-033-C<br>BAP/USR/SCC/BV-067-C|
|BAP 18/1|QoS Configuration – Unicast<br>Server Is Sink - Vendor-Specific|BAP/USR/SCC/BV-133-C|
|BAP 18/1 AND BAP 20/1|USR Sink Streaming A.C.1 -1<br>Stream 1 Channel – VS Codec|BAP/USR/STR/BV-129-C|
|BAP 18/1 AND BAP 20/4|USR Sink Streaming A.C.4 1<br>Stream 2 Channels – VS Codec|BAP/USR/STR/BV-130-C|
|BAP 13/17|Unicast Server - Server as Audio<br>Source – Vendor-Specific Codec<br>Setting|BAP/USR/SCC/BV-034-C<br>BAP/USR/SCC/BV-068-C|
|BAP 19/1|QoS Configuration – Unicast<br>Server as Audio Source - Vendor-<br>Specific|BAP/USR/SCC/BV-134-C|
|BAP 19/1 AND BAP 20/2|USR Source Streaming A.C.2 - 1<br>Stream 1 Channel – VS Codec|BAP/USR/STR/BV-131-C|
|BAP 19/1 AND BAP 20/10|USR Source Streaming A.C.10 -<br>1 Stream 2 Channels – VS Codec|BAP/USR/STR/BV-132-C|
|BAP 18/1 AND BAP 19/1<br>AND BAP 20/3|USR Streaming – A.C.3: 1 Sink<br>ASE, 1 Source ASE, 2 Sink<br>Channels, 2 Streams – Vendor-<br>specific Codec Settings|BAP/USR/STR/BV-229-C|
|BAP 18/1 AND BAP 19/1<br>AND BAP 20/5|USR Streaming – A.C.5:<br>Transmits and Receives Audio<br>Data on Two ASEs – Vendor-<br>specific|BAP/USR/STR/BV-230-C|
|BAP 18/1 AND BAP 19/1<br>AND BAP 20/8|USR Streaming – A.C.7(i): USR<br>Transmits and Receives Audio<br>Data on Two ASEs – Vendor-<br>specific|BAP/USR/STR/BV-231-C|
|**Unicast Client Configuration**|**Unicast Client Configuration**|**Unicast Client Configuration**|
|BAP 29/1 AND BAP 33/1<br>AND BAP 33/3 AND BAP<br>33/5 AND BAP 33/6 AND<br>BAP 33/8|Unicast Client as Audio Sink<br>initiates ASE Control operations|BAP/UCL/SCC/BV-102-C<br>BAP/UCL/SCC/BV-103-C<br>BAP/UCL/SCC/BV-105-C<br>BAP/UCL/SCC/BV-106-C<br>BAP/UCL/SCC/BV-108-C<br>BAP/UCL/SCC/BV-110-C<br>BAP/UCL/SCC/BV-112-C<br>BAP/UCL/SCC/BV-116-C|
|BAP 29/2 AND BAP 33/3<br>AND BAP 33/5 AND<br>BAP 33/6 AND BAP 33/8|Unicast Client as Audio Source<br>initiates ASE Control operations|BAP/UCL/SCC/BV-101-C<br>BAP/UCL/SCC/BV-104-C<br>BAP/UCL/SCC/BV-107-C<br>BAP/UCL/SCC/BV-109-C<br>BAP/UCL/SCC/BV-111-C<br>BAP/UCL/SCC/BV-113-C<br>BAP/UCL/SCC/BV-115-C<br>BAP/UCL/SCC/BV-117-C|



Bluetooth SIG Proprietary Page **252 of 270**


**Basic Audio Profile (BAP) /** Test Suite














|Item|Feature|Test Case(s)|
|---|---|---|
|**Unicast Server Configuration**|**Unicast Server Configuration**|**Unicast Server Configuration**|
|(BAP 6/1 OR BAP 6/2) AND<br>(BAP 6/3 OR BAP 6/4) AND<br>BAP 8/1|Unicast Server as Audio Sink<br>Performs ASE Control operations|BAP/USR/SCC/BV-135-C<br>BAP/USR/SCC/BV-138-C<br>BAP/USR/SCC/BV-144-C<br>BAP/USR/SCC/BV-146-C<br>BAP/USR/SCC/BV-148-C<br>BAP/USR/SCC/BV-162-C<br>BAP/USR/SCC/BV-167-C|
|(BAP 6/1 OR BAP 6/2) AND<br>(BAP 6/3 OR BAP 6/4) AND<br>BAP 8/2|Unicast Server as Audio Source<br>Performs ASE Control operations|BAP/USR/SCC/BV-136-C<br>BAP/USR/SCC/BV-137-C<br>BAP/USR/SCC/BV-139-C<br>BAP/USR/SCC/BV-143-C<br>BAP/USR/SCC/BV-145-C<br>BAP/USR/SCC/BV-147-C<br>BAP/USR/SCC/BV-149-C<br>BAP/USR/SCC/BV-150-C<br>BAP/USR/SCC/BV-161-C<br>BAP/USR/SCC/BV-163-C<br>BAP/USR/SCC/BV-168-C|
|(BAP 6/1 OR BAP 6/2) AND<br>BAP 7/8|Unicast Server as Audio Sink<br>initiates Release operation<br>autonomously|BAP/USR/SCC/BV-153-C<br>BAP/USR/SCC/BV-155-C<br>BAP/USR/SCC/BV-157-C<br>BAP/USR/SCC/BV-159-C|
|(BAP 6/1 OR BAP 6/2) AND<br>BAP 7/7|Unicast Server as Audio Sink<br>initiates Update Metadata<br>operation autonomously|BAP/USR/SCC/BV-165-C|
|(BAP 6/1 OR BAP 6/2) AND<br>(BAP 6/3 OR BAP 6/4) AND<br>BAP 7/8|Unicast Server as Audio Source<br>initiates Release operation<br>autonomously|BAP/USR/SCC/BV-152-C<br>BAP/USR/SCC/BV-154-C<br>BAP/USR/SCC/BV-156-C<br>BAP/USR/SCC/BV-158-C|
|(BAP 6/1 OR BAP 6/2) AND<br>(BAP 6/3 OR BAP 6/4) AND<br>BAP 7/7|Unicast Server as Audio Source<br>initiates Update Metadata<br>operations autonomously|BAP/USR/SCC/BV-164-C<br>BAP/USR/SCC/BV-166-C|
|(BAP 6/1 OR BAP 6/2) AND<br>BAP 7/6|Unicast Server as Audio Sink<br>initiates Disable operation<br>autonomously|BAP/USR/SCC/BV-141-C|
|(BAP 6/1 OR BAP 6/2) AND<br>(BAP 6/3 OR BAP 6/4) AND<br>BAP 7/6|Unicast Server as Audio Source<br>initiates Disable operation<br>autonomously|BAP/USR/SCC/BV-140-C<br>BAP/USR/SCC/BV-142-C|
|**Unicast Server – Error Handling**|**Unicast Server – Error Handling**|**Unicast Server – Error Handling**|
|(BAP 6/1 OR BAP 6/2) AND<br>(BAP 6/3 OR BAP 6/4)|Unicast Server Performs ASE<br>Control operations – Error<br>Conditions|BAP/USR/SPE/BI-01-C<br>BAP/USR/SPE/BI-02-C<br>BAP/USR/SPE/BI-03-C<br>BAP/USR/SPE/BI-04-C<br>BAP/USR/SPE/BI-05-C|



Bluetooth SIG Proprietary Page **253 of 270**


**Basic Audio Profile (BAP) /** Test Suite






















|Item|Feature|Test Case(s)|
|---|---|---|
|**Broadcast**|**Broadcast**|**Broadcast**|
|BAP 1/3|Broadcast Configuration|BAP/BSRC/SCC/BV-35-C<br>BAP/BSRC/SCC/BV-36-C<br>BAP/BSRC/SCC/BV-37-C|
|BAP 1/3 AND BAP 51/2|Broadcast Reconfiguration|BAP/BSRC/SCC/BV-34-C|
|BAP 1/3 AND BAP 51/7|Multi BIG Broadcast<br>Configuration|BAP/BSRC/SCC/BV-38-C|
|BAP 1/4|Broadcast Sink|BAP/BSNK/ADV/BV-01-C|
|BAP 1/6|Receive Basic Audio<br>Announcements – Broadcast<br>Assistant|BAP/BA/ADV/BV-01-C<br>BAP/BA/BASS/BV-01-C|
|BAP 1/6 AND BAP 88/1|Broadcast Assistant – Remote<br>Scan Start|BAP/BA/BASS/BV-02-C|
|BAP 1/6 AND BAP 88/2|Broadcast Assistant – Remote<br>Scan Stop|BAP/BA/BASS/BV-03-C|
|BAP 1/6 AND BAP 88/3|Broadcast Assistant – Add<br>Source|BAP/BA/BASS/BV-04-C|
|BAP 1/6 AND BAP 88/4|Broadcast Assistant – Modify<br>Source|BAP/BA/BASS/BV-05-C|
|BAP 1/6 AND BAP 88/7|Broadcast Assistant – Remove<br>Source|BAP/BA/BASS/BV-06-C|
|BAP 1/6 AND BAP 88/6|Broadcast Assistant – Set<br>Broadcast Code|BAP/BA/BASS/BV-07-C|
|BAP 1/6 AND BAP 88/5|Broadcast Assistant – SyncInfo<br>Transfer|BAP/BA/BASS/BV-08-C|
|BAP 1/6 AND BAP 85/4|Broadcast Assistant discovers<br>Sink Audio Locations|BAP/BA/BASS/BV-09-C|
|BAP 1/5|Broadcast BASS Advertisements|BAP/SDE/BASS/BV-01-C|
|BAP 1/5 AND BAP 3/2 AND<br>BAP 80/12|Broadcast BASS Advertisements,<br>BR/EDR/LE|BAP/SDE/BASS/BV-02-C|
|BAP 1/5 AND BAP 3/2 AND<br>NOT BAP 80/12|Broadcast BASS Advertisements,<br>No CTKD|BAP/SDE/BASS/BV-03-C|
|**Broadcast Source**|**Broadcast Source**|**Broadcast Source**|
|BAP 55/1|Broadcast Source – Configures<br>Broadcast – LC3 8_1_1|BAP/BSRC/SCC/BV-01-C|
|BAP 55/2|Broadcast Source – Configures<br>Broadcast – LC3 8_2_1|BAP/BSRC/SCC/BV-02-C|
|BAP 55/3|Broadcast Source – Configures<br>Broadcast – LC3 16_1_1|BAP/BSRC/SCC/BV-03-C|
|BAP 55/4|Broadcast Source – Configures<br>Broadcast – LC3 16_2_1|BAP/BSRC/SCC/BV-04-C|
|BAP 55/5|Broadcast Source – Configures<br>Broadcast – LC3 24_1_1|BAP/BSRC/SCC/BV-05-C|
|BAP 55/6|Broadcast Source – Configures<br>Broadcast – LC3 24_2_1|BAP/BSRC/SCC/BV-06-C|



Bluetooth SIG Proprietary Page **254 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 55/7|Broadcast Source – Configures<br>Broadcast – LC3 32_1_1|BAP/BSRC/SCC/BV-07-C|
|BAP 55/8|Broadcast Source – Configures<br>Broadcast – LC3 32_2_1|BAP/BSRC/SCC/BV-08-C|
|BAP 55/9|Broadcast Source – Configures<br>Broadcast – LC3 441_1_1|BAP/BSRC/SCC/BV-09-C|
|BAP 55/10|Broadcast Source – Configures<br>Broadcast – LC3 441_2_1|BAP/BSRC/SCC/BV-10-C|
|BAP 55/11|Broadcast Source – Configures<br>Broadcast – LC3 48_1_1|BAP/BSRC/SCC/BV-11-C|
|BAP 55/12|Broadcast Source – Configures<br>Broadcast – LC3 48_2_1|BAP/BSRC/SCC/BV-12-C|
|BAP 55/13|Broadcast Source – Configures<br>Broadcast – LC3 48_3_1|BAP/BSRC/SCC/BV-13-C|
|BAP 55/14|Broadcast Source – Configures<br>Broadcast – LC3 48_4_1|BAP/BSRC/SCC/BV-14-C|
|BAP 55/15|Broadcast Source – Configures<br>Broadcast – LC3 48_5_1|BAP/BSRC/SCC/BV-15-C|
|BAP 55/16|Broadcast Source – Configures<br>Broadcast – LC3 48_6_1|BAP/BSRC/SCC/BV-16-C|
|BAP 56/1|Broadcast Source – Configures<br>Broadcast – LC3 8_1_2|BAP/BSRC/SCC/BV-17-C|
|BAP 56/2|Broadcast Source – Configures<br>Broadcast – LC3 8_2_2|BAP/BSRC/SCC/BV-18-C|
|BAP 56/3|Broadcast Source – Configures<br>Broadcast – LC3 16_1_2|BAP/BSRC/SCC/BV-19-C|
|BAP 56/4|Broadcast Source – Configures<br>Broadcast – LC3 16_2_2|BAP/BSRC/SCC/BV-20-C|
|BAP 56/5|Broadcast Source – Configures<br>Broadcast – LC3 24_1_2|BAP/BSRC/SCC/BV-21-C|
|BAP 56/6|Broadcast Source – Configures<br>Broadcast – LC3 24_2_2|BAP/BSRC/SCC/BV-22-C|
|BAP 56/7|Broadcast Source – Configures<br>Broadcast – LC3 32_1_2|BAP/BSRC/SCC/BV-23-C|
|BAP 56/8|Broadcast Source – Configures<br>Broadcast – LC3 32_2_2|BAP/BSRC/SCC/BV-24-C|
|BAP 56/9|Broadcast Source – Configures<br>Broadcast – LC3 441_1_2|BAP/BSRC/SCC/BV-25-C|
|BAP 56/10|Broadcast Source – Configures<br>Broadcast – LC3 441_2_2|BAP/BSRC/SCC/BV-26-C|
|BAP 56/11|Broadcast Source – Configures<br>Broadcast – LC3 48_1_2|BAP/BSRC/SCC/BV-27-C|
|BAP 56/12|Broadcast Source – Configures<br>Broadcast – LC3 48_2_2|BAP/BSRC/SCC/BV-28-C|
|BAP 56/13|Broadcast Source – Configures<br>Broadcast – LC3 48_3_2|BAP/BSRC/SCC/BV-29-C|



Bluetooth SIG Proprietary Page **255 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 56/14|Broadcast Source – Configures<br>Broadcast – LC3 48_4_2|BAP/BSRC/SCC/BV-30-C|
|BAP 56/15|Broadcast Source – Configures<br>Broadcast – LC3 48_5_2|BAP/BSRC/SCC/BV-31-C|
|BAP 56/16|Broadcast Source – Configures<br>Broadcast – LC3 48_6_2|BAP/BSRC/SCC/BV-32-C|
|BAP 54/17|Broadcast Source – Streaming –<br>Vendor-specific Codec setting|BAP/BSRC/SCC/BV-33-C<br>BAP/BSRC/STR/BV-17-C<br>BAP/BSRC/STR/BV-34-C|
|BAP 54/1|Broadcast Source – Streaming –<br>LC3 8_1|BAP/BSRC/STR/BV-01-C<br>BAP/BSRC/STR/BV-18-C|
|BAP 54/2|Broadcast Source – Streaming –<br>LC3 8_2|BAP/BSRC/STR/BV-02-C<br>BAP/BSRC/STR/BV-19-C|
|BAP 54/3|Broadcast Source – Streaming –<br>LC3 16_1|BAP/BSRC/STR/BV-03-C<br>BAP/BSRC/STR/BV-20-C|
|BAP 54/4|Broadcast Source – Streaming –<br>LC3 16_2|BAP/BSRC/STR/BV-04-C<br>BAP/BSRC/STR/BV-21-C|
|BAP 54/5|Broadcast Source – Streaming –<br>LC3 24_1|BAP/BSRC/STR/BV-05-C<br>BAP/BSRC/STR/BV-22-C|
|BAP 54/6|Broadcast Source – Streaming –<br>LC3 24_2|BAP/BSRC/STR/BV-06-C<br>BAP/BSRC/STR/BV-23-C|
|BAP 54/7|Broadcast Source – Streaming –<br>LC3 32_1|BAP/BSRC/STR/BV-07-C<br>BAP/BSRC/STR/BV-24-C|
|BAP 54/8|Broadcast Source – Streaming –<br>LC3 32_2|BAP/BSRC/STR/BV-08-C<br>BAP/BSRC/STR/BV-25-C|
|BAP 54/9|Broadcast Source – Streaming –<br>LC3 441_1|BAP/BSRC/STR/BV-09-C<br>BAP/BSRC/STR/BV-26-C|
|BAP 54/10|Broadcast Source – Streaming –<br>LC3 441_2|BAP/BSRC/STR/BV-10-C<br>BAP/BSRC/STR/BV-27-C|
|BAP 54/11|Broadcast Source – Streaming –<br>LC3 48_1|BAP/BSRC/STR/BV-11-C<br>BAP/BSRC/STR/BV-28-C|
|BAP 54/12|Broadcast Source – Streaming –<br>LC3 48_2|BAP/BSRC/STR/BV-12-C<br>BAP/BSRC/STR/BV-29-C|
|BAP 54/13|Broadcast Source – Streaming –<br>LC3 48_3|BAP/BSRC/STR/BV-13-C<br>BAP/BSRC/STR/BV-30-C|
|BAP 54/14|Broadcast Source – Streaming –<br>LC3 48_4|BAP/BSRC/STR/BV-14-C<br>BAP/BSRC/STR/BV-31-C|
|BAP 54/15|Broadcast Source – Streaming –<br>LC3 48_5|BAP/BSRC/STR/BV-15-C<br>BAP/BSRC/STR/BV-32-C|
|BAP 54/16|Broadcast Source – Streaming –<br>LC3 48_6|BAP/BSRC/STR/BV-16-C<br>BAP/BSRC/STR/BV-33-C|



Bluetooth SIG Proprietary Page **256 of 270**


**Basic Audio Profile (BAP) /** Test Suite






|Item|Feature|Test Case(s)|
|---|---|---|
|**Broadcast Sink – Low Latency**|**Broadcast Sink – Low Latency**|**Broadcast Sink – Low Latency**|
|BAP 69/1|Broadcast Sink – Streaming –<br>LC3 8_1_1|BAP/BSNK/STR/BV-01-C|
|BAP 69/2|Broadcast Sink – Streaming –<br>LC3 8_2_1|BAP/BSNK/STR/BV-02-C|
|BAP 69/3|Broadcast Sink – Streaming –<br>LC3 16_1_1|BAP/BSNK/STR/BV-03-C|
|BAP 69/4|Broadcast Sink – Streaming –<br>LC3 16_2_1|BAP/BSNK/SCC/BV-04-C<br>BAP/BSNK/STR/BV-04-C|
|BAP 69/5|Broadcast Sink – Streaming –<br>LC3 24_1_1|BAP/BSNK/STR/BV-05-C|
|BAP 69/6|Broadcast Sink – Streaming –<br>LC3 24_2_1|BAP/BSNK/SCC/BV-06-C<br>BAP/BSNK/STR/BV-06-C|
|BAP 69/7|Broadcast Sink – Streaming –<br>LC3 32_1_1|BAP/BSNK/STR/BV-07-C|
|BAP 69/8|Broadcast Sink – Streaming –<br>LC3 32_2_1|BAP/BSNK/STR/BV-08-C|
|BAP 69/9|Broadcast Sink – Streaming –<br>LC3 441_1_1|BAP/BSNK/STR/BV-09-C|
|BAP 69/10|Broadcast Sink – Streaming –<br>LC3 441_2_1|BAP/BSNK/STR/BV-10-C|
|BAP 69/11|Broadcast Sink – Streaming –<br>LC3 48_1_1|BAP/BSNK/STR/BV-11-C|
|BAP 69/12|Broadcast Sink – Streaming –<br>LC3 48_2_1|BAP/BSNK/STR/BV-12-C|
|BAP 69/13|Broadcast Sink – Streaming –<br>LC3 48_3_1|BAP/BSNK/STR/BV-13-C|
|BAP 69/14|Broadcast Sink – Streaming –<br>LC3 48_4_1|BAP/BSNK/STR/BV-14-C|
|BAP 69/15|Broadcast Sink – Streaming –<br>LC3 48_5_1|BAP/BSNK/STR/BV-15-C|
|BAP 69/16|Broadcast Sink – Streaming –<br>LC3 48_6_1|BAP/BSNK/STR/BV-16-C|
|BAP 68/17|Broadcast Sink – Streaming –<br>Vendor-specific Codec setting|BAP/BSNK/SCC/BV-33-C<br>BAP/BSNK/STR/BV-17-C|
|BAP 69/1 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 8_1_1 - Multiple|BAP/BSNK/STR/BV-18-C|
|BAP 69/2 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 8_2_1 - Multiple|BAP/BSNK/STR/BV-19-C|
|BAP 69/3 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 16_1_1 - Multiple|BAP/BSNK/STR/BV-20-C|
|BAP 69/4 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 16_2_1 - Multiple|BAP/BSNK/STR/BV-21-C|
|BAP 69/5 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 24_1_1 - Multiple|BAP/BSNK/STR/BV-22-C|
|BAP 69/6 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 24_2_1 - Multiple|BAP/BSNK/STR/BV-23-C|



Bluetooth SIG Proprietary Page **257 of 270**


**Basic Audio Profile (BAP) /** Test Suite











|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 69/7 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 32_1_1 - Multiple|BAP/BSNK/STR/BV-24-C|
|BAP 69/8 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 32_2_1 - Multiple|BAP/BSNK/STR/BV-25-C|
|BAP 69/9 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 441_1_1 - Multiple|BAP/BSNK/STR/BV-26-C|
|BAP 69/10 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 441_2_1 - Multiple|BAP/BSNK/STR/BV-27-C|
|BAP 69/11 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 48_1_1 - Multiple|BAP/BSNK/STR/BV-28-C|
|BAP 69/12 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 48_2_1 - Multiple|BAP/BSNK/STR/BV-29-C|
|BAP 69/13 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 48_3_1 - Multiple|BAP/BSNK/STR/BV-30-C|
|BAP 69/14 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 48_4_1 - Multiple|BAP/BSNK/STR/BV-31-C|
|BAP 69/15 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 48_5_1 - Multiple|BAP/BSNK/STR/BV-32-C|
|BAP 69/16 AND BAP 66/1|Broadcast Sink – Streaming –<br>LC3 48_6_1 - Multiple|BAP/BSNK/STR/BV-33-C|
|BAP 68/17 AND BAP 66/1|Broadcast Sink – Streaming –<br>Vendor-specific Codec setting -<br>Multiple|BAP/BSNK/STR/BV-34-C|
|(BAP 68/4 OR BAP 68/6 OR<br>BAP 70/4 OR BAP 70/6)|Broadcast Sink – Sync to PA,<br>Unknown|BAP/BSNK/SCC/BV-34-C|
|**Broadcast Sink – High Reliability**|**Broadcast Sink – High Reliability**|**Broadcast Sink – High Reliability**|
|BAP 70/1|Broadcast Sink – LC3 8_1_2|BAP/BSNK/STR/BV-35-C|
|BAP 70/2|Broadcast Sink – LC3 8_2_2|BAP/BSNK/STR/BV-36-C|
|BAP 70/3|Broadcast Sink – LC3 16_1_2|BAP/BSNK/STR/BV-37-C|
|BAP 70/4|Broadcast Sink – LC3 16_2_2|BAP/BSNK/SCC/BV-20-C<br>BAP/BSNK/STR/BV-38-C|
|BAP 70/5|Broadcast Sink – LC3 24_1_2|BAP/BSNK/STR/BV-39-C|
|BAP 70/6|Broadcast Sink – LC3 24_2_2|BAP/BSNK/SCC/BV-22-C<br>BAP/BSNK/STR/BV-40-C|
|BAP 70/7|Broadcast Sink – LC3 32_1_2|BAP/BSNK/STR/BV-41-C|
|BAP 70/8|Broadcast Sink – LC3 32_2_2|BAP/BSNK/STR/BV-42-C|
|BAP 70/9|Broadcast Sink – LC3 441_1_2|BAP/BSNK/STR/BV-43-C|
|BAP 70/10|Broadcast Sink – LC3 441_2_2|BAP/BSNK/STR/BV-44-C|
|BAP 70/11|Broadcast Sink – LC3 48_1_2|BAP/BSNK/STR/BV-45-C|
|BAP 70/12|Broadcast Sink – LC3 48_2_2|BAP/BSNK/STR/BV-46-C|
|BAP 70/13|Broadcast Sink – LC3 48_3_2|BAP/BSNK/STR/BV-47-C|
|BAP 70/14|Broadcast Sink – LC3 48_4_2|BAP/BSNK/STR/BV-48-C|
|BAP 70/15|Broadcast Sink – LC3 48_5_2|BAP/BSNK/STR/BV-49-C|
|BAP 70/16|Broadcast Sink – LC3 48_6_2|BAP/BSNK/STR/BV-50-C|


Bluetooth SIG Proprietary Page **258 of 270**


**Basic Audio Profile (BAP) /** Test Suite



|Item|Feature|Test Case(s)|
|---|---|---|
|BAP 70/1 AND BAP 66/1|Broadcast Sink – LC3 8_1_2 -<br>Multiple|BAP/BSNK/STR/BV-51-C|
|BAP 70/2 AND BAP 66/1|Broadcast Sink – LC3 8_2_2-<br>Multiple|BAP/BSNK/STR/BV-52-C|
|BAP 70/3 AND BAP 66/1|Broadcast Sink – LC3 16_1_2-<br>Multiple|BAP/BSNK/STR/BV-53-C|
|BAP 70/4 AND BAP 66/1|Broadcast Sink – LC3 16_2_2-<br>Multiple|BAP/BSNK/STR/BV-54-C|
|BAP 70/5 AND BAP 66/1|Broadcast Sink – LC3 24_1_2-<br>Multiple|BAP/BSNK/STR/BV-55-C|
|BAP 70/6 AND BAP 66/1|Broadcast Sink – LC3 24_2_2-<br>Multiple|BAP/BSNK/STR/BV-56-C|
|BAP 70/7 AND BAP 66/1|Broadcast Sink - LC3 32_1_2-<br>Multiple|BAP/BSNK/STR/BV-57-C|
|BAP 70/8 AND BAP 66/1|Broadcast Sink - LC3 32_2_2-<br>Multiple|BAP/BSNK/STR/BV-58-C|
|BAP 70/9 AND BAP 66/1|Broadcast Sink - LC3 441_1_2-<br>Multiple|BAP/BSNK/STR/BV-59-C|
|BAP 70/10 AND BAP 66/1|Broadcast Sink - LC3 441_2_2-<br>Multiple|BAP/BSNK/STR/BV-60-C|
|BAP 70/11 AND BAP 66/1|Broadcast Sink - LC3 48_1_2-<br>Multiple|BAP/BSNK/STR/BV-61-C|
|BAP 70/12 AND BAP 66/1|Broadcast Sink - LC3 48_2_2-<br>Multiple|BAP/BSNK/STR/BV-62-C|
|BAP 70/13 AND BAP 66/1|Broadcast Sink - LC3 48_3_2-<br>Multiple|BAP/BSNK/STR/BV-63-C|
|BAP 70/14 AND BAP 66/1|Broadcast Sink - LC3 48_4_2-<br>Multiple|BAP/BSNK/STR/BV-64-C|
|BAP 70/15 AND BAP 66/1|Broadcast Sink - LC3 48_5_2-<br>Multiple|BAP/BSNK/STR/BV-65-C|
|BAP 70/16 AND BAP 66/1|Broadcast Sink - LC3 48_6_2-<br>Multiple|BAP/BSNK/STR/BV-66-C|