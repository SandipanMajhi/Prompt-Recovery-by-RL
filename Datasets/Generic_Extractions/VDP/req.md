|BLUETOOTH DOC|Date / Year-Month-Day|Approved|Revision|Document No|
|---|---|---|---|---|
|_BLUETOOTH_ DOC|2012-07-24|Adopted|V11|VDP_SPEC|
|Prepared<br>Bluetooth Audio Video<br>Working Group|e-mail address<br>avv-main@bluetooth.org|e-mail address<br>avv-main@bluetooth.org|e-mail address<br>avv-main@bluetooth.org|N.B.<br>|

# **VIDEO DISTRIBUTION PROFILE**


### **Abstract** This profile defines the requirements for Bluetooth® devices necessary for support of the video distribution. The requirements are expressed in terms of end-user services, and by defining the features and procedures that are required for interoperability between Bluetooth devices in the Video Distribution usage model.


_BLUETOOTH_ SPECIFICATION Page 2 of 42
_Video Distribution Profile_

### Revision History














|Revision<br>Number|Date|Comments|
|---|---|---|
|D05r00|Apr 2002|Release to Associates|
|D07r00|May 2002|Release to Associates|
|D09r00|Sept 2002|Release to Associates and Early Adopters|
|D09r01|Jan 2003|Updated address to assigned numbers and e-mail reflector.<br>Figure 4.5 not split over two pages|
|D09r02|May 2003|Updated references and wording according to the comment<br>from BQRB’s review (26 March 2003)|
|D09r03|May 2003|Updated mandatory codec to conditional. Updated a profile<br>number in SDP field to 0x0090|
|D09r04|May 2003|Structures of the document was broken by MS word references,<br>so repaired the structures|
|D09r05|June 2003|Section 4.2.1 Mandatory Codec was clarified and remove the<br>section 4.2.4 Pre-encoded Video Data because the description<br>of pre-encoded data is created in section 4.2.1. These changes<br>were discussed in F2F@Stockholm and Profile CC on<br>2003/June/26|
|V09r00|July 2003|The Notice under the Table4-1 in Section 4.2 is revised for<br>clarification. This was discussed test cc on 2003/July/04|
|V09r01|16 April 2004|Updated for Prototyping Specification|
|V09r02|27 April 2004|Changed trademark on Bluetooth to registered trademark on<br>title page. Updated Disclaimer and Copyright Notice to font to<br>match rest of document.|
|V09r03|27 May 2004|Updated reflecting adoption as a Prototyping Specification|
|D10r00|04 June 2004|Updated reflecting version changing. And also fit to the Core<br>1.2|
|D10r01|16 June 2004|Approved by the BARB|
|V10r00|8 September 2004|Updated reflecting adoption as a V1.0 Specification|
|D11r00 -<br>D11r10|December 2009 -<br>17 May 2012|Release for Synchronization Voting Draft<br>Update after Review<br>Core Spec 2.1 + EDR updates<br>ESR05 E4071 Section 4.7.2.1<br>Address reviewer’s comments<br>Remove underscores from IEEE terms<br>Added specification change history as Section 1.4<br>Incorporated comments to Change History Section<br>Editorial corrections to Section 1.4<br>Merged ESR01-05 text. Miscellaneous editorial updates,<br>particularly around references<br>Added SIG formatting. Moved tables from centered to left-<br>justified. Corrected some hyperlink coloring.<br>Undeleted errata tag D4071. Changed date and revision<br>number on title page.|
|V11|24 July 2012|Adopted by the Bluetooth SIG Board of Directors|


_BLUETOOTH_ SPECIFICATION Page 3 of 42
_Video Distribution Profile_

### Contributors


|Name|Company|
|---|---|
|Rüdiger Mosig|Berner and Mattner|
|Alicia Courtney|Broadcom|
|Ash Kapur|Broadcom|
|Jiny Bradshaw|CSR|
|Allan Madsen|CSR|
|David Trainor|CSR|
|Akira Miyajima|Denso|
|Morgan Lindqvist|Ericsson|
|Yuan Quinton|Marvell|
|Masatomo Hori|Matsushita Electric Industrial|
|Tsuyoshi Okada|Matsushita Electric Industrial|
|Thomas Karlsson|Mecel|
|Janne Hamalainen|Nokia|
|Kalervo Kontola|Nokia|
|Jurgen Schnitzler|Nokia|
|Miska M. Hannuksela|Nokia|
|Thierry Wœlfflé|Parrot|
|Shaun Barrett|Philips|
|Christian Bouffioux|Philips|
|Frans de Bont|Philips|
|Emmanuel Mellery|Philips|
|Marc Vauclair|Philips|
|Scott Walsh|Plantronics|
|Brian Gix|Qualcomm|
|John Larkin|Qualcomm|
|Atsushi Ichise|Sony|
|Masahiko Seki|Sony|
|Masakazu Hattori|Sony|
|Harumi Kawamura|Sony|
|Wilhelm Hagg|Sony|
|Yoshiyuki Nezu|Sony|
|Siân James|Symbian|
|Yoshiaki Takabatake|Toshiba|
|Makoto Kobayashi|Toshiba|
|Ichiro Tomoda|Toshiba|
|Kensaku Fujimoto|Toshiba|


_BLUETOOTH_ SPECIFICATION Page 4 of 42
_Video Distribution Profile_

### Disclaimer and Copyright Notice


The copyright in this specification is owned by the Promoter Members of _Bluetooth®_ Special Interest Group
(SIG), Inc. (“ _Bluetooth_ SIG”). Use of these specifications and any related intellectual property (collectively, the
“Specification”), is governed by the Promoters Membership Agreement among the Promoter Members and
_Bluetooth_ SIG (the “Promoters Agreement”), certain membership agreements between _Bluetooth_ SIG and its
Adopter and Associate Members (the “Membership Agreements”) and the _Bluetooth_ Specification Early
Adopters Agreements (1.2 Early Adopters Agreements) among Early Adopter members of the unincorporated
_Bluetooth_ SIG and the Promoter Members (the “Early Adopters Agreement”). Certain rights and obligations of
the Promoter Members under the Early Adopters Agreements have been assigned to _Bluetooth_ SIG by the
Promoter Members.


Use of the Specification by anyone who is not a member of _Bluetooth_ SIG or a party to an Early Adopters
Agreement (each such person or party, a “Member”), is prohibited. The legal rights and obligations of each
Member are governed by their applicable Membership Agreement, Early Adopters Agreement or Promoters
Agreement. No license, express or implied, by estoppel or otherwise, to any intellectual property rights are
granted herein.


Any use of the Specification not in compliance with the terms of the applicable Membership Agreement, Early
Adopters Agreement or Promoters Agreement is prohibited and any such prohibited use may result in
termination of the applicable Membership Agreement or Early Adopters Agreement and other liability permitted
by the applicable agreement or by applicable law to _Bluetooth_ SIG or any of its members for patent, copyright
and/or trademark infringement.


**THE SPECIFICATION IS PROVIDED “AS IS” WITH NO WARRANTIES WHATSOEVER, INCLUDING ANY**
**WARRANTY OF MERCHANTABILITY, NONINFRINGEMENT, FITNESS FOR ANY PARTICULAR**
**PURPOSE, SATISFACTORY QUALITY, OR REASONABLE SKILL OR CARE, OR ANY WARRANTY**
**ARISING OUT OF ANY COURSE OF DEALING, USAGE, TRADE PRACTICE, PROPOSAL,**
**SPECIFICATION OR SAMPLE** .


