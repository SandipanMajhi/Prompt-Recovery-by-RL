# **Video Distribution Profile** **(VDP)**

_**Bluetooth**_ _**[®]**_ **Test Suite**


   - **Revision:** VDP.TS.p7

   - **Revision Date:** 2025-02-18

   - **Prepared By** : BTI

   - **Published during TCRL:** TCRL.2025-1


Bluetooth SIG Proprietary


**Video Distribution Profile (VDP) /** Test Suite


**This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth**
**Patent/Copyright License Agreement (“PCLA”) and Bluetooth Trademark License Agreement. Use of this document by**
**members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc.**
**(“Bluetooth SIG”) and its members, including the PCLA and other agreements posted on Bluetooth SIG’s website located**
**at www.bluetooth.com.**


**THIS DOCUMENT IS PROVIDED “AS IS” AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO**
**REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY**
**WARRANTY OF MERCHANTABILITY, TITLE, NON-INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT**
**THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.**


**TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL**
**LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS**
**DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR**
**SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS**
**OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN**
**ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.**


**This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual**
**property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual**
**property of Bluetooth SIG or its members.**


**This document is subject to change without notice.**


**Copyright © 2002–2025 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other**
**third-party brands and names are the property of their respective owners.**


Bluetooth SIG Proprietary Page **2 of 26**


**Video Distribution Profile (VDP) /** Test Suite

### **Contents**


**1** **Scope ..................................................................................................................................................... 5**


**2** **References, definitions, and abbreviations ....................................................................................... 6**


2.1 References .................................................................................................................................... 6
2.2 Definitions ..................................................................................................................................... 6
2.3 Acronyms and abbreviations ........................................................................................................ 6


**3** **Test Suite Structure (TSS) ................................................................................................................... 7**


3.1 Overview ....................................................................................................................................... 7
3.2 Test Strategy ................................................................................................................................. 7
3.3 Test groups ................................................................................................................................... 7


**4** **Test cases (TC) ..................................................................................................................................... 8**


4.1 Introduction ................................................................................................................................... 8

4.1.1 Test case identification conventions ....................................................................................................... 8
4.1.2 Conformance .......................................................................................................................................... 8
4.1.3 Pass/Fail verdict conventions ................................................................................................................. 9
4.2 Generic SDP Integrated Tests .................................................................................................... 10

4.2.1 Server Generic SDP Integrated Tests ................................................................................................... 10
4.2.1.1 Video Distribution Profile – Source .................................................................................................. 10

VDP/SRC/SGSIT/SERR/BV-01-C [Service record GSIT – VDP SRC] ................................................................. 10
VDP/SRC/SGSIT/ATTR/BV-01-C [Attribute GSIT – Protocol Descriptor List] ....................................................... 10
VDP/SRC/SGSIT/ATTR/BV-03-C [Attribute GSIT – Bluetooth Profile Descriptor List, VDP 1.1] .......................... 10
4.2.1.2 Video Distribution Profile – Sink ...................................................................................................... 10

VDP/SNK/SGSIT/SERR/BV-02-C [Service record GSIT – VDP SNK] .................................................................. 10
VDP/SNK/SGSIT/ATTR/BV-04-C [Attribute GSIT – Protocol Descriptor List] ....................................................... 10
VDP/SNK/SGSIT/ATTR/BV-06-C [Attribute GSIT – Bluetooth Profile Descriptor List, VDP 1.1]........................... 10
4.2.1.3 Video Distribution Profile – Attribute ID Offset String tests .............................................................. 11

VDP/SRC/SGSIT/OFFS/BV-01-C [Attribute ID Offset String GSIT – Service Name] ............................................ 11
VDP/SRC/SGSIT/OFFS/BV-02-C [Attribute ID Offset String GSIT – Provider Name] .......................................... 11
VDP/SNK/SGSIT/OFFS/BV-03-C [Attribute ID Offset String GSIT – Service Name] ............................................ 11
VDP/SNK/SGSIT/OFFS/BV-04-C [Attribute ID Offset String GSIT – Provider Name] .......................................... 11
4.2.2 Client Generic SDP Integrated Tests .................................................................................................... 11
VDP/SRC/CGSIT/SFC/BV-01-C [SDP Future Compatibility – IUT is VDP SRC] .................................................. 11
VDP/SNK/CGSIT/SFC/BV-02-C [SDP Future Compatibility – IUT is VDP SNK] .................................................. 11
4.3 Setup Video Streaming ............................................................................................................... 12

4.3.1 Establish Connection initiated by the SRC ............................................................................................ 12
4.3.1.1 Establish Connection – SRC ........................................................................................................... 12

VDP/SRC/SET/BV-01-C [Establish Connection – SRC] ....................................................................................... 12
VDP/SNK/SET/BV-01-C [Establish Connection – SRC] ....................................................................................... 12
4.3.2 Establish Connection Initiated by the SNK ............................................................................................ 12
4.3.2.1 Establish Connection – SNK............................................................................................................ 12

VDP/SRC/SET/BV-02-C [Establish Connection – SNK] ....................................................................................... 13
VDP/SNK/SET/BV-02-C [Establish Connection – SNK] ........................................................................................ 13
4.3.3 Start Video Streaming initiated by the SRC .......................................................................................... 13
4.3.3.1 Start Streaming – SRC .................................................................................................................... 13

VDP/SRC/SET/BV-03-C [Start Streaming – SRC] ................................................................................................ 13
VDP/SNK/SET/BV-03-C [Start Streaming – SRC] ................................................................................................ 13
4.3.4 Start Video Streaming initiated by the SNK .......................................................................................... 14
4.3.4.1 Start Streaming – SNK .................................................................................................................... 14


Bluetooth SIG Proprietary Page **3 of 26**


**Video Distribution Profile (VDP) /** Test Suite


VDP/SRC/SET/BV-04-C [Start Streaming – SNK] ................................................................................................ 14
VDP/SNK/SET/BV-04-C [Start Streaming – SNK] ................................................................................................ 14
4.4 Release Video Streaming ........................................................................................................... 15

4.4.1 Release Video Streaming initiated by the SRC ..................................................................................... 15
4.4.1.1 Release Streaming – SRC .............................................................................................................. 15

VDP/SRC/REL/BV-01-C [Release Streaming – SRC] .......................................................................................... 15
VDP/SNK/REL/BV-01-C [Release Streaming – SRC] ........................................................................................... 15
4.4.2 Release Video Streaming initiated by the SNK ..................................................................................... 15
4.4.2.1 Release Streaming – SNK ............................................................................................................... 15

VDP/SRC/REL/BV-02-C [Release Streaming – SNK] ........................................................................................... 16
VDP/SNK/REL/BV-02-C [Release Streaming – SNK] ........................................................................................... 16
4.5 Suspend Video Streaming .......................................................................................................... 16

4.5.1 Suspend Video Streaming initiated by the SRC .................................................................................... 16
4.5.1.1 Suspend Stream – SRC .................................................................................................................. 16

VDP/SRC/SUS/BV-01-C [Suspend Stream – SRC] .............................................................................................. 16
VDP/SNK/SUS/BV-01-C [Suspend Stream – SRC] .............................................................................................. 16
4.5.2 Suspend Video Streaming initiated by the SNK .................................................................................... 17
4.5.2.1 Suspend Stream – SNK .................................................................................................................. 17

VDP/SRC/SUS/BV-02-C [Suspend Stream – SNK] .............................................................................................. 17
VDP/SNK/SUS/BV-02-C [Suspend Stream – SNK] .............................................................................................. 17
4.6 Video Streaming ......................................................................................................................... 17

4.6.1 Video Streaming for H.263 baseline ..................................................................................................... 18
4.6.1.1 Streaming – H.263 baseline ............................................................................................................ 18

VDP/SRC/VS/BV-01-C [Streaming – H.263 baseline] .......................................................................................... 18
VDP/SNK/VS/BV-01-C [Streaming – H.263 baseline] ........................................................................................... 18
4.6.2 Video Streaming for Optional Codecs ................................................................................................... 18
4.6.2.1 Streaming – Optional Codecs .......................................................................................................... 18

VDP/SRC/VS/BV-02-C [Streaming – Optional Codecs] ........................................................................................ 19
VDP/SNK/VS/BV-02-C [Streaming – Optional Codecs] ........................................................................................ 19
4.7 Synchronous streaming of Audio and Video .............................................................................. 19

VDP/SNK/SYN/BV-02-C [Delay Reporting with VDP video playback] .................................................................. 19
VDP/SNK/SYN/BV-01-C [Delay Value] ................................................................................................................. 20
4.8 H.263 baseline Codec Conformance Test .................................................................................. 20

4.8.1 H.263 baseline Decoder Conformance ................................................................................................. 21
VDP/SNK/HC/BV-01-C [H.263 baseline Conformance – Decoder] ....................................................................... 21
4.8.2 H.263 baseline Encoder Conformance ................................................................................................. 21
VDP/SRC/HC/BV-02-C [H.263 baseline Conformance – Encoder] ....................................................................... 21


**5** **Test case mapping ............................................................................................................................. 23**


**6** **Revision history and acknowledgments .......................................................................................... 25**


Bluetooth SIG Proprietary Page **4 of 26**


**Video Distribution Profile (VDP) /** Test Suite

## **1 Scope**


This Bluetooth document contains the Test Suite Structure (TSS) and test cases to test the
implementation of the Video Distribution Profile (VDP) Specification with the objective to provide a high
probability of air interface interoperability between the tested implementation and other manufacturers’
Bluetooth devices.


The VDP utilizes the Generic Audio/Video Distribution profile (GAVDP) [2], which defines the signaling
procedures. To test VDP procedures, it is necessary to initiate a part of the GAVDP procedures.
Conformance tests for GAVDP are fully defined in the GAVDP Test Suite [4].


Bluetooth SIG Proprietary Page **5 of 26**


**Video Distribution Profile (VDP) /** Test Suite

## **2 References, definitions, and abbreviations**

#### **2.1 References**


This document incorporates provisions from other publications by dated or undated reference. These
references are cited at the appropriate places in the text, and the publications are listed hereinafter.
Additional definitions and abbreviations can be found in [7] and [9].


[1] Video Distribution Profile


[2] Generic Audio/Video Distribution Profile


[3] ICS Proforma for Video Distribution Profile (VDP)


[4] Generic Audio/Video Distribution Profile Test Suite, GAVDP.TS


[5] ISO/IEC 14496-4:2000, Information technology - Coding of audio-visual objects - Part 4:
Conformance testing


[6] ISO/IEC 14496-5:2000, Information technology - Coding of audio-visual objects - Part 5: Reference
software


[7] Test Strategy and Terminology Overview


[8] Bluetooth SIG, Conformance Test Video available at the Bluetooth SIG website in Test Suite
section


[9] Bluetooth Core Specification, Version 2.0 or later


[10] SDP Test Suite, SDP.TS

#### **2.2 Definitions**


In this Bluetooth document, the definitions from [7] and [9] apply.

#### **2.3 Acronyms and abbreviations**


In this Bluetooth document, the definitions, acronyms, and abbreviations from [7] and [9] apply.


Bluetooth SIG Proprietary Page **6 of 26**


**Video Distribution Profile (VDP) /** Test Suite

## **3 Test Suite Structure (TSS)**

#### **3.1 Overview**


The qualification of products claiming their compliance with the Bluetooth specification involves the
execution of Test Suites.

#### **3.2 Test Strategy**


The test objectives are to verify the functionality of the VDP within a Bluetooth Host and enable
interoperability between Bluetooth Hosts on different devices. The testing approach covers mandatory
and optional requirements in the specification and matches these to the support of the IUT as described
in the ICS. Any defined test herein is applicable to the IUT if the ICS logical expression defined in the Test
Case Mapping Table (TCMT) evaluates to true.


The test equipment provides an implementation of the Radio Controller and the parts of the Host needed
to perform the test cases defined in this Test Suite. A Lower Tester acts as the IUT’s peer device and
interacts with the IUT over-the-air interface. The configuration, including the IUT, needs to implement
similar capabilities to communicate with the test equipment. For some test cases, it is necessary to
stimulate the IUT from an Upper Tester. In practice, this could be implemented as a special test interface,
a Man Machine Interface (MMI), or another interface supported by the IUT.


This Test Suite contains Valid Behavior (BV) tests complemented with Invalid Behavior (BI) tests where
required. The test coverage mirrored in the Test Suite Structure is the result of a process that started with
catalogued specification requirements that were logically grouped and assessed for testability enabling
coverage in defined test purposes.

#### **3.3 Test groups**


The following test groups have been defined:


- Generic SDP Integrated Tests


- Setup Video Streaming


- Release Video Streaming


- Suspend Video Streaming


- Video Streaming


- Synchronous streaming of Audio and Video


- H.263 baseline Codec Conformance Test


Bluetooth SIG Proprietary Page **7 of 26**


**Video Distribution Profile (VDP) /** Test Suite

## **4 Test cases (TC)**

#### **4.1 Introduction**


**4.1.1** **Test case identification conventions**


Test cases are assigned unique identifiers per the conventions in [7]. The convention used here is:
**<spec abbreviation>/<IUT role>/** <class>/ **<feat>** /<func>/<subfunc>/<cap>/ **<xx>-<nn>-<y>** .


Additionally, testing of this specification includes tests from the SDP Test Suite [10] referred to as Generic
SDP Integrated Tests (GSIT); when used, the test cases in GSIT are referred to through a TCID string
using the following convention:
**<spec abbreviation>/<IUT role>/<GSIT test group>** /< GSIT class >/<xx>-<nn>-<y>.

|Identifier Abbreviation|Spec Identifier <spec abbreviation>|
|---|---|
|VDP|Video Distribution Profile|
|**Identifier Abbreviation**|**Role Identifier <IUT role>**|
|SNK|Sink|
|SRC|Source|
|**Identifier Abbreviation**|**Reference Identifier <GSIT test group>**|
|CGSIT|Client Generic SDP Integrated Tests|
|SGSIT|Server Generic SDP Integrated Tests|
|**Identifier Abbreviation**|**Reference Identifier <GSIT class>**|
|ATTR|Attribute|
|OFFS|Attribute ID Offset String|
|SERR|Service Record|
|SFC|SDP Future Compatibility|
|**Identifier Abbreviation**|**Feature Identifier <feat>**|
|HC|H.263 Baseline Decoder Conformance|
|REL|Release Video Streaming|
|SET|Setup Video Streaming|
|SUS|Suspend Video Streaming|
|SYN|Synchronous Streaming of Audio and Video|
|VS|Video Streaming|



_Table 4.1: VDP TC feature naming conventions_


**4.1.2** **Conformance**


When conformance is claimed for a particular specification, all capabilities are to be supported in the
specified manner. The mandated tests from this Test Suite depend on the capabilities to which
conformance is claimed.


The Bluetooth Qualification Program may employ tests to verify implementation robustness. The level of
implementation robustness that is verified varies from one specification to another and may be revised for
cause based on interoperability issues found in the market.


Bluetooth SIG Proprietary Page **8 of 26**


**Video Distribution Profile (VDP) /** Test Suite


Such tests may verify:


- That claimed capabilities may be used in any order and any number of repetitions not excluded by the
specification


- That capabilities enabled by the implementations are sustained over durations expected by the use
case


- That the implementation gracefully handles any quantity of data expected by the use case


- That in cases where more than one valid interpretation of the specification exists, the implementation
complies with at least one interpretation and gracefully handles other interpretations


- That the implementation is immune to attempted security exploits


A single execution of each of the required tests is required to constitute a Pass verdict. However, it is
noted that to provide a foundation for interoperability, it is necessary that a qualified implementation
consistently and repeatedly pass any of the applicable tests.


In any case, where a member finds an issue with the test plan generated by the Bluetooth SIG
qualification tool, with the test case as described in the Test Suite, or with the test system utilized, the
member is required to notify the responsible party via an erratum request such that the issue may be
addressed.


**4.1.3** **Pass/Fail verdict conventions**


Each test case has an Expected Outcome section. The IUT is granted the Pass verdict when all the
detailed pass criteria conditions within the Expected Outcome section are met.


The convention in this Test Suite is that, unless there is a specific set of fail conditions outlined in the test
case, the IUT fails the test case as soon as one of the pass criteria conditions cannot be met. If this
occurs, then the outcome of the test is a Fail verdict.


Bluetooth SIG Proprietary Page **9 of 26**


**Video Distribution Profile (VDP) /** Test Suite

#### **4.2 Generic SDP Integrated Tests**


**4.2.1** **Server Generic SDP Integrated Tests**


**4.2.1.1** **Video Distribution Profile – Source**


Execute the Generic SDP Integrated Tests defined in Section 6.3, Server test procedures (SGSIT), in [10] using Table 4.2 below as input:














|TCID|Reference|Attribute ID name|Attribute ID<br>definition source<br>(Universal,<br>Profile)|Value/secondary value|Attribute presence<br>(Present/Present for [role],<br>Optionally present, TCMT<br>defined)|
|---|---|---|---|---|---|
|VDP/SRC/SGSIT/SERR/BV-01-C<br>[Service record GSIT – VDP SRC]|[1] 5.3|ServiceClassIDList|Universal|“Video Source” (UUID)|Present for SRC|
|VDP/SRC/SGSIT/ATTR/BV-01-C<br>[Attribute GSIT – Protocol Descriptor<br>List]|[1] 5.3|ProtocolDescriptorList|Universal|“L2CAP” (UUID): PSM –<br>“AVDTP” (Uint16),<br>“AVDTP” (UUID): Version –<br>skip (Uint16)|Present for SRC|
|VDP/SRC/SGSIT/ATTR/BV-03-C<br>[Attribute GSIT – Bluetooth Profile<br>Descriptor List, VDP 1.1]|[1] 5.3|BluetoothProfileDescriptorList|Universal|“Video Distribution” (UUID):<br>Version – “0x0101” (Uint16)|TCMT defined|



_Table 4.2: Input for the Video Distribution Profile Source SGSIT SDP test procedure_


**4.2.1.2** **Video Distribution Profile – Sink**


Execute the Generic SDP Integrated Tests defined in Section 6.3, Server test procedures (SGSIT), in [10] using Table 4.3 below as input:














|TCID|Reference|Attribute ID name|Attribute ID<br>definition source<br>(Universal,<br>Profile)|Value/secondary value|Attribute presence<br>(Present/Present for [role],<br>Optionally present, TCMT<br>defined)|
|---|---|---|---|---|---|
|VDP/SNK/SGSIT/SERR/BV-02-C<br>[Service record GSIT – VDP SNK]|[1] 5.3|ServiceClassIDList|Universal|“Video Sink” (UUID)|Present for SNK|
|VDP/SNK/SGSIT/ATTR/BV-04-C<br>[Attribute GSIT – Protocol Descriptor<br>List]|[1] 5.3|ProtocolDescriptorList|Universal|“L2CAP” (UUID): PSM –<br>“AVDTP” (Uint16),<br>“AVDTP” (UUID): Version –<br>skip (Uint16)|Present for SNK|
|VDP/SNK/SGSIT/ATTR/BV-06-C<br>[Attribute GSIT – Bluetooth Profile<br>Descriptor List, VDP 1.1]|[1] 5.3|BluetoothProfileDescriptorList|Universal|“Video Distribution” (UUID):<br>Version – “0x0101” (Uint16)|TCMT defined|



_Table 4.3: Input for the Video Distribution Profile Sink SGSIT SDP test procedure_


Bluetooth SIG Proprietary Page **10 of 26**


**Video Distribution Profile (VDP) /** Test Suite


**4.2.1.3** **Video Distribution Profile – Attribute ID Offset String tests**


Execute the Generic SDP Integrated Tests defined in Section 6.3, Server test procedures (SGSIT), in [10] using Table 4.4 below as input:






|TCID|Reference|ServiceSearchPattern|Attribute ID name|Attribute ID Offset|Attribute presence<br>(Present/Present for [role],<br>Optionally present, TCMT<br>defined)|
|---|---|---|---|---|---|
|VDP/SRC/SGSIT/OFFS/BV-01-C<br>[Attribute ID Offset String GSIT –<br>Service Name]|[1] 5.3|Video Source|ServiceName|0x0000|Optionally present|
|VDP/SRC/SGSIT/OFFS/BV-02-C<br>[Attribute ID Offset String GSIT –<br>Provider Name]|[1] 5.3|Video Source|ProviderName|0x0002|Optionally present|
|VDP/SNK/SGSIT/OFFS/BV-03-C<br>[Attribute ID Offset String GSIT –<br>Service Name]|[1] 5.3|Video Sink|ServiceName|0x0000|Optionally present|
|VDP/SNK/SGSIT/OFFS/BV-04-C<br>[Attribute ID Offset String GSIT –<br>Provider Name]|[1] 5.3|Video Sink|ProviderName|0x0002|Optionally present|



_Table 4.4: Input for the Video Distribution Profile SGSIT Attribute ID Offset String tests_


**4.2.2** **Client Generic SDP Integrated Tests**


Execute the Generic SDP Future Compatibility Tests defined in Section 6.4, Client test procedures (CGSIT), in [10] using Table 4.5 below as input:










|TCID|Reference|Service Record Service Class<br>UUID description|Lower Tester SDP record initial conditions|
|---|---|---|---|
|VDP/SRC/CGSIT/SFC/BV-01-C<br>[SDP Future Compatibility – IUT is<br>VDP SRC]|[1] 5.3|VDP Sink|The Lower Tester exposes a VDP Sink SDP record.<br>The version in the Bluetooth Profile Descriptor List is greater than the most recently<br>adopted version.|
|VDP/SNK/CGSIT/SFC/BV-02-C<br>[SDP Future Compatibility – IUT is<br>VDP SNK]|[1] 5.3|VDP Source|The Lower Tester exposes a VDP Source SDP record.<br>The version in the Bluetooth Profile Descriptor List is greater than the most recently<br>adopted version.|



_Table 4.5: Input for the Client CGSIT SDP future compatibility tests_


Bluetooth SIG Proprietary Page **11 of 26**


**Video Distribution Profile (VDP) /** Test Suite

#### **4.3 Setup Video Streaming**


Verify streaming setup.


**4.3.1** **Establish Connection initiated by the SRC**


Verify that the parameters are configured and stream connection is established by the SRC.


**4.3.1.1** **Establish Connection – SRC**

- Test Purpose


Verify that the SRC can establish stream connection successfully.


- Reference


[1] 5.1.1


[2] 4.1.1


- Initial Condition


   - Both devices are in standby mode.


- Test Case Configuration





_Table 4.6: Establish Connection – SRC test cases_


- Test Procedure


1. Initiate the user action (e.g., press button) on the SRC to set up connection.
2. Initiate another user action (e.g., press button) on the SRC to start video streaming, if it does not

start streaming consecutively after connection establishment.


- Expected Outcome


Pass verdict


If there is a corresponding indicator, then establishment of connection is indicated.


It is indicated that video streaming started upon user action.


**4.3.2** **Establish Connection Initiated by the SNK**


Verify that the parameters are configured and stream connection is established by the SNK.


**4.3.2.1** **Establish Connection – SNK**

- Test Purpose


Verify that the SNK can establish stream connection successfully.


- Reference


[1] 5.1.1


[2] 4.1.1


Bluetooth SIG Proprietary Page **12 of 26**


**Video Distribution Profile (VDP) /** Test Suite




- Initial Condition


   - Both devices are in standby mode.


- Test Case Configuration





_Table 4.7: Establish Connection – SNK test cases_


- Test Procedure


Initiate the user action (e.g., press button) on the SNK to set up connection. If it does not start
streaming consecutively after connection establishment, initiate another user action (e.g., press
button) on the SNK to start video streaming.


- Expected Outcome


Pass verdict


If there is a corresponding indicator, then establishment of connection is indicated.


It is indicated that video streaming started upon user action.


**4.3.3** **Start Video Streaming initiated by the SRC**


Verify that video streaming is started by the SRC.


**4.3.3.1** **Start Streaming – SRC**

- Test Purpose


Verify that the SRC can start video streaming.


- Reference


[1] 5.1.1


[2] 4.1.1


- Initial Condition


   - Connection has been established.


- Test Case Configuration





_Table 4.8: Start Streaming – SRC test cases_


- Test Procedure


Initiate the user action (e.g., press button) on the SRC to start video streaming. No user action may
be required when Start streaming is preceded from connection establishment consecutively.


Bluetooth SIG Proprietary Page **13 of 26**


**Video Distribution Profile (VDP) /** Test Suite


- Expected Outcome


Pass verdict


If there is a corresponding indicator, then start video streaming is indicated. Otherwise, streaming
video is monitored on the SNK.


**4.3.4** **Start Video Streaming initiated by the SNK**


Verify that video streaming is started by the SNK.


**4.3.4.1** **Start Streaming – SNK**

- Test Purpose


Verify that the SNK can start video streaming.


- Reference


[1] 5.1.1


[2] 4.1.1


- Initial Condition


   - Connection has been established.


- Test Case Configuration





_Table 4.9: Start Streaming – SNK_


- Test Procedure


Initiate the user action (e.g., press button) on the SNK to start video streaming. No user action may
be required when Start streaming is preceded from connection establishment consecutively.


- Expected Outcome


Pass verdict


If there is a corresponding indicator, then start video streaming is indicated. Otherwise, streaming
video is monitored on the SNK.


Bluetooth SIG Proprietary Page **14 of 26**


**Video Distribution Profile (VDP) /** Test Suite

#### **4.4 Release Video Streaming**


Verify that the video stream connection is released.


**4.4.1** **Release Video Streaming initiated by the SRC**


Verify that the video stream connection is released by the SRC.


**4.4.1.1** **Release Streaming – SRC**

- Test Purpose


Verify that the SRC can release streaming and that the SNK can accept streaming release.


- Reference


[1] 5.1.1


[2] 4.1.3


- Initial Condition


   - Streaming connection is established.


- Test Case Configuration





_Table 4.10: Release Streaming – SRC test cases_


- Test Procedure


Initiate the user action (e.g., press button) on the SRC to release streaming. Then, re-establish a
video streaming connection and start video streaming.


- Expected Outcome


Pass verdict


If there is a corresponding indicator, release video streaming is indicated. Otherwise, video streaming
is stopped.


The user action releases video streaming connection, and it is possible to re-establish a video
streaming connection and start video streaming.


**4.4.2** **Release Video Streaming initiated by the SNK**


Verify that the video stream connection is released by the SNK.


**4.4.2.1** **Release Streaming – SNK**

- Test Purpose


Verify that the SRC can accept streaming release and that the SNK can release streaming.


- Reference


[1] 5.1.1


[2] 4.1.3


Bluetooth SIG Proprietary Page **15 of 26**


**Video Distribution Profile (VDP) /** Test Suite




- Initial Condition


   - Streaming connection is established.


- Test Case Configuration





_Table 4.11: Release Streaming – SNK test cases_


- Test Procedure


Initiate the user action (e.g., press button) on the SNK to release streaming. Then, re-establish a
video streaming connection and start video streaming.


- Expected Outcome


Pass verdict


If there is a corresponding indicator, release video streaming is indicated. Otherwise, video streaming
is stopped.


The user action releases video streaming connection and is possible to re-establish a video
streaming connection and start video streaming.

#### **4.5 Suspend Video Streaming**


Verify that the video streaming is suspended.


**4.5.1** **Suspend Video Streaming initiated by the SRC**


Verify that the video streaming is suspended by the SRC.


**4.5.1.1** **Suspend Stream – SRC**

- Test Purpose


Verify that the SRC can suspend streaming and that the SNK can accept streaming suspend.


- Reference


[1] 5.1.1


[2] 4.1.4


- Initial Condition


   - Streaming connection is established.


- Test Case Configuration





_Table 4.12: Suspend Stream – SRC test cases_


Bluetooth SIG Proprietary Page **16 of 26**


**Video Distribution Profile (VDP) /** Test Suite


- Test Procedure


Initiate the user action (e.g., press button) on the SRC to suspend streaming. Then resume video
streaming by restarting video streaming afterwards.


- Expected Outcome


Pass verdict


If there is a corresponding indicator, suspend video streaming is indicated.


Video streaming is stopped by the user action. Indication of restart video streaming is monitored
when resumed.


**4.5.2** **Suspend Video Streaming initiated by the SNK**


Verify that the video stream connection is suspended by the SNK.


**4.5.2.1** **Suspend Stream – SNK**

- Test Purpose


Verify that the SNK can suspend streaming and that the SRC can accept streaming suspend.


- Reference


[1] 5.1.1


[2] 4.1.4


- Initial Condition


   - Streaming connection is established.


- Test Case Configuration





_Table 4.13: Suspend Stream – SNK test cases_


- Test Procedure


Initiate the user action (e.g., press button) on the SNK to suspend streaming. Then resume video
streaming by restarting video streaming afterwards.


- Expected Outcome


Pass verdict


If there is a corresponding indicator, suspend video streaming is indicated.


Video streaming is stopped by the user action. Indication of restart video streaming is monitored
when resumed.

#### **4.6 Video Streaming**


Verify that video streaming is executed successfully by streaming video data.


The video data to test this test case can be arbitrary provided that the expected outcome of decoded
video is known beforehand. Some codec has reference test vectors for codec conformance test such as
MPEG-4 in [5] which can be used for streaming. The expected outcome of decoded video from such


Bluetooth SIG Proprietary Page **17 of 26**


**Video Distribution Profile (VDP) /** Test Suite


reference test vectors can be reproduced by using the reference codec software which is also provided.
With the reference codec software test vectors can be generated as well.


If a codec does not have reference test vector nor reference codec software, it is advised to consult with
the codec owner organization on how to verify conformance of codec implementation.


**4.6.1** **Video Streaming for H.263 baseline**


Verify that video streaming based on H.263 baseline is executed successfully.


**4.6.1.1** **Streaming – H.263 baseline**

- Test Purpose


Verify that the SRC can stream video data encoded in H.263 baseline and that the SNK can
successfully receive the video data.


- Reference


[1] 3.2


- Initial Condition


   - Streaming connection is established and configured using H.263 baseline.


- Test Case Configuration





_Table 4.14: Streaming – H.263 baseline test cases_


- Test Procedure


Start streaming on the SRC. If defined test vectors are available, then they should be used for the
input, otherwise appropriate input is applied. For more information on test vectors for H.263 baseline,
refer to Section 4.8 of this document.


- Expected Outcome


Pass verdict


If a video output is available, the video is monitored. Otherwise, it is indicated that streaming was
successfully executed.


If a test vector is used as an input of the SRC, the video output matches the expected outcome
derived by the reference codec software.


**4.6.2** **Video Streaming for Optional Codecs**


Verify that video streaming based on optional codec format is executed successfully.


**4.6.2.1** **Streaming – Optional Codecs**

- Test Purpose


Verify that the SRC can stream video data encoded in an optional codec and that the SNK can
successfully receive the video data.


Bluetooth SIG Proprietary Page **18 of 26**


**Video Distribution Profile (VDP) /** Test Suite


- Reference


[1] 3.2


- Initial Condition


   - Streaming connection is established and configured using an optional codec.


- Test Case Configuration





_Table 4.15: Streaming – Optional Codecs test cases_


- Test Procedure


Start streaming on the SRC. If defined test vectors for the codec under test are available, then they
should be used for the input, otherwise appropriate input is applied. For more information on test
vectors for the optional codec, refer to the codec owner organization.


- Expected Outcome


Pass verdict


If a video output is available, the video is monitored. Otherwise, it is indicated that streaming was
successfully executed.


If a test vector is used as an input of the SRC, the video output matches to expected outcome derived
by the reference codec software.

#### **4.7 Synchronous streaming of Audio and Video**


Verify the correct implementation of audio video synchronization.


**VDP/SNK/SYN/BV-02-C [Delay Reporting with VDP video playback]**

- Test Purpose


The presentation of audio and video is synchronized, e.g., the presentation has to occur without a
noticeable delay.


- Reference


[2] 4.1.18


[8]


- Initial Condition


   - The Source is connected with an A2DP sink and a VDP sink (IUT).


- Test Procedure


Start streaming of a test video.


A sample video [8] is provided that contains a sequence of numbers that are spoken by a user and
displayed at the same time. An acoustic marker appears whenever the number changes.


It is up to the manufacturer to use the provided video or to apply their own test procedure to ensure
audio and video presentation is synchronized if the sample video cannot be used for some reason.


Bluetooth SIG Proprietary Page **19 of 26**


**Video Distribution Profile (VDP) /** Test Suite


- Expected Outcome


Pass verdict


Audio and video are synchronized.


This means the spoken number needs to be the same as the number shown on the screen and the
number change in the video needs to be aligned with the corresponding acoustic marker in the video.


- Notes


If the test video is not used the manufacturer is responsible to use an effective method to verify the
synchronization.


**VDP/SNK/SYN/BV-01-C [Delay Value]**

- Test Purpose


Verify that the reported delay value is correct.


- Reference


[2] 4.1.18


- Initial Condition


   - A stream connection is established.


   - IUT is SNK.


- Test Procedure


Start streaming and receive a delay report from SNK.


- Expected Outcome


Pass verdict


The reported delay value is within a given range expected by the manufacturer.


- Notes


This is a subjective plausibility test.

#### **4.8 H.263 baseline Codec Conformance Test**


Verify that the mandatory codec H.263 baseline is properly implemented.


This conformance test is conducted locally by the implementer. Furthermore, the intent of this test is to
assure basic conformity to the codec specification and is not to control the quality or performance of the
codec implementation. The quality and performance of the codec is up to the implementation as far as it
complies with the specification.


The conformance test of H.263 baseline codec is performed according to the MPEG-4 conformance
testing [5] and its reference software [6]. It is mandated to satisfy the requirement described in [5] to be
compliant with H.263 baseline. The reasons for utilizing MPEG-4 conformance test [5] to H.263 baseline
codec are:


   - There is no conformance Test Suite in ITU standard for H.263 baseline codec available in public.


   - H.263 baseline (without annexes) is incorporated as part of MPEG-4 visual specification (known
as ‘short header’ in the specification), and the conformance Test Suite of MPEG-4 [5] covers
H.263 baseline as well.


Bluetooth SIG Proprietary Page **20 of 26**


**Video Distribution Profile (VDP) /** Test Suite


**4.8.1** **H.263 baseline Decoder Conformance**


Verify that H.263 baseline decoder is properly implemented.


**VDP/SNK/HC/BV-01-C [H.263 baseline Conformance – Decoder]**

- Test Purpose


Verify that H.263 baseline decoder is properly implemented on the SNK.


Check that the decoder satisfies the requirement for conformance. See [5] and [6].


- Reference


[5]


[6]


- Initial Condition


   - SNK device is in decoding mode of H.263 baseline bitstreams.


   - IUT in normal operation with supported parameters defined in Section 4.3 in [1].


- Test Procedure


Input test bitstreams in the electronics annex in [5]. The bitstream files are located on the CD-ROM
which is included as an electronic annex in reference [5] as following:
./CONFORMANCE_BITSTREAMS_CD1/Visual/natural/simple/Short.zip.


- Expected Outcome


Pass verdict


The video output of the decoder satisfies the requirement in [5].


**4.8.2** **H.263 baseline Encoder Conformance**


Verify that H.263 baseline Encoder is properly implemented.


**VDP/SRC/HC/BV-02-C [H.263 baseline Conformance – Encoder]**

- Test Purpose


Verify that H.263 baseline encoder is properly implemented on the SRC.


Check that the bitstreams produced by the encoder satisfies the requirement for conformance. See

[5] and [6].


- Reference


[5]


[6]


- Initial Condition


   - SRC device is in encoding mode of H.263 baseline.


   - IUT in normal operation with supported parameters defined Section 4.3 in [1].


- Test Procedure


Activate the encoder and input video sequence.


Bluetooth SIG Proprietary Page **21 of 26**


**Video Distribution Profile (VDP) /** Test Suite


- Expected Outcome


Pass verdict


The video output of the encoder satisfies the requirement in [5]. Furthermore, in detail, the following
items are observed:


   - The reference decoder [6] can decode the bitstreams encoded by the implementation without an
error.


   - It is confirmed that the reference decoder [6] can decode the bitstreams encoded by the
implementation as a short header bitstream.


Bluetooth SIG Proprietary Page **22 of 26**


**Video Distribution Profile (VDP) /** Test Suite

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


_Table 5.1: Test case mapping_


Bluetooth SIG Proprietary Page **24 of 26**


**Video Distribution Profile (VDP) /** Test Suite

## **6 Revision history and acknowledgments**


_**Revision History**_




















|Publication<br>Number|Revision<br>Number|Date|Comments|
|---|---|---|---|
|0|D10r00|2004-08-11|Clarification amended in section 4.6.1.1.|
|1|1.0.1r1|2006-02-28|Editorial Updates|
|2|1.2.0|2006-05-31|Update document number, prepare for publication|
||1.1.0r1|2011-03-01|Update after AV F2F|
||1.1.0r2|2011-11-01|Incorporated changes from Core Spec 2.1+EDR<br>updates|
||1.1.0r3|2012-04-01|BTI comment resolution|
||1.1.0r4|2012-04-15|Removed redundant references from Section 2.1|
||1.1.0r5|2012-05-01|Changed the TCMT to align with the revised PICS|
||1.1.0r6|2012-06-01|Added a Conformance section with the current text to<br>4.2.1. Miscellaneous editing of bulleting in test cases.|
||1.1.0r7|2012-07-01|Added reference to A/V synchronization test video<br>and referred to this from test case VDP/SNK/SYN/BV-<br>01-I (legacy test case ID TP/SYN/BV-01-I).|
|3|1.1.0|2012-07-24|Prepare for publication.|
||1.1.1r00|2016-08-03|Converted to new Test Case ID conventions as<br>defined in TSTO v4.1.|
||1.1.1r01|2016-11-06|Converted test specification template.|
|4|1.1.1|2016-12-13|Approved by BTI. Prepared for TCRL 2016-2<br>publication.|
||p5r00|2022-02-25 –<br>2022-02-28|TSE 17931 (rating 2): Updated the TCMT to reflect<br>the renumbered VDP Sink features and codecs tables<br>to align with Launch Studio.<br>Template-related editorials, including aligning the<br>copyright page with v2 of the DNMD and assigning<br>publication number 4 to previous v1.1.1.|
|5|p5|2022-06-28|Approved by BTI on 2022-05-31. Prepared for<br>TCRL 2022-1 publication.|
||p6r00–r05|2023-10-24 –<br>2024-04-09|TSE 23889 (rating 1): Converted -I tests to -C tests as<br>appropriate; updated the TCMT and TCRL<br>accordingly. Removed intro text in the TSS overview<br>related to interoperability. Renumbered<br>VDP/SNK/SYN/BV-01-I to VDP/SNK/SYN/BV-02-C to<br>avoid duplicate created by the -I to -C conversion.<br>TSE 24538 (rating 4): Added new GSIT section with<br>new TCs VDP/SRC/CGSIT/SFC/BV-01-C,<br>VDP/SRC/SGSIT/SERR/BV-01-C,<br>VDP/SRC/SGSIT/OFFS/BV-01-C and -02-C,<br>VDP/SRC/SGSIT/ATTR/BV-01-C – -03-C,<br>VDP/SNK/CGSIT/SFC/BV-02-C,<br>VDP/SNK/SGSIT/SERR/BV-02-C,<br>VDP/SNK/SGSIT/OFFS/BV-03-C and -04-C, and<br>VDP/SNK/SGSIT/ATTR/BV-04-C – -06-C. Updated<br>the TCMT accordingly. Added a reference to the SDP|



Bluetooth SIG Proprietary Page **25 of 26**


**Video Distribution Profile (VDP) /** Test Suite









|Publication<br>Number|Revision<br>Number|Date|Comments|
|---|---|---|---|
||||TS. Updated the Test Groups and TC Conventions<br>sections. Modernized test language/format globally.<br>Editorials to align the document with the latest TS<br>template, including simplifying the test groups section,<br>adding the boilerplate test strategy, and removing<br>draft rev history entries.|
|6|p6|2024-07-01|Approved by BTI on 2024-05-22. Prepared for<br>TCRL 2024-1 publication.|
||p7r00–r02|2024-10-15 –<br>2024-12-09|TSE 25420 (rating 2): Updated TCMT for<br>VDP/SNK/CGSIT/SFC/BV-02-C.<br>TSE 26775 (rating 2): Deleted<br>VDP/SRC/SGSIT/ATTR/BV-02-C and<br>VDP/SNK/SGSIT/ATTR/BV-05-C because VDP v1.0<br>is deprecated. Updated the TCMT accordingly.<br>Updated the TCMT introduction to align with the<br>current TS template.|
|7|p7|2025-02-18|Approved by BTI on 2024-12-25. Prepared for TCRL<br>2025-1 publication.|


_**Acknowledgments**_

|Name|Company|
|---|---|
|Rüdiger Mosig|Berner and Mattner|
|Alicia Courtney|Broadcom|
|Ash Kapur|Broadcom|
|Allan Madsen|CSR|
|David Trainor|CSR|
|Morgan Lindqvist|Ericsson|
|Tsuyoshi Okada|Matsushita Electric Industrial|
|Toshio Sakimura|Matsushita Electric Industrial|
|Stephen Raxter|National Analysis Center|
|Janne Hamalainen|Nokia|
|Miska M. Hannuksela|Nokia|
|Kalervo Kontola|Nokia|
|Thierry Wœlfflé|Parrot|
|Scott Walsh|Plantronics|
|Wilhelm Hagg|Sony|
|Masahiko Seki|Sony|
|Makoto Kobayashi|Toshiba|
|Yoshiaki Takabatake|Toshiba|



Bluetooth SIG Proprietary Page **26 of 26**


