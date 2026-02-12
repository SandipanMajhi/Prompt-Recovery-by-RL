## **5 Test case mapping**


The Test Case Mapping Table (TCMT) maps test cases to specific requirements in the ICS. The IUT is
tested in all roles for which support is declared in the ICS document.


The columns for the TCMT are defined as follows:


**Item:** Contains a logical expression based on specific entries from the associated ICS document.
Contains a logical expression (using the operators AND, OR, NOT as needed) based on specific entries
from the applicable ICS document(s). The entries are in the form of y/x references, where y corresponds
to the table number and x corresponds to the feature number as defined in the ICS document for Video
Distribution Profile (VDP) [3].


If a test case is mandatory within the respective layer, then the y/x reference is omitted.


**Feature:** A brief, informal description of the feature being tested.


**Test Case(s):** The applicable test case identifiers are required for Bluetooth Qualification if the
corresponding y/x references defined in the Item column are supported. Further details about the function
of the TCMT are elaborated in [7].


For purpose and structure of the ICS/IXIT, refer to [7].












|Item|Feature|Test Case(s)|
|---|---|---|
|VDP 1/1|VDP Source SDP Service|VDP/SRC/SGSIT/SERR/BV-01-C<br>VDP/SRC/SGSIT/ATTR/BV-01-C<br>VDP/SRC/SGSIT/OFFS/BV-01-C<br>VDP/SRC/SGSIT/OFFS/BV-02-C<br>VDP/SRC/CGSIT/SFC/BV-01-C|
|VDP 0/2 AND VDP 1/1|VDP Source SDP Service, VDP 1.1|VDP/SRC/SGSIT/ATTR/BV-03-C|
|VDP 1/2|VDP Sink SDP Service|VDP/SNK/SGSIT/SERR/BV-02-C<br>VDP/SNK/SGSIT/ATTR/BV-04-C<br>VDP/SNK/SGSIT/OFFS/BV-03-C<br>VDP/SNK/SGSIT/OFFS/BV-04-C|
|VDP 1/2 AND VDP 4/1|Successful Connection with future<br>SDP Record value – VDP Sink|VDP/SNK/CGSIT/SFC/BV-02-C|
|VDP 0/2 AND VDP 1/2|VDP Sink SDP Service, VDP 1.1|VDP/SNK/SGSIT/ATTR/BV-06-C|
|VDP 2/1|Connection Establishment by SRC|VDP/SRC/SET/BV-01-C|
|VDP 4/2|Connection Establishment by SRC|VDP/SNK/SET/BV-01-C|
|VDP 2/2|Connection Establishment by SNK|VDP/SRC/SET/BV-02-C|
|VDP 4/1|Connection Establishment by SNK|VDP/SNK/SET/BV-02-C|
|VDP 2/3|Start Streaming by SRC|VDP/SRC/SET/BV-03-C|
|VDP 4/4|Start Streaming by SRC|VDP/SNK/SET/BV-03-C|
|VDP 2/4|Start Streaming by SNK|VDP/SRC/SET/BV-04-C|
|VDP 4/3|Start Streaming by SNK|VDP/SNK/SET/BV-04-C|
|VDP 2/5|H.263 baseline Video Stream|VDP/SRC/VS/BV-01-C|
|VDP 4/5|H.263 baseline Video Stream|VDP/SNK/VS/BV-01-C|
|VDP 2/6 OR VDP 2/7 OR<br>VDP 2/8|Other Video Streams|VDP/SRC/VS/BV-02-C|



Bluetooth SIG Proprietary Page **23 of 26**


**Video Distribution Profile (VDP) /** Test Suite













|Item|Feature|Test Case(s)|
|---|---|---|
|VDP 4/6 OR VDP 4/7 OR<br>VDP 4/8|Other Video Streams|VDP/SNK/VS/BV-02-C|
|VDP 2/10|Connection Release by SRC|VDP/SRC/REL/BV-01-C|
|VDP 4/10|Connection Release by SRC|VDP/SNK/REL/BV-01-C|
|VDP 2/11|Connection Release by SNK|VDP/SRC/REL/BV-02-C|
|VDP 4/9|Connection Release by SNK|VDP/SNK/REL/BV-02-C|
|VDP 2/12|Suspend by SRC|VDP/SRC/SUS/BV-01-C|
|VDP 4/12|Suspend by SRC|VDP/SNK/SUS/BV-01-C|
|VDP 2/13|Suspend by SNK|VDP/SRC/SUS/BV-02-C|
|VDP 4/11|Suspend by SNK|VDP/SNK/SUS/BV-02-C|
|VDP 5/2|Decode H.263 baseline|VDP/SNK/HC/BV-01-C|
|VDP 3/2|Encode H.263 baseline|VDP/SRC/HC/BV-02-C|
|VDP 4/13|Delay Reporting with VDP video<br>playback|VDP/SNK/SYN/BV-02-C|
|VDP 4/13|Delay Value|VDP/SNK/SYN/BV-01-C|