Each Member hereby acknowledges that products equipped with the _Bluetooth_ technology (" _Bluetooth_
products") may be subject to various regulatory controls under the laws and regulations of various governments
worldwide. Such laws and regulatory controls may govern, among other things, the combination, operation,
use, implementation and distribution of _Bluetooth_ products. Examples of such laws and regulatory controls
include, but are not limited to, airline regulatory controls, telecommunications regulations, technology transfer
controls and health and safety regulations. Each Member is solely responsible for the compliance by their
_Bluetooth_ Products with any such laws and regulations and for obtaining any and all required authorizations,
permits, or licenses for their _Bluetooth_ products related to such regulations within the applicable jurisdictions.
Each Member acknowledges that nothing in the Specification provides any information or assistance in
connection with securing such compliance, authorizations or licenses **. NOTHING IN THE SPECIFICATION**
**CREATES ANY WARRANTIES, EITHER EXPRESS OR IMPLIED, REGARDING SUCH LAWS OR**
**REGULATIONS.**


**ALL LIABILITY, INCLUDING LIABILITY FOR INFRINGEMENT OF ANY INTELLECTUAL PROPERTY**
**RIGHTS OR FOR NONCOMPLIANCE WITH LAWS, RELATING TO USE OF THE SPECIFICATION IS**
**EXPRESSLY DISCLAIMED.  BY USE OF THE SPECIFICATION, EACH MEMBER EXPRESSLY WAIVES**
**ANY CLAIM AGAINST** _**BLUETOOTH**_ **SIG AND ITS PROMOTER MEMBERS RELATED TO USE OF THE**
**SPECIFICATION.**


_Bluetooth_ SIG reserve the right to adopt any changes or alterations to the Specification as it deems necessary
or appropriate.


**Copyright © 2012. Bluetooth® SIG, Inc. All copyrights in the Bluetooth Specifications themselves are**
**owned by Ericsson AB, Lenovo (Singapore) Pte. Ltd., Intel Corporation, Microsoft Corporation,**
**Motorola Mobility, Inc., Nokia Corporation, and Toshiba Corporation.**


***Other third-party brands and names are the property of their respective owners.**


_BLUETOOTH_ SPECIFICATION Page 5 of 42
_Video Distribution Profile_

### Document Terminology

The Bluetooth SIG has adopted Section 13.1 of the IEEE Standards Style Manual,
which dictates use of the words ``shall’’, ``should’’, ``may’’, and ``can’’ in the
development of documentation, as follows:

- The word _shall_ is used to indicate mandatory requirements strictly to be followed in

order to conform to the standard and from which no deviation is permitted ( _shall_
equals _is required to_ ).

- The use of the word _must_ is deprecated and shall not be used when stating

mandatory requirements; _must_ is used only to describe unavoidable situations.

- The use of the word _will_ is deprecated and shall not be used when stating mandatory

requirements; _will_ is only used in statements of fact.

- The word _should_ is used to indicate that among several possibilities one is

recommended as particularly suitable, without mentioning or excluding others; or
that a certain course of action is preferred but not necessarily required; or that (in the
negative form) a certain course of action is deprecated but not prohibited ( _should_
equals _is recommended that_ ).

- The word _may_ is used to indicate a course of action permissible within the limits of

the standard ( _may_ equals _is permitted_ ).

- The word _can_ is used for statements of possibility and capability, whether material,

physical, or causal ( _can_ equals _is able to_ ).


_BLUETOOTH_ SPECIFICATION Page 6 of 42
_Video Distribution Profile_

## Contents


**1** **Introduction .................................................................................................................................. 10**
1.1 Scope ....................................................................................................................................... 10
1.2 Profile Dependency ................................................................................................................. 10
1.3 Symbols and Conventions ....................................................................................................... 11
1.3.1 Requirement Status Symbols ........................................................................................... 11
1.3.2 Definition ........................................................................................................................... 11
1.3.3 Notation for Timers and Counters ..................................................................................... 12
1.4 Bluetooth VDP Profile Change History .................................................................................... 12
1.4.1 Changes from 1.0 to 1.1 ................................................................................................... 12
**2** **Profile Overview ........................................................................................................................... 13**
2.1 Profile Stacks ........................................................................................................................... 13
2.2 Configurations and Roles ........................................................................................................ 13
2.3 User Requirements and Scenarios ......................................................................................... 14
2.4 Profile Fundamentals ............................................................................................................... 15
2.5 Conformance ........................................................................................................................... 15
**3** **Application Layer ......................................................................................................................... 16**
3.1 Video Streaming Set Up .......................................................................................................... 16
3.2 Video Streaming ...................................................................................................................... 16
3.2.1 Send Video Stream ........................................................................................................... 17
3.2.2 Receive Video Stream ...................................................................................................... 17
**4** **Video and Multimedia Codec Interoperability Requirements .................................................. 19**
4.1 Overview .................................................................................................................................. 19
4.2 Support of Codecs ................................................................................................................... 19
4.2.1 Mandatory Codec .............................................................................................................. 20
4.2.2 Optional codecs ................................................................................................................ 20
4.2.3 Vendor Specific VDP Codecs ........................................................................................... 20
4.2.4 Codec Type Field Values .................................................................................................. 21
4.2.5 Media Type Field Values .................................................................................................. 21
4.3 H.263 baseline ......................................................................................................................... 21
4.3.1 Reference .......................................................................................................................... 21
4.3.2 Codec Specific Information Elements ............................................................................... 21
4.3.3 Media Packet Header Requirements ................................................................................ 22
4.3.4 Media Payload Format ...................................................................................................... 22
4.4 MPEG-4 Visual Simple Profile ................................................................................................. 22
4.4.1 Reference .......................................................................................................................... 22
4.4.2 Codec Specific Information Elements ............................................................................... 22
4.4.3 Media Packet Header Requirements ................................................................................ 23
4.4.4 Media Payload Format ...................................................................................................... 23
4.5 H.263 Profile 3 ......................................................................................................................... 23
4.5.1 Reference .......................................................................................................................... 23
4.5.2 Codec Specific Information Elements ............................................................................... 23
4.5.3 Media Packet Header Requirements ................................................................................ 24
4.5.4 Media Payload Format ...................................................................................................... 24
4.6 H.263 Profile 8 ......................................................................................................................... 24
4.6.1 Reference .......................................................................................................................... 24
4.6.2 Codec Specific Information Elements ............................................................................... 24
**1** **Introduction .................................................................................................................................. 10**
1.1 Scope ....................................................................................................................................... 10
1.2 Profile Dependency ................................................................................................................. 10
1.3 Symbols and Conventions ....................................................................................................... 11
1.3.1 Requirement Status Symbols ........................................................................................... 11
1.3.2 Definition ........................................................................................................................... 11
1.3.2.1 RFA ............................................................................................................................. 11


_BLUETOOTH_ SPECIFICATION Page 7 of 42
_Video Distribution Profile_


1.3.2.2 RFD ............................................................................................................................ 12
1.3.2.3 Forbidden.................................................................................................................... 12
1.3.3 Notation for Timers and Counters ..................................................................................... 12
1.4 Bluetooth VDP Profile Change History .................................................................................... 12
1.4.1 Changes from 1.0 to 1.1 ................................................................................................... 12
1.4.1.1 General Changes ....................................................................................................... 12
1.4.1.2 New Features ............................................................................................................. 12
**2** **Profile Overview ........................................................................................................................... 13**
2.1 Profile Stacks ........................................................................................................................... 13
2.2 Configurations and Roles ........................................................................................................ 13
2.3 User Requirements and Scenarios ......................................................................................... 14
2.4 Profile Fundamentals ............................................................................................................... 15
2.5 Conformance ........................................................................................................................... 15
**3** **Application Layer ......................................................................................................................... 16**
3.1 Video Streaming Set Up .......................................................................................................... 16
3.2 Video Streaming ...................................................................................................................... 16
3.2.1 Send Video Stream ........................................................................................................... 17
3.2.2 Receive Video Stream ...................................................................................................... 17
**4** **Video and Multimedia Codec Interoperability Requirements .................................................. 19**
4.1 Overview .................................................................................................................................. 19
4.2 Support of Codecs ................................................................................................................... 19
4.2.1 Mandatory Codec .............................................................................................................. 20
4.2.1.1 SRC Device Supporting Video Encoder ..................................................................... 20
4.2.1.2 SRC Device Using Pre-encoded Video Data ............................................................. 20
4.2.1.3 Mismatch Between SRC and SNK Video Data Format .............................................. 20
4.2.2 Optional codecs ................................................................................................................ 20
4.2.3 Vendor Specific VDP Codecs ........................................................................................... 20
4.2.4 Codec Type Field Values .................................................................................................. 21
4.2.5 Media Type Field Values .................................................................................................. 21
4.3 H.263 baseline ......................................................................................................................... 21
4.3.1 Reference .......................................................................................................................... 21
4.3.2 Codec Specific Information Elements ............................................................................... 21
4.3.2.1 Level ........................................................................................................................... 21
4.3.3 Media Packet Header Requirements ................................................................................ 22
4.3.4 Media Payload Format ...................................................................................................... 22
4.4 MPEG-4 Visual Simple Profile ................................................................................................. 22
4.4.1 Reference .......................................................................................................................... 22
4.4.2 Codec Specific Information Elements ............................................................................... 22
4.4.2.1 Level ........................................................................................................................... 22
4.4.3 Media Packet Header Requirements ................................................................................ 23
4.4.4 Media Payload Format ...................................................................................................... 23
4.5 H.263 Profile 3 ......................................................................................................................... 23
4.5.1 Reference .......................................................................................................................... 23
4.5.2 Codec Specific Information Elements ............................................................................... 23
4.5.2.1 Level ........................................................................................................................... 23
4.5.3 Media Packet Header Requirements ................................................................................ 24
4.5.4 Media Payload Format ...................................................................................................... 24
4.6 H.263 Profile 8 ......................................................................................................................... 24
4.6.1 Reference .......................................................................................................................... 24
4.6.2 Codec Specific Information Elements ............................................................................... 24
4.6.2.1 Level ........................................................................................................................... 24
4.6.3 Media Packet Header Requirements ................................................................................ 25
4.6.4 Media Payload Format ...................................................................................................... 25
4.7 Vendor Specific VDP Codec.................................................................................................... 25
4.7.1 Reference .......................................................................................................................... 25
4.7.2 Codec Specific Information Elements ............................................................................... 25


_BLUETOOTH_ SPECIFICATION Page 8 of 42
_Video Distribution Profile_


4.7.2.1 Vendor ID.................................................................................................................... 25
4.7.2.2 Vendor Specific Codec ID .......................................................................................... 25
4.7.2.3 Vendor Specific Value ................................................................................................ 25
4.7.3 Media Packet Header Requirements ................................................................................ 25
4.7.4 Media Payload Format ...................................................................................................... 26
**5** **GAVDP Interoperability Requirements ...................................................................................... 27**
5.1 AVDTP Interoperability Requirements .................................................................................... 27
5.1.1 Signaling procedures ........................................................................................................ 27
Streaming Roles ................................................................................................................................... 27
Delay Reporting Roles .......................................................................................................................... 27

5.1.2 Transport Services ............................................................................................................ 27
5.1.3 Error Codes ....................................................................................................................... 28
5.2 L2CAP Interoperability Requirements ..................................................................................... 29
5.2.1 Maximum Transmission Unit ............................................................................................. 29
5.3 SDP Interoperability Requirements ......................................................................................... 29
5.4 Link Manager Interoperability Requirements ........................................................................... 30
5.5 Link Controller Interoperability Requirements ......................................................................... 30
5.5.1 Class of Device ................................................................................................................. 30
**6** **Generic Access Profile Interoperability Requirements ............................................................ 31**
6.1 Modes ...................................................................................................................................... 31
6.2 Security Aspects ...................................................................................................................... 31
6.3 Idle Mode Procedures ............................................................................................................. 31
**7** **Timers and Counters ................................................................................................................... 32**
**8** **Testing........................................................................................................................................... 33**
**9** **References .................................................................................................................................... 34**
**10** **List of Figures .............................................................................................................................. 35**
**11** **List of Tables ................................................................................................................................ 36**
**12** **Appendix A (Informative): Video Streaming with Content Protection .................................... 37**
**13** **Appendix B (Informative): Video Streaming with High quality Audio .................................... 38**
13.1 Audio and Video Streaming Set Up ......................................................................................... 38
13.2 Audio and Video Streaming Procedure ................................................................................... 39
13.3 Media Synchronization ............................................................................................................ 40
**14** **Appendix C: Acronyms and Abbreviations ............................................................................... 42**

4.6.4 Media Payload Format ...................................................................................................... 25
4.7 Vendor Specific VDP Codec.................................................................................................... 25
4.7.1 Reference .......................................................................................................................... 25
4.7.2 Codec Specific Information Elements ............................................................................... 25
4.7.3 Media Packet Header Requirements ................................................................................ 25
4.7.4 Media Payload Format ...................................................................................................... 26
**5** **GAVDP Interoperability Requirements ...................................................................................... 27**
5.1 AVDTP Interoperability Requirements .................................................................................... 27
5.1.1 Signaling procedures ........................................................................................................ 27
Streaming Roles ................................................................................................................................... 27
Delay Reporting Roles .......................................................................................................................... 27

5.1.2 Transport Services ............................................................................................................ 27
5.1.3 Error Codes ....................................................................................................................... 28
5.2 L2CAP Interoperability Requirements ..................................................................................... 29
5.2.1 Maximum Transmission Unit ............................................................................................. 29
5.3 SDP Interoperability Requirements ......................................................................................... 29
5.4 Link Manager Interoperability Requirements ........................................................................... 30
5.5 Link Controller Interoperability Requirements ......................................................................... 30
5.5.1 Class of Device ................................................................................................................. 30
**6** **Generic Access Profile Interoperability Requirements ............................................................ 31**
6.1 Modes ...................................................................................................................................... 31
6.2 Security Aspects ...................................................................................................................... 31


_BLUETOOTH_ SPECIFICATION Page 9 of 42
_Video Distribution Profile_


6.3 Idle Mode Procedures ............................................................................................................. 31
**7** **Timers and Counters ................................................................................................................... 32**
**8** **Testing........................................................................................................................................... 33**
**9** **References .................................................................................................................................... 34**
**10** **List of Figures .............................................................................................................................. 35**
**11** **List of Tables ................................................................................................................................ 36**
**12** **Appendix A (Informative): Video Streaming with Content Protection .................................... 37**
**13** **Appendix B (Informative): Video Streaming with High quality Audio .................................... 38**
13.1 Audio and Video Streaming Set Up ......................................................................................... 38
13.2 Audio and Video Streaming Procedure ................................................................................... 39
13.3 Media Synchronization ............................................................................................................ 40
**14** **Appendix C: Acronyms and Abbreviations ............................................................................... 42**


_BLUETOOTH_ SPECIFICATION Page 10 of 42
_Video Distribution Profile_

## **1 Introduction**

### **1.1 Scope**

The Video Distribution Profile (VDP) defines the protocols and procedures that realize
distribution of video content, using ACL channels. A typical usage case is streaming of
video content from an observation camera to a monitor. The Video data is compressed
in a specific format for efficient use of the limited bandwidth.

VDP focuses on video streaming, while the Advanced Audio Distribution Profile (A2DP)

[2] specifies high quality audio streaming. Support of both profiles enables the
distribution of video content accompanied with high-quality audio. The usage of video
and audio streaming is described in Appendix B. VDP does not include remote control
functions, and uses same transport architecture as A2DP (i.e. AVDTP [5] over L2CAP

[1]). Devices may support remote control features on Bluetooth by implementing both
VDP and the control profile as depicted, for example, in the usage scenario of
Audio/Video Remote Control Profile [3].

_Note1_ : VDP supports vendor specific extension to facilitate transport of multimedia
content as a pre-multiplexed stream of audio and video. The multiplexing is performed
on application level.

### **1.2 Profile Dependency**

In Figure 1.1, the structure and the dependencies of the profiles are depicted. A profile
is dependent upon another profile if it re-uses parts of that profile, by implicitly or
explicitly referencing it. Dependency is illustrated in the figure. A profile has
dependencies on the profile(s) in which it is contained – directly and indirectly.

As indicated in the figure, the VDP is dependent upon the Generic Access Profile (GAP),
and also the Generic Audio/Video Distribution Profile (GAVDP) [4] that defines
procedures required to setup an audio/video streaming. The VDP defines parameters
and procedures that are specific for video streaming. The terminology, user interface
and procedures as defined in the GAP and GAVDP are applicable to this profile, unless
explicitly stated otherwise.


_BLUETOOTH_ SPECIFICATION Page 11 of 42
_Video Distribution Profile_



_Figure 1.1: Profile Dependencies_

### **1.3 Symbols and Conventions**


**1.3.1 Requirement Status Symbols**

In this document the following symbols are used:

‘M’ for mandatory to support (used for capabilities that shall be used in the profile).

‘O’ for optional to support (used for capabilities that may be used in the profile).

‘C’ for conditional support (used for capabilities that shall be used in case a certain other
capability is supported).

‘X’ for excluded (used for capabilities that may be supported by the unit, but which shall
never be used in the profile).

‘N/A’ for not applicable (in the given context it is impossible to use this capability).

Some excluded capabilities are capabilities that, according to the relevant Bluetooth
specification, are mandatory. These are features that may degrade operation of devices
following this profile. Therefore, these features shall never be activated while a unit is
operating as a unit within this profile.


**1.3.2 Definition**


**1.3.2.1** **RFA**

Reserved for Future Additions. Bits with this designation shall be set to zero. Receivers
shall ignore these bits.


_BLUETOOTH_ SPECIFICATION Page 12 of 42
_Video Distribution Profile_


**1.3.2.2** **RFD**

Reserved for Future Definition. These bit value combinations or bit values are not
allowed in the current specification but may be used in future versions. The receiver
shall check that unsupported bit value combination is not used.


**1.3.2.3** **Forbidden**

This bit value combination is not allowed in this specification. The receiver shall check
that this bit value combination is not used.


**1.3.3 Notation for Timers and Counters**

Bluetooth timers and counters may be introduced in this profile. To distinguish them
from timers and counters used in other parts of the specification, these timers and
counters are named according to the following convention:

- “TVDP _nnn_ ” for timers

- “NVDP _nnn_ ” for counters

### **1.4 Bluetooth VDP Profile Change History**


**1.4.1 Changes from 1.0 to 1.1**


**1.4.1.1** **General Changes**

- Non-VDP codecs from VDP 1.0 are now referred to as Vendor-Specific VDP codecs

- Incorporation of adopted changes to correct errata. Relevant erratum is 4071.


**1.4.1.2** **New Features**

- Interoperability with the Delay Reporting feature from Audio/Video Distribution
Transport Protocol 1.3 to enhance A/V synchronization

- Interoperability with Generic Access Profile modes, security and idle mode
procedures defined in Core Specification 2.1 + EDR

- Clarification on the criteria to use Optional VDP codecs in a compliant way and
promote Vendor-Specific VDP codecs to Optional VDP codecs


_BLUETOOTH_ SPECIFICATION Page 13 of 42
_Video Distribution Profile_

## **2 Profile Overview**

### **2.1 Profile Stacks**

Figure 2.1 shows the protocols and entities used in this profile.



|Application<br>Video Source or<br>Audio and Video Source|Col2|Col3|
|---|---|---|
|AVDTP<br>|AVDTP<br>|SDP|
|LMP|L2CAP|L2CAP|
|Baseband|Baseband|Baseband|


Video or
Audio and Video

Source Side



|Application<br>Video Sink or<br>Audio and Video Sink|Col2|Col3|
|---|---|---|
|AVDTP<br>|AVDTP<br>|SDP|
|LMP|L2CAP|L2CAP|
|Baseband|Baseband|Baseband|


Video or
Audio and Video

Sink Side



_Figure 2.1: Protocol Model_
The Baseband [1], LMP [1], L2CAP [1], SDP [1] are Bluetooth protocols defined in the
Bluetooth Core specifications. AVDTP [5] consists of a signaling entity for negotiation of
streaming parameters and a transport entity that can handle streaming itself.

The Application layer shown in Figure 2.1 is the entity in which the device can set
application service and transport service parameters. The entity also adapts the video
streaming data into/from the defined packet format.

For the shaded protocols/entities in Figure 2.1, the GAVDP applies, except in those
cases where this profile explicitly states deviations.

### **2.2 Configurations and Roles**

The following roles are defined for devices that implement this profile:

**Source (SRC) –** A device is the **SRC** when it acts as a source of a digital video stream
that is delivered to the **SNK** of the piconet.

**Sink (SNK) –** A device is the **SNK** when it acts as a sink of a digital video stream
delivered from the **SRC** on the same piconet.


_BLUETOOTH_ SPECIFICATION Page 14 of 42
_Video Distribution Profile_


Examples of configurations illustrating the roles for this profile are depicted in Figure 2.2.





_Figure 2.2: Example of Configuration_

### **2.3 User Requirements and Scenarios**

The following scenario is covered by this profile:

- Setup/control/manipulate a streaming of video or pre-multiplexed audio and video
data from the **SRC** to the **SNK** (s).

The following restrictions are applied to this profile:

1. The profile does not support a synchronized point-to-multipoint distribution.

2. There exists certain delay between the **SRC** and the **SNK** due to radio signal

processing, data buffering, and encode/decode of the stream data. Countering the
effects of such delays depends on implementation.

The following requirements are set in this profile:

1. The required media stream (or pre-multiplexed audio and video) data rate shall be

limited to allow packet retransmissions on the Bluetooth data link. Using packet
retransmission will reduce the effects of packet loss, and improve the user
experience.

2. The profile does not exclude any content protection method.


_BLUETOOTH_ SPECIFICATION Page 15 of 42
_Video Distribution Profile_

### **2.4 Profile Fundamentals**

The profile fundamentals are same as defined in the GAVDP in addition to the following
requirement.

- Content Protection is provided at the application level and is not a function of the
Bluetooth link level security protocol.

### **2.5 Conformance**

When conformance to this profile is claimed, all capabilities indicated mandatory for this
profile shall be supported in the specified manner (process mandatory). This also
applies for optional and conditional capabilities for which support is indicated. All
mandatory, optional, and conditional capabilities, for which support is indicated, are
subject to verification as part of the Bluetooth certification program.


_BLUETOOTH_ SPECIFICATION Page 16 of 42
_Video Distribution Profile_

## **3 Application Layer**


This section describes the feature requirements on units complying with the VDP.

Table 3.1 shows the feature requirements for this profile.



|Item<br>No.|Feature|Support in<br>SRC|Support in<br>SNK|
|---|---|---|---|
|1|Video Streaming|M|M|


_Table 3.1: Application Layer Features_
Table 3.2 maps each feature to the procedures used for that feature, and shows
whether the procedure is optional, mandatory, or conditional. The procedures are
described in the reference section.

|Item<br>No.|Feature|Procedure|Ref.|Support<br>in SRC|Support<br>in SNK|
|---|---|---|---|---|---|
|1|Video Streaming|Send Video Stream|3.2.1|M|N/A|
|||Receive Video Stream|3.2.2|N/A|M|



_Table 3.2: Application Layer Features to Procedure Mapping_










### **3.1 Video Streaming Set Up**

When a device wishes to start streaming of video or pre-multiplexed audio and video
content, the device firstly needs to set up a streaming connection. Signaling procedures
and typical signaling flows are illustrated in Section 4.1 and Appendix A of GAVDP [4],
respectively. During such set-up procedure, the devices select the most suitable video
or pre-multiplexed audio and video streaming parameters. There are two kinds of
services configured; one is an application service capability, and the other is a transport
service capability. (For details, see Section 6.6 in AVDTP [5].) This profile specifies
video and pre-multiplexed audio and video specific parameters necessary for these
signaling procedures.

The application service capability for VDP consists of video codec capability, multimedia
codec capability and content protection capability. Details of these parameters such as
mode, frame rate, and bit rate are described in Section 4. The content protection
capability is described in Appendix A as informative.

The transport service capability is to select the services provided by AVDTP in order to
manipulate the streaming packets more intelligently. Such treatment will help effective
use of bandwidth. Available modes, parameters and their requirements are explained in
Section 5.1.

### **3.2 Video Streaming**

Once streaming connection is established and _Start Streaming_ procedure in GAVDP is
executed, both SRC and SNK are in the STREAMING state, in which the SRC (SNK) is
ready to send (receive) video stream. (See Section 4.1 in GAVDP.) The SRC uses the
_Send Video Stream_ procedure to send video data to the SNK, which in turn employs the
_Receive Video Stream_ procedure to receive the video data. The block diagram of these
procedures and created packet format are shown in


_BLUETOOTH_ SPECIFICATION Page 17 of 42
_Video Distribution Profile_


Figure 3.1. In section 4, video-specific parameters in AVDTP header and media payload
format are also specified.

Note again that the devices shall be in the STREAMING state to send/receive video
stream. If the **SRC** / **SNK** wishes to send/receive the video stream whereas the state is
still at OPEN, the **SRC** / **SNK** shall initiate _Start Streaming_ procedure defined in GAVDP.


**3.2.1 Send Video Stream**

In the _Send Video Stream_ procedure, the **SRC** may encode the data into a selected
format in the signaling session, if needed. Then, the application layer of the **SRC** shall
adapt the encoded data into the defined media payload format. The frame of encoded
video or pre-multiplexed audio and video data is adapted to the defined payload format
as defined in section 4.

When content protection is in use, a content protection header may precede encrypted
video content. This is content protection method dependent.

Afterwards, the stream data shall be handed down to the AVDTP entity through the
exposed interface (Interface 4) defined in Section 2 of AVDTP. The stream data shall be
sent out on the transport channel using the selected transport services defined in
AVDTP, Section 5.5.


**3.2.2 Receive Video Stream**

The AVDTP entity of the **SNK** shall receive the stream data from the transport channel
using the selected transport services and pass it to the application layer by exposed
interface defined in Section 2 of AVDTP.

When a content protection method is active, the application layer of the **SNK** shall
process the retrieved AVDTP payload as described by the content protection method.
Typically, this processing entails content protection header analysis and decryption of
associated encrypted content.

Finally the frame of video or pre-multiplexed audio and video data will be decoded
according to the selected coding format.


_BLUETOOTH_ SPECIFICATION Page 18 of 42
_Video Distribution Profile_









_Figure 3.1: Block Diagram of Video Streaming Procedures and the Packet Format_


_BLUETOOTH_ SPECIFICATION Page 19 of 42
_Video Distribution Profile_

## **4 Video and Multimedia Codec Interoperability** **Requirements**

### **4.1 Overview**

This chapter defines necessary information specific for video and multimedia codec. In
section 4.2 definition of codecs used in this profile and their requirements are fully
described. Additional information about codecs introduced after the publication of this
profile is described in Bluetooth Assigned Numbers [6].

Remaining sections provide reference for each codec as well as the following
information:

- _Video codec capabilities_ define the capability field for video codec and its
parameters necessary for signaling procedures in the streaming set up. Related
procedures in GAVDP are _Connection Establishment_ and _Change Parameters_
procedures.

- _Media packet header requirements_ define video codec specific parameters in the
media packet header, which shall be added to the media payload in the AVDTP
entity (see Figure 3.1)

- _Media payload format_ defines the video codec specific payload format in the AVDTP
packet, which shall be used in the _Video Streaming_ procedures in Section 3.2 (see
also Figure 3.1).

- _Multimedia codec capabilities_ define the capability field for multimedia codec and its
parameters necessary for signaling procedures in the streaming set up. Related
procedures in GAVDP are _Connection Establishment_ and _Change Parameters_
procedures.

- _Note:_ In VDP no multimedia codec capabilities are specified. The multimedia codec
is treated as Vendor Specific VDP codec (see section 4.2.3).

### **4.2 Support of Codecs**

Table 4.1 shows supported _Mandatory_ and _Optional_ codecs in this profile.

|Codec Type|Support|Media Type|Ref.|
|---|---|---|---|
|H.263 baseline|C1|Video|4.3|
|MPEG-4 Visual Simple Profile|O|Video|4.4|
|H.263 profile 3|O|Video|4.5|
|H.263 profile 8|O|Video|4.6|



_Table 4.1: Supported codecs_


C1: Optional if used like in the exception presented in 4.2.1.3 otherwise Mandatory

The following codecs are treated as _Vendor Specific VDP_ codecs:

- The codecs that are not on Table 4.1 or in Bluetooth Assigned Numbers [6].

- The Mandatory or Optional codecs on Table 4.1 used in non-conforming way.
Requirements for the use of _Vendor Specific_ VDP codecs are defined in sections 4.2.3
and 4.7.


_BLUETOOTH_ SPECIFICATION Page 20 of 42
_Video Distribution Profile_


**4.2.1 Mandatory Codec**

The VDP mandates H.263 Baseline Profile (Profile 0) codec (H.263 baseline) to ensure
the interoperability.

The device shall implement a H.263 baseline decoder when the device is the **SNK** and
it uses a video decoder for rendering the received video stream.


**4.2.1.1** **SRC Device Supporting Video Encoder**

The device shall implement a H.263 baseline encoder when the device is the **SRC** and
it uses a video encoder for creating the video streaming.


**4.2.1.2** **SRC Device Using Pre-encoded Video Data**

Pre-encoded video data is video data that is not encoded by the **SRC** device but is
received from an external digital interface and possibly stored in the device. The preencoded video data can be in any of mandatory, optional or Vendor Specific VDP
format.

If the **SRC** device supports a capability to send pre-encoded video data and also
implements a H.263 baseline encoder for creating the video streaming, the **SRC** device
shall support the capability to send pre-encoded H.263 baseline video data format.


**4.2.1.3** **Mismatch Between SRC and SNK Video Data Format**

If the **SRC** device supports a capability to send pre-encoded video data but the **SNK**
device does not support that pre-encoded video data format then the **SRC** device is not
required to transcode the pre-encoded data into the mandatory codec format.


**4.2.2 Optional codecs**

The device may also support _Optional_ codecs to maximize its usability. When both **SRC**
and **SNK** support the same _Optional_ codec, this codec may be used instead of
Mandatory codec. _Optional_ codecs supported by this profile are listed in _Table 4.1_ and
additionally defined in _Bluetooth_ Assigned Numbers [6].

For all optional codecs listed in Bluetooth Assigned Numbers [6] but not described in
this specification, Bluetooth Assigned Numbers [6] shall contain information on how to
obtain information about Codec Specific Information Element, Media Packet Header
Requirement, and all other codec specific information.


**4.2.3 Vendor Specific VDP Codecs**

The device may support other codecs as _Vendor Specific VDP_ codecs. A user of a
Vendor Specific _VDP_ codec (hereafter the Vendor) will need to define any parameters
and other information necessary for use of the codec in VDP. The profile does not
specify anything for _Vendor Specific VDP_ codecs. The _Vendor Specific VDP_ codec may
be upgraded to _Optional_ when the following requirements are met:

- The proposed codec shall be successfully tested in a formal interoperability (IOP)
testing session:


_BLUETOOTH_ SPECIFICATION Page 21 of 42
_Video Distribution Profile_


 Successfully testing a codec means that at least two source and two sink

implementations shall provide evidence to the BARB that the proposed codec
has been successfully implemented.

 The formal IOP test plan shall be submitted to and approved by BARB prior to

the formal IOP testing session.

- Any license applicable to the proposed codec shall be available under fair and
reasonable terms and accessible in a non-discriminatory way.

- The specification of the proposed codec shall be available to all companies that plan
to implement the codec, under NDA if needed.
If a Vendor Specific VDP codec is upgraded to _Optional_, it will only be listed in the
_Bluetooth_ Assigned Numbers [6] and not in this or future profile versions.


**4.2.4 Codec Type Field Values**

Refer to Bluetooth Assigned Numbers [6] for video codec types and multimedia codec
types available in this profile. Message format of video codec capabilities and
multimedia codec capabilities are defined in Section 8.19.2 of AVDTP.


**4.2.5 Media Type Field Values**

Refer to Bluetooth Assigned Numbers [6] for Media Type of video and multimedia
codecs.

### **4.3 H.263 baseline**


**4.3.1 Reference**

For H.263 baseline, refer to [11], [12].


**4.3.2 Codec Specific Information Elements**

Figure 4.1 shows Codec Specific Information Elements for H.263 baseline used in the
signaling procedures. The following section defines the field values and their
requirements. If the packet includes improper settings, the error code shall be returned
as specified in Section 5.1.3.


**7** **6** **5** **4** **3** **2** **1** **0**
Level Octet0
_Figure 4.1: Codec Specific Information Elements for H.263 baseline_
_Note_ : In the Get All Capabilities Response of AVDTP, one or more bits may be
defined/set in each field. On the other hand, in the Set Configuration Command and the
Reconfigure Command of AVDTP, only one bit shall be defined/set in each field.


**4.3.2.1** **Level**

Table 4.2 shows the value of _Level_ field for H.263 baseline. The **SRC** and **SNK** shall
support H.263 baseline Level 10, Levels 20 and 30 are optional.


_BLUETOOTH_ SPECIFICATION Page 22 of 42
_Video Distribution Profile_

|Position|Level|Support<br>in SRC|Support<br>in SNK|
|---|---|---|---|
|Octet0; b7|10|M|M|
|Octet0; b6|20|O|O|
|Octet0; b5|30|O|O|
|Octet0; b4|RFA|–|–|
|Octet0; b3|RFA|–|–|
|Octet0; b2|RFA|–|–|
|Octet0; b1|RFA|–|–|
|Octet0; b0|RFA|–|–|



_Table 4.2: Level for H.263 baseline_


**4.3.3 Media Packet Header Requirements**

The media packet header requirements for H.263 baseline are contained in the
specification of media payload format referenced in Section 4.3.4.


**4.3.4 Media Payload Format**

H.263 baseline uses payload format defined in [13].

### **4.4 MPEG-4 Visual Simple Profile**


**4.4.1 Reference**

For MPEG-4 Visual Simple Profile, refer to [9].


**4.4.2 Codec Specific Information Elements**

Figure 4-2 shows _Codec Specific Information Elements_ for MPEG-4 used in the
signaling procedures. The following section defines the field values and their
requirements. If the packet includes improper settings, the error code shall be returned
as specified in Section 5.1.3.


**7** **6** **5** **4** **3** **2** **1** **0**
Level Octet0
_Figure 4-2: Codec Specific Information Elements for MPEG-4_
_Note_ : In the Get All Capabilities Response of AVDTP, one or more bits may be
defined/set in each field. On the other hand, in the Set Configuration Command and the
Reconfigure Command of AVDTP, only one bit shall be defined/set in each field.


**4.4.2.1** **Level**

Table 4.3 shows the value of Level field specified in Annex G of MPEG-4 specification

[9]. The **SRC** and **SNK** shall support the Level 0, and Level 1, 2 and 3 are optional.


|Position|Level|Support<br>in SRC|Support<br>in SNK|
|---|---|---|---|
|Octet0; b7|0|M|M|
|Octet0; b6|1|O|O|
|Octet0; b5|2|O|O|
|Octet0; b4|3|O|O|


_BLUETOOTH_ SPECIFICATION Page 23 of 42
_Video Distribution Profile_

|Position|Level|Support<br>in SRC|Support<br>in SNK|
|---|---|---|---|
|Octet0; b3|RFA|–|–|
|Octet0; b2|RFA|–|–|
|Octet0; b1|RFA|–|–|
|Octet0; b0|RFA|–|–|



_Table 4.3: Level of MPEG-4 Visual Simple Profile_


**4.4.3 Media Packet Header Requirements**

The media packet header requirements for MPEG-4 are contained in the specification of
media payload format referenced in Section 4.4.4.


**4.4.4 Media Payload Format**

MPEG-4 uses payload formats defined in [10].

### **4.5 H.263 Profile 3**


**4.5.1 Reference**

For H.263 profile 3 (" Version 2 Interactive and Streaming Wireless Profile (Profile 3)"),
refer to [11][12].


**4.5.2 Codec Specific Information Elements**

Figure 4.3 shows Codec Specific Information Elements for H.263 profile 3 used in the
signaling procedures. The following section defines the field values and their
requirements. If the packet includes improper settings, the error code shall be returned
as specified in section 5.1.3.


**7** **6** **5** **4** **3** **2** **1** **0**
Level Octet0
_Figure 4.3: Codec Specific Information Elements for H.263 profile 3_
_Note_ : In the Get All Capabilities Response of AVDTP, one or more bits may be
defined/set in each field. On the other hand, in the Set Configuration Command and the
Reconfigure Command of AVDTP, only one bit shall be defined/set in each field.


**4.5.2.1** **Level**

Table 4.4 shows the value of _Level_ field for H.263 profile 3. The **SRC** and **SNK** shall
support H.263 baseline Level 10, Levels 20 and 30 are optional.


|Position|Level|Support<br>in SRC|Support<br>in SNK|
|---|---|---|---|
|Octet0; b7|10|M|M|
|Octet0; b6|20|O|O|
|Octet0; b5|30|O|O|
|Octet0; b4|RFA|–|–|
|Octet0; b3|RFA|–|–|
|Octet0; b2|RFA|–|–|


_BLUETOOTH_ SPECIFICATION Page 24 of 42
_Video Distribution Profile_

|Position|Level|Support<br>in SRC|Support<br>in SNK|
|---|---|---|---|
|Octet0; b1|RFA|–|–|
|Octet0; b0|RFA|–|–|



_Table 4.4: Level for H.263 profile 3_


**4.5.3 Media Packet Header Requirements**

The media packet header requirements for H.263 profile 3 are contained in the
specification of media payload format referenced in Section 4.3.3.


**4.5.4 Media Payload Format**

H.263 profile 3 uses payload format defined in [13].

### **4.6 H.263 Profile 8**


**4.6.1 Reference**

For H.263 profile 8 ("high latency profile"), refer to [11][12].


**4.6.2 Codec Specific Information Elements**

Figure 4.4 shows Codec Specific Information Elements for H.263 profile 8 used in the
signaling procedures. The following section defines the field values and their
requirements. If the packet includes improper settings, the error code shall be returned
as specified in section 5.1.3.


**7** **6** **5** **4** **3** **2** **1** **0**
Level Octet0
_Figure 4.4: Codec Specific Information Elements for H.263 profile 8_
_Note_ : In the Get All Capabilities Response of AVDTP, one or more bits may be
defined/set in each field. On the other hand, in the Set Configuration Command and the
Reconfigure Command of AVDTP, only one bit shall be defined/set in each field.


**4.6.2.1** **Level**

Table 4.5 shows the value of _Level_ field for H.263 profile 8. The **SRC** and **SNK** shall
support H.263 baseline Level 10, Levels 20 and 30 are optional.

|Position|Level|Support in SRC|Support in SNK|
|---|---|---|---|
|Octet0; b7|10|M|M|
|Octet0; b6|20|O|O|
|Octet0; b5|30|O|O|
|Octet0; b4|RFA|–|–|
|Octet0; b3|RFA|–|–|
|Octet0; b2|RFA|–|–|
|Octet0; b1|RFA|–|–|
|Octet0; b0|RFA|–|–|



_Table 4.5: Level for H.263 profile 8_


_BLUETOOTH_ SPECIFICATION Page 25 of 42
_Video Distribution Profile_


**4.6.3 Media Packet Header Requirements**

The media packet header requirements for H.263 profile 8 are contained in the
specification of media payload format referenced in Section 4.3.3.


**4.6.4 Media Payload Format**

H.263 profile 8 uses payload format defined in [13].

### **4.7 Vendor Specific VDP Codec**


**4.7.1 Reference**

Definition and treatment of _Vendor Specific VDP_ codec is defined in Section 4.2.3.


**4.7.2 Codec Specific Information Elements**

Figure 4.5 shows _Codec Specific Information Elements_ for _Vendor Specific VDP_ codec
used in the signaling procedures. If the packet includes improper settings, the error
code shall be returned as specified in Section 5.1.3.


**7** **6** **5** **4** **3** **2** **1** **0**





Octet0
Octet1
Octet2
Octet3



Octet4
Octet5

Octet6


Octet _n_
_Figure 4.5: Codec Specific Information Elements for Vendor Specific VDP Codec_


**4.7.2.1** **Vendor ID**

The lower 16 bits of the 32-bit Vendor ID defined shall contain a valid, non-reserved 16bit Company ID as in Bluetooth Assigned Numbers [6]. The LSB of the Vendor ID shall
be placed in octet 0. The upper 16 bits of the 32-bit Vendor ID shall be set to zero.


**4.7.2.2** **Vendor Specific Codec ID**

The _Vendor Specific Codec ID_ field in Figure 4.5 contains 16-bit codec ID defined by the
Vendor.


**4.7.2.3** **Vendor Specific Value**

The _Vendor Specific Value_ field in Figure 4.5 contains values specifically defined by the
Vendor. Details are out of scope of this profile.


**4.7.3 Media Packet Header Requirements**

Media Packet Header requirements shall be defined by the Vendor.


_BLUETOOTH_ SPECIFICATION Page 26 of 42
_Video Distribution Profile_


**4.7.4 Media Payload Format**

Media Payload Format shall be defined by the Vendor.


_BLUETOOTH_ SPECIFICATION Page 27 of 42
_Video Distribution Profile_

## **5 GAVDP Interoperability Requirements**


This profile requires compliance to the Generic A/V Distribution Profile (GAVDP). The
following text together with the associated sub-clauses defines the requirements with
regards to this profile, in addition to the requirements defined in GAVDP.

### **5.1 AVDTP Interoperability Requirements**


**5.1.1 Signaling procedures**

There are different requirements for the streaming and for the delay reporting
procedure. While streaming might be initiated from SRC or SNK, the delay report is
always sent from SNK to SRC.


**Streaming Roles**

In the Video Distribution Profile, it is mandatory for the **SRC** and optional for the **SNK** to
be able to establish a streaming connection, start streaming and release the streaming
connection. The **SRC** can assume the role of both **INT** and **ACP**, while the **SNK** device
can assume the role of **ACP** and optionally the role of **INT** . Therefore, it is mandatory for
**SRC** to support **ACP** role, so that signaling procedures can be manipulated between
any combination of a **SRC** device and a **SNK** device.

|Col1|Role in GAVDP|Support in SRC|Support in SNK|
|---|---|---|---|
|1|**INT**|M|O|
|2|**ACP**|M|M|



_Table 5.1: Roles in GAVDP_


**Delay Reporting Roles**

Delay reports are sent from SNK to SRC, thus the SNK is always the INT and the SRC
is always the ACP. The INT role in SNK devices is mandatory for delay reporting while.
the ACP role in SRC devices is optional.

|Col1|Role in GAVDP|Support in SRC|Support in SNK|
|---|---|---|---|
|1|**INT**|X|M|
|2|**ACP**|O|X|



_Table 5.2: Roles in GAVDP for Delay Reporting_


**5.1.2 Transport Services**

Table 5.3 shows support of AVDTP transport capabilities for this profile. In this profile
Basic service is mandatory to support.







|Item<br>no.|Capability|Ref.|Support|
|---|---|---|---|
|1|Basic service|7.2 in[5]|M|
|2|Reporting service|7.3 in[5]|O|
|3|Recovery service|7.4 in[5]|O|
|4|Multiplexing service|7.5 in[5]|O|
|5|Header compression service|7.6 in[5]|O|


_Table 5.3: AVDTP transport capabilities_


_BLUETOOTH_ SPECIFICATION Page 28 of 42
_Video Distribution Profile_


**5.1.3 Error Codes**

If the _Codec Specific Information Elements_ include improper settings, the error code
shall be returned as follows. Apart from the error codes specified in GAVDP [4], Table
5.4 below lists additional error codes that shall be used by the application if applicable
errors are found in the commands received.












































|Error<br>ID|Related<br>Signaling<br>command|Related CODEC|Error Abbreviation|Error Description|
|---|---|---|---|---|
|0xC1|Set<br>Configuration<br>Reconfigure|ALL|INVALID_CODEC_TYP<br>E|Media Codec Type is<br>not valid|
|0xC2|Set<br>Configuration<br>Reconfigure|ALL|NOT_SUPPORTED_CO<br>DEC_TYPE|Media Codec Type is<br>not supported|
|0xC3|Set<br>Configuration<br>Reconfigure|H.263 baseline<br>MPEG-4 Visual<br>Simple Profile<br>H.263 Profile 3<br>H.263 Profile 8|INVALID_LEVEL|Level is not valid or<br>multiple values have<br>been selected|
|0xC4|Set<br>Configuration<br>Reconfigure|H.263 baseline<br>MPEG-4 Visual<br>Simple Profile<br>H.263 Profile 3<br>H.263 Profile 8|NOT_SUPPORTED_LE<br>VEL|Level is not<br>supported|
|0xC5-<br>0xDF||||RFD|
|0xE0|Set<br>Configuration<br>Reconfigure|ALL<br>|INVALID_CP_TYPE|The requested CP<br>Type is not<br>supported.|
|0xE1|Set<br>Configuration<br>Reconfigure<br>Security Control|ALL<br>|INVALID_CP_FORMAT|The format of Content<br>Protection Service<br>Capability/Content<br>Protection Scheme<br>Dependent Data is<br>not correct.|
|0xE2|Set<br>Configuration<br>Reconfigure|ALL<br>|INVALID_CODEC_PAR<br>AMETER<br>|The codec parameter<br>is invalid. Used if a<br>more specific error<br>code does not exist<br>for the codec in use.|
|0xE3|Set<br>Configuration<br>Reconfigure|ALL<br>|NOT_SUPPORTED_CO<br>DEC_PARAMETER|The codec parameter<br>is not supported.<br>Used if a more<br>specific error code<br>does not exist for the<br>codec in use.|
|0xE4-<br>0xFF||||RFD|



_Table 5.4: Error Codes_


_BLUETOOTH_ SPECIFICATION Page 29 of 42
_Video Distribution Profile_

### **5.2 L2CAP Interoperability Requirements**

For the L2CAP layer, no additions to the requirements as stated in the GAVDP shall
apply except for the following requirements.


**5.2.1 Maximum Transmission Unit**

The minimum MTU that a L2CAP implementation for this profile shall support is 335
bytes. ( _Note_ : DH5 packet size equals 339byte including 4-byte L2CAP header.)

### **5.3 SDP Interoperability Requirements**

This profile defines the following service records for the source and the sink respectively.

The codes assigned to the mnemonics used in the Value column as well as the codes
assigned to the attribute identifiers (if not specifically mentioned in the AttrID column)
can be found in Bluetooth Assigned Numbers [6].













|Item|Definition|Type|Value|AttrID|Status|Default|
|---|---|---|---|---|---|---|
|Service Class ID List||||See[6]|M||
|Service Class #0||UUID|Video Source||M||
|Protocol Descriptor List||||See[6]|M||
|Protocol #0||UUID|L2CAP||M||
|Parameter #0 for<br>Protocol #0|PSM|Uint 16|PSM= AVDTP||M||
|Protocol #1||UUID|AVDTP||M||
|Parameter #0 for<br>Protocol #1|Version|Uint 16|0x0103*||M||
|Bluetooth Profile<br>Descriptor List||||See[6]|M||
|Profile #0||UUID|Video<br>Distribution<br>||M||
|Parameter #0 for<br>Profile #0|Version|Uint 16|0x0101*~~1~~||M||
|Provider Name|Displayable<br>Text Name|String|Provider Name|See[6]|O||
|Service Name|Displayable<br>Text Name|String|Service-provider<br>defined|See[6]|O||


_Figure 5.1: Service Record for Source_

- Indicating AVDTP Version 1.3
*1 Indicating VDP Version 1.1










|Item|Definition|Type|Value|AttrID|Status|Default|
|---|---|---|---|---|---|---|
|Service Class ID List||||See[6]|M||
|Service Class #0||UUID|Video Sink||M||
|Protocol Descriptor List||||See[6]|M||
|Protocol #0||UUID|L2CAP||M||
|Parameter #0 for<br>Protocol #0|PSM|Uint 16|PSM= AVDTP||M||
|Protocol #1||UUID|AVDTP||M||
|Parameter #0 for<br>Protocol #1|Version|Uint 16|0x0103*||M||


_BLUETOOTH_ SPECIFICATION Page 30 of 42
_Video Distribution Profile_













|Item|Definition|Type|Value|AttrID|Status|Default|
|---|---|---|---|---|---|---|
|Bluetooth Profile<br>Descriptor List||||See[6]|M||
|Profile #0||UUID|Video<br>Distribution<br>||M||
|Parameter #0 for<br>Profile #0|Version|Uint 16|0x0101*~~1~~||M||
|Provider Name|Displayable<br>Text Name|String|Provider Name|See[6]|O||
|Service Name|Displayable<br>Text Name|String|Service-provider<br>defined|See[6]|O||


_Figure 5.2: Service Record for Sink_

- Indicating AVDTP Version 1.3
*1 Indicating VDP Version 1.1.








### **5.4 Link Manager Interoperability Requirements**

For the LMP layer, no additions to the requirements as stated in the GAVDP shall apply.

### **5.5 Link Controller Interoperability Requirements**

For the LC layer, the requirements as stated in the GAVDP shall apply. Furthermore the
following packets shall be supported in both **SNK** and **SRC** :
DH3, DM3, DH5 and DM5.

_Note_ : Requirements described in GAVDP are described for **INT** / **ACP** . For **SRC**, it is
mandatory to support both **INT** and **ACP** . For **SNK**, it is mandatory to support **ACP** and
it is optional to support **INT** .


**5.5.1 Class of Device**

For the Class of Device field the following applies:

1. Mandatory to set the ‘Rendering’ bit for the **SNK** and the ‘Capturing’ bit for the **SRC**

in the Service Class field.

2. Recommended to set ‘Audio/Video’ as Major Device class both for the **SNK** and the

**SRC** .

3. Select the appropriate Minor Device class as defined in the Bluetooth Assigned

Numbers [6].


_BLUETOOTH_ SPECIFICATION Page 31 of 42
_Video Distribution Profile_

## **6 Generic Access Profile Interoperability Requirements**


The Video Distribution profile requires compliance to the Generic Access Profile. This
section defines the support requirements for the capabilities as defined in the Generic
Access Profile.

### **6.1 Modes**

Table 6.1 shows the support status for Modes within this profile.

|Col1|Procedure|Support in SRC|Support in SNK|
|---|---|---|---|
|1.|Discoverability modes|||
||Non-Discoverable mode|C1|C1|
||Limited discoverable mode|C2|C2|
||General discoverable mode|C2|C2|
|2.|Connectability modes|||
||Non-Connectable mode|X|X|
||Connectable mode|M|M|
|3.|Bondable modes|||
||Non-bondable mode|O|O|
||Bondable mode|M|M|



_Table 6.1: Modes_


C1. If limited discoverable mode is supported, non-discoverable mode is mandatory, otherwise optional.
C2. Either limited discoverable mode or general discoverable mode shall be supported.

### **6.2 Security Aspects**

There is no change to the requirements as stated in the Generic Access Profile.

### **6.3 Idle Mode Procedures**

Table 6.2 shows the support status for Idle mode procedures within this profile.

|Col1|Procedure|Support in SRC|Support in SNK|
|---|---|---|---|
|1.|Initiation of general inquiry|M|O|
|2.|Initiation of limited inquiry|O|O|
|3.|Initiation of name discovery|O|O|
|4.|Initiation of device discovery|O|O|
|5.|Initiation of bonding|O|O|



_Table 6.2_ : Supported Idle Mode Procedures


_BLUETOOTH_ SPECIFICATION Page 32 of 42
_Video Distribution Profile_

## **7 Timers and Counters**


There are no specific timers and counters defined in the VDP Specification.


_BLUETOOTH_ SPECIFICATION Page 33 of 42
_Video Distribution Profile_

## **8 Testing**


The Video Distribution profile requires interoperability test. The details of the test
strategy are described in [7]. Tested functionality is defined in [8].


_BLUETOOTH_ SPECIFICATION Page 34 of 42
_Video Distribution Profile_

## **9 References**


[1] Bluetooth SIG, Specification of the Bluetooth System, Core, Version 1.2 or later

[2] Bluetooth SIG, Specification of the Bluetooth System, Profiles, version 1.0 or later, Advanced Audio

Distribution Profile

[3] Bluetooth SIG, Specification of the Bluetooth System, Profiles, version 1.0 or later, Audio/Video

Remote Control Profile

[4] Bluetooth SIG, Specification of the Bluetooth System, Profiles, version 1.0 or later, Generic

Audio/Video Distribution Profile

[5] Bluetooth SIG, Specification of the Bluetooth System, Core, version 1.0 or later, Audio/Video

Distribution Transport Protocol

[[6] Bluetooth SIG, Bluetooth Assigned Numbers, https://www.bluetooth.org/](https://www.bluetooth.org/)

[7] Bluetooth SIG, Specification of the Bluetooth System, TSS, version 1.0, Test Suite Structure (TSS)

and Test Procedures (TP) for Video Distribution Profile

[8] Bluetooth SIG, Specification of the Bluetooth System, ICS, version 1.0, Profile ICS proforma for

Video Distribution Profile

[9] ISO/IEC JTC 1/SC 29/WG 11, 14496-2: 1999 / Amendment 1: 2000

[10] IETF RFC 3016: " RTP Payload Format for MPEG-4 Audio/Visual Streams", [http://www.ietf.org/](http://www.ietf.org/)

[11] ITU-T Recommendation H.263: Video coding for low bit rate communication. 02/1998.

[12] ITU-T Recommendation H.263, Annex X: Profiles and Levels Definition. 04/2001.

[13] IETF RFC 2429: " RTP Payload Format for the 1998 Version of ITU-T Rec. H.263 Video (H.263+) ",

[http://www.ietf.org/](http://www.ietf.org/)

[14] IETF RFC 1305: “Network Time Protocol (version 3) Specification, Implementation and Analysis",

[http://www.ietf.org/](http://www.ietf.org/)

[15] IETF RFC 3550/ RFC 1889 (obsoleted): “RTP: A Transport Protocol for Real-Time Applications”,

[http://www.ietf.org/](http://www.ietf.org/)


_BLUETOOTH_ SPECIFICATION Page 35 of 42
_Video Distribution Profile_

## **10 List of Figures**


Figure 1.1: Profile Dependencies ................................................................................................................ 11
Figure 2.1: Protocol Model .......................................................................................................................... 13
Figure 2.2: Example of Configuration ......................................................................................................... 14
Figure 3.1: Block Diagram of Video Streaming Procedures and the Packet Format.................................. 18
Figure 4-1: Codec Specific Information Elements for H.263 baseline ........................................................ 21
Figure 4-2: Codec Specific Information Elements for MPEG-4 .................................................................. 22
Figure 4.3: Codec Specific Information Elements for H.263 profile 3 ......................................................... 23
Figure 4.4: Codec Specific Information Elements for H.263 profile 8 ......................................................... 24
Figure 4.5: Codec Specific Information Elements for Vendor Specific VDP Codec ................................... 25
Figure 5.1: Service Record for Source ........................................................................................................ 29
Figure 5.2: Service Record for Sink ............................................................................................................ 30
Figure 13-1: Example of High Quality Audio and Video Streaming ............................................................ 38
Figure 13-2: Audio and Video Streaming Set Up ........................................................................................ 39
Figure 13-3: Audio and Video Streaming Procedure .................................................................................. 40


_BLUETOOTH_ SPECIFICATION Page 36 of 42
_Video Distribution Profile_

## **11 List of Tables**


Table 3.1: Application Layer Features ........................................................................................................ 16
Table 3.2: Application Layer Features to Procedure Mapping .................................................................... 16
_Table 4.1: Supported codecs_ ...................................................................................................................... 19
Table 4.2: Level for H.263 baseline ............................................................................................................ 22
Table 4.3: Level of MPEG-4 Visual Simple Profile ..................................................................................... 23
Table 4.4: Level for H.263 profile 3 ............................................................................................................. 24
Table 4.5: Level for H.263 profile 8 ............................................................................................................. 24
Table 5.1: Roles in GAVDP......................................................................................................................... 27
Table 5.2: Roles in GAVDP for Delay Reporting ........................................................................................ 27
Table 5.3: AVDTP transport capabilities ..................................................................................................... 27
Table 5.4: Error Codes ................................................................................................................................ 28
Table 6.1: Modes ........................................................................................................................................ 31
Table 6.2: Supported Idle Mode Procedures .............................................................................................. 31


_BLUETOOTH_ SPECIFICATION Page 37 of 42
_Video Distribution Profile_

## **12 Appendix A (Informative): Video Streaming with Content** **Protection**


This profile does not specify a particular content protection method rather it only
provides support for various content protection methods. Specifically, AVDTP provides
for the identification and negotiation of a particular content protection method via the
_Get All Capabilities_ and _Stream Configuration_ procedures.

The _Security Control_ procedure in AVDTP provides for the exchange of the activated
content protection method.


_BLUETOOTH_ SPECIFICATION Page 38 of 42
_Video Distribution Profile_

## **13 Appendix B (Informative): Video Streaming with High** **quality Audio**


This section contains an example of typical signaling procedures defined in AVDTP for
audio and video streaming set up. The audio streaming is defined in A2DP [2]. This
section is informative only. For details, refer to GAVDP [4] and AVDTP [5]. In this
example, the **SRC** of audio stream and video stream is assumed to be the **INT**, while
the **SNK** to be the **ACP** .

### **13.1 Audio and Video Streaming Set Up**

**SRC** device supports two _Stream Endpoints_ (SEP1 and SEP2). SEP1 is the source of
audio and SEP2 is the source of video. **SNK** device also supports two _Stream_
_Endpoints_ (SEP1 and SEP2). SEP1 is the sink of audio and SEP2 is the sink of video.













_Figure 13.1: Example of High Quality Audio and Video Streaming_
The initial states of the both devices are <IDLE>.

The **SRC** initiates _Stream Endpoint (SEP) Discovery_ procedure. This procedure serves
to return the media type and SEID for each stream end-point. The **SRC** finds the audiotype SEP (SEP1) and video-type SEP (SEP2) in the **SNK** .

Then, _Get All Capabilities_ procedure is initiated to collect service capabilities of these
two SEPs in the **SNK** . There are two kinds of service capabilities; one is an application
service capability and the other is a transport service capability. The application service
capability of SEP1 consists of audio codec capability and content protection capability.
The application service capability of SEP2 consists of video codec capability and
content protection capability. Regarding the transport service capability, refer to Section
5.4 in AVDTP [5].

Based on collected SEP information and service capabilities, the **SRC** determines the
most suitable audio streaming parameters (codec, content protection and transport
service) for SEP1 in the **SNK** and video streaming parameters (codec, content
protection and transport service) for SEP2 in the **SNK** . Then, the **SRC** requests the
**SNK** to configure the audio streaming parameters of SEP1 and video streaming
parameters of SEP2 in the **SNK** by using the _Stream_ _Configuration_ procedure. The **SRC**


_BLUETOOTH_ SPECIFICATION Page 39 of 42
_Video Distribution Profile_


also configures the audio streaming parameters of SEP1 and video streaming
parameters of SEP2 in it.

Then, L2CAP channels for both audio and video streams are established as defined in
the _Stream_ _Establishment_ procedure. The **SRC** establishes the L2CAP channels
between SEP1 in the **SRC** and SEP1 in the **SNK** for audio streaming, and also
establishes the L2CAP channels between SEP2 in the **SRC** and SEP2 in the **SNK** for
video streaming. Finally, the states of both devices are set at <OPEN>.











_Figure 13.2: Audio and Video Streaming Set Up_

### **13.2 Audio and Video Streaming Procedure**

The **SRC** initiates _Start Streaming_ procedure by a user initiated action or an internal
event. This procedure indicates the **SNK** to start to send the audio stream from SEP1
and the video stream from SEP2 in the **SRC** . The states of both devices are changed


_BLUETOOTH_ SPECIFICATION Page 40 of 42
_Video Distribution Profile_


from <OPEN> to <STREAMING>. Audio and video streaming is started after this
procedure is completed.











_Figure 13.3: Audio and Video Streaming Procedure_

### **13.3 Media Synchronization**

There are some A/V applications that require the media synchronization between audio
and video streams. The Delay Reporting Feature defined by AVDTP [5] (used for the
transport protocol of both A2DP and VDP) can provide the function of media
synchronization.

The Basic Service specifies the media packet format that contains the time stamp field
in its header area. The time stamp value is used to indicate the sampling instant of the
first octet in the media packet from the **SRC** to the **SNK** . However, the value of the time
stamp is added by the transport protocol, and it is independent from the wall clock value
of the **SRC** .

The Reporting Service specifies the Sender Report Reporting packet to indicate some
transport service information of the corresponding media stream from the **SRC** to the
**SNK** . The Sender Report Reporting packet contains NTP [14] Time Stamp to indicate
the wall clock value of the **SRC,** and RTP [15] Time Stamp to indicate the time stamp
value in the media packet corresponding to the above NTP [14] Time Stamp value. The
difference between the NTP[14] Time Stamp value and RTP [15] Time Stamp value in


_BLUETOOTH_ SPECIFICATION Page 41 of 42
_Video Distribution Profile_


the Sender Report Reporting packet for the audio stream indicates the difference
between the wall clock value and the time stamp value in the media packet of audio
stream. It is the same for the video stream.

By using above mechanisms, when the **SNK** receives the media packets of audio
stream and video stream from the **SRC**, the **SNK** can estimate the real sampling time of
the first octet in the received media packets of audio stream and video stream. The
**SNK** can then render synchronized audio and video.


_BLUETOOTH_ SPECIFICATION Page 42 of 42
_Video Distribution Profile_

## **14 Appendix C: Acronyms and Abbreviations**


|Acronym|Description|
|---|---|
|A/V|Audio/Video|
|A2DP|Advanced Audio Distribution Profile|
|ACP|Acceptor|
|AVDTP|Audio/Video Distribution Transport Protocol|
|AVRCP|Audio/Video Remote Control Profile|
|CP_Type|Content Protection Type|
|CRC|Cyclic Redundancy Check|
|GAP|Generic Access Profile|
|GAVDP|Generic Audio/Video Distribution Profile|
|ICS|Implementation Conformance Statement|
|IETF|Internet Engineering Task Force|
|INT|Initiator|
|LC|Link Controller|
|LM|Link Manager|
|LSB|Least Significant Bit (Byte)|
|MPEG|Moving Picture Expert Group|
|MSB|Most Significant Bit (Byte)|
|MTU|Maximum Transmission Unit|
|NTP|Network Time Protocol|
|PSM|Protocol/Service Multiplexer|
|QoS|Quality of Service|
|RFA|Reserved for Future Additions|
|RFD|Reserved for Future Definition|
|RTP|Real-time Transport Protocol|
|SDP|Service Discovery Protocol|
|SNK|Sink|
|SRC|Source|
|TSS|Test Suite Structure|
|VDP|Video Distribution Profile|


