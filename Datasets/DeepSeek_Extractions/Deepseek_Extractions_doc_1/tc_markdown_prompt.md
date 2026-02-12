=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>title<|/ref|><|det|>[[67, 333, 872, 444]]<|/det|>
# Audio/Video Remote Control Profile (AVRCP)  

<|ref|>text<|/ref|><|det|>[[66, 474, 268, 493]]<|/det|>
Bluetooth®Test Suite  

<|ref|>text<|/ref|><|det|>[[92, 528, 598, 595]]<|/det|>
Revision: AVRCP.TS.p23Revision Date: 2025- 02- 18Prepared By: Audio, Telephony, and Automotive Working GroupPublishedduring TCRL: TCRL.2025- 1=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 70, 884, 128]]<|/det|>
This document, regardless of its title or content, is not a Bluetooth Specification as defined in the Bluetooth Patent/Copyright License Agreement ("PCLA") and Bluetooth Trademark License Agreement. Use of this document by members of Bluetooth SIG is governed by the membership and other related agreements between Bluetooth SIG Inc. ("Bluetooth SIG") and its members, including the PCLA and other agreements posted on Bluetooth SIG's website located at www.bluetooth.com.  

<|ref|>text<|/ref|><|det|>[[115, 133, 868, 183]]<|/det|>
THIS DOCUMENT IS PROVIDED "AS IS" AND BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES MAKE NO REPRESENTATIONS OR WARRANTIES AND DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTY OF MERCHANTABILITY, TITLE, NON- INFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, THAT THE CONTENT OF THIS DOCUMENT IS FREE OF ERRORS.  

<|ref|>text<|/ref|><|det|>[[115, 185, 875, 258]]<|/det|>
TO THE EXTENT NOT PROHIBITED BY LAW, BLUETOOTH SIG, ITS MEMBERS, AND THEIR AFFILIATES DISCLAIM ALL LIABILITY ARISING OUT OF OR RELATING TO USE OF THIS DOCUMENT AND ANY INFORMATION CONTAINED IN THIS DOCUMENT, INCLUDING LOST REVENUE, PROFITS, DATA OR PROGRAMS, OR BUSINESS INTERRUPTION, OR FOR SPECIAL, INDIRECT, CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, AND EVEN IF BLUETOOTH SIG, ITS MEMBERS, OR THEIR AFFILIATES HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.  

<|ref|>text<|/ref|><|det|>[[115, 260, 876, 298]]<|/det|>
This document is proprietary to Bluetooth SIG. This document may contain or cover subject matter that is intellectual property of Bluetooth SIG and its members. The furnishing of this document does not grant any license to any intellectual property of Bluetooth SIG or its members.  

<|ref|>text<|/ref|><|det|>[[116, 307, 437, 320]]<|/det|>
This document is subject to change without notice.  

<|ref|>text<|/ref|><|det|>[[115, 330, 876, 357]]<|/det|>
Copyright © 2001- 2025 by Bluetooth SIG, Inc. The Bluetooth word mark and logos are owned by Bluetooth SIG, Inc. Other third- party brands and names are the property of their respective owners.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 72, 231, 93]]<|/det|>
## Contents  

<|ref|>text<|/ref|><|det|>[[113, 102, 900, 120]]<|/det|>
1 Scope 10  

<|ref|>text<|/ref|><|det|>[[113, 124, 899, 142]]<|/det|>
2 References, definitions, and abbreviations 11  

<|ref|>text<|/ref|><|det|>[[142, 145, 899, 202]]<|/det|>
2.1 References 11  2.2 Definitions 11  2.3 Acronyms and abbreviations 11  

<|ref|>text<|/ref|><|det|>[[113, 203, 899, 220]]<|/det|>
3 Test Suite Structure (TSS) 12  

<|ref|>text<|/ref|><|det|>[[142, 220, 899, 237]]<|/det|>
3.1 Test Strategy 12  

<|ref|>text<|/ref|><|det|>[[142, 237, 899, 253]]<|/det|>
3.1 Test groups 12  

<|ref|>text<|/ref|><|det|>[[142, 254, 899, 270]]<|/det|>
3.2  

<|ref|>text<|/ref|><|det|>[[142, 270, 899, 286]]<|/det|>
3.2.1 Firstleveltest group 12  

<|ref|>text<|/ref|><|det|>[[142, 286, 899, 302]]<|/det|>
3.2.2 Second level test group 12  

<|ref|>text<|/ref|><|det|>[[142, 302, 899, 317]]<|/det|>
3.2.3 Initialization 12  

<|ref|>text<|/ref|><|det|>[[113, 322, 899, 339]]<|/det|>
4 Test cases (TC) 13  

<|ref|>text<|/ref|><|det|>[[142, 341, 899, 358]]<|/det|>
4.1 Introduction 13  

<|ref|>text<|/ref|><|det|>[[142, 360, 899, 376]]<|/det|>
4.1.1 Test caseidentificationconventions 13  

<|ref|>text<|/ref|><|det|>[[142, 377, 899, 393]]<|/det|>
4.1.2 Conformance 14  

<|ref|>text<|/ref|><|det|>[[142, 393, 899, 409]]<|/det|>
4.1.3 Other general information 14  

<|ref|>text<|/ref|><|det|>[[142, 410, 899, 425]]<|/det|>
4.1.4 Pass/Failverdictionconventions 14  

<|ref|>text<|/ref|><|det|>[[142, 426, 899, 443]]<|/det|>
4.2 Generic SDP Integrated Tests 15  

<|ref|>text<|/ref|><|det|>[[142, 443, 899, 459]]<|/det|>
4.2.1 ServerGenericSDPIntegratedTests 15  

<|ref|>text<|/ref|><|det|>[[142, 459, 899, 475]]<|/det|>
4.2.1.1 Controller 15  

<|ref|>text<|/ref|><|det|>[[142, 476, 899, 492]]<|/det|>
AVRCP/CT/SGSIT/SERR/BV- 01- C [Service record GSIT - AVRCP CT] 15  

<|ref|>text<|/ref|><|det|>[[142, 492, 899, 507]]<|/det|>
AVRCP/CT/SGSIT/ATTR/BV- 01- C [Attribute GSIT - Protocol Descriptor List] 15  

<|ref|>text<|/ref|><|det|>[[142, 507, 899, 523]]<|/det|>
AVRCP/CT/SGSIT/ATTR/BV- 02- C [Attribute GSIT - Additional Protocol Descriptor Lists, Browsing Channel] 15  

<|ref|>text<|/ref|><|det|>[[142, 523, 899, 538]]<|/det|>
AVRCP/CT/SGSIT/ATTR/BV- 03- C [Attribute GSIT - Bluetooth Profile Descriptor List, AVRCP 1.5] 15  

<|ref|>text<|/ref|><|det|>[[142, 538, 899, 554]]<|/det|>
AVRCP/CT/SGSIT/ATTR/BV- 04- C [Attribute GSIT - Bluetooth Profile Descriptor List, AVRCP 1.6] 15  

<|ref|>text<|/ref|><|det|>[[142, 554, 899, 570]]<|/det|>
AVRCP/CT/SGSIT/ATTR/BV- 05- C [Attribute GSIT - Supported Features] 15  

<|ref|>text<|/ref|><|det|>[[142, 570, 899, 586]]<|/det|>
4.2.1.2 Target 16  

<|ref|>text<|/ref|><|det|>[[142, 587, 899, 603]]<|/det|>
AVRCP/TG/SGSIT/SERR/BV- 01- C [Service record GSIT - AVERCP TG] 16  

<|ref|>text<|/ref|><|det|>[[142, 603, 899, 619]]<|/det|>
AVRCP/TG/SGSIT/ATTR/BV- 01- C [Attribute GSIT - Protocol descriptor List] 16  

<|ref|>text<|/ref|><|det|>[[142, 619, 899, 635]]<|/det|>
AVRCP/TG/SGSIT/ATTR/BV- 02- C [Attribute GSIT - Additional protocol descriptor Lists, Browsing Channel] 16  

<|ref|>text<|/ref|><|det|>[[142, 635, 899, 651]]<|/det|>
AVRCP/TG/SGSIT/ATTR/BV- 03- C [Attribute GSIT - Additional protocol descriptor Lists, Cover Art] 16  

<|ref|>text<|/ref|><|det|>[[142, 651, 899, 667]]<|/det|>
AVRCP/TG/SGSIT/ATTR/BV- 04- C [Attribute GSIT - Bluetooth profile Descriptor List, AVRCP 1.5] 16  

<|ref|>text<|/ref|><|det|>[[142, 667, 899, 683]]<|/det|>
AVRCP/TG/SGSIT/ATTR/BV- 05- C [Attribute GSIT - Bluetooth profile Descriptor List, AVRCP 1.6] 16  

<|ref|>text<|/ref|><|det|>[[142, 683, 899, 699]]<|/det|>
AVRCP/TG/SGSIT/ATTR/BV- 06- C [Attribute GSIT - Supported Features] 16  

<|ref|>text<|/ref|><|det|>[[142, 699, 899, 715]]<|/det|>
4.2.1.3 Audio/Video Remote Control Profile - Attribute ID Offset String tests 17  

<|ref|>text<|/ref|><|det|>[[142, 715, 899, 731]]<|/det|>
AVRCP/CT/SGSIT/OFFS/BV- 01- C [Attribute ID Offset String GSIT - Service Name] 17  

<|ref|>text<|/ref|><|det|>[[142, 731, 899, 747]]<|/det|>
AVRCP/CT/SGSIT/OFFS/BV- 02- C [Attribute ID Offset String GSIT - Provider Name] 17  

<|ref|>text<|/ref|><|det|>[[142, 747, 899, 763]]<|/det|>
AVRCP/TG/SGSIT/OFFS/BV- 03- C [Attribute ID Offset String GSIT - Service Name] 17  

<|ref|>text<|/ref|>成为 17  

<|ref|>text<|/ref|><|det|>[[142, 763, 899, 779]]<|/det|>
AVRCP/TG/SGSIT/OFFS/BV- 04- C [Attribute ID Offset String GSIT - Provider Name] 17  

<|ref|>text<|/ref|>成为 18  

<|ref|>text<|/ref|><|det|>[[142, 780, 899, 796]]<|/det|>
AVRCP/CT/CGSIT/SFC/BV- 01- C [SDP Future Compatibility - IUT is AVRCP CT] 18  

<|ref|>text<|/ref|><|det|>[[142, 796, 899, 812]]<|/det|>
AVRCP/TG/CGSIT/SFC/BV- 02- C [SDP Future Compatibility - IUT is AVRCP TG] 18  

<|ref|>text<|/ref|><|det|>[[142, 814, 899, 830]]<|/det|>
Connection Establishment for Browsing 19  

<|ref|>text<|/ref|><|det|>[[142, 832, 899, 848]]<|/det|>
AVRCP/CT/CONV/BV- 01- C [Connection establishment for browsing - CT] 19  

<|ref|>text<|/ref|><|det|>[[142, 848, 899, 864]]<|/det|>
AVRCP/TG/CONV/BV- 02- C [Connection establishment for browsing - TG] 19  

<|ref|>text<|/ref|><|det|>[[142, 864, 899, 880]]<|/det|>
AVRCP/TG/CONV/BV- 05- C [Connection establishment for browsing - TG initiates control channel and CT  

<|ref|>text<|/ref|><|det|>[[142, 880, 899, 896]]<|/det|>
initiates browsing channel] 20=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[142, 68, 899, 886]]<|/det|>
4.4 Connection Release for Browsing 21AVRCP/CT/CON/BV-03- C [Connection release for browsing - CT] 21AVRCP/TG/CON/BV-04- C [Connection release for browsing - TG] 224.5 Media Player Selection Commands and Notifications 23AVRCP/CT/MPS/BV-01- C [SetAddressedPlayer - CT] 23AVRCP/TG/MPS/BV-02- C [SetAddressedPlayer - TG] 24AVRCP/CT/MPS/BV-03- C [SetBrowsedPlayer - CT] 25AVRCP/TG/MPS/BV-04- C [SetBrowsedPlayer - TG] 26AVRCP/TG/MPS/BV-05- C [AddressedPlayerChanged notification - TG] 27AVRCP/TG/MPS/BV-06- C [PlayerFeatureBitmask - TG] 28AVRCP/TG/MPS/BV-07- C [AvailablePlayersChanged notification - TG] 29AVRCP/CT/MPS/BV-08- C [GetFoldertems - CT] 30AVRCP/TG/MPS/BV-09- C [GetFoldertems - TG] 31AVRCP/TG/MPS/BV-10- C [DefaultAddressedPlayer - TG] 32AVRCP/CT/MPS/BV-11- C [GetTotalNumberOfItems - CT] 33AVRCP/TG/MPS/BV-12- C [GetTotalNumberOfItems - TG] 34AVRCP/TG/MPS/BI-01- C [SetAddressedPlayer - TG] 35AVRCP/TG/MPS/BI-02- C [SetBrowsedPlayer - TG] 364.6 Media Content Navigation Commands and Notifications for Content Browsing 37AVRCP/CT/MCN/CB/BV-01- C [GetFoldertems - CT] 37AVRCP/TG/MCN/CB/BV-02- C [GetFoldertems - TG] 38AVRCP/TG/MCN/CB/BV-03- C [GetFoldertems - TG] 39AVRCP/CT/MCN/CB/BV-04- C [ChangePath - CT] 40AVRCP/TG/MCN/CB/BV-05- C [ChangePath - TG] 41AVRCP/TG/MCN/CB/BV-06- C [ChangePath - TG] 42AVRCP/CT/MCN/CB/BV-07- C [GettlemAttributes - CT] 43AVRCP/TG/MCN/CB/BV-08- C [GettlemAttributes - TG] 44AVRCP/TG/MCN/CB/BV-09- C [UIDcounter - TG] 45AVRCP/TG/MCN/CB/BV-10- C [UIDcounter - TG] 46AVRCP/TG/MCN/CB/BV-11- C [UIDcounter - TG] 47AVRCP/CT/MCN/CB/BV-12- C [GetTotalNumberOfItems - CT] 48AVRCP/TG/MCN/CB/BV-13- C [GetTotalNumberOfItems - TG] 49AVRCP/TG/MCN/CB/BI-01- C [GetFoldertems - TG] 50AVRCP/TG/MCN/CB/BI-02- C [GetFoldertems - TG] 51AVRCP/TG/MCN/CB/BI-03- C [GetFoldertems - TG] 52AVRCP/TG/MCN/CB/BI-04- C [ChangePath - TG] 53AVRCP/TG/MCN/CB/BI-05- C [UIDcounter - TG] 54AVRCP/TG/MCN/CB/BV-01- C [Search - CT] 55AVRCP/TG/MCN/SRC/BV-01- C [Search - TG] 56AVRCP/CT/MCN/SRC/BV-02- C [Search - TG] 57AVRCP/CT/MCN/SRC/BV-03- C [GetFoldertems - CT] 58AVRCP/TG/MCN/SRC/BV-04- C [GetFoldertems - TG] 59AVRCP/CT/MCN/SRC/BV-05- C [GettlemAttributes - CT] 60AVRCP/TG/MCN/SRC/BV-06- C [GettlemAttributes - TG] 61AVRCP/CT/MCN/SRC/BV-07- C [GetTotalNumberOfItems - CT] 62AVRCP/TG/MCN/SRC/BV-08- C [GetTotalNumberOfItems - TG] 63AVRCP/CT/MCN/NP/BV-01- C [PlayItem - CT] 63AVRCP/TG/MCN/NP/BV-02- C [PlayItem - TG] 64AVRCP/CT/MCN/NP/BV-03- C [AddToNowPlaying - CT] 65AVRCP/TG/MCN/NP/BV-04- C [AddToNowPlaying - TG] 66AVRCP/CT/MCN/NP/BV-05- C [GetFoldertems - CT] 67AVRCP/TG/MCN/NP/BV-06- C [GetFoldertems - TG] 68AVRCP/TG/MCN/NP/BV-07- C [NowPlayingContentChanged notification - TG] 69AVRCP/CT/MCN/NP/BV-08- C [GettlemAttributes - CT] 70=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[142, 68, 892, 135]]<|/det|>
AVRCP/TG/MCN/NP/BV- 09- C [GettlemAttributes - TG] 71  AVRCP/CT/MCN/NP/BV- 10- C [GetTotalNumberOfItems - CT] 72  AVRCP/TG/MCN/NP/BV- 11- C [GetTotalNumberOfItems - TG] 73  AVRCP/TG/MCN/NP/BI- 01- C [PlayItem_Invalid - TG] 74  AVRCP/TG/MCN/NP/BI- 02- C [AddToNowPlaying_Invalid - TG] 75  

<|ref|>text<|/ref|><|det|>[[142, 140, 884, 291]]<|/det|>
AVRCP/TG/MCN/NP/BV- 01- C [GetTotalNumberOfItems - CT] 76  AVRCP/TG/MCN/NP/BI- 02- C [GetTotalNumberOfItems - TG] 77  AVRCP/CT/VLH/BV- 03- C [NotifyVolumeChange - CT] 78  AVRCP/TG/VLH/BV- 04- C [NotifyVolumeChange - TG] 79  AVRCP/TG/VLH/BI- 01- C [GetAbsoluteVolume invalid behavior - TG] 80  AVRCP/TG/VLH/BI- 02- C [GetAbsoluteVolume invalid behavior - TG] 81  AVRCP/CT/VLH/BI- 03- C [GetAbsoluteVolume invalid behavior - CT] 82  AVRCP/CT/VLH/BI- 04- C [GetAbsoluteVolume invalid behavior - CT] 83  

<|ref|>text<|/ref|><|det|>[[142, 290, 884, 304]]<|/det|>
4.10 PASS THROUGH Handling 84  

<|ref|>text<|/ref|><|det|>[[142, 305, 884, 319]]<|/det|>
AVRCP/CT/PTH/BV- 01- C [Press and release - CT] 84  

<|ref|>text<|/ref|><|det|>[[142, 320, 884, 333]]<|/det|>
AVRCP/CT/PTH/BV- 02- C [Press and hold - CT] 85  

<|ref|>text<|/ref|><|det|>[[142, 335, 884, 348]]<|/det|>
4.11 Cover Art 86  

<|ref|>text<|/ref|><|det|>[[142, 350, 888, 364]]<|/det|>
AVRCP/CT/CA/BV- 01- C [Use GetFolderItems to request Cover Art attribute - CT] 86  

<|ref|>text<|/ref|><|det|>[[142, 365, 884, 379]]<|/det|>
AVRCP/TG/CA/BV- 02- C [Use GetFolderItems to request Cover Art attribute - TG] 88  

<|ref|>text<|/ref|><|det|>[[142, 380, 884, 394]]<|/det|>
AVRCP/CT/CA/BV- 03- C [Use GettlemAttributes to request Cover Art attribute - CT] 89  

<|ref|>text<|/ref|><|det|>[[142, 395, 884, 409]]<|/det|>
AVRCP/TG/CA/BV- 04- C [Use GettlemAttributes to request Cover Art attribute - TG] 90  

<|ref|>text<|/ref|><|det|>[[142, 410, 884, 424]]<|/det|>
AVRCP/CT/CA/BV- 05- C [Use GetElementAttributes to request Cover Art attribute - CT] 91  

<|ref|>text<|/ref|><|det|>[[142, 425, 884, 439]]<|/det|>
AVRCP/TG/CA/BV- 06- C [Use GetElementAttributes to request Cover Art attribute - TG] 92  

<|ref|>text<|/ref|><|det|>[[142, 440, 884, 454]]<|/det|>
AVRCP/CT/CA/BV- 07- C [Use the Imaging Property Object - CT] 94  

<|ref|>text<|/ref|><|det|>[[142, 455, 884, 469]]<|/det|>
AVRCP/TG/CA/BV- 08- C [Use the Imaging Property Object - TG] 95  

<|ref|>text<|/ref|><|det|>[[142, 470, 884, 484]]<|/det|>
AVRCP/CT/CA/BV- 09- C [Pull an Image as a Thumbnail - CT] 97  

<|ref|>text<|/ref|><|det|>[[142, 485, 884, 499]]<|/det|>
AVRCP/TG/CA/BV- 10- C [Pull an Image as a Thumbnail - TG] 98  

<|ref|>text<|/ref|><|det|>[[142, 500, 884, 514]]<|/det|>
AVRCP/CT/CA/BV- 11- C [Pull a Thumbnail - CT] 99  

<|ref|>text<|/ref|><|det|>[[142, 515, 884, 529]]<|/det|>
AVRCP/TG/CA/BV- 12- C [Pull a Thumbnail - TG] 101  

<|ref|>text<|/ref|><|det|>[[142, 530, 884, 544]]<|/det|>
AVRCP/CT/CA/BV- 13- C [Pull a Native Image - CT] 102  

<|ref|>text<|/ref|><|det|>[[142, 545, 884, 559]]<|/det|>
AVRCP/TG/CA/BV- 14- C [Pull a Native Image - TG] 103  

<|ref|>text<|/ref|><|det|>[[142, 560, 884, 574]]<|/det|>
AVRCP/CT/CA/BV- 15- C [Cover Art SDP record - CT] 104  

<|ref|>text<|/ref|><|det|>[[142, 575, 884, 589]]<|/det|>
AVRCP/TG/CA/BV- 16- C [Cover Art SDP record - TG] 105  

<|ref|>text<|/ref|><|det|>[[142, 590, 884, 604]]<|/det|>
AVRCP/CT/CA/BV- 17- C [UIDs Changed during Cover Art - CT] 106  

<|ref|>text<|/ref|><|det|>[[142, 605, 884, 619]]<|/det|>
AVRCP/CT/CA/BV- 18- C [Database- Unaware Folder Change during Cover Art - CT] 108  

<|ref|>text<|/ref|><|det|>[[142, 620, 884, 634]]<|/det|>
AVRCP/TG/CA/BI- 01- C [Retrieval of Cover Art attribute with no OBEX connection - TG] 110  

<|ref|>text<|/ref|><|det|>[[142, 635, 884, 649]]<|/det|>
AVRCP/TG/CA/BI- 04- C [Retrieval of Cover Art attribute with no OBEX connection using GettlemAttributes -  

<|ref|>text<|/ref|><|det|>[[142, 650, 884, 664]]<|/det|>
TG] 111  

<|ref|>text<|/ref|><|det|>[[142, 665, 884, 679]]<|/det|>
AVRCP/TG/CA/BI- 05- C [Retrieval of Cover Art attribute with no OBEX connection using  

<|ref|>text<|/ref|><|det|>[[142, 680, 884, 694]]<|/det|>
GetElementAttributes - TG] 112  

<|ref|>text<|/ref|><|det|>[[142, 695, 884, 709]]<|/det|>
AVRCP/TG/CA/BI- 06- C [Request of Unsupported Image Type - TG] 113  

<|ref|>text<|/ref|><|det|>[[142, 710, 884, 724]]<|/det|>
AVRCP/TG/CA/BI- 07- C [Request of Unsupported Image Type without browsing - TG] 115  

<|ref|>text<|/ref|><|det|>[[142, 725, 884, 739]]<|/det|>
AVRCP/TG/CA/BI- 08- C [Use GetFolderItems to request Cover Art attribute - TG] 116  

<|ref|>text<|/ref|><|det|>[[142, 740, 884, 754]]<|/det|>
AVRCP/TG/CA/BI- 09- C [Use GettlemAttributes to request Cover Art attribute - TG] 117  

<|ref|>text<|/ref|><|det|>[[142, 755, 884, 769]]<|/det|>
AVRCP/TG/CA/BI- 10- C [Use GetElementAttributes to request Cover Art attribute - TG] 118  

<|ref|>text<|/ref|><|det|>[[142, 770, 884, 784]]<|/det|>
AVRCP/TG/CA/BI- 11- C [Use GettlemAttributes to request Cover Art attribute - TG] 119  

<|ref|>text<|/ref|><|det|>[[142, 794, 888, 808]]<|/det|>
AVRCP/CT/MPS/BV- 04- C [Listing of available Media Players] 119  

<|ref|>text<|/ref|><|det|>[[142, 809, 888, 823]]<|/det|>
AVRCP/TG/MPS/BV- 01- C [Listing of available Media Players] 119  

<|ref|>text<|/ref|><|det|>[[142,- 824, 888, 838]]<|/det|>
4.12.2 Availability of Media Players 120  

<|ref|>text<|/ref|><|det|>[[142, 840, 888, 854]]<|/det|>
AVRCP/CT/MPS/BV- 05- C [Availability of Media Players] 120  

<|ref|>text<|/ref|><|det|>[[142, 855, 888, 869]]<|/det|>
AVRCP/TG/MPS/BV- 08- C [Availability of Media Players] 120  

<|ref|>text<|/ref|><|det|>[[142, 870, 888, 884]]<|/det|>
4.12.3 PASS THROUGH functionality of Media Players 120  

<|ref|>text<|/ref|><|det|>[[142, 885, 888, 899]]<|/det|>
AVRCP/CT/MPS/BV- 06- C [PASS THROUGH functionality of Media Players] 121=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[140, 68, 895, 92]]<|/det|>
AVRCP/TG/MPS/BV- 03- C [PASS THROUGH functionality of Media Players] 121  

<|ref|>text<|/ref|><|det|>[[144, 88, 891, 103]]<|/det|>
4.13 Media Content Navigation tests for Content Browsing 121  

<|ref|>text<|/ref|><|det|>[[144, 103, 896, 118]]<|/det|>
4.13.1 Browsing of the current folder 121  

<|ref|>text<|/ref|><|det|>[[150, 120, 896, 135]]<|/det|>
AVRCP/CT/MCN/CB/BV- 08- C [Browsing of the current folder] 121  

<|ref|>text<|/ref|><|det|>[[150, 135, 896, 150]]<|/det|>
AVRCP/TG/MCN/CB/BV- 01- C [Browsing of the current folder] 121  

<|ref|>text<|/ref|><|det|>[[144, 150, 896, 165]]<|/det|>
4.13.2 Browsing up 122  

<|ref|>text<|/ref|><|det|>[[150, 166, 896, 181]]<|/det|>
AVRCP/CT/MCN/CB/BV- 02- C [Browsing up] 122  

<|ref|>text<|/ref|><|det|>[[150, 182, 896, 197]]<|/det|>
AVRCP/TG/MCN/CB/BV- 14- C [Browsing up] 122  

<|ref|>text<|/ref|><|det|>[[144, 197, 896, 212]]<|/det|>
4.13.3 Browsing down 122  

<|ref|>text<|/ref|><|det|>[[150, 212, 896, 227]]<|/det|>
AVRCP/CT/MCN/CB/BV- 03- C [Browsing down] 123  

<|ref|>text<|/ref|><|det|>[[150, 228, 896, 243]]<|/det|>
AVRCP/TG/MCN/CB/BV- 15- C [Browsing down] 123  

<|ref|>text<|/ref|><|det|>[[144, 243, 896, 258]]<|/det|>
4.13.4 Playing of a track from the Virtual Media Player Filesystem 123  

<|ref|>text<|/ref|><|det|>[[150, 259, 896, 274]]<|/det|>
AVRCP/CT/MCN/CB/BV- 10- C [Playing of a track from the Virtual Media Player Filesystem] 123  

<|ref|>text<|/ref|><|det|>[[150, 274, 896, 289]]<|/det|>
AVRCP/TG/MCN/CB/BV- 04- C [Playing of a track from the Virtual Media Player Filesystem] 123  

<|ref|>title<|/ref|><|det|>[[144, 289, 896, 304]]<|/det|>
#### 4.13.5 Change in media database 124  

<|ref|>text<|/ref|><|det|>[[150, 305, 896, 320]]<|/det|>
AVRCP/CT/MCN/CB/BV- 05- C [Change in media database] 124  

<|ref|>text<|/ref|><|det|>[[150, 320, 896, 335]]<|/det|>
AVRCP/TG/MCN/CB/BV- 16- C [Change in media database] 124  

<|ref|>text<|/ref|><|det|>[[144, 336, 816, 351]]<|/det|>
Mata for Virtual Filesystem 124  

<|ref|>text<|/ref|><|det|>[[144, 352, 896, 367]]<|/det|>
AVRCP/CT/MCN/CB/BV- 06- C [Metadata from Virtual Filesystem] 125  

<|ref|>text<|/ref|><|det|>[[144, 368, 896, 383]]<|/det|>
AVRCP/TG/MCN/CB/BV- 17- C [Metadata from Virtual Filesystem] 125  

<|ref|>text<|/ref|><|det|>[[144, - 383, 896, 398]]<|/det|>
AVRCP/TG/MCN/CB/BV- 07- C [Browsing of a folder if the player is not addressed] 125  

<|ref|>text<|/ref|><|det|>[[144, 398, 896, 413]]<|/det|>
AVRCP/TG/MCN/CB/BV- 08- C [Browsing of a folder in the player only when addressed] 126  

<|ref|>text<|/ref|><|det|>[[144, 413, 896, 428]]<|/det|>
AVRCP/CT/MCN/CB/BV- 09- C [CT can retrieve the metadata Virtual Filesystem from TG with future SDP  

<|ref|>text<|/ref|><|det|>[[144, 428, 896, 444]]<|/det|>
version] 126  

<|ref|>text<|/ref|><|det|>[[144, 444, 896, 459]]<|/det|>
4.14 Media Content Navigation tests for Search 127  

<|ref|>text<|/ref|><|det|>[[144, 460, 896, 475]]<|/det|>
4.14.1 Search request 127  

<|ref|>text<|/ref|><|det|>[[150, 476, 896, 491]]<|/det|>
AVRCP/CT/MCN/SRC/BV- 08- C [Search request] 127  

<|ref|>text<|/ref|><|det|>[[150, 491, 896, 506]]<|/det|>
AVRCP/TG/MCN/SRC/BV- 01- C [Search request] 127  

<|ref|>text<|/ref|><|det|>[[144, 506, 896, 521]]<|/det|>
4.14.2 Browsing of the Search results 127  

<|ref|>text<|/ref|><|det|>[[150, 522, 896, 537]]<|/det|>
AVRCP/CT/MCN/SRC/BV- 09- C [Browsing of the Search results] 128  

<|ref|>text<|/ref|><|det|>[[150, 537, 896, 552]]<|/det|>
AVRCP/TG/MCN/SRC/BV- 05- C [Browsing of the Search results] 128  

<|ref|>text<|/ref|><|det|>[[144, 552, 896, 567]]<|/det|>
4.14.3 Play from Search results 128  

<|ref|>text<|/ref|><|det|>[[150, 568, 896, 583]]<|/det|>
AVRCP/CT/MCN/SRC/BV- 10- C [Play from Search results] 128  

<|ref|>text<|/ref|><|det|>[[150, 584, 896, 599]]<|/det|>
AVRCP/TG/MCN/SRC/BV- 03- C [Play from Search results] 128  

<|ref|>text<|/ref|><|det|>[[144, 599, 896, 614]]<|/det|>
4.14.4 Metadata from Search results 129  

<|ref|>text<|/ref|><|det|>[[150, 614, 896, 629]]<|/det|>
AVRCP/CT/MCN/SRC/BV- 11- C [Metadata from Search results] 129  

<|ref|>text<|/ref|><|det|>[[150, 630, 896, 645]]<|/det|>
AVRCP/TG/MCN/SRC/BV- 07- C [Metadata from Search results] 129  

<|ref|>text<|/ref|><|det|>[[150, 645, 896, 661]]<|/det|>
4.15 Media Content Navigation tests for Now Playing 129  

<|ref|>text<|/ref|><|det|>[[144, 662, 896, 677]]<|/det|>
4.15.1 Playing of a track from the Now Playing folder 129  

<|ref|>text<|/ref|><|det|>[[150, 678, 896, 693]]<|/det|>
AVRCP/CT/MCN/NP/BV- 11- C [Playing of a track from the Now Playing folder] 130  

<|ref|>text<|/ref|><|det|>[[150, 693, 896, 708]]<|/det|>
AVRCP/TG/MCN/NP/BV- 01- C [Playing of a track from the Now Playing folder] 130  

<|ref|>text<|/ref|>成为 4.15.2 Adding a Filesystem track to Now Playing list 130  

<|ref|>text<|/ref|><|det|>[[150, 708, 896, 723]]<|/det|>
4.15.2 Adding a Filesystem track to Now Playing list 130  

<|ref|>text\[\text{AVRCP/CT/MCN/NP/BV- 12- C [Adding a Filesystem track to Now Playing list] 130} \]  

<|ref|>text<|/ref|><|det|>[[150, 724, 896, 739]]<|/det|>
AVRCP/TG/MCN/NP/BV- 13- C [Adding a Search result track to Now Playing list] 131  

<|ref|>text<|/ref|><|det|>[[150, 739, 896, 754]]<|/det|>
AVRCP/TG/MCN/NP/BV- 08- C [Adding a Filesystem track to Now Playing list] 130  

<|ref|>text<|/ref|><|det|>[[150, 754, 896, 769]]<|/det|>
4.15.3 Adding a Search result track to Now Playing list 131  

<|ref|>text<|/ref|><|det|>[[150, 769, 896, 784]]<|/det|>
AVRCP/CT/MCN/NP/BV- 13- C [Adding a Search result track to Now playing list] 131  

<|ref|>text<|/ref|><|det|>[[150, 784, 896, 799]]<|/det|>
AVRCP/TG/MCN/NP/BV- 03- C [Adding a Search result track to Now Playing list] 131  

<|ref|>text<|/ref|>成为 4.15.4 Local change of Now Playing list on TG 131  

<|ref|>text<|/ref|><|det|>[[150, 800, 896, 815]]<|/det|>
4.15.4 Local change of Now Playing list on TG 131  

<|ref|>text<|/ref|>成为 4.15.4 Local change of Now Playing list 131  

<|ref|>text<|/ref|><|det|>[[150, 816, 896, 831]]<|/det|>
AVRCP/CT/MCN/NP/BV- 14- C [Local change of Now Playing list on TG] 132  

<|ref|>text<|/ref|><|det|>[[150, 831, 896, 846]]<|/det|>
AVRCP/TG/MCN/NP/BV- 10- C [Local change of Now Playing list on TG] 132  

<|ref|>text<|/ref|><|det|> [[150, 846, 896, 861]]<|/det|>
4.15.5 Metadata from Now Playing list 132  

<|ref|>text<|/ref|><|det|>[[150, 861, 896, 876]]<|/det|>
AVRCP/CT/MCN/NP/BV- 15- C [Metadata from Now Playing list] 132  

<|ref|>text<|/ref|><|det|>[[150, 876, 896, 891]]<|/det|>
AVRCP/TG/MCN/NP/BV- 05- C [Metadata from Now Playing list] 132  

<|ref|>text<|/ref|><|det|>[[150, - 891, 896, 906]]<|/det|>
4.15.6 Browsing the Now Playing folder 133=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[140, 70, 895, 899]]<|/det|>
AVRCP/CT/MCN/NP/BV- 16- C [Browsing the Now Playing folder] 133AVRCP/TG/MCN/NP/BV- 12- C [Browsing the Now Playing folder] 1334.15.7 Adding a Playable Folder to Now Playing list 133AVRCP/CT/MCN/NP/BV- 17- C [Adding a Playable Folder to Now Playing list] 134AVRCP/TG/MCN/NP/BV- 13- C [Adding a Playable Folder to Now Playing list] 1344.16 Volume Level Handling tests 1344.16.1 Monitoring the TG volume on the CT 134AVRCP/CT/VLH/BV- 04- C [Monitoring the TG volume on the CT] 134AVRCP/TG/VLH/BV- 01- C [Monitoring the TG volume on the CT] 1344.16.2 Changing the volume 135AVRCP/CT/VLH/BV- 05- C [Changing the volume] 135AVRCP/TG/VLH/BV- 03- C [Changing the volume] 1354.17 Cover Art tests 1354.17.1 Retrieval of multiple Cover Art images 135AVRCP/CT/CA/BV- 04- C [Retrieval of multiple Cover Art images] 136AVRCP/TG/CA/BV- 01- C [Retrieval of multiple Cover Art images] 1364.17.2 Retrieval of Cover Art image for the currently playing track 136AVRCP/CT/CA/BV- 02- C [Retrieval of Cover Art image for the currently playing track] 137AVRCP/TG/CA/BV- 05- C [Retrieval of Cover Art image for the currently playing track] 1374.17.3 Retrieval of Cover Art image for the currently playing track without browsing 137AVRCP/CT/CA/BV- 06- C [Retrieval of Cover Art image for the currently playing track without browsing] 137AVRCP/TG/CA/BV- 03- C [Retrieval of Cover Art image for the currently playing track without browsing] 1384.18 Connection establishment for control 1384.18.1 Connection establishment for control initiated from the CT 1384.18.1.1 Connection establishment - CT 138AVRCP/CT/CEC/BV- 01- C [Connection establishment - CT] 138AVRCP/TG/CEC/BV- 01- C [Connection establishment - CT] 1384.18.2 Connection establishment for control initiated from the TG 1394.18.2.1 Connection establishment - TG 139AVRCP/CT/CEC/BV- 02- C [Connection establishment - TG] 139AVRCP/TG/CEC/BV- 02- C [Connection establishment - TG] 1394.18.3 Connection release for control initiated from the CT 1394.18.3.1 Connection release - CT 139AVRCP/CT/CRC/BV- 01- C [Connection release - CT] 140AVRCP/TG/CRC/BV- 01- C [Connection release - CT] 1404.18.4 Connection release for control initiated from the TG 1404.18.4.1 Connection release - TG 140AVRCP/CT/CRC/BV- 02- C [Connection release - TG] 140AVRCP/TG/CRC/BV- 02- C [Connection release - TG] 1404.19 Information collection for control 1414.19.1 Information collection by UNIT INFO command 1414.19.1.1 Information collection by UNIT INFO command 141AVRCP/CT/ICC/BV- 01- C [Information collection by UNIT INFO command] 141AVRCP/TG/ICC/BV- 01- C [Information collection by UNIT INFO command] 1414.19.2 Information collection by SUBUNIT INFO command 1424.19.2.1 Information collection by SUBUNIT INFO command 142AVRCP/CT/ICC/BV- 02- C [Information collection by SUBUNIT INFO command] 142AVRCP/TG/ICC/BV- 02- C [Information collection by SUBUNIT INFO command] 1414.20 PASS THROUGH commands 1434.20.1 Category 1 of PASS THROUGH command 1434.20.1.1 PASS THROUGH command transfer - category 1 143AVRCP/CT/PTT/BV- 01- C [PASS THROUGH command transfer - category 1] 143AVRCP/TG/PTT/BV- 01- C [PASS THROUGH command transfer - category=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[142, 69, 899, 86]]<|/det|>
4.20.2 Category 2 of PASS THROUGH command 144  

<|ref|>text<|/ref|><|det|>[[142, 87, 899, 120]]<|/det|>
4.20.2.1 PASS THROUGH command transfer - category 2 144  AVRCP/CT/PTT/BV- 02- C [PASS THROUGH command transfer - category 2] 144  

<|ref|>text<|/ref|><|det|>[[142, 120, 899, 135]]<|/det|>
AVRCP/TG/PTT/BV- 02- C [PASS THROUGH command transfer - category2] 144  

<|ref|>text<|/ref|><|det|>[[142, 136, 899, 151]]<|/det|>
4.20.3 Category 3 of PASS THROUGH command 145  

<|ref|>text<|/ref|><|det|>[[142, 152, 899, 167]]<|/det|>
4.20.3.1 PASS THROUGH command transfer - category 3 145  

<|ref|>text<|/ref|><|det|>[[142, 168, 899, 198]]<|/det|>
AVRCP/CT/PTT/BV- 03- C [PASS THROUGH command transfer - category 3] 145  AVRCP/TG/PTT/BV- 03- C [PASS THROUGH command transfer - category3] 145  

<|ref|>text<|/ref|><|det|>[[142, 199, 899, 213]]<|/det|>
4.20.4 Category 4 of PASS THROUGH command 146  

<|ref|>text<|/ref|><|det|>[[142, 214, 899, 228]]<|/det|>
4.20.4.1 PASS THROUGH command transfer - category 4 146  

<|ref|>text<|/ref|><|det|>[[142, 229, 899, 244]]<|/det|>
AVRCP/CT/PTT/BV- 04- C [PASS THROUGH command transfer - category 4] 146  

<|ref|>text<|/ref|><|det|>[[142, 245, 899, 260]]<|/det|>
AVRCP/TG/PTT/BV- 04- C [PASS THROUGH command transfer - category4] 146  

<|ref|>text<|/ref|><|det|>[[142, 260, 899, 275]]<|/det|>
4.20.5 Press and hold of PASS THROUGH command 147  

<|ref|>text<|/ref|><|det|>[[142, 275, 899, 290]]<|/det|>
4.20.5.1 PASS THROUGH command transfer - press and hold 147  

<|ref|>text<|/ref|><|det|>[[142, 290, 899, 305]]<|/det|>
AVRCP/CT/PTT/BV- 05- C [PASS THROUGH command transfer - press and hold] 147  

<|ref|>text<|/ref|><|det|>[[142, 305, 899, 320]]<|/det|>
AVRCP/TG/PTT/BV- 05- C [PASS THROUGH command transfer - pressand hold] 147  

<|ref|>text<|/ref|><|det|>[[152, 321, 899, 336]]<|/det|>
4.21 Metadata Transfer 147  

<|ref|>text<|/ref|><|det|>[[142, 342, 899, 357]]<|/det|>
4.21.1 Configuration commands 147  

<|ref|>text<|/ref|><|det|>[[142, 358, 899, 373]]<|/det|>
AVRCP/CT/CFG/BV- 01- C [Get Capabilities - CT] 148  

<|ref|>text<|/ref|><|det|>[[142, 373, 899, 388]]<|/det|>
AVRCP/TG/CFG/BV- 02- C [Get Capabilities response - TG] 148  

<|ref|>text<|/ref|><|det|>[[142, 388, 899, 403]]<|/det|>
AVRCP/TG/CFG/BI- 01- C [Get Capabilities invalid behavior response - TG] 149  

<|ref|>text<|/ref|><|det|>[[142, 404, 899, 419]]<|/det|>
4.21.2 Player Application Settings commands 150  

<|ref|>text<|/ref|><|det|>[[142, 420, 899, 435]]<|/det|>
AVRCP/CT/PAS/BV- 01- C [List Player Application Setting Attributes - CT] 150  

<|ref|>text<|/ref|><|det|>[[142, 435, 899, 450]]<|/det|>
AVRCP/TG/PAS/BV- 02- C [List Player Application Setting Attributes - TG] 151  

<|ref|>text<|/ref|><|det|>[[142, 450, 899, 465]]<|/det|>
AVRCP/CT/PAS/BV- 03- C [Get Player Application Setting Attribute Text - CT] 152  

<|ref|>text<|/ref|><|det|>[[142, 465, 899, 480]]<|/det|>
AVRCP/TG/PAS/BV- 04- C [Get Player Application Setting Attribute Text - TG] 153  

<|ref|>text<|/ref|><|det|>[[142, 481, 899, 496]]<|/det|>
AVRCP/CT/PAS/BV- 05- C [List Player Application Setting Values - CT] 154  

<|ref|>text<|/ref|><|det|>[[142, 496, 899, 511]]<|/det|>
AVRCP/TG/PAS/BV- 06- C [List Player Application Setting Values - TG] 155  

<|ref|>text<|/ref|><|det|>[[142, 511, 899, 526]]<|/det|>
AVRCP/CT/PAS/BV- 07- C [Get Player Application Setting Value Text - CT] 156  

<|ref|>text<|/ref|><|det|>[[142, 526, 899, 541]]<|/det|>
AVRCP/TG/PAS/BV- 08- C [Get Player Application Setting Value Text - TG] 157  

<|ref|>text<|/ref|><|det|>[[142, 541, 899, 556]]<|/det|>
AVRCP/CT/PAS/BV- 09- C [Get Current Player Application Setting Value - CT] 158  

<|ref|>text<|/ref|><|det|>[[142, 556, 899, 571]]<|/det|>
AVRCP/TG/PAS/BV- 10- C [Get Current Player Application Setting Value - TG] 159  

<|ref|>text<|/ref|><|det|>[[142, 571, 899, 586]]<|/det|>
AVRCP/CT/PAS/BV- 11- C [Set Player Application Setting Value - CT] 160  

<|ref|>text<|/ref|><|det|>[[142, 586, 899, 601]]<|/det|>
AVRCP/TG/PAS/BI- 01- C [Get Player Application Settings Attribute Text invalid behavior - TG] 161  

<|ref|>text<|/ref|><|det|>[[142, 601, 899, 616]]<|/det|>
AVRCP/TG/PAS/BI- 02- C [List Player Application Setting Values invalid behavior - TG] 162  

<|ref|>text<|/ref|><|det|>[[142, 616, 899, 631]]<|/det|>
AVRCP/TG/PAS/BI- 03- C [Get Player Application Setting Value Text invalid behavior - TG] 163  

<|ref|>text<|/ref|><|det|>[[142, 631, 899, 646]]<|/det|>
AVRCP/TG/PAS/BI- 04- C [Get Current Player Application Setting Value invalid behavior - TG] 164  

<|ref|>text<|/ref|><|det|>[[142, 646, 899, 661]]<|/det|>
AVRCP/TG/PAS/BI- 05- C [Set Player Application Setting Value invalid behavior - TG] 165  

<|ref|>text<|/ref|><|det|>[[142, 666, 819, 681]]<|/det|>
Media Information commands 166  

<|ref|>text<|/ref|><|det|>[[142, 682, 899, 697]]<|/det|>
AVRCP/CT/MDI/BV- 01- C [Get Play Status - CT] 166  

<|ref|>text<|/ref|><|det|>[[142, 697, 899, 712]]<|/det|>
AVRCP/TG/MDI/BV- 02- C [Get Play Status - TG] 167  

<|ref|>text<|/ref|><|det|>[[142, 712, 899, 727]]<|/det|>
AVRCP/CT/MDI/BV- 03- C [Get Element Attributes - CT] 168  

<|ref|>text<|/ref|><|det|>[[142, 727, 899, 742]]<|/det|>
AVRCP/TG/MDI/BV- 04- C [Get Element Attributes - TG] 169  

<|ref|>text<|/ref|><|det|>[[142, 742, 899, 757]]<|/det|>
AVRCP/TG/MDI/BV- 05- C [Get Element Attributes - TG] 170  

<|ref|>text<|/ref|><|det|>[[142, 757, 899, 772]]<|/det|>
AVRCP/CT/MDI/BV- 06- C [CT can retrieve the Metadata for the currently playing track from TG with future  

<|ref|>text<|/ref|><|det|>[[142, 772, 899, 787]]<|/det|>
SDP version - Get Element Attributes] 171  

<|ref|>text<|/ref|><|det|>[[142, 787, 819, 802]]<|/det|>
Notification commands 172  

<|ref|>text<|/ref|><|det|>[[142, 802, 899, 817]]<|/det|>
AVRCP/CT/NFY/BV- 01- C [Register Notification - CT] 172  

<|ref|>text<|/ref|><|det|>[[142, 817, 899, 832]]<|/det|>
AVRCP/TG/NFY/BV- 02- C [Register Notification - TG] 173  

<|ref|>text<|/ref|><|det|>[[142, 832, 899, 847]]<|/det|>
AVRCP/TG/NFY/BV- 03- C [Register Notification EVENT PLAYER APPLICATION SETTING CHANGED -  

<|ref|>text<|/ref|><|det|>[[142, 847, 899, 862]]<|/det|>
TG] 174  

<|ref|>text<|/ref|><|det|>[[142, 862, 899, 877]]<|/det|>
AVRCP/TG/NFY/BV- 04- C [Track Changed - No Selected Track - TG] 175  

<|ref|>text<|/ref|><|det|>[[142, 877, 899, 892]]<|/det|>
AVRCP/TG/NFY/BV- 05- C [Track Changed - Playing Track - TG] 176  

<|ref|>text<|/ref|><|det|>[[142, 892, 899, 907]]<|/det|>
AVRCP/TG/NFY/BV- 06- C [Track Changed - Playing Track in NowPlaying - TG] 177  

<|ref|>text<|/ref|><|det|>[[142, 907, 899, 922]]<|/det|>
AVRCP/TG/NFY/BV- 07- C [Track Changed - Changing Track in NowPlaying - TG] 177=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[140, 68, 899, 325]]<|/det|>
AVRCP/TG/NFY/BV- 08- C [Track Changed - Selected Track - TG] 179  AVRCP/TG/NFY/BI- 01- C [Register for events invalid behavior - TG] 179  4.21.5 Invalid commands 180  AVRCP/TG/INV/BI- 01- C [Invalid PDU ID - TG] 180  AVRCP/TG/INV/BI- 02- C [General Reject - TG] 181  4.21.6 Basic Group Navigation commands 182  4.21.6.1 Next Group command transfer 182  AVRCP/CT/BGN/BV- 01- C [Next Group command transfer] 183  AVRCP/TG/BGN/BV- 01- C [Next Group command transfer] 183  4.21.6.2 Previous Group command transfer 183  AVRCP/CT/BGN/BV- 02- C [Previous Group command transfer] 183  AVRCP/TG/BGN/BV- 02- C [Previous Group command transfer] 183  4.21.7 Continuation PDUs commands 184  AVRCP/CT/RCR/BV- 01- C [Request continuing response - CT] 184  AVRCP/TG/RCR/BV- 02- C [Request continuing response - TG] 185  AVRCP/CT/RCR/BV- 03- C [Abort continuing response - CT] 186  AVRCP/TG/RCR/BV- 04- C [Abort continuing response - TG] 187  

<|ref|>text<|/ref|><|det|>[[112, 342, 899, 560]]<|/det|>
5 Test case mapping 189  6 Appendix A - Operation_id list tables 198  6.1 Operation_id of Category 1 198  6.2 Operation_id of Category 2 199  6.3 Operation_id of Category 3 199  6.4 Operation_id of Category 4 200  7 Appendix B - Supplementary Interoperability Tests 202  CT Handles Different TG Volume Resolutions 202  7.1 AVRCP/CT/VLH/BV- 06- C [Volume Control - LowresolutionTG] 202  AVRCP/CT/VLH/BV- 07- C [Volume Control - Higher resolution TG] 202  8 Revision history and acknowledgments 205=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[116, 72, 250, 96]]<|/det|>
## 1 Scope  

<|ref|>text<|/ref|><|det|>[[115, 110, 852, 175]]<|/det|>
This Bluetooth document contains the Test Suite Structure (TSS) and test cases to test the implementation of the Bluetooth Audio/Video Remote Control Profile (AVRCP) with the objective to provide a high probability of air interface interoperability between the tested implementation and other manufacturers' Bluetooth devices.  

<|ref|>text<|/ref|><|det|>[[115, 182, 841, 250]]<|/det|>
AVRCP provides support for multiple Media Player applications within the same physical device. Therefore, the features supported by an individual Media Player application might be a subset of the physical device's features marked in the ICS [3]. Therefore, the AVRCP IXIT document [6] allows announcing an individual Media Player application's features, see Figure 1.1.  

<|ref|>image<|/ref|><|det|>[[188, 264, 732, 417]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[115, 433, 509, 448]]<|/det|>
<center>Figure 1.1: IXIT dependencies for Media Player applications </center>  

<|ref|>text<|/ref|><|det|>[[115, 461, 870, 508]]<|/det|>
The IXIT contains a field to specify a player name to allow a player to be selected against which the browsing tests are run. Furthermore, the IXIT contains fields for one empty and one non- empty folder on the IUT.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[114, 72, 733, 97]]<|/det|>
## 2 References, definitions, and abbreviations  

<|ref|>sub_title<|/ref|><|det|>[[115, 112, 315, 132]]<|/det|>
### 2.1 References  

<|ref|>text<|/ref|><|det|>[[114, 139, 846, 188]]<|/det|>
This document incorporates provisions from other publications by dated or undated reference. These references are cited at the appropriate places in the text, and the publications are listed hereinafter. Additional definitions and abbreviations can be found in [1], [2], and [4].  

<|ref|>text<|/ref|><|det|>[[113, 197, 816, 425]]<|/det|>
[1] Bluetooth Core Specification  [2] Audio/Video Remote Control Profile, Version 1.0  [3] ICS Proforma for Audio/Video Remote Control Profile (AVRCP)  [4] Test Strategy and Terminology Overview  [5] Audio/Video Remote Control Profile Specification, Versions 1.4 and 1.5, Advanced Control Extension  [6] IXIT Proforma for Audio/Video Remote Control Profile  [7] Audio/Video Remote Control Profile Specification, Version 1.3, Enhanced Metadata  [8] Audio/Video Remote Control Profile Specification, Version 1.6  [9] Basic Imaging Profile Specification, Versions 1.1 or later  

<|ref|>text<|/ref|><|det|>[[113, 430, 852, 536]]<|/det|>
[10] irOBEX Specification, Version 1.5, Infrared Data Association  [11] Generic Object Exchange Profile Specification, Version 2.0 or later  [12] ITU-T X.290 series, OSI CONFORMANCE TESTING METHODOLOGY AND FRAMEWORK PROTOCOL RECOMMENDATIONS FOR ITU- T APPLICATIONS, ITU Recommendation X.290 series (equivalent to ISO 9646)  [13] SDP Test Suite, SDP.TS  

<|ref|>text<|/ref|><|det|>[[115, 536, 343, 552]]<|/det|>
[13] SDP Test Suite, SDP.TS  

<|ref|>sub_title<|/ref|><|det|>[[115, 557, 280, 576]]<|/det|>
### 2.2 Definitions  

<|ref|>text<|/ref|><|det|>[[115, 594, 583, 611]]<|/det|>
In this Bluetooth document, the definitions from [1] and [2] apply.  

<|ref|>table<|/ref|><|det|>[[115, 618, 881, 701]]<|/det|>

<table><tr><td>Definition</td><td>Description</td></tr><tr><td>Standby mode</td><td>a) for CT: no L2CAP channel for control to TG<br>b) for TG: no L2CAP channel for control to CT.</td></tr><tr><td>Normal condition</td><td>CT and TG are active and they are not in Park, Sniff or Hold mode.</td></tr></table>

<|ref|>table_footnote<|/ref|><|det|>[[115, 707, 333, 721]]<|/det|>
Table 2.1:Definitions for AVRCP  

<|ref|>sub_title<|/ref|><|det|>[[115, 736, 506, 757]]<|/det|>
### 2.3 Acronyms and abbreviations  

<|ref|>text<|/ref|><|det|>[[112, 763, 800, 781]]<|/det|>
In this Bluetooth document, the definitions, acronyms, and abbreviations from [1] and [2] apply.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[114, 72, 526, 98]]<|/det|>
## 3 Test Suite Structure (TSS)  

<|ref|>sub_title<|/ref|><|det|>[[115, 104, 336, 131]]<|/det|>
### 3.1 Test Strategy  

<|ref|>text<|/ref|><|det|>[[115, 138, 830, 172]]<|/det|>
The qualification of products claiming their compliance with the Bluetooth specification involves the execution of Test Suites.  

<|ref|>text<|/ref|><|det|>[[115, 178, 861, 234]]<|/det|>
In AVRCP, there are four AV/C commands to be applied to the AV/C command procedure: UNIT INFO, SUBUNIT INFO, PASS THROUGH, and VENDOR DEPENDENT commands. Note that the VENDOR DEPENDENT command is out of the scope of testing.  

<|ref|>sub_title<|/ref|><|det|>[[115, 252, 323, 272]]<|/det|>
### 3.2 Test groups  

<|ref|>title<|/ref|><|det|>[[115, 275, 400, 295]]<|/det|>
#### 3.2.1 First level test group  

<|ref|>text<|/ref|><|det|>[[115, 307, 848, 357]]<|/det|>
The first level defines the test groups following the Audio/Video Remote Control Profile procedure: Connection establishment for control, connection release for control and AV/C commands as defined in [2].  

<|ref|>text<|/ref|><|det|>[[115, 363, 840, 397]]<|/det|>
The AV/C commands are classified into two branches: information collection and PASS THROUGH command transfer.  

<|ref|>text<|/ref|><|det|>[[115, 400, 868, 435]]<|/det|>
Metadata Transfer conformance is verified in the following test groups: Configuration, Player Application Setting, Media Information, Notification, and Invalid Commands and Basic Group Navigation.  

<|ref|>title<|/ref|><|det|>[[115, 451, 428, 470]]<|/det|>
#### 3.2.2 Second level test group  

<|ref|>text<|/ref|><|det|>[[115, 478, 868, 511]]<|/det|>
The second level defines the test groups following the procedure to establish and release connection for control defined in [2] applicable to cases initiated from either CT or TG.  

<|ref|>text<|/ref|><|det|>[[115, 517, 812, 551]]<|/det|>
The second level also defines the test groups following AV/C commands used in [2]: UNIT INFO command and SUBUNIT INFO command.  

<|ref|>text<|/ref|><|det|>[[115, 554, 880, 605]]<|/det|>
In addition, in the test procedure for PASS THROUGH command transfer, operation_ids defined in [2] are tested. The operation_ids for vendor unique and function keys are out of scope in this specification, with the exception of the vendor_id specified for the Bluetooth SIG for purposes of Metadata transfer.  

<|ref|>title<|/ref|><|det|>[[115, 621, 319, 639]]<|/det|>
#### 3.2.3 Initialization  

<|ref|>text<|/ref|><|det|>[[115, 647, 893, 729]]<|/det|>
Before performing any test cases, an initialization procedure between CT and TG is performed to ensure that the devices have stored the information with which device they will interoperate while performing the AVRCP. As this procedure depends on the implementation and capabilities of the devices and is not part of the AVRCP specification, it is not covered by any test cases. For all test cases, it is assumed as a general precondition that this initialization has been performed for this pair of devices.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 72, 380, 97]]<|/det|>
## 4 Test cases (TC)  

<|ref|>sub_title<|/ref|><|det|>[[115, 102, 325, 140]]<|/det|>
### 4.1 Introduction  

<|ref|>sub_title<|/ref|><|det|>[[203, 144, 544, 162]]<|/det|>
## Test case identification conventions  

<|ref|>text<|/ref|><|det|>[[115, 170, 830, 202]]<|/det|>
Test cases are assigned unique identifiers per the conventions in [4]. The convention used here is: <spec abbreviation></IUT role></class></feat></func></subfunc></cap></xx></nn></y>.  

<|ref|>text<|/ref|><|det|>[[115, 209, 880, 260]]<|/det|>
Additionally, testing of this specification includes tests from the SDP Test Suite [13] referred to as Generic SDP Integrated Tests (GSIT); when used, the GSIT tests are referred to through a TCID string using the following convention:  

<|ref|>text<|/ref|><|det|>[[115, 261, 732, 277]]<|/det|>
<spec abbreviation></IUT role></GSIT test group></ GSIT class></xx></nn></y>.  

<|ref|>table<|/ref|><|det|>[[114, 281, 863, 927]]<|/det|>

<table><tr><td>Identifier Abbreviation</td><td>Spec Identifier &lt;spec abbreviation&gt;</td></tr><tr><td>AVRCP</td><td>Audio/Video Remote Control Profile</td></tr><tr><td>Identifier Abbreviation</td><td>Role Identifier &lt;IUT role&gt;</td></tr><tr><td>CT</td><td>Controller Role</td></tr><tr><td>TG</td><td>Target Role</td></tr><tr><td>Identifier Abbreviation</td><td>Reference Identifier &lt;GSIT test group&gt;</td></tr><tr><td>-CGSIT</td><td>Client Generic SDP Integrated Tests</td></tr><tr><td>-SGSIT</td><td>Server Generic SDP Integrated Tests</td></tr><tr><td>Identifier Abbreviation</td><td>Reference Identifier &lt;GSIT class&gt;</td></tr><tr><td>ATTR</td><td>Attribute</td></tr><tr><td>OFFS</td><td>Attribute ID Offset String</td></tr><tr><td>SERR</td><td>Service Record</td></tr><tr><td>SFC</td><td>SDP Future Compatibility</td></tr><tr><td>Identifier Abbreviation</td><td></td></tr><tr><td>BGN</td><td>Feature Identifier &lt;feat&gt;</td></tr><tr><td>CA</td><td>Basic Group Navigation</td></tr><tr><td>CEC</td><td>Cover Art</td></tr><tr><td>CFG</td><td>Connection Establishment for Control</td></tr><tr><td>CON</td><td>Configuration Commands of Metadata Transfer</td></tr><tr><td>CRC</td><td>Connection Establishment and Release for Browsing</td></tr><tr><td>ICC</td><td>Connection Release for Control</td></tr><tr><td>INV</td><td>Information Collection for Control</td></tr><tr><td>MCN</td><td>Invalid Commands</td></tr><tr><td>MDI</td><td>Media Content Navigation</td></tr><tr><td>MPS</td><td>Media Information Commands of Metadata Transfer</td></tr><tr><td>NFY</td><td>Media Player Selection</td></tr><tr><td>PAS</td><td>Notification Commands of Metadata Transfer</td></tr><tr><td>PTH</td><td>Player Application Setting Commands</td></tr><tr><td>PTT</td><td>PASS THROUGH Handling</td></tr><tr><td>RCR</td><td>PASS THROUGH Transfer</td></tr><tr><td>VLH</td><td>Continuation PDU Commands (Request Continuing Response)</td></tr><tr><td></td><td>Volume Level Handling</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[115, 71, 861, 156]]<|/det|>

<table><tr><td>Identifier Abbreviation</td><td>Function Identifier &lt;func&gt;</td></tr><tr><td>CB NP SRC</td><td>Content Browsing function</td></tr><tr><td></td><td>NowPlaying function</td></tr><tr><td></td><td>Search function</td></tr></table>

<|ref|>table_caption<|/ref|><|det|>[[115, 164, 448, 176]]<|/det|>
Table 4.1: AVRCP TC feature naming conventions

<|ref|>title<|/ref|><|det|>[[115, 192, 334, 205]]<|/det|>
# 4.1.2 Conformance

<|ref|>text<|/ref|><|det|>[[115, 217, 841, 262]]<|/det|>
When conformance is claimed for a particular specification, all capabilities are to be supported in the specified manner. The mandated tests from this Test Suite depend on the capabilities to which conformance is claimed.

<|ref|>text<|/ref|><|det|>[[115, 274, 877, 320]]<|/det|>
The Bluetooth Qualification Program may employ tests to verify implementation robustness. The level of implementation robustness that is verified varies from one specification to another and may be revised for cause based on interoperability issues found in the market.

<|ref|>text<|/ref|><|det|>[[115, 333, 279, 345]]<|/det|>
Such tests may verify:

<|ref|>text<|/ref|><|det|>[[115, 359, 877, 388]]<|/det|>
· That claimed capabilities may be used in any order and any number of repetitions not excluded by the specification

<|ref|>text<|/ref|><|det|>[[115, 393, 859, 422]]<|/det|>
· That capabilities enabled by the implementations are sustained over durations expected by the use case

<|ref|>text<|/ref|><|det|>[[115, 428, 793, 443]]<|/det|>
That the implementation gracefully handles any quantity of data expected by the use case

<|ref|>text<|/ref|><|det|>[[115, 450, 870, 480]]<|/det|>
· That in cases where more than one valid interpretation of the specification exists, the implementation complies with at least one interpretation and gracefully handles other interpretations

<|ref|>text<|/ref|><|det|>[[144, 490, 616, 503]]<|/det|>
That the implementation is immune to attempted security exploits

<|ref|>text<|/ref|><|det|>[[115, 516, 128, 525]]<|/det|>
·

<|ref|>text<|/ref|><|det|>[[115, 540, 846, 585]]<|/det|>
A single execution of each of the required tests is required to constitute a Pass verdict. However, it is noted that to provide a foundation for interoperability, it is necessary that a qualified implementation consistently and repeatedly pass any of the applicable tests.

<|ref|>text<|/ref|><|det|>[[115, 596, 850, 656]]<|/det|>
In any case, where a member finds an issue with the test plan generated by the Bluetooth SIG qualification tool, with the test case as described in the Test Suite, or with the test system utilized, the member is required to notify the responsible party via an erratum request such that the issue may be addressed.

<|ref|>title<|/ref|><|det|>[[115, 656, 163, 668]]<|/det|>
# 4.1.3

<|ref|>title<|/ref|><|det|>[[203, 677, 448, 690]]<|/det|>
# Other general information

<|ref|>text<|/ref|><|det|>[[115, 702, 486, 714]]<|/det|>
Only one point-to-point configuration is considered.

<|ref|>text<|/ref|><|det|>[[115, 725, 866, 754]]<|/det|>
All TG AV/C transactions are confirmed to comply with the time periods specified in Section 6.2, Timers,in [2]. Failure of the TG IUT to meet the time periods results in a Fail verdict assigned for the TG IUT.

<|ref|>title<|/ref|><|det|>[[115, 771, 483, 784]]<|/det|>
# 4.1.4 Pass/Fail verdict conventions

<|ref|>text<|/ref|><|det|>[[115, 797, 836, 825]]<|/det|>
Each test case has an Expected Outcome section. The IUT is granted the Pass verdict when all the detailed pass criteria conditions within the Expected Outcome section are met.

<|ref|>text<|/ref|><|det|>[[115, 837, 875, 883]]<|/det|>
The convention in this Test Suite is that, unless there is a specific set of fail conditions outlined in the test case, the IUT fails the test case as soon as one of the pass criteria conditions cannot be met. If this occurs, then the outcome of the test is a Fail verdict.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[70, 123, 380, 150]]<|/det|>
## 4.2 Generic SDP Integrated Tests  

<|ref|>sub_title<|/ref|><|det|>[[70, 156, 405, 183]]<|/det|>
### 4.2.1 Server Generic SDP Integrated Tests  

<|ref|>title<|/ref|><|det|>[[70, 196, 176, 216]]<|/det|>
#### 4.2.1.1 Controller  

<|ref|>text<|/ref|><|det|>[[70, 217, 840, 241]]<|/det|>
Execute the Generic SDP Integrated Tests defined in Section 6.3, Server test procedures (SGSIT), in [13] using Table 4.2 below as input:  

<|ref|>table<|/ref|><|det|>[[68, 258, 930, 750]]<|/det|>

<table><tr><td>TCID</td><td>Reference</td><td>Attribute ID Name</td><td>Attribute ID definition source (Universal, Profile)</td><td>Value/Secondary Value</td><td>Attribute presence (Present/Present for [role], Optionally present, TCMT defined)</td></tr><tr><td>AVRCP/CT/SGSIT/SERR/BV-01-C [Service record GSIT – AVRCP CT]</td><td>[2] 8</td><td>ServiceClassIDList</td><td>Universal</td><td>“A/V Remote Control” (UUID), “A/V Remote Control Controller” (UUID)</td><td>Present for CT</td></tr><tr><td>AVRCP/CT/SGSIT/ATTR/BV-01-C [Attribute GSIT – Protocol Descriptor List]</td><td>[2] 8</td><td>ProtocolDescriptorList</td><td>Universal</td><td>“L2CAP” (UUID): PSM – “AVCTP” (Uint16), “AVCTP” (UUID): Version – “0x0104” (Uint16)</td><td>Present for CT</td></tr><tr><td>AVRCP/CT/SGSIT/ATTRIB/BV-02-C [Attribute GSIT – Additional Protocol Descriptor Lists, Browsing Channel]</td><td>[2] 8</td><td>AdditionalProtocolDescriptorLists</td><td>Universal</td><td>“L2CAP” (UUID): PSM – “AVCTBrowsing” (Uint16), “AVCTP” (UUID): Version – “0x1014” (Uint16)</td><td>TCMT defined</td></tr><tr><td>AVRCP/CT/SGSIT/ATTR/BV-03-C [Attribute GSIT – Bluetooth Profile Descriptor List, AVRCP 1.5]</td><td>[2] 8</td><td>BluetoothProfileDescriptorList</td><td>Universal</td><td>“A/V Remote Control” (UUID): Version – “0x0105” (Uint16)</td><td>TCMT defined</td></tr><tr><td>AVRCP/C/T/SGSIT/ATTR/BV-04-C [Attribute GSIT – Bluetooth Profile Descriptor List, AVRCP 1.6]</td><td>[2] 8</td><td>BluetoothProfileDescriptorList</td><td>Universal</td><td rowspan="2">“A/V Remote Control” (UUID): Version – “0x0106” (Uint16)</td><td rowspan="2">TCMT defined</td></tr><tr><td>AVRCP/CT/SGSIT/ATTR/AVP-05-C [Attribute GSIT – Supported Features]</td><td>[2] 8</td><td>Supported Features</td><td>Profile</td></tr></table>

<|ref|>table_footnote<|/ref|><|det|>[[71, 755, 380, 775]]<|/det|>
Table 4.2: Input for the Controller SGSIT SDP test procedure=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>title<|/ref|><|det|>[[70, 116, 155, 133]]<|/det|>
#### 4.2.1.2 Target  

<|ref|>text<|/ref|><|det|>[[75, 136, 840, 159]]<|/det|>
Execute the Generic SDP Integrated Tests defined in Section 6.3, Server test procedures (SGSIT), in [13] using Table 4.3 below as input:  

<|ref|>table<|/ref|><|det|>[[70, 175, 930, 710]]<|/det|>
<|ref|>table_caption<|/ref|><|det|>[[72, 714, 364, 733]]<|/det|>
Table 4.3: Input for the Target SGSIT SDP test procedure   

<table><tr><td>TCID</td><td>Reference</td><td>Attribute ID name</td><td>Attribute ID definition source (Universal, Profile)</td><td>Value/secondary value</td><td>Attribute presence (Present/Present for [role], Optionally present, TCMT defined)</td></tr><tr><td>AVRCP/TG/SGSIT/SERR/BV-01-C [Service record GSIT – AVRCP TG]</td><td>[2] 8</td><td>ServiceClassIDList</td><td>Universal</td><td>“A/V Remote Control Target” (UUID)</td><td>Present for TG</td></tr><tr><td>AVRCP/TG/SGSIT/ATTR/BV-01-C [Attribute GSIT – Protocol Descriptor List]</td><td>[2] 8</td><td>ProtocolDescriptorList</td><td>Universal</td><td>“L2CAP” (UUID): PSM – “AVCTP” (Uint16), “AVCTP” (UUID): Version – “0x0104” (Uint16)</td><td>Present for TG</td></tr><tr><td>AVRCP/TG/SGSIT/ATTRIBV-02-C [Attribute GSIT – Additional Protocol Descriptor Lists, Browsing Channel]</td><td>[2] 8</td><td>AdditionalProtocolDescriptorLists</td><td>Universal</td><td>“L2CAP” (UUID): PSM – “AVCTF_Browsing” (Uint16), “AVCTP” (UUID): Version – “0x1014” (Uint16)</td><td>TCMT defined</td></tr><tr><td>AVRCP/TG/SGSIT/ATTR/BV-03-C [Attribute GSIT – Additional Protocol Descriptor Lists, Cover Art]</td><td>[2] 8</td><td>AdditionalProtocolDescriptorLists</td><td>Universal</td><td></td><td>TCMT defined</td></tr><tr><td>AVRCP/TG/SGSIT/ATTRIBV-04-C [Attribute GSIT – Bluetooth Profile Descriptor List, AVRCP 1.5]</td><td>[2] 8</td><td>BluetoothProfileDescriptorList</td><td>Universal</td><td>“A/V Remote Control” (UUID): Version – “0x0105” (Uint16)</td><td>TCMT defined</td></tr><tr><td>AVRCP/TCG/SGSIT/ATTR/BV-05-C [Attribute GSIT – Bluetooth Profile Descriptor List, AVRCP 1.6]</td><td>[2] 8</td><td>BluetoothProfileDescriptorList</td><td>Universal</td><td rowspan="2">“A/V Remote Control” (UUID): Version – “0x0106” (Uint16)</td><td rowspan="2">TCMT defined</td></tr><tr><td>AVRCP/TG/SGSIT/ATTRB/V-06-C [Attribute GSIT – Supported Features]</td><td>[2] 8</td><td>Supported Features</td><td>Profile</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>title<|/ref|><|det|>[[70, 117, 525, 135]]<|/det|>
#### 4.2.1.3 Audio/Video Remote Control Profile - Attribute ID Offset String tests  

<|ref|>text<|/ref|><|det|>[[70, 137, 840, 160]]<|/det|>
Execute the Generic SDP Integrated Tests defined in Section 6.3, Server test procedures (SGSIT), in [13] using Table 4.4 below as input:  

<|ref|>table<|/ref|><|det|>[[68, 177, 928, 490]]<|/det|>

<table><tr><td>TCID</td><td>Reference</td><td>ServiceSearchPattern</td><td>Attribute ID name</td><td>Attribute ID Offset</td><td>Attribute presence (Present/Present for [role], Optionally present, TCMT defined)</td></tr><tr><td>AVRCP/CT/SGSIT/OFFS/BV-01-C [Attribute ID Offset String GSIT – Service Name]</td><td>[2] 8</td><td>A/V Remote Control Controller</td><td>ServiceName</td><td>0x0000</td><td>Optionally present</td></tr><tr><td>AVRCP/CT/SGSIT/OFFS/BV-02-C [Attribute ID Offset String GSIT – Provider Name]</td><td>[2] 8</td><td>A/V Remote Control Controller</td><td>ProviderName</td><td>0x0002</td><td>Optionally present</td></tr><tr><td>AVRCP/TG/SGSIT/OFFS/BV-03-C [Attribute ID Offset String GSIT – Service Name]</td><td>[2] 8&lt;fce&gt;A/V Remote Control Target</td><td>ServiceName</td><td>0x0000</td><td>Optionally present</td><td></td></tr><tr><td>AVRCP/TG/SGSIT/OFFS/BV-04-C [Attribute ID Offset String GSIT – Provider Name]</td><td>[2] 8&lt;fce&gt;A/V Remote ControlTarget</td><td>ProviderName</td><td>0x0002</td><td>Optionally present</td><td></td></tr></table><br><br><br></ce>  

<|ref|>text<|/ref|><|det|>[[71, 496, 561, 516]]<|/det|>
Table 4.4: Input for the Audio/Video Remote Control Profile SGSIT Attribute ID Offset String tests=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>title<|/ref|><|det|>[[70, 117, 402, 137]]<|/det|>
#### 4.2.2 Client Generic SDP Integrated Tests  

<|ref|>text<|/ref|><|det|>[[75, 147, 890, 170]]<|/det|>
Execute the Generic SDP Future Compatibility Tests defined in Section 6.4, Client test procedures (CGSIT), in [13] using Table 4.5 below as input:  

<|ref|>table<|/ref|><|det|>[[70, 179, 928, 462]]<|/det|>

<table><tr><td>TCID</td><td>Reference</td><td>Service Record Service Class UUID description</td><td>Lower Tester SDP record initial conditions</td></tr><tr><td>AVRCP/CT/CGSIT/SFC/BV-01-C [SDP Future Compatibility – IUT is AVRCP CT]</td><td>[2] 8</td><td>A/V Remote Control Target</td><td>The Lower Tester exposes an AVRCP TG SDP record.<br>The version in the Bluetooth Profile Descriptor List is greater than the most recently adopted version.<br>All bits are set in the supported features attribute, including RFU bits.<br>An A2DP SDP record is exposed if specified by IXIT [6], and an A2DP connection may also be established.</td></tr><tr><td>AVRCP/TG/CGSIT/SFC/BV-02-C [SDP Future Compatibility – IUT is AVRCP TG]</td><td>[2] 8</td><td>A/V Remote Control, A/V Remote Control Controller</td><td>The Lower Tester exposes an AVRCP CT SDP record.<br>The version in the Bluetooth Profile Descriptor List is greater than the most Recently adopted version.<br>All bits are set in the supported features attribute, including RFU bits. An A2DP SDP record is exposed if specified by IXIT [6], and an A1DP connection may also be established.</td></tr></table>

<|ref|>table_footnote<|/ref|><|det|>[[72, 468, 411, 487]]<|/det|>
Table 4.5: Input for the Client CGSIT SDP future compatibility tests=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 77, 629, 98]]<|/det|>
### 4.3 Connection Establishment for Browsing  

<|ref|>text<|/ref|><|det|>[[115, 103, 595, 120]]<|/det|>
Verify the procedure of establishing the AVCTP browsing channel.  

<|ref|>sub_title<|/ref|><|det|>[[115, 134, 732, 153]]<|/det|>
## AVRCP/CT/CON/BV-01-C [Connection establishment for browsing - CT]  

<|ref|>text<|/ref|><|det|>[[115, 161, 639, 203]]<|/det|>
- Test PurposeVerify the connection establishment for browsing initiated by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 211, 230, 250]]<|/det|>
- Reference [5], [8] 4.1.1  

<|ref|>text<|/ref|><|det|>[[115, 260, 260, 275]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 286, 864, 377]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- No AVCTP connection is established between the IUT and the Lower Tester.- The IUT is acting as AVRCP CT role in category 1.- The IUT has performed an SDP query with the Lower Tester exposing AVRCP browse support.  

<|ref|>text<|/ref|><|det|>[[115, 387, 260, 403]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 410, 652, 428]]<|/det|>
The Upper Tester triggers the IUT to establish an AVRCP connection.  

<|ref|>image<|/ref|><|det|>[[146, 434, 714, 701]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 710, 732, 725]]<|/det|>
<center>Figure 4.1: AVRCP/CT/CON/BV-01-C [Connection establishment for browsing - CTJ MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 740, 287, 780]]<|/det|>
- Expected OutcomePass verdict  

<|ref|>text<|/ref|><|det|>[[144, 788, 879, 820]]<|/det|>
The IUT initiates the establishment of the AVCTP control channel and immediately afterwards the IUT initiates the establishment of the AVCTP browsing channel.  

<|ref|>sub_title<|/ref|><|det|>[[115, 836, 732, 855]]<|/det|>
## AVRCP/TG/CON/BV-02-C [Connection establishment for browsing - TG]  

<|ref|>text<|/ref|><|det|>[[115, 864, 245, 879]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 887, 866, 920]]<|/det|>
Verify the connection establishment for the control channel and the browsing channel, both initiated by the TG.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 223, 88]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 97, 233, 114]]<|/det|>
[5], [8] 4.1.1  

<|ref|>text<|/ref|><|det|>[[115, 123, 260, 139]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 147, 863, 237]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- No AVCTP connection is established between the IUT and the Lower Tester.- The IUT is acting as AVRCP TG role in category 1.- The IUT has performed an SDP query with the Lower Tester exposing AVRCP browse support.  

<|ref|>text<|/ref|><|det|>[[115, 248, 260, 264]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 271, 650, 288]]<|/det|>
The Upper Tester triggers the IUT to establish an AVRCP connection.  

<|ref|>image<|/ref|><|det|>[[144, 295, 707, 562]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 570, 733, 586]]<|/det|>
<center>Figure 4.2: AVRCP/TG/CON/BV-02-C [Connection establishment for browsing – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 601, 285, 640]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 648, 879, 681]]<|/det|>
The IUT initiates the establishment of the AVCTP control channel and immediately afterwards the IUT initiates the establishment of the AVCTP browsing channel.  

<|ref|>sub_title<|/ref|><|det|>[[115, 697, 867, 730]]<|/det|>
## AVRCP/TG/CON/BV-05-C [Connection establishment for browsing – TG initiates control channel and CT initiates browsing channel]  

<|ref|>text<|/ref|><|det|>[[115, 740, 245, 755]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 763, 879, 796]]<|/det|>
Verify the connection establishment for browsing channel initiated by the CT after the TG has initiated the control channel establishment.  

<|ref|>text<|/ref|><|det|>[[115, 802, 228, 817]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 825, 233, 840]]<|/det|>
[5], [8] 4.1.1  

<|ref|>text<|/ref|>造成 Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 882, 731, 923]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- No AVRCP connection is established between the IUT and the Lower Tester.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[144, 70, 545, 87]]<|/det|>
- The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 94, 861, 111]]<|/det|>
- The IUT has performed an SDP query with the Lower Tester exposing AVRCP browse support.  

<|ref|>text<|/ref|><|det|>[[116, 122, 260, 137]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 145, 850, 196]]<|/det|>
1. The Upper Tester triggers the IUT to initiate establishment of an AVCTP control channel.  
2. Upon receipt of control channel establishment signaling from the IUT the Lower Tester initiates the establishment of an AVCTP browsing channel with the IUT.  

<|ref|>image<|/ref|><|det|>[[147, 204, 700, 469]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 476, 880, 504]]<|/det|>
<center>Figure 4.3: AVRCP/TG/CON/BV-05-C [Connection establishment for browsing – TG initiates control channel and CT initiates browsing channel] MSC </center>  

<|ref|>text<|/ref|><|det|>[[116, 521, 287, 537]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[145, 546, 238, 561]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[145, 568, 622, 585]]<|/det|>
The IUT initiates the establishment of the AVCTP control channel.  

<|ref|>text<|/ref|><|det|>[[144, 592, 825, 625]]<|/det|>
The IUT successfully responds to the Lower Tester initiation to establish the AVCTP browsing channel.  

<|ref|>text<|/ref|><|det|>[[145, 629, 844, 696]]<|/det|>
In the alternative scenario where the IUT supports browsing channel initiation and immediately initiates the browsing channel establishment following the control channel establishment, the IUT successfully responds to the Lower Tester's request to initiate the browsing channel release and subsequently allows the Lower Tester to initiate the AVCTP browsing channel establishment.  

<|ref|>sub_title<|/ref|><|det|>[[115, 715, 559, 735]]<|/det|>
### 4.4 Connection Release for Browsing  

<|ref|>text<|/ref|><|det|>[[115, 742, 575, 758]]<|/det|>
Verify the procedure of releasing the AVCTP browsing channel.  

<|ref|>sub_title<|/ref|><|det|>[[115, 772, 671, 790]]<|/det|>
## AVRCP/CT/CON/BV-03-C [Connection release for browsing – CT]  

<|ref|>text<|/ref|><|det|>[[115, 800, 591, 841]]<|/det|>
- Test PurposeVerify the connection release for browsing initiated by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 851, 231, 891]]<|/det|>
- Reference[5], [8] 4.1.2=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 96, 679, 161]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the Lower Tester.- An AVCTP Control and an AVCTP Browsing channel are established.- The IUT is acting as AVRCP CT role in category 1.  

<|ref|>text<|/ref|><|det|>[[115, 172, 260, 188]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 195, 644, 212]]<|/det|>
The Upper Tester triggers the IUT to release the AVRCP connection.  

<|ref|>image<|/ref|><|det|>[[146, 220, 696, 486]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 495, 690, 510]]<|/det|>
<center>Figure 4.4: AVRCP/CT/CON/BV-03-C [Connection release for browsing – CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 526, 287, 566]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 574, 850, 606]]<|/det|>
The IUT initiates the release of the AVCTP browsing channel and immediately afterwards the IUT initiates the release of the AVCTP control channel.  

<|ref|>sub_title<|/ref|><|det|>[[115, 621, 675, 640]]<|/det|>
## AVRCP/TG/CON/BV-04-C [Connection release for browsing – TG]  

<|ref|>text<|/ref|><|det|>[[115, 649, 592, 690]]<|/det|>
Test PurposeVerify the connection release for browsing initiated by the TG.  

<|ref|>text<|/ref|><|det|>[[115, 699, 256, 740]]<|/det|>
Reference [5], [8] 4.1.2  

<|ref|>text<|/ref|><|det|>[[115, 748, 260, 763]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 774, 679, 840]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the Lower Tester.  - An AVCTP Control and an AVCTP Browsing channel are established.  - The IUT is acting as AVRCP TG role in category 1.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 644, 113]]<|/det|>
The Upper Tester triggers the IUT to release the AVRCP connection.  

<|ref|>image<|/ref|><|det|>[[152, 121, 707, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 395, 692, 411]]<|/det|>
<center>Figure 4.5: AVRCP/TG/CON/BV-04-C [Connection release for browsing – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 426, 287, 442]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 451, 237, 467]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[143, 474, 850, 507]]<|/det|>
The IUT initiates the release of the AVCtP browsing channel and immediately afterwards the IUT initiates the release of the AVCtP control channel.  

<|ref|>sub_title<|/ref|><|det|>[[115, 520, 763, 543]]<|/det|>
### 4.5 Media Player Selection Commands and Notifications  

<|ref|>text<|/ref|><|det|>[[115, 548, 668, 565]]<|/det|>
Verify the commands and notifications related to Selection of Media Players.  

<|ref|>sub_title<|/ref|><|det|>[[115, 578, 567, 597]]<|/det|>
## AVRCP/CT/MPS/BV-01-C [SetAddressedPlayer - CT]  

<|ref|>text<|/ref|><|det|>[[115, 606, 577, 648]]<|/det|>
- Test PurposeVerify the SetAddressedPlayer command issued by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 657, 230, 697]]<|/det|>
- Reference [5], [8] 6.9.1  

<|ref|>text<|/ref|><|det|>[[115, 705, 260, 721]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 730, 801, 850]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCtP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP CT role in category 1.- Available Playerdls have to be provided to the IUT. This can be achieved by executing AVRCP/CT/MPS/BV-08-C [GetFolderltems - CT].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 598, 113]]<|/det|>
The Upper Tester triggers the IUT to set the addressed player.  

<|ref|>image<|/ref|><|det|>[[144, 121, 700, 396]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 403, 612, 419]]<|/det|>
<center>Figure 4.6: AVRCP/CT/MPS/BV-01-C [SetAddressedPlayer - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 433, 285, 450]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 459, 238, 474]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 481, 865, 498]]<|/det|>
The IUT issues a SetAddressedPlayer command with Parameter Length \(= 0x2\) and a valid PlayerId.  

<|ref|>sub_title<|/ref|><|det|>[[113, 513, 568, 532]]<|/det|>
## AVRCP/TG/MPS/BV-02-C [SetAddressedPlayer - TG]  

<|ref|>text<|/ref|><|det|>[[115, 541, 574, 583]]<|/det|>
Test PurposeVerify the SetAddressedPlayer response issued by the TG.  

<|ref|>text<|/ref|><|det|>[[115, 592, 228, 630]]<|/det|>
Reference [5], [8] 6.9.1  

<|ref|>text<|/ref|><|det|>[[115, 640, 260, 655]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 666, 875, 784]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester has retrieved the valid PlayerIds of the IUT. This can be retrieved by executing AVRCP/TG/MPS/BV-09-C [GetFolderltems - TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 842, 114]]<|/det|>
The Lower Tester sends a SetAddressedPlayer command containing a valid PlayerId to the IUT.  

<|ref|>image<|/ref|><|det|>[[155, 120, 707, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 395, 614, 411]]<|/det|>
<center>Figure 4.7: AVRCP/TG/MPS/BV-02-C [SetAddressedPlayer - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 425, 686, 491]]<|/det|>
Expected Outcome  Pass verdict  The IUT responds with a valid status field indicating that no error occurred.  

<|ref|>sub_title<|/ref|><|det|>[[115, 505, 550, 524]]<|/det|>
## AVRCP/CT/MPS/BV-03-C [SetBrowsedPlayer - CT]  

<|ref|>text<|/ref|><|det|>[[115, 532, 563, 575]]<|/det|>
Test Purpose  Verify the SetBrowsedPlayer command issued by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 584, 255, 625]]<|/det|>
Reference [5], [8] 6.9.3  

<|ref|>text<|/ref|><|det|>[[115, 632, 260, 648]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 658, 866, 777]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP CT role in category 1.- The IUT has retrieved the list of available players on the Lower Tester. This can be achieved by executing AVRCP/CT/MPS/BV-08-C [GetFolderItems - CT].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 720, 114]]<|/det|>
The Upper Tester triggers the IUT to set the browsed player to a valid PlayerID.  

<|ref|>image<|/ref|><|det|>[[152, 121, 700, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 395, 600, 412]]<|/det|>
<center>Figure 4.8: AVRCP/CT/MPS/BV-03-C [SetBrowsedPlayer - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 426, 640, 491]]<|/det|>
Expected Outcome Pass verdict The IUT issues a SetBrowsedPlayer command with a valid PlayerId.  

<|ref|>sub_title<|/ref|><|det|>[[115, 505, 551, 524]]<|/det|>
## AVRCP/TG/MPS/BV-04-C [SetBrowsedPlayer - TG]  

<|ref|>text<|/ref|><|det|>[[115, 533, 560, 576]]<|/det|>
Test Purpose Verify the SetBrowsedPlayer response issued by the TG.  

<|ref|>text<|/ref|><|det|>[[115, 585, 252, 626]]<|/det|>
Reference [5], [8] 6.9.3  

<|ref|>text<|/ref|><|det|>[[115, 633, 260, 648]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 659, 875, 777]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester has retrieved the valid PlayerIds of the IUT. This can be retrieved by executing AVRCP/TG/MPS/BV- 09- C [GetFolderltems - TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 97, 670, 113]]<|/det|>
The Lower Tester sends a valid SetBrowsedPlayer command to the IUT.  

<|ref|>image<|/ref|><|det|>[[152, 121, 699, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 395, 601, 411]]<|/det|>
<center>Figure 4.9: AVRCP/TG/MPS/BV-04-C [SetBrowsedPlayer - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 426, 287, 442]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 451, 238, 466]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 474, 866, 522]]<|/det|>
The IUT responds with a valid Status field in the SetBrowsedPlayer response. The fields UID Counter, Number of Items, Character Set Id, Folder Depth, Folder Name Size and Folder Name are correctly formatted reflecting the current folder.  

<|ref|>sub_title<|/ref|><|det|>[[115, 538, 719, 557]]<|/det|>
## AVRCP/TG/MPS/BV-05-C [AddressedPlayerChanged notification - TG]  

<|ref|>text<|/ref|><|det|>[[115, 567, 245, 582]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 589, 864, 622]]<|/det|>
Verify the AddressedPlayerChanged Notification issued by the TG and the procedure associated to this.  

<|ref|>text<|/ref|><|det|>[[115, 627, 223, 642]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 650, 234, 666]]<|/det|>
[5], [8] 6.9.2  

<|ref|>text<|/ref|><|det|>[[115, 675, 260, 690]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 707, 800, 812]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester. The AVCTP control and browsing channels between the IUT and the Lower Tester are established. The IUT is acting as AVRCP TG role in category 1. At least one player specific notification is registered with the IUT.  

<|ref|>text<|/ref|><|det|>[[115, 826, 260, 841]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 849, 752, 884]]<|/det|>
1. The Lower Tester sends a RegisterNotificationCommand to the IUT to register for AddressedPlayerChanged.  

<|ref|>text<|/ref|><|det|>[[140, 884, 850, 917]]<|/det|>
2. The Upper Tester subsequently triggers a change of addressed player in the IUT by selecting a new Addressed Player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[145, 70, 712, 337]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 344, 734, 360]]<|/det|>
<center>Figure 4.10: AVRCP/TG/MPS/BV-05-C [AddressedPlayerChanged notification – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 375, 286, 391]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 400, 238, 415]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 422, 880, 456]]<|/det|>
The IUT issues a correctly AddressedPlayerChanged notification final response with the correct value of PlayerId and UID Counter for the Player selected by the Upper Tester.  

<|ref|>text<|/ref|><|det|>[[144, 459, 682, 476]]<|/det|>
The IUT completes all player specific notifications with AV/C type rejected.  

<|ref|>sub_title<|/ref|><|det|>[[115, 496, 582, 514]]<|/det|>
## AVRCP/TG/MPS/BV-06-C [PlayerFeatureBitmask - TG]  

<|ref|>text<|/ref|><|det|>[[115, 523, 512, 565]]<|/det|>
- Test PurposeVerify the PlayerFeatureBitmask issued by the TG.  

<|ref|>text<|/ref|><|det|>[[115, 574, 256, 614]]<|/det|>
- Reference[5], [8] 6.10.2.1  

<|ref|>text<|/ref|><|det|>[[115, 623, 260, 638]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 648, 802, 750]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- There is an IXIT feature list for each Media Player application on the TG [6].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 97, 610, 113]]<|/det|>
The Lower Tester sends a GetFolderltems command to the IUT.  

<|ref|>image<|/ref|><|det|>[[152, 120, 707, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 395, 633, 411]]<|/det|>
<center>Figure 4.11: AVRCP/TG/MPS/BV-06-C [PlayerFeatureBitmask - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 426, 285, 442]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 451, 238, 466]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 474, 870, 507]]<|/det|>
The features announced in each Media Player's feature bitmask are according to the Media Player's IXIT entry.  

<|ref|>sub_title<|/ref|><|det|>[[115, 521, 715, 541]]<|/det|>
## AVRCP/TG/MPS/BV-07-C [AvailablePlayersChanged notification - TG]  

<|ref|>text<|/ref|><|det|>[[115, 549, 625, 591]]<|/det|>
- Test PurposeVerify the AvailablePlayersChanged Notification issued by the TG.  

<|ref|>text<|/ref|><|det|>[[115, 600, 234, 640]]<|/det|>
- Reference [5], [8] 6.9.4  

<|ref|>text<|/ref|><|det|>[[115, 648, 260, 664]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 674, 802, 755]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[115, 768, 260, 784]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 792, 752, 844]]<|/det|>
1. The Lower Tester sends a RegisterNotificationCommand to the IUT to register for AvailablePlayersChanged.  
2. The Upper Tester subsequently triggers a change of available players in the IUT.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[145, 70, 714, 343]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 352, 733, 368]]<|/det|>
<center>Figure 4.12: AVRCP/TG/MPS/BV-07-C [AvailablePlayersChanged Notification – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 382, 795, 448]]<|/det|>
- Expected OutcomePass verdictThe IUT issues a correctly formatted AvailablePlayersChanged notification final response.  

<|ref|>sub_title<|/ref|><|det|>[[115, 462, 525, 481]]<|/det|>
## AVRCP/CT/MPS/BV-08-C [GetFolderltems - CT]  

<|ref|>text<|/ref|><|det|>[[115, 490, 722, 533]]<|/det|>
- Test PurposeVerify the GetFolderltems command issued by the CT on the Media Player List.  

<|ref|>text<|/ref|><|det|>[[115, 541, 258, 581]]<|/det|>
- Reference [5], [8] 6.10.4.2  

<|ref|>text<|/ref|><|det|>[[115, 590, 260, 605]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 616, 802, 695]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP CT role in category 1.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 620, 113]]<|/det|>
The Upper Tester triggers the IUT to retrieve the MediaPlayerList.  

<|ref|>image<|/ref|><|det|>[[144, 121, 714, 396]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 403, 588, 419]]<|/det|>
<center>Figure 4.13: AVRCP/CT/MPS/BV-08-C [GetFolderItems - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 434, 285, 450]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 459, 238, 474]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 481, 870, 514]]<|/det|>
The IUT issues a GetFolderItems command with the scope of MediaPlayerList and valid parameters for StartItem, EndItem, AttributeCount and AttributeList.  

<|ref|>sub_title<|/ref|><|det|>[[115, 530, 525, 549]]<|/det|>
## AVRCP/TG/MPS/BV-09-C [GetFolderItems - TG]  

<|ref|>text<|/ref|><|det|>[[115, 558, 245, 573]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 581, 716, 598]]<|/det|>
Verify the GetFolderItems response for the Media Player List issued by the TG.  

<|ref|>text<|/ref|><|det|>[[115, 608, 225, 623]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 631, 256, 648]]<|/det|>
[5], [8] 6.10.4.2  

<|ref|>text<|/ref|><|det|>[[115, 657, 260, 672]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 683, 656, 700]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 707, 800, 740]]<|/det|>
- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 743, 543, 760]]<|/det|>
- The IUT is acting as AVRCP TG role in category 1.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[116, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 97, 878, 145]]<|/det|>
The Lower Tester sends a valid GetFolderltems command to the IUT to retrieve the MediaPlayerList. The command contains the MediaPlayerList as Scope parameter and valid entries for Start Item, End Item, AttributeCount and AttributeList.  

<|ref|>image<|/ref|><|det|>[[144, 155, 707, 428]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 436, 590, 452]]<|/det|>
<center>Figure 4.14: AVRCP/TG/MPS/BV-09-C [GetFolderltems - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 467, 285, 483]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 492, 238, 507]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 515, 864, 548]]<|/det|>
The IUT responds with a correctly formatted list of available Media Player Items with correct entries for each field in each Media Player Item.  

<|ref|>sub_title<|/ref|><|det|>[[115, 563, 601, 581]]<|/det|>
## AVRCP/TG/MPS/BV-10-C [DefaultAddressedPlayer - TG]  

<|ref|>text<|/ref|><|det|>[[115, 590, 490, 655]]<|/det|>
Test Purpose Verify the Default Addressed Player on the TG. Reference [5], [8] 6.9  

<|ref|>text<|/ref|><|det|>[[144, 664, 220, 680]]<|/det|>
[5], [8] 6.9  

<|ref|>text<|/ref|><|det|>[[115, 690, 260, 705]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 716, 802, 818]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- No SetAddressedPlayer command has been executed before.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 96, 864, 129]]<|/det|>
The Lower Tester send the PASS THROUGH commands for Play pushed and Play released to the IUT.  

<|ref|>image<|/ref|><|det|>[[150, 138, 707, 410]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 420, 647, 436]]<|/det|>
<center>Figure 4.15: AVRCP/TG/MPS/BV-10-C [DefaultAddressedPlayer - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 451, 287, 490]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 497, 839, 515]]<|/det|>
The IUT responds with valid PASS THROUGH responses indicating success and starts playing.  

<|ref|>sub_title<|/ref|><|det|>[[115, 529, 600, 549]]<|/det|>
## AVRCP/CT/MPS/BV-11-C [GetTotalNumberOftems - CT]  

<|ref|>text<|/ref|><|det|>[[115, 557, 245, 573]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 581, 875, 599]]<|/det|>
Verify the GetTotalNumberOftems command issued by the IUT (CT) for the Media Player List scope.  

<|ref|>text<|/ref|><|det|>[[115, 608, 225, 624]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 631, 230, 647]]<|/det|>
[8] 6.10.4.4  

<|ref|>text<|/ref|><|det|>[[115, 656, 260, 672]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 682, 860, 748]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP CT role in category 1.  

<|ref|>text<|/ref|><|det|>[[115, 759, 260, 775]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 783, 840, 816]]<|/det|>
1. The Upper Tester triggers the IUT to issue a GetTotalNumberOftems command to the Lower Tester with the scope parameter set to Media Player List.  

<|ref|>text<|/ref|><|det|>[[142, 817, 847, 850]]<|/det|>
2. Upon receipt of a GetTotalNumberOftems command from the IUT, the Lower Tester issues an appropriate GetTotalNumberOftems response message.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[144, 70, 699, 338]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 345, 647, 361]]<|/det|>
<center>Figure 4.16: AVRCP/CT/MPS/BV-11-C [GetTotalNumberOftems - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 375, 287, 414]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 421, 864, 455]]<|/det|>
The IUT issues a GetTotalNumberOftems command to the Lower Tester with the scope parameter set to Media Player List.  

<|ref|>sub_title<|/ref|><|det|>[[115, 471, 601, 490]]<|/det|>
## AVRCP/TG/MPS/BV-12-C [GetTotalNumberOftems - TG]  

<|ref|>text<|/ref|><|det|>[[115, 499, 245, 515]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 522, 875, 556]]<|/det|>
Verify that the IUT (TG) correctly responds to the GetTotalNumberOftems command issued from the CT for the Media Player List scope.  

<|ref|>text<|/ref|><|det|>[[115, 560, 225, 576]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 584, 230, 599]]<|/det|>
[8] 6.10.4.4  

<|ref|>text<|/ref|><|det|>[[115, 608, 259, 623]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 640, 661, 657]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 665, 860, 682]]<|/det|>
- AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 689, 545, 705]]<|/det|>
- The IUT is acting as AVRCP TG role in category 1.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 96, 864, 130]]<|/det|>
The Lower Tester issues a GetTotalNumberOfftemms command to the IUT with the scope parameter set to Media Player List.  

<|ref|>image<|/ref|><|det|>[[144, 137, 700, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 412, 648, 428]]<|/det|>
<center>Figure 4.17: AVRCP/TG/MPS/BV-12-C [GetTotalNumberOfftemms - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 443, 285, 459]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 467, 238, 483]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 490, 850, 507]]<|/det|>
The IUT issues a well- formatted GetTotalNumberOfftemms response message to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 514, 850, 547]]<|/det|>
The GetTotalNumberOfftemms response message indicates the correct number of available media players.  

<|ref|>text<|/ref|><|det|>[[143, 550, 875, 585]]<|/det|>
The total number of items returned by the IUT is the correct number for the current folder as specified in the IXIT [6].  

<|ref|>sub_title<|/ref|><|det|>[[115, 604, 561, 622]]<|/det|>
## AVRCP/TG/MPS/BI-01-C [SetAddressedPlayer - TG]  

<|ref|>text<|/ref|><|det|>[[115, 631, 245, 647]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 655, 832, 673]]<|/det|>
Verify the SetAddressedPlayer response issued by the TG when an invalid player is requested.  

<|ref|>text<|/ref|><|det|>[[115, 682, 225, 722]]<|/det|>
Reference [5], [8] 6.9.1  

<|ref|>text<|/ref|><|det|>[[115, 731, 260, 746]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 757, 875, 875]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester has retrieved the valid Playrelds of the IUT. This can be retrieved by executing AVRCP/TG/MPS/BV-09-C [GetFolderltems - TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 821, 114]]<|/det|>
The Lower Tester sends a SetAddressedPlayer command to the IUT with an invalid PlayerID.  

<|ref|>image<|/ref|><|det|>[[144, 121, 707, 395]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 402, 617, 419]]<|/det|>
<center>Figure 4.18: AVRCP/TG/MPS/BI-01-C [SetAddressedPlayer - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 433, 586, 499]]<|/det|>
Expected Outcome  Pass verdict  The IUT responds with an 'Invalid Player Id' status response.  

<|ref|>sub_title<|/ref|><|det|>[[115, 513, 545, 532]]<|/det|>
## AVRCP/TG/MPS/BI-02-C [SetBrowsedPlayer - TG]  

<|ref|>text<|/ref|><|det|>[[115, 540, 820, 583]]<|/det|>
Test Purpose  Verify the SetBrowsedPlayer response issued by the TG when an invalid player is requested.  

<|ref|>text<|/ref|><|det|>[[115, 591, 260, 632]]<|/det|>
Reference  [5], [8] 6.9.3  

<|ref|>text<|/ref|><|det|>[[115, 641, 260, 656]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 666, 875, 784]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester has retrieved the valid Playrelds of the IUT. This can be retrieved by executing AVRCP/TG/MPS/BV-09-C [GetFolderltems - TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 806, 114]]<|/det|>
The Lower Tester sends a SetBrowsedPlayer command to the IUT with an invalid PlayerID.  

<|ref|>image<|/ref|><|det|>[[152, 121, 707, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 395, 603, 412]]<|/det|>
<center>Figure 4.19: AVRCP/TG/MPS/BI-02-C [SetBrowsedPlayer - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 426, 586, 492]]<|/det|>
Expected Outcome  Pass verdict  The IUT responds with an 'Invalid Player Id' status response.  

<|ref|>sub_title<|/ref|><|det|>[[115, 505, 833, 546]]<|/det|>
### 4.6 Media Content Navigation Commands and Notifications for Content Browsing  

<|ref|>text<|/ref|><|det|>[[115, 552, 678, 569]]<|/det|>
Verify the commands and notifications related to Navigation of Media Content  

<|ref|>sub_title<|/ref|><|det|>[[115, 582, 557, 601]]<|/det|>
## AVRCP/CT/MCN/CB/BV-01-C [GetFolderltems - CT]  

<|ref|>text<|/ref|><|det|>[[115, 610, 540, 652]]<|/det|>
Test Purpose  Verify the GetFolderltems command issued by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 661, 260, 701]]<|/det|>
Reference [5], [8] 6.10.4.2  

<|ref|>text<|/ref|><|det|>[[115, 709, 260, 725]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 735, 884, 856]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP CT role in category 1.- The IUT has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 847, 114]]<|/det|>
The Upper Tester triggers the IUT to retrieve the Current Folder content in the Virtual Filesystem.  

<|ref|>image<|/ref|><|det|>[[144, 121, 700, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 395, 614, 411]]<|/det|>
<center>Figure 4.20: AVRCP/CT/MCN/CB/BV-01-C [GetFoldertems - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 426, 285, 442]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 451, 240, 466]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 474, 881, 507]]<|/det|>
The IUT issues a GetFoldertems command with the scope of Virtual Filesystem and valid parameters for StartItem, EndItem, AttributeCount, and AttributeList.  

<|ref|>sub_title<|/ref|><|det|>[[115, 522, 558, 541]]<|/det|>
## AVRCP/TG/MCN/CB/BV-02-C [GetFoldertems - TG]  

<|ref|>text<|/ref|><|det|>[[115, 550, 245, 565]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 573, 620, 590]]<|/det|>
Verify the GetFoldertems response issued by the TG for a folder.  

<|ref|>text<|/ref|><|det|>[[115, 599, 222, 615]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 623, 258, 639]]<|/det|>
[5], [8] 6.10.4.2  

<|ref|>text<|/ref|><|det|>[[115, 648, 260, 663]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 675, 661, 692]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 699, 800, 732]]<|/det|>
The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 736, 543, 752]]<|/det|>
The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 759, 870, 793]]<|/det|>
The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 73, 260, 89]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 97, 870, 130]]<|/det|>
The Lower Tester sends a GetFolderItems command to the IUT with the VirtualFilesystem as Scope parameter and valid entries for Start Item, End Item, AttributeCount and AttributeList.  

<|ref|>image<|/ref|><|det|>[[152, 137, 707, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 411, 616, 428]]<|/det|>
<center>Figure 4.21: AVRCP/TG/MCN/CB/BV-02-C [GetFolderItems - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 443, 275, 459]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 467, 238, 483]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 490, 766, 507]]<|/det|>
The IUT responds with a correctly formatted list of only Folder Items and Media Items.  

<|ref|>sub_title<|/ref|><|det|>[[113, 522, 559, 541]]<|/det|>
## AVRCP/TG/MCN/CB/BV-03-C [GetFolderItems - TG]  

<|ref|>text<|/ref|><|det|>[[115, 550, 245, 565]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 574, 839, 607]]<|/det|>
Verify the GetFolderItems response issued by the TG while the BrowsedPlayer is other than the AddressedPlayer.  

<|ref|>text<|/ref|><|det|>[[115, 611, 225, 625]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 634, 256, 650]]<|/det|>
[5], [8] 6.10.4.2  

<|ref|>text<|/ref|><|det|>[[115, 658, 260, 673]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 691, 660, 708]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 715, 800, 749]]<|/det|>
The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 752, 543, 769]]<|/det|>
The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 776, 844, 810]]<|/det|>
The Lower Tester has retrieved a list of available players. This can be achieved by executing AVRCP/TG/MPS/BV- 09- C [GetFolderItems - TG].  

<|ref|>text<|/ref|><|det|>[[144, 816, 615, 833]]<|/det|>
The IUT has at least two media player applications available.  

<|ref|>text<|/ref|><|det|>[[115, 850, 260, 865]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 873, 844, 924]]<|/det|>
1. The Lower Tester sets the addressed and browsed players on the IUT to valid PlayerID values  
2. The Lower Tester sends a GetFolderItems command to the IUT with the VirtualFilesystem as Scopeparameter and valid entries for Start Item, End Item, AttributeCount and AttributeList.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[150, 70, 707, 336]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[150, 344, 616, 360]]<|/det|>
<center>Figure 4.22: AVRCP/TG/MCN/CB/BV-03-C [GetFolderItems - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 375, 287, 415]]<|/det|>
- Expected OutcomePass verdict  

<|ref|>text<|/ref|><|det|>[[144, 422, 866, 455]]<|/det|>
The IUT responds with a correctly formatted list of only Folder Items and Media Items of the current folder on PlayerB.  

<|ref|>sub_title<|/ref|><|det|>[[115, 471, 530, 490]]<|/det|>
## AVRCP/CT/MCN/CB/BV-04-C [ChangePath - CT]  

<|ref|>text<|/ref|><|det|>[[115, 499, 520, 541]]<|/det|>
- Test PurposeVerify the ChangePath command issued by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 550, 220, 565]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 572, 255, 589]]<|/det|>
[5], [8] 6.10.4.1  

<|ref|>text<|/ref|><|det|>[[115, 598, 259, 613]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 624, 752, 640]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[142, 648, 800, 682]]<|/det|>
- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[142, 685, 543, 701]]<|/det|>
- The IUT is acting as AVRCP CT role in category 1.  

<|ref|>text<|/ref|><|det|>[[142, 708, 872, 742]]<|/det|>
- The IUT has retrieved the currently valid Folder UIDs on the Lower Tester. This can be achieved by executing AVRCP/CT/MCN/CB/BV-01-C [GetFolderItems - CT].  

<|ref|>text<|/ref|><|det|>[[142, 748, 876, 783]]<|/det|>
- The IUT has successfully issued a SetBrowseredPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[116, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 833, 130]]<|/det|>
The Upper Tester triggers the IUT to issue the ChangePath command with a valid UIDCounter, FolderUID, and Direction indication FolderDown.  

<|ref|>image<|/ref|><|det|>[[144, 137, 700, 411]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 419, 595, 435]]<|/det|>
<center>Figure 4.23: AVRCP/CT/MCN/CB/BV-04-C [ChangePath - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 835, 515]]<|/det|>
- Expected OutcomePass verdictThe IUT issues a ChangePath command with the valid parameters for Direction and FolderUID.  

<|ref|>sub_title<|/ref|><|det|>[[115, 530, 531, 548]]<|/det|>
## AVRCP/TG/MCN/CB/BV-05-C [ChangePath - TG]  

<|ref|>text<|/ref|><|det|>[[115, 557, 516, 600]]<|/det|>
- Test PurposeVerify the ChangePath response issued by the TG.  

<|ref|>text<|/ref|><|det|>[[115, 608, 256, 648]]<|/det|>
- Reference[5], [8] 6.10.4.1  

<|ref|>text<|/ref|><|det|>[[115, 656, 260, 671]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 682, 868, 844]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester is aware of the currently valid FolderUIDs exposed by the IUT. This can be achieved by executing AVRCP/TG/MCN/CB/BV-02-C [GetFolderltems - TG].- The Lower Tester has successfully issued a SetBrowserPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 96, 877, 130]]<|/det|>
The Lower Tester sends a ChangePath command to the IUT containing a currently valid UIDCounter, FolderUID, and the Direction indication Folder Down.  

<|ref|>image<|/ref|><|det|>[[144, 137, 712, 412]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 419, 596, 435]]<|/det|>
<center>Figure 4.24: AVRCP/TG/MCN/CB/BV-05-C [ChangePath - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 285, 466]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 474, 238, 490]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[142, 497, 877, 531]]<|/det|>
The IUT responds with a correctly formatted ChangePath Response with the correct Number of Items of the current folder on the IUT.  

<|ref|>sub_title<|/ref|><|det|>[[114, 546, 531, 565]]<|/det|>
## AVRCP/TG/MCN/CB/BV-06-C [ChangePath - TG]  

<|ref|>text<|/ref|><|det|>[[115, 574, 240, 590]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 597, 742, 615]]<|/det|>
Verify the ChangePath response issued by the TG when the Direction is FolderUp.  

<|ref|>text<|/ref|><|det|>[[115, 623, 223, 639]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 647, 255, 663]]<|/det|>
[5], [8] 6.10.4.1  

<|ref|>text<|/ref|><|det|>[[115, 673, 260, 688]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 698, 870, 844]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The IUT is in a state that allows the ChangePath direction of FolderUp.- The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 97, 835, 130]]<|/det|>
The Lower Tester sends a ChangePath command to the IUT containing the Direction indication Folder Up.  

<|ref|>image<|/ref|><|det|>[[146, 137, 714, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 412, 596, 428]]<|/det|>
<center>Figure 4.25: AVRCP/TG/MCN/CB/BV-06-C [ChangePath - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 443, 287, 459]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 467, 238, 483]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[142, 490, 877, 523]]<|/det|>
The IUT responds with a correctly formatted ChangePath Response with the correct Number of Items of the current folder on the IUT.  

<|ref|>sub_title<|/ref|><|det|>[[115, 539, 576, 558]]<|/det|>
## AVRCP/CT/MCN/CB/BV-07-C [GettlemAttributes - CT]  

<|ref|>text<|/ref|><|det|>[[115, 567, 245, 583]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 590, 870, 624]]<|/det|>
Verify the GettlemAttributes command issued by the CT on a Media Item in the Virtual Media Player Filesystem other than the currently playing one.  

<|ref|>text<|/ref|><|det|>[[115, 628, 223, 643]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 650, 256, 667]]<|/det|>
[5], [8] 6.10.4.3  

<|ref|>text<|/ref|><|det|>[[115, 675, 259, 690]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 708, 660, 725]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 732, 800, 767]]<|/det|>
The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 770, 543, 787]]<|/det|>
The IUT is acting as AVRCP CT role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 793, 864, 826]]<|/det|>
The IUT is aware of the currently valid Media Item UIDs exposed by the Lower Tester. This can be achieved by executing AVRCP/CT/MCN/CB/BV- 01- C [GetFolderltems - CT].  

<|ref|>text<|/ref|><|det|>[[144, 833, 879, 867]]<|/det|>
The IUT has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 880, 130]]<|/det|>
The Upper Tester triggers the IUT to issue the GettlemAttributes command for a currently valid Media Item UID other than the currently playing media item.  

<|ref|>image<|/ref|><|det|>[[145, 137, 712, 410]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 419, 627, 435]]<|/det|>
<center>Figure 4.26: AVRCP/CT/MCN/CB/BV-07-C [GettlemAttributes - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 285, 466]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 475, 238, 490]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 497, 789, 530]]<|/det|>
The IUT issues a GettlemAttributes command with valid parameters for UID, UIDcounter, NumberOfAttributes, and AttributeID list.  

<|ref|>sub_title<|/ref|><|det|>[[115, 546, 578, 565]]<|/det|>
## AVRCP/TG/MCN/CB/BV-08-C [GettlemAttributes - TG]  

<|ref|>text<|/ref|><|det|>[[115, 574, 245, 590]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 597, 866, 630]]<|/det|>
Verify the GettlemAttributes response issued by the TG on a Media Item in the Virtual Media Player Filesystem other than the currently playing one.  

<|ref|>text<|/ref|><|det|>[[115, 635, 225, 650]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 658, 258, 674]]<|/det|>
[5], [8] 6.10.4.3  

<|ref|>text<|/ref|><|det|>[[115, 682, 258, 697]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 715, 660, 732]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 739, 801, 773]]<|/det|>
The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 777, 543, 794]]<|/det|>
The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 801, 820, 834]]<|/det|>
The Lower Tester is aware of the currently valid Media Item UIDs on the IUT. This can be achieved by executing AVRCP/TG/MCN/CB/BV- 02- C [GetFolderltems - TG].  

<|ref|>text<|/ref|><|det|>[[144, 841, 870, 875]]<|/det|>
The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[116, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 97, 880, 130]]<|/det|>
The Lower Tester sends a GettlemAttributes command to the IUT containing the VirtualFilesystem as Scope parameter and valid entries for UID, UIDcounter, Number of Attributes, and AttributeID list.  

<|ref|>image<|/ref|><|det|>[[146, 138, 714, 411]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 419, 629, 435]]<|/det|>
<center>Figure 4.27: AVRCP/TG/MCN/CB/BV-08-C [GettlemAttributes - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 285, 488]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 496, 881, 530]]<|/det|>
The IUT responds with a correctly formatted GettlemAttributes Response with the expected values for Number of Attributes and Attribute Value List.  

<|ref|>sub_title<|/ref|><|det|>[[115, 546, 523, 565]]<|/det|>
## AVRCP/TG/MCN/CB/BV-09-C [UIDcounter - TG]  

<|ref|>text<|/ref|><|det|>[[115, 574, 728, 616]]<|/det|>
Test Purpose Verify the initial value of the UID counter if the TG is a database unaware player.  

<|ref|>text<|/ref|><|det|>[[115, 624, 248, 664]]<|/det|>
Reference [5], [8] 6.10.3  

<|ref|>text<|/ref|><|det|>[[115, 673, 260, 688]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 698, 872, 844]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The IUT is reset to factory settings so that the UID counter is reset to the initial value.- The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[141, 96, 870, 130]]<|/det|>
The Lower Tester registers with the IUT for UID change notifications. No change to the database on the IUT is applied between the reset and the RegisterNotification for EVENT_UIDS_CHANGED.  

<|ref|>image<|/ref|><|det|>[[144, 137, 714, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 412, 589, 428]]<|/det|>
<center>Figure 4.28: AVRCP/TG/MCN/CB/BV-09-C [UIDcounter - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 443, 822, 508]]<|/det|>
Expected Outcome  Pass verdict  The IUT issues an InterimResponse for the EVENT_UIDS_CHANGED with a UID Counter=0.  

<|ref|>sub_title<|/ref|><|det|>[[115, 522, 525, 541]]<|/det|>
## AVRCP/TG/MCN/CB/BV-10-C [UIDcounter - TG]  

<|ref|>text<|/ref|><|det|>[[115, 550, 710, 616]]<|/det|>
Test Purpose  Verify the initial value of the UID counter if the TG is a database aware player.  Reference  

<|ref|>text<|/ref|><|det|>[[144, 622, 245, 639]]<|/det|>
[5], [8] 6.10.3  

<|ref|>text<|/ref|><|det|>[[115, 648, 260, 663]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 674, 872, 820]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The IUT is reset to factory settings so that the UID counter is reset to the initial value.- The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 870, 130]]<|/det|>
The Lower Tester registers with the IUT for UID change notifications. No change to the database on the IUT is applied between the reset and the RegisterNotification for EVENT_UIDS_CHANGED.  

<|ref|>image<|/ref|><|det|>[[146, 137, 714, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 411, 589, 428]]<|/det|>
<center>Figure 4.29: AVRCP/TG/MCN/CB/BV-10-C [UIDcounter - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 443, 287, 459]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 467, 238, 483]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 490, 768, 523]]<|/det|>
The IUT issues an InterimResponse for the EVENT_UIDS_CHANGED with \(0\times 1< =\) UID Counter \(< = 0\times\) FFF.  

<|ref|>sub_title<|/ref|><|det|>[[115, 539, 523, 558]]<|/det|>
## AVRCP/TG/MCN/CB/BV-11-C [UIDcounter - TG]  

<|ref|>text<|/ref|><|det|>[[115, 567, 245, 583]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 590, 870, 623]]<|/det|>
Verify that the TG increments the UID counter and sends a UIDSCchangedNotification when updates on existing UIDs occur if the TG is database aware.  

<|ref|>text<|/ref|><|det|>[[115, 627, 222, 642]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 650, 243, 666]]<|/det|>
[5], [8] 6.10.3  

<|ref|>text<|/ref|><|det|>[[115, 674, 258, 689]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 707, 870, 827]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 660, 113]]<|/det|>
1. The Lower Tester registers with the IUT for UID change notifications.  

<|ref|>text<|/ref|><|det|>[[144, 113, 833, 145]]<|/det|>
2. The Upper Tester triggers a database change on the IUT, e.g., by adding or removing media tracks.  

<|ref|>text<|/ref|><|det|>[[144, 147, 866, 181]]<|/det|>
3. The Lower Tester registers with the IUT for UID change notifications. No database change occurs afterwards until after the second Interim Response has been sent to the Lower Tester.  

<|ref|>image<|/ref|><|det|>[[144, 188, 712, 455]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 462, 593, 477]]<|/det|>
<center>Figure 4.30: AVRCP/TG/MCN/CB/BV-11-C [UID counter - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 492, 285, 508]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 516, 238, 532]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 539, 857, 572]]<|/det|>
The IUT issues a FinalResponse for the EVENT_UIDS_CHANGED with UIDcounterB not equal to UIDcounterA.  

<|ref|>text<|/ref|><|det|>[[144, 576, 866, 610]]<|/det|>
The IUT issues an Interim response after the second Registration for the EVENT_UIDS_CHANGED with UIDcounterB.  

<|ref|>sub_title<|/ref|><|det|>[[115, 630, 631, 648]]<|/det|>
## AVRCP/CT/MCN/CB/BV-12-C [GetTotalNumberOftems - CT]  

<|ref|>text<|/ref|><|det|>[[115, 657, 245, 673]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 680, 847, 714]]<|/det|>
Verify the GetTotalNumberOftems command issued by the IUT (CT) for the Virtual Media Player Filesystem scope.  

<|ref|>text<|/ref|><|det|>[[115, 718, 225, 733]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 741, 230, 756]]<|/det|>
[8] 6.10.4.4  

<|ref|>text<|/ref|><|det|>[[115, 764, 260, 780]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 799, 661, 816]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 823, 860, 840]]<|/det|>
AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 847, 543, 863]]<|/det|>
The IUT is acting as AVRCP CT role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 870, 864, 905]]<|/det|>
The IUT has successfully issued a SetBrowsedPlayer command to the player specified in [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[116, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 842, 130]]<|/det|>
1. The Upper Tester triggers the IUT to issue a GetTotalNumberOfltems command to the Lower Tester with the scope parameter set to Virtual Media Player Filesystem.  

<|ref|>text<|/ref|><|det|>[[144, 131, 847, 165]]<|/det|>
2. Upon receipt of a GetTotalNumberOfltems command from the IUT, the Lower Tester issues an appropriate GetTotalNumberOfltems response message.  

<|ref|>image<|/ref|><|det|>[[145, 172, 714, 436]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 444, 673, 460]]<|/det|>
<center>Figure 4.31: AVRCP/CT/MCN/CB/BV-12-C [GetTotalNumberOfltems - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[116, 476, 285, 492]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 500, 238, 516]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 523, 864, 557]]<|/det|>
The IUT issues a GetTotalNumberOfltems command to the Lower Tester with the scope parameter set toVirtual Media Player Filesystem.  

<|ref|>sub_title<|/ref|><|det|>[[113, 572, 634, 590]]<|/det|>
## AVRCP/TG/MCN/CB/BV-13-C [GetTotalNumberOfltems - TG]  

<|ref|>text<|/ref|><|det|>[[116, 599, 245, 615]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 623, 874, 657]]<|/det|>
Verify that the IUT (TG) correctly responds to the GetTotalNumberOfltems command issued from the CT for the Virtual Media Player Filesystem scope.  

<|ref|>text<|/ref|><|det|>[[116, 660, 225, 675]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 684, 230, 699]]<|/det|>
[8] 6.10.4.4  

<|ref|>text<|/ref|><|det|>[[116, 708, 259, 723]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 741, 661, 758]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 766, 860, 784]]<|/det|>
AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 790, 544, 807]]<|/det|>
The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 814, 872, 849]]<|/det|>
The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in [6] as the browsable player.  

<|ref|>text<|/ref|><|det|>[[144, 851, 875, 886]]<|/det|>
The Lower Tester has successfully issued any necessary ChangePath commands to navigate to a folder on the Browsed Player on the IUT containing at least one item as specified in the IXIT [6].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 864, 130]]<|/det|>
The Lower Tester issues a GetTotalNumberOfflems command to the IUT with the scope parameter set to Virtual Media Player Filesystem.  

<|ref|>image<|/ref|><|det|>[[144, 137, 712, 412]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 419, 675, 435]]<|/det|>
<center>Figure 4.32: AVRCP/TG/MCN/CB/BV-13-C [GetTotalNumberOfflems - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 285, 466]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 474, 238, 490]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 497, 863, 530]]<|/det|>
The status parameter of the GetTotalNumberOfflems response message from the IUT to the Lower Tester indicates that the operation completed without error.  

<|ref|>text<|/ref|><|det|>[[144, 533, 857, 568]]<|/det|>
The total number of items returned by the IUT is the correct number of playable media items in the current folder [6].  

<|ref|>sub_title<|/ref|><|det|>[[115, 586, 551, 605]]<|/det|>
## AVRCP/TG/MCN/CB/BI-01-C [GetFolderltems - TG]  

<|ref|>text<|/ref|><|det|>[[115, 615, 245, 630]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 638, 797, 671]]<|/det|>
Verify the GetFolderltems response issued by the TG when the command contains invalid parameters.  

<|ref|>text<|/ref|><|det|>[[115, 676, 228, 691]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 699, 257, 715]]<|/det|>
[5], [8] 6.10.4.2  

<|ref|>text<|/ref|><|det|>[[115, 723, 259, 739]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 756, 661, 774]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 781, 800, 815]]<|/det|>
The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 818, 543, 835]]<|/det|>
The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 841, 870, 875]]<|/det|>
The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 97, 868, 130]]<|/det|>
The Lower Tester sends a GetFolderltems command to the IUT with invalid parameters: a Startltem parameter larger than the Endltem.  

<|ref|>image<|/ref|><|det|>[[152, 137, 707, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 412, 610, 428]]<|/det|>
<center>Figure 4.33: AVRCP/TG/MCN/CB/BI-01-C [GetFolderltems - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 444, 270, 459]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 468, 238, 483]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 490, 605, 507]]<|/det|>
The IUT responds with error code 0x0B (Range out of Bounds).  

<|ref|>sub_title<|/ref|><|det|>[[113, 522, 552, 541]]<|/det|>
## AVRCP/TG/MCN/CB/BI-02-C [GetFolderltems - TG]  

<|ref|>text<|/ref|><|det|>[[115, 550, 245, 566]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 574, 821, 606]]<|/det|>
Verify the GetFolderltems response issued by the TG for an empty folder when the command contains invalid parameters.  

<|ref|>text<|/ref|><|det|>[[115, 611, 228, 625]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 634, 256, 650]]<|/det|>
[5], [8] 6.10.4.2  

<|ref|>text<|/ref|><|det|>[[115, 658, 260, 673]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 691, 870, 836]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The IUT has issued ChangePath to the folder defined in the IXIT [6] as an empty folder.- The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 97, 839, 130]]<|/det|>
The Lower Tester sends a GetFolderltems command to the IUT specifying the empty folder and setting Startltem \(= 0\) and Endltem \(= 1\) .  

<|ref|>image<|/ref|><|det|>[[152, 138, 707, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[146, 412, 610, 428]]<|/det|>
<center>Figure 4.34: AVRCP/TG/MCN/CB/BI-02-C [GetFolderltems - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 443, 610, 508]]<|/det|>
Expected Outcome  Pass verdict  The IUT responds with error code 0x0B (Range out of Bounds).  

<|ref|>sub_title<|/ref|><|det|>[[115, 522, 552, 541]]<|/det|>
## AVRCP/TG/MCN/CB/BI-03-C [GetFolderltems - TG]  

<|ref|>text<|/ref|><|det|>[[115, 550, 797, 610]]<|/det|>
Test Purpose  Verify the GetFolderltems response issued by the TG when the command contains invalid parameters accessing items beyond the end of a folder.  

<|ref|>text<|/ref|><|det|>[[115, 612, 260, 670]]<|/det|>
Reference [5], [8] 6.10.4.2 Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 690, 870, 852]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester has issued ChangePath to the folder defined in the IXIT [6] as a non-empty folder.- The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[116, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 866, 145]]<|/det|>
The Lower Tester sends a GetFolderItems command to the IUT specifying the empty folder and setting StartItem \(= n + 1\) and EndItem \(= n + 2\) , where n is the number of items in the non- empty folder as retrieved by the ChangePath command.  

<|ref|>image<|/ref|><|det|>[[152, 154, 700, 420]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 428, 610, 444]]<|/det|>
<center>Figure 4.35: AVRCP/TG/MCN/CB/BI-03-C [GetFolderItems - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 459, 608, 525]]<|/det|>
Expected Outcome Pass verdict The IUT responds with error code 0x0B (Range out of Bounds).  

<|ref|>sub_title<|/ref|><|det|>[[115, 539, 525, 558]]<|/det|>
## AVRCP/TG/MCN/CB/BI-04-C [ChangePath - TG]  

<|ref|>text<|/ref|><|det|>[[115, 567, 810, 609]]<|/det|>
Test Purpose Verify the ChangePath response issued by the TG when an invalid Folder UID is requested.  

<|ref|>text<|/ref|><|det|>[[115, 616, 260, 656]]<|/det|>
Reference [5], [8] 6.10.4.1  

<|ref|>text<|/ref|><|det|>[[115, 665, 260, 680]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 690, 872, 852]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester is aware of the currently valid FolderUIDs exposed by the IUT. This can be achieved by executing AVRCP/TG/MCN/CB/BV-02-C [GetFolderItems - TG].- The Lower Tester has successfully issued a SetBrowseredPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 796, 130]]<|/det|>
The Lower Tester sends a ChangePath command to the IUT containing a currently invalid UIDCounter, FolderUID and the Direction indicating Folder Down.  

<|ref|>image<|/ref|><|det|>[[145, 137, 714, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 411, 590, 428]]<|/det|>
<center>Figure 4.36: AVRCP/TG/MCN/CB/BI-04-C [ChangePath - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 443, 648, 508]]<|/det|>
Expected Outcome  Pass verdict  The IUT responds with an error code indicating an invalid Folder UID.  

<|ref|>sub_title<|/ref|><|det|>[[113, 522, 516, 541]]<|/det|>
## AVRCP/TG/MCN/CB/BI-05-C [UIDcounter - TG]  

<|ref|>text<|/ref|><|det|>[[115, 550, 784, 616]]<|/det|>
Test Purpose  Verify that the TG issues an error when receiving a command for an invalid UID counter.  - Reference  

<|ref|>text<|/ref|><|det|>[[145, 622, 245, 639]]<|/det|>
[5], [8] 6.10.3  

<|ref|>text<|/ref|><|det|>[[115, 648, 260, 663]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 674, 872, 794]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.  

<|ref|>text<|/ref|><|det|>[[115, 809, 260, 824]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 832, 866, 899]]<|/det|>
1. The Lower Tester registers with the IUT for notification of UID change.  
2. The Lower Tester sends a GettlemAttributes command to the IUT, where the value of UIDcounterB in the GettlemAttributes is different from the UIDcounterA issued by the IUT in the InterimResponse.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[144, 70, 712, 345]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 352, 583, 368]]<|/det|>
<center>Figure 4.37: AVRCP/TG/MCN/CB/BI-05-C [UIDcounter - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 383, 720, 447]]<|/det|>
- Expected OutcomePass verdictThe IUT issues a GeltlemAttributes Response with Status Code UID Changed.  

<|ref|>sub_title<|/ref|><|det|>[[115, 461, 833, 501]]<|/det|>
### 4.7 Media Content Navigation Commands and Notifications for Search  

<|ref|>sub_title<|/ref|><|det|>[[115, 515, 495, 534]]<|/det|>
## AVRCP/CT/MCN/SRC/BV-01-C [Search - CT]  

<|ref|>text<|/ref|><|det|>[[115, 543, 480, 585]]<|/det|>
- Test PurposeVerify the Search command issued by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 593, 264, 634]]<|/det|>
- Reference[5], [8] 6.11  

<|ref|>text<|/ref|><|det|>[[115, 643, 260, 658]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 668, 881, 814]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP CT role in category 1.- The IUT is aware of the Character Sets supported by the Lower Tester.- The IUT has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 97, 544, 113]]<|/det|>
The Upper Tester triggers the IUT to execute a search.  

<|ref|>image<|/ref|><|det|>[[144, 121, 713, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 396, 570, 412]]<|/det|>
<center>Figure 4.38: AVRCP/CT/MCN/SRC/BV-01-C [Search - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 427, 285, 443]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 452, 238, 467]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 475, 842, 508]]<|/det|>
The IUT issues a Search command with the expected parameters for Character Set, Length and Search String.  

<|ref|>sub_title<|/ref|><|det|>[[114, 522, 498, 541]]<|/det|>
## AVRCP/TG/MCN/SRC/BV-02-C [Search - TG]  

<|ref|>text<|/ref|><|det|>[[115, 550, 230, 566]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 574, 475, 590]]<|/det|>
Verify the Search response issued by the TG.  

<|ref|>text<|/ref|><|det|>[[115, 600, 222, 640]]<|/det|>
- Reference 
[5], [8] 6.11  

<|ref|>text<|/ref|><|det|>[[115, 649, 260, 664]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 675, 872, 820]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester is aware of a valid Character Set on the IUT.- The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 805, 113]]<|/det|>
The Lower Tester sends a Search command to the IUT with valid entries for all parameters.  

<|ref|>image<|/ref|><|det|>[[146, 120, 700, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 395, 571, 411]]<|/det|>
<center>Figure 4.39: AVRCP/TG/MCN/SRC/BV-02-C [Search - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 426, 872, 492]]<|/det|>
Expected Outcome  Pass verdict  The IUT responds with a correctly formatted Search response with correct entries for all parameters.  

<|ref|>sub_title<|/ref|><|det|>[[115, 505, 568, 524]]<|/det|>
## AVRCP/CT/MCN/SRC/BV-03-C [GetFolderltems - CT]  

<|ref|>text<|/ref|><|det|>[[115, 533, 692, 576]]<|/det|>
Test Purpose  Verify the GetFolderltems command issued by the CT on the Search folder.  

<|ref|>text<|/ref|><|det|>[[115, 584, 297, 625]]<|/det|>
Reference  [5], [8] 6.10.4.2, 6.11  

<|ref|>text<|/ref|><|det|>[[115, 632, 260, 648]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[141, 658, 870, 820]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP CT role in category 1.- A successful Search operation has been performed by the IUT with the Search results still being valid; see AVRCP/CT/MCN/SRC/BV-01-C [Search - CT].- The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 660, 113]]<|/det|>
The Upper Tester triggers the IUT to retrieve the Search folder content.  

<|ref|>image<|/ref|><|det|>[[144, 121, 712, 395]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 402, 625, 418]]<|/det|>
<center>Figure 4.40: AVRCP/CT/MCN/SRC/BV-03-C [GetFolderltems - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 433, 286, 449]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 458, 238, 474]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 481, 872, 514]]<|/det|>
The IUT issues a GetFolderltems command with the scope of Search folder and valid parameters for Startltem, Endltem, AttributeCount and AttributeList.  

<|ref|>sub_title<|/ref|><|det|>[[115, 530, 570, 549]]<|/det|>
## AVRCP/TG/MCN/SRC/BV-04-C [GetFolderltems - TG]  

<|ref|>text<|/ref|><|det|>[[115, 558, 241, 573]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 581, 689, 598]]<|/det|>
Verify the GetFolderltems response for the Search folder issued by the TG.  

<|ref|>text<|/ref|><|det|>[[115, 607, 223, 622]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 630, 296, 647]]<|/det|>
[5], [8] 6.10.4.2, 6.11  

<|ref|>text<|/ref|><|det|>[[115, 656, 258, 671]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 682, 661, 699]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 706, 800, 740]]<|/det|>
The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 743, 543, 760]]<|/det|>
The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 767, 866, 801]]<|/det|>
A successful Search operation has been performed by the Lower Tester with the Search results still being valid; see AVRCP/TG/MCN/SRC/BV- 02- C [Search - TG].  

<|ref|>text<|/ref|><|det|>[[144, 807, 870, 842]]<|/det|>
The Lower Tester has successfully issued a SetBrowseredPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 97, 838, 130]]<|/det|>
The Lower Tester sends a GetFolderltems command to the IUT containing the Search folder as Scope parameter and valid entries for Start Item, End Item, AttributeCount and AttributeList.  

<|ref|>image<|/ref|><|det|>[[152, 137, 707, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[146, 412, 627, 428]]<|/det|>
<center>Figure 4.41: AVRCP/TG/MCN/SRC/BV-04-C [GetFolderltems - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 443, 640, 508]]<|/det|>
Expected Outcome  Pass verdict  The IUT responds with a correctly formatted list of only Media Items.  

<|ref|>sub_title<|/ref|><|det|>[[115, 523, 588, 541]]<|/det|>
## AVRCP/CT/MCN/SRC/BV-05-C [GetItemAttributes - CT]  

<|ref|>text<|/ref|><|det|>[[115, 550, 860, 608]]<|/det|>
Test Purpose  Verify the GetItemAttributes command issued by the CT on a Media Item in the Search folder other than the currently playing one.  

<|ref|>text<|/ref|><|det|>[[115, 611, 260, 627]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 634, 296, 650]]<|/det|>
[5], [8] 6.10.4.3, 6.11  

<|ref|>text<|/ref|><|det|>[[115, 658, 260, 673]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 691, 660, 707]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 715, 800, 749]]<|/det|>
The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 753, 542, 769]]<|/det|>
The IUT is acting as AVRCP CT role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 776, 870, 810]]<|/det|>
A successful Search operation has been performed by the IUT with the Search results still being valid; see AVRCP/CT/MCN/SRC/BV- 01- C [Search - CT].  

<|ref|>text<|/ref|><|det|>[[144, 816, 870, 850]]<|/det|>
The IUT is aware of the currently valid Media Item UIDs exposed by the Lower Tester. This can be achieved by executing AVRCP/CT/MCN/SRC/BV- 03- C [GetFolderltems - CT].  

<|ref|>text<|/ref|><|det|>[[144, 853, 878, 887]]<|/det|>
The IUT has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 863, 130]]<|/det|>
The Upper Tester triggers the GettlemAttributes command for a currently valid Search result Media Item UID other than the currently playing media item.  

<|ref|>image<|/ref|><|det|>[[144, 137, 713, 410]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 419, 637, 435]]<|/det|>
<center>Figure 4.42: AVRCP/CT/MCN/SRC/BV-05-C [GettlemAttributes - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 285, 466]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 475, 237, 490]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 497, 789, 530]]<|/det|>
The IUT issues a GettlemAttributes command with valid parameters for UID, UIDcounter, NumberOfAttributes and AttributeID list.  

<|ref|>sub_title<|/ref|><|det|>[[115, 546, 590, 565]]<|/det|>
## AVRCP/TG/MCN/SRC/BV-06-C [GettlemAttributes - TG]  

<|ref|>text<|/ref|><|det|>[[115, 574, 245, 590]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 597, 857, 630]]<|/det|>
Verify the GettlemAttributes response issued by the TG on a Media Item in the Search folder other than the currently playing one.  

<|ref|>text<|/ref|><|det|>[[115, 635, 223, 650]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 657, 296, 673]]<|/det|>
[5], [8] 6.10.4.3, 6.11  

<|ref|>text<|/ref|><|det|>[[115, 682, 259, 697]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 716, 660, 732]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 740, 800, 774]]<|/det|>
The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 777, 543, 794]]<|/det|>
The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 800, 865, 834]]<|/det|>
A successful Search operation has been performed by the Lower Tester with the Search results still being valid; see AVRCP/TG/MCN/SRC/BV- 02- C [Search - TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[144, 70, 880, 122]]<|/det|>
- The Lower Tester is aware of the currently valid Media Item UIDs in the Search folder exposed by the IUT. This can be achieved by executing AVRCP/TG/MCN/SRC/BV-04-C [GetFolderItems – TG].  

<|ref|>text<|/ref|><|det|>[[144, 128, 870, 162]]<|/det|>
- The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.  

<|ref|>sub_title<|/ref|><|det|>[[115, 173, 260, 188]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 196, 852, 229]]<|/det|>
The Lower Tester sends a GettemAttributes command to the IUT containing the Search folder as Scope parameter and valid entries for UID, UIDcounter, Number of Attributes and AttributeID list.  

<|ref|>image<|/ref|><|det|>[[144, 237, 714, 512]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 519, 640, 535]]<|/det|>
<center>Figure 4.43: AVRCP/TG/MCN/SRC/BV-06-C [GettemAttributes – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 550, 285, 565]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 574, 238, 589]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 597, 881, 629]]<|/det|>
The IUT responds with a correctly formatted GettemAttributes Response with the expected values for Number of Attributes and Attribute Value List.  

<|ref|>sub_title<|/ref|><|det|>[[115, 645, 644, 664]]<|/det|>
## AVRCP/CT/MCN/SRC/BV-07-C [GetTotalNumberOfItems - CT]  

<|ref|>text<|/ref|><|det|>[[115, 672, 802, 714]]<|/det|>
- Test PurposeVerify the GetTotalNumberOfItems command issued by the IUT (CT) for the Search scope.  

<|ref|>text<|/ref|><|det|>[[115, 722, 228, 761]]<|/det|>
- Reference [8] 6.10.4.4  

<|ref|>text<|/ref|><|det|>[[115, 771, 260, 786]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 797, 860, 862]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP CT role in category 1.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[144, 70, 866, 143]]<|/det|>
- IUT has successfully issued a SetBrowsedPlayer command to the player specified in [6] as the browsable player.- A successful Search operation has been performed by the IUT with the Search results still being valid; see AVRCP/CT/MCN/SRC/BV-01-C [Search - CT].  

<|ref|>text<|/ref|><|det|>[[115, 155, 260, 171]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 179, 840, 214]]<|/det|>
1. The Upper Tester triggers the IUT to issue a GetTotalNumberOfltems command to the Lower Tester with the scope parameter set to Search.  

<|ref|>text<|/ref|><|det|>[[142, 214, 846, 248]]<|/det|>
2. Upon receipt of a GetTotalNumberOfltems command from the IUT, the Lower Tester issues an appropriate GetTotalNumberOfltems response message.  

<|ref|>image<|/ref|><|det|>[[145, 253, 700, 519]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 528, 684, 544]]<|/det|>
<center>Figure 4.44: AVRCP/CT/MCN/SRC/BV-07-C [GetTotalNumberOfltems - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 559, 285, 575]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 583, 238, 598]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 606, 864, 639]]<|/det|>
The IUT issues a GetTotalNumberOfltems command to the Lower Tester with the scope parameter set toSearch.  

<|ref|>sub_title<|/ref|><|det|>[[115, 654, 647, 673]]<|/det|>
## AVRCP/TG/MCN/SRC/BV-08-C [GetTotalNumberOfltems - TG]  

<|ref|>text<|/ref|><|det|>[[115, 682, 245, 698]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 705, 875, 738]]<|/det|>
Verify that the IUT (TG) correctly responds to the GetTotalNumberOfltems command issued from the CT for the Search scope.  

<|ref|>text<|/ref|><|det|>[[115, 743, 225, 758]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 765, 229, 781]]<|/det|>
[8] 6.10.4.4  

<|ref|>text<|/ref|><|det|>[[115, 789, 259, 805]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 823, 661, 840]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 847, 860, 864]]<|/det|>
AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 871, 544, 888]]<|/det|>
The IUT is acting as AVRCP TG role in category 1.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[142, 70, 870, 142]]<|/det|>
- The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in [6] as the browsable player.- A successful Search operation has been performed by the Lower Tester with the Search results still being valid; see AVRCP/TG/MCN/SRC/BV-02-C [Search – TG].  

<|ref|>text<|/ref|><|det|>[[115, 155, 260, 171]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 179, 864, 212]]<|/det|>
The Lower Tester issues a GetTotalNumberOftems command to the IUT with the scope parameter set to Search.  

<|ref|>image<|/ref|><|det|>[[147, 220, 700, 485]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 493, 686, 509]]<|/det|>
<center>Figure 4.45: AVRCP/TG/MCN/SRC/BV-08-C [GetTotalNumberOftems – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 524, 285, 540]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 549, 238, 564]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 572, 864, 605]]<|/det|>
The status parameter of the GetTotalNumberOftems response message from the IUT to the Lower Tester indicates that the operation completed without error.  

<|ref|>text<|/ref|><|det|>[[144, 608, 857, 643]]<|/det|>
The total number of items returned by the IUT is the correct number of playable media items in the search result as specified in the IXIT [6].  

<|ref|>sub_title<|/ref|><|det|>[[115, 661, 835, 703]]<|/det|>
### 4.8 Media Content Navigation Commands and Notifications for NowPlaying  

<|ref|>sub_title<|/ref|><|det|>[[115, 715, 496, 733]]<|/det|>
## AVRCP/CT/MCN/NP/BV-01-C [Playltem - CT]  

<|ref|>text<|/ref|><|det|>[[115, 742, 490, 806]]<|/det|>
- Test PurposeVerify the Playltem command issued by the CT.  

<|ref|>text<|/ref|><|det|>[[144, 814, 242, 830]]<|/det|>
[5], [8] 6.12.1  

<|ref|>text<|/ref|><|det|>[[115, 840, 260, 856]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 867, 656, 884]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 892, 800, 926]]<|/det|>
- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[144, 70, 543, 87]]<|/det|>
- The IUT is acting as AVRCP CT role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 94, 815, 128]]<|/det|>
- The IUT is aware of the currently playable Media Items on the Lower Tester. This can be achieved by executing AVRCP/CT/MCN/CB/BV-01-C [GetFolderItems - CT].  

<|ref|>text<|/ref|><|det|>[[116, 139, 259, 155]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 162, 874, 196]]<|/det|>
The Upper Tester triggers the execution of the Playltem command on the IUT for a currently playable Media Item on the Lower Tester in a valid Scope (Media Filesystem, Search or NowPlaying).  

<|ref|>image<|/ref|><|det|>[[146, 204, 714, 468]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 476, 570, 492]]<|/det|>
<center>Figure 4.46: AVRCP/CT/MCN/NP/BV-01-C [Playltem - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[116, 508, 285, 550]]<|/det|>
- Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[142, 557, 872, 590]]<|/det|>
The IUT issues a Playltem command with the expected parameters as triggered by the Upper Tester for Scope and UID and the currently valid UID counter.  

<|ref|>sub_title<|/ref|><|det|>[[114, 605, 500, 623]]<|/det|>
## AVRCP/TG/MCN/NP/BV-02-C [Playltem - TG]  

<|ref|>text<|/ref|><|det|>[[116, 632, 245, 648]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 656, 488, 672]]<|/det|>
Verify the Playltem response issued by the TG.  

<|ref|>text<|/ref|><|det|>[[116, 683, 223, 699]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 707, 241, 723]]<|/det|>
[5], [8] 6.12.1  

<|ref|>text<|/ref|><|det|>[[116, 732, 259, 747]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 757, 800, 874]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester is aware of the currently playable UIDs exposed by the IUT. This can be achieved by executing AVRCP/TG/MCN/CB/BV-02-C [GetFolderItems - TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 97, 857, 130]]<|/det|>
The Lower Tester sends a Playltem Command to the IUT with valid entries for all parameters. The UID must be a UID for a currently playable UID.  

<|ref|>image<|/ref|><|det|>[[145, 138, 700, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 412, 572, 428]]<|/det|>
<center>Figure 4.47: AVRCP/TG/MCN/NP/BV-02-C [Playltem - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 443, 861, 508]]<|/det|>
Expected Outcome  Pass verdict  The IUT responds with a correctly formatted Playltem Response with the status indicating success.  

<|ref|>sub_title<|/ref|><|det|>[[115, 522, 582, 541]]<|/det|>
## AVRCP/CT/MCN/NP/BV-03-C [AddToNowPlaying - CT]  

<|ref|>text<|/ref|><|det|>[[115, 550, 562, 592]]<|/det|>
Test Purpose  Verify the AddToNowPlaying command issued by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 600, 247, 641]]<|/det|>
Reference [5], [8] 6.12.2  

<|ref|>text<|/ref|><|det|>[[115, 650, 260, 664]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 675, 802, 793]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP CT role in category 1.- The IUT is aware of the currently playable UIDs. This can be achieved by executing AVRCP/CT/MCN/CB/BV-01-C [GetFolderltems - CT].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 96, 877, 114]]<|/det|>
The Upper Tester triggers the AddToNowPlaying command from the IUT for a currently playable UID.  

<|ref|>image<|/ref|><|det|>[[144, 120, 712, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 395, 634, 412]]<|/det|>
<center>Figure 4.48: AVRCP/CT/MCN/NP/BV-03-C [AddToNowPlaying - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 426, 285, 442]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 451, 238, 466]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 474, 854, 507]]<|/det|>
The IUT issues an AddToNowPlaying command with the expected parameters as triggered by the Upper Tester for Scope and UID and the currently valid UID counter.  

<|ref|>sub_title<|/ref|><|det|>[[115, 522, 585, 541]]<|/det|>
## AVRCP/TG/MCN/NP/BV-04-C [AddToNowPlaying - TG]  

<|ref|>text<|/ref|><|det|>[[115, 550, 245, 565]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 574, 558, 591]]<|/det|>
Verify the AddToNowPlaying response issued by the TG.  

<|ref|>text<|/ref|><|det|>[[115, 600, 223, 615]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 624, 244, 640]]<|/det|>
[5], [8] 6.12.2  

<|ref|>text<|/ref|><|det|>[[115, 649, 260, 664]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 675, 661, 692]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 699, 800, 732]]<|/det|>
The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 736, 543, 753]]<|/det|>
The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 759, 854, 793]]<|/det|>
The Lower Tester is aware of the currently playable UIDs on the IUT. This can be achieved by executing AVRCP/TG/MCN/CB/BV- 02- C [GetFoldertems - TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[140, 96, 853, 114]]<|/det|>
The Lower Tester sends an AddToNowPlaying command with a currently playable UID to the IUT.  

<|ref|>image<|/ref|><|det|>[[144, 121, 714, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 395, 635, 411]]<|/det|>
<center>Figure 4.49: AVRCP/TG/MCN/NP/BV-04-C [AddToNowPlaying - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 426, 285, 442]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 451, 238, 466]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 474, 866, 507]]<|/det|>
The IUT responds with a correctly formatted AddToNowPlaying Response with the status indicating success.  

<|ref|>sub_title<|/ref|><|det|>[[115, 522, 555, 541]]<|/det|>
## AVRCP/CT/MCN/NP/BV-05-C [GetFolderltems - CT]  

<|ref|>text<|/ref|><|det|>[[115, 550, 235, 565]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 573, 730, 590]]<|/det|>
Verify the GetFolderltems command issued by the CT on the Now Playing folder.  

<|ref|>text<|/ref|><|det|>[[115, 599, 223, 615]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 622, 257, 639]]<|/det|>
[5], [8] 6.10.4.2  

<|ref|>text<|/ref|><|det|>[[115, 648, 260, 663]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 674, 661, 691]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 699, 800, 732]]<|/det|>
The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 736, 542, 752]]<|/det|>
The IUT is acting as AVRCP CT role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 759, 877, 793]]<|/det|>
The IUT has successfully issued a SetBrowserPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 700, 114]]<|/det|>
The Upper Tester triggers the IUT to retrieve the Now Playing folder content.  

<|ref|>image<|/ref|><|det|>[[145, 121, 713, 389]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 396, 614, 412]]<|/det|>
<center>Figure 4.50: AVRCP/CT/MCN/NP/BV-05-C [GetFolderltems - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 426, 287, 442]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 451, 240, 466]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 474, 802, 507]]<|/det|>
The IUT issues a GetFolderltems command with the scope of Now Playing folder and valid parameters for Startltem, Endltem, AttributeCount and AttributeList.  

<|ref|>sub_title<|/ref|><|det|>[[115, 522, 558, 541]]<|/det|>
## AVRCP/TG/MCN/NP/BV-06-C [GetFolderltems - TG]  

<|ref|>text<|/ref|><|det|>[[115, 550, 230, 565]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 573, 728, 590]]<|/det|>
Verify the GetFolderltems response for the Now Playing folder issued by the TG.  

<|ref|>text<|/ref|><|det|>[[115, 599, 222, 615]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 623, 258, 639]]<|/det|>
[5], [8] 6.10.4.2  

<|ref|>text<|/ref|><|det|>[[115, 648, 260, 663]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 675, 660, 692]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 699, 800, 733]]<|/det|>
The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 736, 543, 753]]<|/det|>
The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 765, 528, 782]]<|/det|>
The player on the IUT is currently playing media.  

<|ref|>text<|/ref|><|det|>[[144, 794, 870, 828]]<|/det|>
The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[116, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 875, 130]]<|/det|>
The Lower Tester sends a GetFolderltems command to the IUT containing the Now Playing folder as Scope parameter and valid entries for Start Item, End Item, AttributeCount and AttributeList.  

<|ref|>image<|/ref|><|det|>[[152, 137, 707, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[146, 412, 616, 428]]<|/det|>
<center>Figure 4.51: AVRCP/TG/MCN/NP/BV-06-C [GetFolderltems - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 443, 640, 508]]<|/det|>
Expected Outcome Pass verdict The IUT responds with a correctly formatted list of only Media Items.  

<|ref|>sub_title<|/ref|><|det|>[[115, 522, 775, 542]]<|/det|>
## AVRCP/TG/MCN/NP/BV-07-C [NowPlayingContentChanged notification - TG]  

<|ref|>text<|/ref|><|det|>[[115, 550, 645, 616]]<|/det|>
Test Purpose Verify the NowPlayingContentChanged notification issued by the TG. Reference [5], [8] 6.9.5  

<|ref|>text<|/ref|><|det|>[[115, 620, 240, 636]]<|/det|>
[5], [8] 6.9.5  

<|ref|>text<|/ref|><|det|>[[115,配 0, 875, 0]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 675, 801, 777]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester. The AVCTP control and browsing channels between the IUT and the Lower Tester are established. The IUT is acting as AVRCP TG role in category 1. The EVENT_NOW_PLAYING_CONTENT_CHANGED is registered with the IUT=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 690, 114]]<|/det|>
The Upper Tester triggers the change of the Now Playing folder on the IUT.  

<|ref|>image<|/ref|><|det|>[[144, 121, 713, 396]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 403, 777, 420]]<|/det|>
<center>Figure 4.52: AVRCP/TG/MCN/NP/BV-07-C [NowPlayingContentChanged notification – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 433, 799, 500]]<|/det|>
Expected Outcome  Pass verdict  The IUT issues a FinalResponse for the EVENT_NOW_PLAYING_CONTENT_CHANGED.  

<|ref|>sub_title<|/ref|><|det|>[[115, 514, 576, 533]]<|/det|>
## AVRCP/CT/MCN/NP/BV-08-C [GettlemAttributes - CT]  

<|ref|>text<|/ref|><|det|>[[115, 541, 863, 608]]<|/det|>
Test Purpose  Verify the GettlemAttributes command issued by the CT on a Media Item in the Now Playing folder.  Reference  

<|ref|>text<|/ref|><|det|>[[144, 615, 258, 631]]<|/det|>
[5], [8] 6.10.4.3  

<|ref|>text<|/ref|><|det|>[[115, 640, 258, 656]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 666, 864, 784]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP CT role in category 1.- The IUT is aware of the currently valid UIDs in the Now Playing folder. This can be achieved by executing AVRCP/CT/MCN/NP/BV-05-C [GetFoldertems - CT].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 96, 866, 130]]<|/det|>
The Upper Tester triggers the IUT to send a GettlemAttributes command for a currently valid UID in the Now Playing folder.  

<|ref|>image<|/ref|><|det|>[[144, 137, 699, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 412, 627, 428]]<|/det|>
<center>Figure 4.53: AVRCP/CT/MCN/NP/BV-08-C [GettlemAttributes - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 443, 285, 459]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 467, 238, 483]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[142, 490, 879, 523]]<|/det|>
The IUT issues a GettlemAttributes command with the Scope of NowPlaying and valid parameters for UID, UIDcounter, NumberOfAttributes and AttributeID list.  

<|ref|>sub_title<|/ref|><|det|>[[115, 539, 577, 558]]<|/det|>
## AVRCP/TG/MCN/NP/BV-09-C [GettlemAttributes - TG]  

<|ref|>text<|/ref|><|det|>[[115, 567, 245, 583]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 590, 858, 607]]<|/det|>
Verify the GettlemAttributes response issued by the TG on a Media Item in the Now Playing folder.  

<|ref|>text<|/ref|><|det|>[[115, 616, 223, 632]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 640, 257, 656]]<|/det|>
[5], [8] 6.10.4.3  

<|ref|>text<|/ref|><|det|>[[115, 666, 259, 681]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 691, 707, 708]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 715, 800, 749]]<|/det|>
The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 752, 543, 769]]<|/det|>
The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 777, 528, 793]]<|/det|>
The player on the IUT is currently playing media.  

<|ref|>text<|/ref|><|det|>[[144, 800, 840, 835]]<|/det|>
The Lower Tester is aware of the currently valid UIDs in the Now Playing folder. This can be achieved by executing AVRCP/TG/MCN/NP/BV- 06- C [GetFolderltems - TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 870, 145]]<|/det|>
The Lower Tester sends a GettemAttributes command to the IUT containing the Now Playing folder as Scope parameter and valid entries for UID (other than 0x0), UID Counter, Number of Attributes, and AttributeID list.  

<|ref|>image<|/ref|><|det|>[[144, 155, 714, 428]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 436, 629, 451]]<|/det|>
<center>Figure 4.54: AVRCP/TG/MCN/NP/BV-09-C [GettemAttributes - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 467, 287, 483]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 492, 238, 507]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 515, 881, 547]]<|/det|>
The IUT responds with a correctly formatted GettemAttributes Response with the expected values for Number of Attributes and Attribute Value List.  

<|ref|>sub_title<|/ref|><|det|>[[115, 563, 630, 581]]<|/det|>
## AVRCP/CT/MCN/NP/BV-10-C [GetTotalNumberOfltems - CT]  

<|ref|>text<|/ref|><|det|>[[115, 590, 240, 605]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 613, 857, 630]]<|/det|>
Verify the GetTotalNumberOfltems command issued from the IUT (CT) for the Now Playing scope.  

<|ref|>text<|/ref|><|det|>[[115, 640, 222, 655]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 664, 230, 680]]<|/det|>
[8] 6.10.4.4  

<|ref|>text<|/ref|><|det|>[[115, 690, 259, 705]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 716, 863, 823]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP CT role in category 1.- The IUT has successfully issued a SetBrowsedPlayer command to the player specified in [6] as the browsable player.  

<|ref|>text<|/ref|><|det|>[[115, 833, 259, 848]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 857, 839, 890]]<|/det|>
1. The Upper Tester triggers the IUT to issue a GetTotalNumberOfltems command to the Lower Tester with the scope parameter set to Now Playing.  

<|ref|>text<|/ref|><|det|>[[141, 891, 846, 924]]<|/det|>
2. Upon receipt of a GetTotalNumberOfltems command from the IUT, the Lower Tester issues an appropriate GetTotalNumberOfltems response message.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[144, 70, 700, 337]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 344, 673, 360]]<|/det|>
<center>Figure 4.55: AVRCP/CT/MCN/NP/BV-10-C [GetTotalNumberOfftimes - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 375, 288, 415]]<|/det|>
- Expected OutcomePass verdict  

<|ref|>text<|/ref|><|det|>[[144, 422, 864, 455]]<|/det|>
The IUT issues a GetTotalNumberOfftimes command to the Lower Tester with the scope parameter set to Now Playing.  

<|ref|>sub_title<|/ref|><|det|>[[115, 471, 633, 490]]<|/det|>
## AVRCP/TG/MCN/NP/BV-11-C [GetTotalNumberOfftimes - TG]  

<|ref|>text<|/ref|><|det|>[[115, 499, 245, 515]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 522, 875, 555]]<|/det|>
Verify that the IUT (TG) correctly responds to the GetTotalNumberOfftimes command issued from the CT for the Now Playing scope.  

<|ref|>text<|/ref|><|det|>[[115, 560, 225, 575]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 583, 230, 598]]<|/det|>
[8] 6.10.4.4  

<|ref|>text<|/ref|><|det|>[[115, 607, 258, 622]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 640, 661, 657]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 664, 860, 682]]<|/det|>
- AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 688, 544, 705]]<|/det|>
- The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 712, 870, 746]]<|/det|>
- The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in [6] as the browsable player.  

<|ref|>text<|/ref|><|det|>[[144, 750, 528, 766]]<|/det|>
- The player on the IUT is currently playing media.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 864, 130]]<|/det|>
The Lower Tester issues a GetTotalNumberOfftemms command to the IUT with the scope parameter set to Now Playing.  

<|ref|>image<|/ref|><|det|>[[146, 137, 714, 410]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 419, 675, 435]]<|/det|>
<center>Figure 4.56: AVRCP/TG/MCN/NP/BV-11-C [GetTotalNumberOfftemms - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 285, 466]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 474, 238, 490]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 497, 864, 531]]<|/det|>
The status parameter of the GetTotalNumberOfftemms response message from the IUT to the Lower Tester indicates that the operation completed without error.  

<|ref|>text<|/ref|><|det|>[[144, 534, 863, 569]]<|/det|>
The total number of items returned by the IUT is the correct number of the currently playable media items as specified in the IXIT [6].  

<|ref|>sub_title<|/ref|><|det|>[[115, 587, 560, 606]]<|/det|>
## AVRCP/TG/MCN/NP/BI-01-C [Playltem_Invalid - TG]  

<|ref|>text<|/ref|><|det|>[[115, 615, 243, 631]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 638, 730, 656]]<|/det|>
Verify the Playltem response issued by the TG when an invalid UID is requested.  

<|ref|>text<|/ref|><|det|>[[115, 665, 223, 681]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 689, 241, 705]]<|/det|>
[5], [8] 6.12.1  

<|ref|>text<|/ref|><|det|>[[115, 714, 260, 729]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 739, 852, 858]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester is aware of the currently playable UIDs on the IUT. This can be achieved by executing AVRCP/TG/MCN/CB/BV-02-C [GetFoldertems - TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 852, 114]]<|/det|>
The Lower Tester sends a Playltem Command to the IUT with a UID that is currently not playable.  

<|ref|>image<|/ref|><|det|>[[145, 121, 714, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 395, 617, 411]]<|/det|>
<center>Figure 4.57: AVRCP/TG/MCN/NP/BI-01-C [Playltem_Invalid - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 426, 285, 442]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 451, 238, 466]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 474, 857, 507]]<|/det|>
The IUT responds with a correctly formatted Playltem Response with the Status indicating the UID does not exist.  

<|ref|>sub_title<|/ref|><|det|>[[115, 522, 644, 542]]<|/det|>
## AVRCP/TG/MCN/NP/BI-02-C [AddToNowPlaying_Invalid - TG]  

<|ref|>text<|/ref|><|det|>[[115, 550, 245, 566]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 573, 802, 591]]<|/det|>
Verify the AddToNowPlaying response issued by the TG when an invalid UID is requested.  

<|ref|>text<|/ref|><|det|>[[115, 600, 223, 640]]<|/det|>
Reference [5], [8] 6.12.2  

<|ref|>text<|/ref|><|det|>[[115, 648, 260, 664]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 674, 828, 794]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester is aware of the currently valid UIDs on the IUT. This can be achieved by executing AVRCP/TG/MCN/CB/BV-02-C [GetFolderltems - TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 780, 114]]<|/det|>
The Lower Tester sends an AddToNowPlaying command to the IUT with an invalid UID.  

<|ref|>image<|/ref|><|det|>[[146, 121, 714, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 395, 680, 412]]<|/det|>
<center>Figure 4.58: AVRCP/TG/MCN/NP/BI-02-C [AddToNowPlaying_Invalid - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 426, 285, 465]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[142, 473, 866, 507]]<|/det|>
The IUT responds with a correctly formatted AddToNowPlaying Response with the status indicating that the UID does not exist.  

<|ref|>sub_title<|/ref|><|det|>[[115, 521, 444, 543]]<|/det|>
### 4.9 Volume Level Handling  

<|ref|>text<|/ref|><|det|>[[115, 548, 642, 565]]<|/det|>
Verify the commands and notifications related to Volume Level Handling.  

<|ref|>sub_title<|/ref|><|det|>[[115, 579, 559, 598]]<|/det|>
## AVRCP/CT/VLH/BV-01-C [SetAbsoluteVolume - CT]  

<|ref|>text<|/ref|><|det|>[[115, 607, 571, 650]]<|/det|>
Test Purpose Verify the SetAbsoluteVolume command issued by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 658, 245, 699]]<|/det|>
Reference [5], [8] 6.13.2  

<|ref|>text<|/ref|><|det|>[[115, 706, 260, 722]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 731, 730, 797]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The IUT is acting as AVRCP CT role in category 2.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 692, 113]]<|/det|>
The Upper Tester triggers the IUT to send a SetAbsoluteVolume command.  

<|ref|>image<|/ref|><|det|>[[144, 121, 712, 396]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 403, 612, 419]]<|/det|>
<center>Figure 4.59: AVRCP/CT/VLH/BV-01-C [SetAbsoluteVolume - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 433, 841, 499]]<|/det|>
Expected Outcome  Pass verdict  The IUT issues a correctly formatted SetAbsoluteVolume command with a valid value of volume.  

<|ref|>sub_title<|/ref|><|det|>[[115, 513, 561, 532]]<|/det|>
## AVRCP/TG/VLH/BV-02-C [SetAbsoluteVolume - TG]  

<|ref|>text<|/ref|><|det|>[[115, 540, 707, 585]]<|/det|>
Test Purpose  Verify the behavior of the TG receiving a valid SetAbsoluteVolume command.  

<|ref|>text<|/ref|><|det|>[[115, 592, 260, 633]]<|/det|>
Reference  [5], [8] 6.13.2  

<|ref|>text<|/ref|><|det|>[[115, 641, 260, 656]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 666, 730, 730]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The IUT is acting as AVRCP TG role in category 2.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 96, 850, 114]]<|/det|>
The Lower Tester sends a SetAbsoluteVolume command to the IUT with a valid value for volume.  

<|ref|>image<|/ref|><|det|>[[144, 121, 714, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 395, 614, 412]]<|/det|>
<center>Figure 4.60: AVRCP/TG/VLH/BV-02-C [SetAbsoluteVolume - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 426, 287, 465]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 473, 875, 507]]<|/det|>
The IUT responds with a correctly formatted SetAbsoluteVolume Response with the current value for volume.  

<|ref|>sub_title<|/ref|><|det|>[[115, 522, 570, 542]]<|/det|>
## AVRCP/CT/VLH/BV-03-C [NotifyVolumeChange - CT]  

<|ref|>text<|/ref|><|det|>[[115, 550, 584, 616]]<|/det|>
Test Purpose Verify the NotifyVolumeChange command issued by the CT. Reference [5], [8] 6.13.3  

<|ref|>text<|/ref|><|det|>[[115, 621, 260, 660]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 672, 731, 739]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The IUT is acting as AVRCP CT role in category 2.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 704, 113]]<|/det|>
The Upper Tester triggers the IUT to register for Volume Change Notification.  

<|ref|>image<|/ref|><|det|>[[146, 121, 700, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 395, 623, 411]]<|/det|>
<center>Figure 4.61: AVRCP/CT/VLH/BV-03-C [NotifyVolumeChange - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 426, 840, 491]]<|/det|>
Expected Outcome  Pass verdict  The IUT issues a correctly formatted RegisterNotification for the EVENT_VOLUME_CHANGED.  

<|ref|>sub_title<|/ref|><|det|>[[115, 505, 573, 524]]<|/det|>
## AVRCP/TG/VLH/BV-04-C [NotifyVolumeChange - TG]  

<|ref|>text<|/ref|><|det|>[[115, 533, 579, 576]]<|/det|>
Test Purpose  Verify the NotifyVolumeChange response issued by the TG.  

<|ref|>text<|/ref|><|det|>[[115, 585, 241, 626]]<|/det|>
Reference [5], [8] 6.13.3  

<|ref|>text<|/ref|><|det|>[[115, 633, 260, 649]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 659, 730, 723]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The IUT is acting as AVRCP TG role in category 2.  

<|ref|>text<|/ref|><|det|>[[115, 735, 260, 750]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 758, 684, 791]]<|/det|>
1. The Lower Tester registers with the IUT for Volume Change Notification.  
2. Subsequently the Upper Tester triggers a volume change on the IUT.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[145, 70, 712, 338]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 345, 624, 361]]<|/det|>
<center>Figure 4.62: AVRCP/TG/VLH/BV-04-C [NotifyVolumeChange - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 375, 287, 415]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 422, 816, 455]]<|/det|>
The IUT issues a FinalResponse for the EVENT_VOLUME_CHANGED with a valid value for Absolute Volume.  

<|ref|>sub_title<|/ref|><|det|>[[115, 471, 696, 490]]<|/det|>
## AVRCP/TG/VLH/BI-01-C [SetAbsoluteVolume invalid behavior - TG]  

<|ref|>text<|/ref|><|det|>[[115, 499, 728, 543]]<|/det|>
Test Purpose Verify the behavior of the TG receiving an invalid SetAbsoluteVolume command.  

<|ref|>text<|/ref|><|det|>[[115, 550, 245, 590]]<|/det|>
Reference [5], [8] 6.13.2  

<|ref|>text<|/ref|><|det|>[[115, 598, 260, 614]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 624, 730, 712]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The IUT is acting as AVRCP TG role in category 2.- The EVENT_VOLUME_CHANGED notification is registered at the IUT.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 812, 130]]<|/det|>
The Lower Tester sends a SetAbsoluteVolume command to the IUT with an invalid value for Parameter Length (too short to carry the absolute value parameter).  

<|ref|>image<|/ref|><|det|>[[144, 137, 714, 410]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 419, 714, 435]]<|/det|>
<center>Figure 4.63: AVRCP/TG/VLH/BI-01-C [SetAbsoluteVolume invalid behavior - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 287, 466]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 475, 237, 490]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 497, 860, 531]]<|/det|>
The IUT responds with a correctly formatted SetAbsoluteVolume Response indicating failure. If the IUT does not return Invalid Parameter Content (0x02), then the Lower Tester gives a warning.  

<|ref|>sub_title<|/ref|><|det|>[[115, 545, 696, 564]]<|/det|>
## AVRCP/TG/VLH/BI-02-C [SetAbsoluteVolume invalid behavior - TG]  

<|ref|>text<|/ref|><|det|>[[115, 573, 243, 590]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 597, 841, 614]]<|/det|>
Verify the behavior of the TG receiving a SetAbsoluteVolume command with the top level bit set.  

<|ref|>text<|/ref|><|det|>[[115, 623, 223, 639]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 647, 243, 663]]<|/det|>
[5], [8] 6.13.2  

<|ref|>text<|/ref|><|det|>[[115, 673, 260, 688]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 699, 732, 787]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The IUT is acting as AVRCP TG role in category 2.- The EVENT_VOLUME_CHANGED notification is registered at the IUT.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 96, 832, 130]]<|/det|>
The Lower Tester sends a SetAbsoluteVolume command to the IUT with the top bit of the level parameter set.  

<|ref|>image<|/ref|><|det|>[[145, 137, 714, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 411, 714, 428]]<|/det|>
<center>Figure 4.64: AVRCP/TG/VLH/BI-02-C [SetAbsoluteVolume invalid behavior – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 443, 287, 459]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 467, 238, 483]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[143, 490, 850, 523]]<|/det|>
The IUT responds with a correctly formatted SetAbsoluteVolume Response with the current value and the top bit set to zero.  

<|ref|>sub_title<|/ref|><|det|>[[115, 539, 694, 558]]<|/det|>
## AVRCP/CT/VLH/BI-03-C [SetAbsoluteVolume invalid behavior – CT]  

<|ref|>text<|/ref|><|det|>[[115, 567, 245, 583]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 590, 850, 607]]<|/det|>
Verify the behavior of the CT receiving a SetAbsoluteVolume Response with the top bit (bit 7) set.  

<|ref|>text<|/ref|><|det|>[[115, 616, 222, 632]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 640, 244, 656]]<|/det|>
[5], [8] 6.13.2  

<|ref|>text<|/ref|><|det|>[[115, 666, 260, 681]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 691, 730, 708]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 716, 730, 732]]<|/det|>
The AVCTP connection between the IUT and the Lower Tester is completed.  

<|ref|>text<|/ref|><|det|>[[144, 740, 542, 756]]<|/det|>
The IUT is acting as AVRCP CT role in category 2.  

<|ref|>text<|/ref|><|det|>[[144, 764, 688, 781]]<|/det|>
The EVENT_VOLUME_CHANGED notification is registered at the IUT.  

<|ref|>text<|/ref|><|det|>[[115, 792, 260, 808]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[140, 815, 850, 849]]<|/det|>
1. The Upper Tester triggers the IUT to issue a Valid Set Absolute volume command to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[140, 850, 850, 883]]<|/det|>
2. The Lower Tester issues the response for Set Absolute volume Response with the top bit (bit 7) of absolute volume parameter set (Volume).=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[147, 70, 712, 338]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 345, 712, 361]]<|/det|>
<center>Figure 4.65: AVRCP/CT/VLH/BI-03-C [SetAbsoluteVolume invalid behavior – CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 375, 287, 414]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 421, 852, 455]]<|/det|>
The IUT ignores the top bit (bit 7) and considers only the lower seven bits for the current value for volume.  

<|ref|>sub_title<|/ref|><|det|>[[115, 471, 693, 490]]<|/det|>
## AVRCP/CT/VLH/BI-04-C [SetAbsoluteVolume invalid behavior – CT]  

<|ref|>text<|/ref|><|det|>[[115, 499, 245, 515]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 522, 861, 556]]<|/det|>
Verify the behavior of the CT receiving an Interim and Final Response for Absolute Volume change notification with the top bit (bit 7) set.  

<|ref|>text<|/ref|><|det|>[[115, 560, 228, 576]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 583, 245, 599]]<|/det|>
[5], [8] 6.13.2  

<|ref|>text<|/ref|><|det|>[[115, 608, 258, 622]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 640, 680, 657]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 664, 730, 682]]<|/det|>
The AVCTP connection between the IUT and the Lower Tester is completed.  

<|ref|>text<|/ref|><|det|>[[144, 689, 542, 705]]<|/det|>
The IUT is acting as AVRCP CT role in category 2.  

<|ref|>text<|/ref|><|det|>[[144, 712, 688, 728]]<|/det|>
The EVENT_VOLUME_CHANGED notification is registered at the IUT.  

<|ref|>text<|/ref|><|det|>[[115, 741, 259, 757]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 764, 715, 781]]<|/det|>
1. The Upper Tester triggers the IUT to register for Volume Change Notification  

<|ref|>text<|/ref|><|det|>[[140, 781, 848, 815]]<|/det|>
2. Subsequently the Lower Tester issues an interim response EVENT_VOLUME_CHANGED with the top bit (bit 7) of absolute volume parameter set.  

<|ref|>text<|/ref|><|det|>[[140, 816, 848, 849]]<|/det|>
3. Subsequently the Lower Tester issues a final response EVENT_VOLUME_CHANGED with the top bit (bit 7) of absolute Volume parameter set.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[145, 70, 710, 338]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[143, 344, 712, 360]]<|/det|>
<center>Figure 4.66: AVRCP/CT/VLH/BI-04-C [SetAbsoluteVolume invalid behavior - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 375, 287, 415]]<|/det|>
- Expected OutcomePass verdict  

<|ref|>text<|/ref|><|det|>[[142, 422, 850, 456]]<|/det|>
The IUT ignores the top bit (bit 7) and considers only the lower seven bits of the Interim and Final Response for the absolute volume on TG.  

<|ref|>sub_title<|/ref|><|det|>[[115, 470, 480, 491]]<|/det|>
### 4.10 PASS THROUGH Handling  

<|ref|>text<|/ref|><|det|>[[115, 497, 857, 515]]<|/det|>
Verify that the state flag in the PASS THROUGH command is correctly set to convey the button action.  

<|ref|>sub_title<|/ref|><|det|>[[115, 528, 542, 547]]<|/det|>
## AVRCP/CT/PTH/BV-01-C [Press and release - CT]  

<|ref|>text<|/ref|><|det|>[[115, 555, 900, 592]]<|/det|>
- Test Purpose Verify that the button release is sent following a button press when the CT issues a PASS THROUGH command.  

<|ref|>text<|/ref|><|det|>[[115, 596, 230, 611]]<|/det|>
command.  

<|ref|>text<|/ref|><|det|>[[115, 618, 225, 680]]<|/det|>
Reference [2], [7] 4.6.1 [8] 4.4.1  

<|ref|>text<|/ref|><|det|>[[115, 690, 259, 706]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 720, 730, 787]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The IUT is acting as AVRCP CT.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 96, 749, 113]]<|/det|>
The Upper Tester triggers the IUT to issue commands for button press and release.  

<|ref|>image<|/ref|><|det|>[[144, 120, 714, 395]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 402, 602, 418]]<|/det|>
<center>Figure 4.67: AVRCP/CT/PTH/BV-01-C [Press and release - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 434, 285, 450]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 459, 237, 474]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 482, 872, 530]]<|/det|>
The IUT issues a correctly formatted PASS THROUGH command with the state flag set to button press, followed within 2 seconds by a correctly formatted PASS THROUGH command with the same operation id with the state flag set to button release.  

<|ref|>sub_title<|/ref|><|det|>[[113, 546, 517, 565]]<|/det|>
## AVRCP/CT/PTH/BV-02-C [Press and hold - CT]  

<|ref|>text<|/ref|><|det|>[[115, 574, 245, 590]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 598, 853, 630]]<|/det|>
Verify that when a button to send a PASS THROUGH command is held down the CT continues to issue button presses every 2 seconds until the button is released.  

<|ref|>text<|/ref|><|det|>[[115, 636, 223, 652]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 659, 230, 675]]<|/det|>
[2], [7] 4.6.1  

<|ref|>text<|/ref|><|det|>[[144, 683, 205, 698]]<|/det|>
[8] 4.4.1  

<|ref|>text<|/ref|><|det|>[[115, 708, 259, 723]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 740, 730, 805]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The IUT is acting as AVRCP CT.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 97, 850, 129]]<|/det|>
The Upper Tester triggers the IUT to issue commands for button press and release. The button is held for longer than 2 seconds.  

<|ref|>image<|/ref|><|det|>[[145, 138, 714, 492]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 500, 582, 515]]<|/det|>
<center>Figure 4.68: AVRCP/CT/PTH/BV-02-C [Press and hold - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 531, 287, 547]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 555, 238, 570]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 578, 850, 610]]<|/det|>
The IUT issues a correctly formatted PASS THROUGH command with the state flag set to button press.  

<|ref|>text<|/ref|><|det|>[[144, 614, 869, 667]]<|/det|>
Another PASS THROUGH command with the same operation id and state flag set to button press is issued within 2 seconds of each previous PASS THROUGH command until the button is released. At least two PASS THROUGH commands are sent with the state flag set to button press.  

<|ref|>text<|/ref|><|det|>[[141, 674, 869, 708]]<|/det|>
A final PASS THROUGH command with the same operation id and state flag set to button release is sent within 2 seconds of the last button press.  

<|ref|>sub_title<|/ref|><|det|>[[115, 733, 297, 752]]<|/det|>
### 4.11 Cover Art  

<|ref|>text<|/ref|><|det|>[[115, 760, 603, 776]]<|/det|>
Verify the commands and notifications related to Cover Art transfer.  

<|ref|>sub_title<|/ref|><|det|>[[115, 791, 803, 809]]<|/det|>
## AVRCP/CT/CA/BV-01-C [Use GetFolderItems to request Cover Art attribute - CT]  

<|ref|>text<|/ref|><|det|>[[115, 819, 245, 834]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[141, 842, 840, 874]]<|/det|>
Verify that the IUT can correctly use the GetFolderItems function with the scope of Virtual Media Player Filesystem to retrieve the Cover Art Image Handle.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 223, 89]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 97, 230, 113]]<|/det|>
[8] 6.10.4.2  

<|ref|>text<|/ref|><|det|>[[144, 121, 207, 136]]<|/det|>
[9] 4.4.4  

<|ref|>text<|/ref|><|det|>[[115, 146, 260, 161]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 171, 660, 188]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 195, 800, 228]]<|/det|>
- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 231, 543, 247]]<|/det|>
- The IUT is acting as AVRCP CT role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 254, 866, 287]]<|/det|>
- The IUT has successfully issued a SetBrowsedPlayer command to the player specified in [6] as the browsable player.  

<|ref|>text<|/ref|><|det|>[[144, 294, 865, 328]]<|/det|>
- There is an active Cover Art OBEX connection where the IUT is the OBEX client and the Lower Tester is the OBEX server.  

<|ref|>text<|/ref|><|det|>[[144, 332, 856, 365]]<|/det|>
- At least one item with Cover Art is available in the default folder on the Browsed Player on the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[115, 387, 259, 402]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 410, 857, 460]]<|/det|>
1. The Upper Tester triggers the IUT to issue a GetFoldertems command to the Lower Tester with the scope parameter set to Virtual Media Player Filesystem and the attribute list containing the Cover Art attribute.  

<|ref|>text<|/ref|><|det|>[[141, 461, 867, 495]]<|/det|>
2. Upon receipt of a GetFoldertems command from the IUT, the Lower Tester issues an appropriate GetFoldertems response message.  

<|ref|>image<|/ref|><|det|>[[144, 502, 714, 768]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 777, 799, 792]]<|/det|>
<center>Figure 4.69: AVRCP/CT/CA/BV-01-C [Use GetFoldertems to request Cover Art attribute – CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 808, 286, 824]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 832, 238, 847]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 855, 720, 871]]<|/det|>
The IUT issues a well- formatted GetFoldertems command to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 878, 835, 895]]<|/det|>
The GetFoldertems command has the scope parameter set to Virtual Media Player Filesystem.  

<|ref|>text<|/ref|><|det|>[[144, 902, 800, 918]]<|/det|>
The Cover Art attribute is among the attributes requested in the GetFoldertems command.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 191, 88]]<|/det|>
Notes  

<|ref|>text<|/ref|><|det|>[[142, 96, 850, 130]]<|/det|>
NotesNote that although the test does not directly use the Cover Art OBEX connection, it must exist for there to be valid Image Handles available on the TG (Imaging Responder).  

<|ref|>sub_title<|/ref|><|det|>[[115, 144, 806, 163]]<|/det|>
## AVRCP/TG/CA/BV-02-C [Use GetFolderltems to request Cover Art attribute - TG]  

<|ref|>text<|/ref|><|det|>[[115, 172, 245, 188]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[141, 196, 875, 229]]<|/det|>
Verify that the IUT can correctly respond to a GetFolderltems request with the scope of Virtual Media Player Filesystem to retrieve the Cover Art Image Handle.  

<|ref|>text<|/ref|><|det|>[[115, 234, 225, 250]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 257, 230, 273]]<|/det|>
[8] 6.10.4.2  

<|ref|>text<|/ref|><|det|>[[144, 281, 207, 296]]<|/det|>
[9] 4.4.4  

<|ref|>text<|/ref|><|det|>[[115, 307, 260, 323]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 338, 660, 355]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 362, 800, 395]]<|/det|>
The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 400, 544, 417]]<|/det|>
The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 423, 866, 456]]<|/det|>
The Tester has successfully issued a SetBrowsedPlayer command to the player specified in [6] as the browsable player.  

<|ref|>text<|/ref|><|det|>[[144, 462, 872, 496]]<|/det|>
There is an active Cover Art OBEX connection where the IUT is the OBEX server and the Lower Tester is the OBEX client.  

<|ref|>text<|/ref|><|det|>[[144, 500, 880, 534]]<|/det|>
The Tester has successfully issued any necessary ChangePath commands to navigate to a folder on the Browsed Player on the IUT containing at least one item with Cover Art [6].  

<|ref|>text<|/ref|><|det|>[[115, 553, 259, 569]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 577, 842, 610]]<|/det|>
The Lower Tester issues a GetFolderltems command to the IUT with the scope parameter set to Virtual Media Player Filesystem and the attribute list containing the Cover Art attribute.  

<|ref|>image<|/ref|><|det|>[[144, 618, 700, 875]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[142, 883, 800, 899]]<|/det|>
<center>Figure 4.70: AVRCP/TG/CA/BV-02-C [Use GetFolderltems torequest Cover Art attribute - TG] MSC </center>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 285, 88]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 97, 238, 112]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 119, 785, 137]]<|/det|>
The IUT issues a well- formatted GetFolderltems response message to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 143, 857, 161]]<|/det|>
The GetFolderltems response message contains at least one item with a Cover Art Image Handle.  

<|ref|>text<|/ref|><|det|>[[115, 170, 191, 185]]<|/det|>
Notes  

<|ref|>text<|/ref|><|det|>[[144, 193, 880, 291]]<|/det|>
NotesThe linkage between the returned Image Handle and retrieval of an image is covered in other tests (AVRCP/TG/CA/BV- 08- C [Use the Imaging Property Object - TG], AVRCP/TG/CA/BV- 10- C [Pull an Image as a Thumbnail - TG], AVRCP/TG/CA/BV- 12- C [Pull a Thumbnail - TG] and AVRCP/TG/CA/BV- 14- C [Pull a Native Image - TG]). Note that although the test does not directly use the Cover Art OBEX connection, it must exist for there to be valid Image Handles available on the TG (Imaging Responder).  

<|ref|>sub_title<|/ref|><|det|>[[115, 310, 825, 329]]<|/det|>
## AVRCP/CT/CA/BV-03-C [Use GettlemAttributes to request Cover Art attribute - CT]  

<|ref|>text<|/ref|><|det|>[[115, 337, 245, 353]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 360, 856, 394]]<|/det|>
Verify that the IUT can correctly use the GettlemAttributes function with the scope of Virtual Media Player Filesystem to retrieve the Cover Art Image Handle.  

<|ref|>text<|/ref|><|det|>[[115, 398, 225, 414]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 421, 230, 437]]<|/det|>
[8] 6.10.4.3  

<|ref|>text<|/ref|><|det|>[[115, 445, 259, 460]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 479, 660, 496]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 503, 800, 538]]<|/det|>
The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 541, 542, 558]]<|/det|>
The IUT is acting as AVRCP CT role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 564, 866, 599]]<|/det|>
The IUT has successfully issued a SetBrowsedPlayer command to the player specified in [6] as the browsable player.  

<|ref|>text<|/ref|><|det|>[[144, 605, 864, 640]]<|/det|>
There is an active Cover Art OBEX connection where the IUT is the OBEX client and the Lower Tester is the OBEX server.  

<|ref|>text<|/ref|><|det|>[[144, 642, 850, 677]]<|/det|>
At least one item with Cover Art is available in the default folder on the Browsed Player at the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[115, 696, 259, 711]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 719, 881, 770]]<|/det|>
1. The Upper Tester triggers the IUT to issue a GettlemAttributes command to the Lower Tester with the scope parameter set to Virtual Media Player Filesystem and the AttributeID list containing the Cover Art AttributeID.  

<|ref|>text<|/ref|><|det|>[[144, 770, 795, 804]]<|/det|>
2. Upon receipt of a GettlemAttributes command from the IUT, the Lower Tester issues an appropriate GettlemAttributes response message.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[145, 70, 714, 338]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 345, 812, 361]]<|/det|>
<center>Figure 4.71: AVRCP/CT/CA/BV-03-C [Use GettlemAttributes to request Cover Art attribute – CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 375, 288, 391]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 400, 238, 415]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 422, 736, 440]]<|/det|>
The IUT issues a well- formatted GettlemAttributes command to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 446, 850, 464]]<|/det|>
The GettlemAttributes command has the scope parameter set to Virtual Media Player Filesystem.  

<|ref|>text<|/ref|><|det|>[[144, 470, 852, 488]]<|/det|>
The Cover Art AttributeID is among the AttributeIDs requested in the GettlemAttributes command.  

<|ref|>sub_title<|/ref|><|det|>[[115, 503, 828, 522]]<|/det|>
## AVRCP/TG/CA/BV-04-C [Use GettlemAttributes to request Cover Art attribute – TG]  

<|ref|>text<|/ref|><|det|>[[115, 531, 245, 546]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 554, 880, 588]]<|/det|>
Verify that the IUT can correctly respond to a GettlemAttributes with the scope of Virtual Media Player Filesystem to retrieve the Cover Art Image Handle.  

<|ref|>text<|/ref|><|det|>[[115, 592, 223, 607]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 615, 230, 630]]<|/det|>
[8] 6.10.4.3  

<|ref|>text<|/ref|><|det|>[[144, 638, 207, 653]]<|/det|>
[9] 4.5.8  

<|ref|>text<|/ref|><|det|>[[115, 665, 259, 680]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 696, 661, 713]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 721, 800, 754]]<|/det|>
- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 758, 870, 792]]<|/det|>
- There is an active Cover Art OBEX connection where the IUT is the OBEX server and the Lower Tester is the OBEX client.  

<|ref|>text<|/ref|><|det|>[[144, 796, 543, 813]]<|/det|>
- The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 820, 864, 853]]<|/det|>
- The Tester is aware of the currently valid Media Item UIDs on the IUT. This can be achieved by executing AVRCP/TG/MCN/CB/BV-02-C [GetFoldertems – TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[142, 70, 880, 160]]<|/det|>
- The Tester has successfully issued a SetBrowserPlayer command to the player specified in the IXIT [6] as the browsable player.- The Tester has successfully issued any necessary ChangePath commands to navigate to a folder on the Browse Player of the IUT, containing at least one item with Cover Art as specified in the IXIT [6].  

<|ref|>sub_title<|/ref|><|det|>[[116, 171, 259, 187]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 196, 881, 245]]<|/det|>
The Lower Tester issues a GettlemAttributes command to the IUT with the scope parameter set to Virtual Media Player Filesystem and with valid entries for UID, UID Counter, Number of Attributes and AttributeID list. The AttributeID list contains the Cover Art AttributeID.  

<|ref|>image<|/ref|><|det|>[[146, 252, 716, 510]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 518, 812, 534]]<|/det|>
<center>Figure 4.72: AVRCP/TG/CA/BV-04-C [Use GettlemAttributes to request Cover Art attribute – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[116, 549, 285, 565]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 574, 238, 589]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 596, 801, 613]]<|/det|>
The IUT issues a well-formatted GettlemAttributes response message to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[140, 620, 870, 637]]<|/det|>
The GettlemAttributes response message contains at least one item with a Cover Art Image Handle.  

<|ref|>text<|/ref|><|det|>[[116, 647, 186, 661]]<|/det|>
Notes  

<|ref|>text<|/ref|><|det|>[[144, 670, 868, 737]]<|/det|>
The linkage between the returned Image Handle and retrieval of an image is covered in other tests (AVRCP/TG/CA/BV- 08- C [Use the Imaging Property Object – TG], AVRCP/TG/CA/BV- 10- C [Pull an Image as a Thumbnail – TG], AVRCP/TG/CA/BV- 12- C [Pull a Thumbnail – TG] and AVRCP/TG/CA/BV- 14- C [Pull a Native Image – TG]).  

<|ref|>sub_title<|/ref|><|det|>[[113, 753, 857, 772]]<|/det|>
## AVRCP/CT/CA/BV-05-C [Use GetElementAttributes to request Cover Art attribute – CT]  

<|ref|>text<|/ref|><|det|>[[116, 781, 243, 797]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 804, 835, 838]]<|/det|>
Verify that the IUT can correctly use the GetElementAttributes function to retrieve the Cover Art Image Handle of the currently playing item.  

<|ref|>text<|/ref|><|det|>[[116, 842, 222, 880]]<|/det|>
Reference [8] 6.6.1=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 96, 866, 223]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control channel between the IUT and the Lower Tester is established.- There is an active Cover Art OBEX connection where the IUT is the OBEX client and the Lower Tester is the OBEX server.- The IUT is acting as AVRCP CT role in category 1.- An item with Cover Art is playing on the default Addressed Player at the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[115, 238, 260, 253]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 261, 864, 310]]<|/det|>
1. The Upper Tester triggers the IUT to issue a GetElementAttributes command to the Lower Tester with the identifier parameter set to Playing and the AttributeID list containing the Cover Art AttributeID.  

<|ref|>text<|/ref|><|det|>[[144, 312, 825, 345]]<|/det|>
2. Upon receipt of a GetElementAttributes command from the IUT, the Lower Tester issues an appropriate GetElementAttributes response message.  

<|ref|>image<|/ref|><|det|>[[144, 352, 714, 626]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[142, 635, 838, 650]]<|/det|>
<center>Figure 4.73: AVRCP/CT/CA/BV-05-C [Use GetElementAttributes to request Cover Art attribute – CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 666, 880, 780]]<|/det|>
Expected OutcomePass verdictThe IUT issues a well- formatted GetElementAttributes command to the Lower Tester. The GetElementAttributes command has the identifier parameter set to Playing. The Cover Art AttributeID is among the AttributeIDs requested in the GetElementAttributes command.  

<|ref|>sub_title<|/ref|><|det|>[[115, 794, 860, 812]]<|/det|>
## AVRCP/TG/CA/BV-06-C [Use GetElementAttributes to request Cover Art attribute – TG]  

<|ref|>text<|/ref|><|det|>[[115, 821, 245, 836]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[141, 844, 860, 877]]<|/det|>
Verify that the IUT can correctly respond to a GetElementAttributes command to retrieve the Cover Art Image Handle of the currently playing item.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 223, 88]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 97, 206, 113]]<|/det|>
[8] 6.6.1  

<|ref|>text<|/ref|><|det|>[[115, 123, 260, 139]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 148, 870, 275]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control channel between the IUT and the Lower Tester is established.- There is an active Cover Art OBEX connection where the IUT is the OBEX server and the Lower Tester is the OBEX client.- The IUT is acting as AVRCP TG role in category 1.- An item with Cover Art is playing on the default Addressed Player at the IUT.  

<|ref|>text<|/ref|><|det|>[[115, 289, 260, 304]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 313, 860, 345]]<|/det|>
The Lower Tester issues a GetElementAttributes command to the IUT with the identifier parameter set to Playing and the AttributeID list containing the Cover Art AttributeID.  

<|ref|>image<|/ref|><|det|>[[144, 353, 700, 608]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 617, 839, 633]]<|/det|>
<center>Figure 4.74: AVRCP/TG/CA/BV-06-C [Use GetElementAttributes to request Cover Art attribute – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 649, 284, 664]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 673, 238, 688]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[142, 696, 830, 713]]<|/det|>
The IUT issues a well- formatted GetElementAttributes response message to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 720, 754, 737]]<|/det|>
The GetElementAttributes response message contains the Cover Art Image Handle.  

<|ref|>text<|/ref|><|det|>[[115, 747, 191, 761]]<|/det|>
Notes  

<|ref|>text<|/ref|><|det|>[[144, 769, 867, 835]]<|/det|>
The linkage between the returned Image Handle and retrieval of an image is covered in other tests (AVRCP/TG/CA/BV- 08- C [Use the Imaging Property Object – TG], AVRCP/TG/CA/BV- 10- C [Pull an Image as a Thumbnail – TG], AVRCP/TG/CA/BV- 12- C [Pull a Thumbnail – TG] and AVRCP/TG/CA/BV- 14- C [Pull a Native Image – TG]).=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[113, 70, 657, 88]]<|/det|>
## AVRCP/CT/CA/BV-07-C [Use the Imaging Property Object - CT]  

<|ref|>text<|/ref|><|det|>[[115, 97, 245, 112]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[143, 120, 866, 169]]<|/det|>
Verify that the IUT can correctly use the image- properties object to individually check images for versions other than the native format, and request an image in a format other than the native one or the mandatory imaging thumbnail.  

<|ref|>text<|/ref|><|det|>[[115, 179, 223, 193]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 201, 384, 217]]<|/det|>
[8] 5.14, 6.6.1, 6.10.4.2, 6.10.4.3  

<|ref|>text<|/ref|><|det|>[[144, 226, 311, 241]]<|/det|>
[9] 4.4.6.2, 4.5.7, 4.5.8  

<|ref|>text<|/ref|><|det|>[[115, 253, 259, 268]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 280, 660, 297]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[143, 304, 770, 320]]<|/det|>
- The AVCTP control channel between the IUT and the Lower Tester is established.  

<|ref|>text<|/ref|><|det|>[[143, 327, 857, 360]]<|/det|>
- If the IUT uses GettlemAttributes, the browsing channel (ALT 1 only) between the IUT and the Lower Tester is established.  

<|ref|>text<|/ref|><|det|>[[1439, 364, 864, 397]]<|/det|>
- There is an active Cover Art OBEX connection where the IUT is the OBEX client and the Lower Tester is the OBEX server.  

<|ref|>text<|/ref|><|det|>[[173, 400, 543, 416]]<|/det|>
The IUT is acting as AVRCP CT role in category 1.  

<|ref|>text<|/ref|><|det|>[[173, 423, 844, 455]]<|/det|>
The IUT has successfully retrieved a Cover Art Image Handle by using either of the following methods:  

<|ref|>text<|/ref|><|det|>[[201, 475, 880, 580]]<|/det|>
ALT 1: The IUT issues a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player. The IUT issues the GettlemAttributes or GetFolderltems commands to the Lower Tester. At least one item with Cover Art is available in the default folder on the Browsed Player at the Lower Tester. ALT 2: An item with Cover Art is playing on the default Addressed Player at the Lower Tester. The IUT issues the GetElementAttributes command to the Lower Tester.  

<|ref|>sub_title<|/ref|><|det|>[[115, 594, 258, 609]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 617, 878, 666]]<|/det|>
1. The Upper Tester triggers the IUT to issue a GettlmageProperties request to the Lower Tester with the Image Handle parameter set to one of the handles retrieved during the setup of the initial condition.  

<|ref|>text<|/ref|><|det|>[[143, 668, 835, 701]]<|/det|>
2. Upon receipt of a GettlmageProperties request from the IUT, the Lower Tester issues an appropriate GettlmageProperties response message containing an image-properties object.  

<|ref|>text<|/ref|><|det|>[[144, 702, 841, 783]]<|/det|>
3. Repeat Steps 1 and 2 until the Lower Tester returns an image-properties object indicating an image in a format other than the native and the mandatory imaging thumbnail. The image-properties object for the image at least contains a non-empty variant element with at least <variant encoding="JPEG" pixel="200*200" /> and another variant (for example, <variant encoding="GIF" pixel ="640*420" />) that is different from the native image.  

<|ref|>text<|/ref|><|det|>[[144, 785, 875, 833]]<|/det|>
4. The IUT is triggered to issue a Gettlmage request to the Lower Tester with the Image Handle parameter corresponding to the image identified from Step 3 and an Image Descriptor parameter describing a non-thumbnail image variant.  

<|ref|>text<|/ref|><|det|>[[144, 835, 810, 868]]<|/det|>
5. Upon receipt of a Gettlmage request from the IUT, the Lower Tester issues an appropriate Gettlmage response message.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[153, 68, 712, 298]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 304, 692, 320]]<|/det|>
<center>Figure 4.75: AVRCP/CT/CA/BV-07-C [Use the Imaging Property Object – CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[116, 335, 285, 351]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 360, 238, 375]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 382, 744, 399]]<|/det|>
The IUT issues a well- formatted GetImageProperties requests to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 406, 825, 439]]<|/det|>
Each GetImageProperties request includes a valid Connection ID, a Type header of "x- bt/img- properties", and a valid Image Handle.  

<|ref|>text<|/ref|><|det|>[[144, 442, 661, 459]]<|/det|>
The IUT issues a well- formatted GetImage request to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 466, 866, 499]]<|/det|>
The GetImage request includes a valid ConnectionID, a Type header of x- bt/img- img, a valid Image Handle, and a well- formatted Image Descriptor.  

<|ref|>text<|/ref|><|det|>[[144, 506, 878, 523]]<|/det|>
The Image Handle used in the GetImage request is that of an image that has a non- thumbnail variant.  

<|ref|>text<|/ref|><|det|>[[144, 530, 775, 547]]<|/det|>
The Image Descriptor used in the GetImage request describes a non- thumbnail format.  

<|ref|>text<|/ref|><|det|>[[144, 555, 191, 569]]<|/det|>
Notes  

<|ref|>text<|/ref|><|det|>[[144, 577, 876, 626]]<|/det|>
The Lower Tester will make sure that the variant is offered in at least one format that is supported by the IUT as declared in [6] for the Cover Art feature. For IUTs that support only the mandatory imaging thumbnail format, this test does not apply.  

<|ref|>sub_title<|/ref|><|det|>[[115, 653, 660, 672]]<|/det|>
## AVRCP/TG/CA/BV-08-C [Use the Imaging Property Object – TG]  

<|ref|>text<|/ref|><|det|>[[116, 681, 245, 697]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 705, 861, 753]]<|/det|>
Verify that the IUT can correctly handle the image- properties object, and individually provide image versions other than the native format, and respond with an image in a format other than the native one or the mandatory imaging thumbnail.  

<|ref|>text<|/ref|><|det|>[[115, 763, 223, 778]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 786, 384, 802]]<|/det|>
[8] 5.14, 6.6.1, 6.10.4.2, 6.10.4.3  

<|ref|>text<|/ref|><|det|>[[144, 810, 311, 825]]<|/det|>
[9] 4.4.6.2, 4.5.7, 4.5.8  

<|ref|>text<|/ref|><|det|>[[115, 836, 260, 852]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 864, 660, 880]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 888, 768, 904]]<|/det|>
- The AVCTP control channel between the IUT and the Lower Tester is established.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[141, 70, 872, 205]]<|/det|>
If the Lower Tester uses GettlemAttributes (ALT 1), the browsing channel between the IUT and the Lower Tester is established.- There is an active Cover Art OBEX connection where the IUT is the OBEX server and the Lower Tester is the OBEX client.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester has successfully retrieved a Cover Art Image Handle by using either of the following methods:  

<|ref|>text<|/ref|><|det|>[[201, 217, 875, 322]]<|/det|>
ALT 1: The Lower Tester issues a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player. The Lower Tester issues the GettlemAttributes or GetFolderltems commands to the IUT. At least one item with Cover Art is available in the default folder on the Browsed Player of the IUT.- ALT 2: An item with Cover Art is playing on the default Addressed Player of the IUT. The Lower Tester issues the GetElementAttributes command to the IUT.  

<|ref|>sub_title<|/ref|><|det|>[[116, 335, 259, 351]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[140, 358, 872, 590]]<|/det|>
1. The Lower Tester issues a GettlageProperties request to the IUT with the Image Handle parameter set to one of the handles retrieved during the setup of the initial condition. 
2. Upon receipt of a GettlageProperties request from the Lower Tester, the IUT issues an appropriate GettlageProperties response message containing an image-properties object. 
3. Repeat Steps 1 and 2 until the IUT returns an image-properties object indicating an image in a format other than the native and the mandatory imaging thumbnail. The image-properties object for the image at least contains a non-empty variant element with at least <variant encoding="JPEG" pixel="200*200"/> and another variant (for example, <variant encoding="GIF" pixel="640*420"/> that is different from the native image. 
4. The Lower Tester issues a Gettlage request to the IUT with the Image Handle parameter corresponding to the image identified from Step 3 and an Image Descriptor parameter describing a non-thumbnail image variant. 
5. Upon receipt of a Gettlage request from the Lower Tester, the IUT issues an appropriate Gettlage response message.  

<|ref|>image<|/ref|><|det|>[[145, 597, 700, 840]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 846, 690, 862]]<|/det|>
<center>Figure 4.76: AVRCP/TG/CA/BV-08-C [Use the Imaging Property Object – TG] MSC </center>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 285, 88]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 97, 238, 112]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 120, 708, 137]]<|/det|>
The IUT responds to the GetImageProperties requests from the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 144, 830, 177]]<|/det|>
The IUT responds to the GetImage request from the Lower Tester with a non- thumbnail format Image.  

<|ref|>text<|/ref|><|det|>[[115, 181, 191, 196]]<|/det|>
Notes  

<|ref|>text<|/ref|><|det|>[[144, 204, 861, 253]]<|/det|>
NotesThe IUT will make sure that the variant is offered in at least one format other than the native one or the mandatory imaging thumbnail. For IUTs that support only the mandatory imaging thumbnail format, this test does not apply.  

<|ref|>sub_title<|/ref|><|det|>[[115, 277, 630, 296]]<|/det|>
## AVRCP/CT/CA/BV-09-C [Pull an Image as a Thumbnail - CT]  

<|ref|>text<|/ref|><|det|>[[115, 305, 245, 320]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 328, 763, 345]]<|/det|>
Verify that the IUT can correctly retrieve the thumbnail format of the available images.  

<|ref|>text<|/ref|><|det|>[[115, 354, 223, 369]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 377, 384, 393]]<|/det|>
[8] 5.14, 6.6.1, 6.10.4.2, 6.10.4.3  

<|ref|>text<|/ref|><|det|>[[144, 401, 207, 416]]<|/det|>
[9] 4.5.8  

<|ref|>text<|/ref|><|det|>[[115, 427, 260, 443]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 454, 660, 470]]<|/det|>
One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 478, 770, 494]]<|/det|>
The AVCTP control channel between the IUT and the Lower Tester is established.  

<|ref|>text<|/ref|><|det|>[[144, 502, 875, 533]]<|/det|>
If the IUT uses GetItemAttributes, the browsing channel between the IUT and the Lower Tester is established.  

<|ref|>text<|/ref|><|det|>[[145, 538, 864, 571]]<|/det|>
There is an active Cover Art OBEX connection where the IUT is the OBEX client and the Lower Tester is the OBEX server.  

<|ref|>text<|/ref|><|det|>[[144, 574, 542, 590]]<|/det|>
The IUT is acting as AVRCP CT role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 598, 844, 630]]<|/det|>
The IUT has successfully retrieved a Cover Art Image Handle by using either of the following methods:  

<|ref|>text<|/ref|><|det|>[[201, 649, 881, 755]]<|/det|>
ALT 1: The IUT issues a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player. The IUT issues the GetItemAttributes or GetFolderItems commands to the Lower Tester. At least one item with Cover Art is available in the default folder on the Browsed Player at the Lower Tester. ALT 2: An item with Cover Art is playing on the default Addressed Player at the Lower Tester. The IUT issues the GetElementAttributes command to the Lower Tester.  

<|ref|>sub_title<|/ref|><|det|>[[115, 769, 259, 784]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 792, 822, 841]]<|/det|>
1. The Upper Tester triggers the IUT to issue a GetImage request to the Lower Tester with the Image Handle parameter set to one of the handles retrieved during the setup of the initial condition and an Image Descriptor parameter describing the thumbnail format.  

<|ref|>text<|/ref|><|det|>[[144, 843, 810, 875]]<|/det|>
2. Upon receipt of a GetImage request from the IUT, the Lower Tester issues an appropriate GetImage response message.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[144, 70, 714, 344]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 352, 670, 368]]<|/det|>
<center>Figure 4.77: AVRCP/CT/CA/BV-09-C [Pull an Image as a Thumbnail – CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 383, 285, 399]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 407, 238, 422]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 430, 661, 447]]<|/det|>
The IUT issues a well- formatted GetImage request to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 454, 852, 487]]<|/det|>
The ConnectionID, Image Handle, and Image Descriptor parameters in the GetImage request are present and valid.  

<|ref|>text<|/ref|><|det|>[[144, 490, 801, 508]]<|/det|>
The Image Descriptor parameter in the GetImage request describes an imaging thumbnail.  

<|ref|>sub_title<|/ref|><|det|>[[115, 527, 633, 546]]<|/det|>
## AVRCP/TG/CA/BV-10-C [Pull an Image as a Thumbnail – TG]  

<|ref|>text<|/ref|><|det|>[[115, 555, 245, 571]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 579, 875, 596]]<|/det|>
Verify that the IUT can correctly respond to requests for the thumbnail format of the available images.  

<|ref|>text<|/ref|><|det|>[[115, 605, 223, 620]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 628, 384, 644]]<|/det|>
[8] 5.14, 6.6.1, 6.10.4.2, 6.10.4.3  

<|ref|>text<|/ref|><|det|>[[144, 652, 208, 668]]<|/det|>
[9] 4.5.8  

<|ref|>text<|/ref|><|det|>[[115, 679, 260, 694]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 704, 864, 825]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control channel between the IUT and the Lower Tester is established.- If the Lower Tester uses GetItemAttributes (ALT 1), the browsing channel between the IUT and the Lower Tester is established.- There is an active Cover Art OBEX connection where the Lower Tester is the OBEX client and the IUT is the OBEX server.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[144, 70, 544, 87]]<|/det|>
- The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 94, 848, 127]]<|/det|>
- The Lower Tester has successfully retrieved a Cover Art Image Handle by using either of the following methods:  

<|ref|>text<|/ref|><|det|>[[201, 135, 875, 241]]<|/det|>
ALT 1: The Lower Tester issues a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player. The Lower Tester issues the GettemAttributes or GetFolderltems commands to the IUT. At least one item with Cover Art is available in the default folder on the Browsed Player at the IUT. ALT 2: An item with Cover Art is playing on the default Addressed Player at the IUT. The Lower Tester issues the GetElementAttributes command to the IUT.  

<|ref|>sub_title<|/ref|><|det|>[[116, 254, 259, 270]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 278, 863, 328]]<|/det|>
1. The Lower Tester issues a Gettmage request to the IUT, with the Image Handle parameter set to one of the handles retrieved during the setup of the initial condition, and an Image Descriptor parameter describing the thumbnail format.  

<|ref|>text<|/ref|><|det|>[[144, 329, 810, 362]]<|/det|>
2. Upon receipt of a Gettmage request from the Lower Tester, the IUT issues an appropriate Gettmage response message.  

<|ref|>image<|/ref|><|det|>[[145, 368, 700, 636]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 643, 671, 659]]<|/det|>
<center>Figure 4.78: AVRCP/TG/CA/BV-10-C [Pull an Image as a Thumbnail – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 674, 805, 737]]<|/det|>
- Expected OutcomePass verdictThe IUT responds to the Gettmage request from the Lower Tester with a Thumbnail Image.  

<|ref|>sub_title<|/ref|><|det|>[[113, 752, 522, 771]]<|/det|>
## AVRCP/CT/CA/BV-11-C [Pull a Thumbnail – CT]  

<|ref|>text<|/ref|><|det|>[[115, 780, 523, 820]]<|/det|>
- Test PurposeVerify that the IUT can correctly retrieve thumbnails.  

<|ref|>text<|/ref|><|det|>[[115, 830, 384, 894]]<|/det|>
- Reference[8] 5.14, 6.6.1, 6.10.4.2, 6.10.4.3[9] 4.5.9=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 96, 872, 300]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control channel between the IUT and the Lower Tester is established.- If the IUT uses GettlemAttributes or GetFoldertlms, the browsing channel between the IUT and the Lower Tester is established.- There is an active Cover Art OBEX connection where the IUT is the OBEX client and the Lower Tester is the OBEX server.- The IUT is acting as AVRCP CT role in category 1.- The IUT has successfully retrieved a Cover Art Image Handle by using either of the following methods:  

<|ref|>text<|/ref|><|det|>[[202, 293, 881, 397]]<|/det|>
ALT 1: The IUT issues a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player. The IUT issues the GettlemAttributes or GetFoldertlms commands to the Lower Tester. At least one item with Cover Art is available in the default folder on the Browsed Player at the Lower Tester. ALT 2: An item with Cover Art is playing on the default Addressed Player at the Lower Tester. The IUT issues the GetElementAttributes command to the Lower Tester.  

<|ref|>sub_title<|/ref|><|det|>[[116, 410, 259, 425]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 433, 843, 483]]<|/det|>
1. The Upper Tester triggers the IUT to issue a GetLinkedThumbnail request to the Lower Tester with the Image Handle parameter set to the handle retrieved during the setup of the initial condition.  

<|ref|>text<|/ref|><|det|>[[144, 485, 802, 518]]<|/det|>
2. Upon receipt of a GetLinkedThumbnail request from the IUT, the Lower Tester issues an appropriate GetLinkedThumbnail response message.  

<|ref|>image<|/ref|><|det|>[[145, 526, 700, 794]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 800, 584, 816]]<|/det|>
<center>Figure 4.79: AVRCP/CT/CA/BV-11-C [Pull a Thumbnail - CT] MSC </center>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 285, 88]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 97, 238, 112]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 120, 740, 136]]<|/det|>
The IUT issues a well- formatted GetLinkedThumbnail request to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[142, 143, 857, 177]]<|/det|>
The GetLinkedThumbnail request includes a valid Connection ID, a Type header of "x- bt/img- thm", and a valid Image Handle.  

<|ref|>sub_title<|/ref|><|det|>[[115, 193, 525, 211]]<|/det|>
## AVRCP/TG/CA/BV-12-C [Pull a Thumbnail - TG]  

<|ref|>text<|/ref|><|det|>[[115, 220, 240, 235]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 243, 635, 260]]<|/det|>
Verify that the IUT can correctly respond to requests for thumbnails.  

<|ref|>text<|/ref|><|det|>[[115, 270, 223, 285]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 293, 384, 310]]<|/det|>
[8] 5.14, 6.6.1, 6.10.4.2, 6.10.4.3  

<|ref|>text<|/ref|><|det|>[[144, 318, 208, 333]]<|/det|>
[9] 4.5.9  

<|ref|>text<|/ref|><|det|>[[115, 344, 260, 360]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 370, 660, 386]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 394, 770, 410]]<|/det|>
- The AVCTP control channel between the IUT and the Lower Tester is established.  

<|ref|>text<|/ref|><|det|>[[144, 417, 875, 450]]<|/det|>
- If the Lower Tester uses GetItemAttributes or GetFolderItems (both ALT 1), the browsing channel between the IUT and the Lower Tester is established.  

<|ref|>text<|/ref|><|det|>[[145, 454, 870, 488]]<|/det|>
- There is an active Cover Art OBEX connection where the IUT is the OBEX server and the Lower Tester is the OBEX client.  

<|ref|>text<|/ref|><|det|>[[144, 491, 544, 507]]<|/det|>
- The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 514, 844, 547]]<|/det|>
- The Lower Tester has successfully retrieved a Cover Art Image Handle by using either of the following methods:  

<|ref|>text<|/ref|><|det|>[[202, 565, 875, 670]]<|/det|>
ALT 1: The Lower Tester issues a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player. The Lower Tester issues the GetItemAttributes or GetFolderItems commands to the IUT. At least one item with Cover Art is available in the default folder on the Browsed Player at the IUT. ALT 2: An item with Cover Art is playing on the default Addressed Player at the IUT. The Lower Tester issues the GetElementAttributes command to the IUT.  

<|ref|>text<|/ref|><|det|>[[115, 684, 259, 699]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 707, 812, 741]]<|/det|>
1. The Lower Tester issues a GetLinkedThumbnail request to the IUT with the Image Handle parameter set to the handle retrieved during the setup of the initial condition.  

<|ref|>text<|/ref|><|det|>[[144, 742, 802, 775]]<|/det|>
2. Upon receipt of a GetLinkedThumbnail request from the Lower Tester, the IUT issues an appropriate GetLinkedThumbnail response message.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[147, 70, 714, 338]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[147, 345, 586, 360]]<|/det|>
<center>Figure 4.80: AVRCP/TG/CA/BV-12-C [Pull a Thumbnail – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 375, 287, 414]]<|/det|>
- Expected OutcomePass verdict  

<|ref|>text<|/ref|><|det|>[[144, 421, 830, 455]]<|/det|>
The IUT responds to the GetLinkedThumbnail request from the Lower Tester with a Thumbnail Image.  

<|ref|>sub_title<|/ref|><|det|>[[115, 471, 543, 490]]<|/det|>
## AVRCP/CT/CA/BV-13-C [Pull a Native Image – CT]  

<|ref|>text<|/ref|><|det|>[[115, 499, 696, 540]]<|/det|>
- Test PurposeVerify that the IUT can correctly retrieve an available image in native format.  

<|ref|>text<|/ref|><|det|>[[115, 549, 368, 590]]<|/det|>
- Reference[9] 5.14, 4.4.6.2, 4.4.7.2, 4.5.8  

<|ref|>text<|/ref|><|det|>[[115, 598, 260, 613]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 624, 860, 780]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- There is an active Cover Art OBEX connection where the IUT is the OBEX client and the Lower Tester is the OBEX server.- The IUT is acting as AVRCP CT role in category 1.- The IUT has successfully retrieved a Cover Art Image Handle by using either of the following methods:  

<|ref|>text<|/ref|><|det|>[[202, 795, 881, 900]]<|/det|>
- ALT 1: The IUT issues a SetBrowseredPlayer command to the player specified in the IXIT [6] as the browsable player. The IUT issues the GettlemAttributes or GetFolderltems commands to the Lower Tester. At least one item with Cover Art is available in the default folder on the Browsed Player at the Lower Tester.- ALT 2: An item with Cover Art is playing on the default Addressed Player at the Lower Tester. The IUT issues the GetElementAttributes command to the Lower Tester.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 868, 147]]<|/det|>
1. The Upper Tester triggers the IUT to issue a GetImage request to the Lower Tester with the Image Handle parameter set to the handle retrieved during the set-up of the initial condition and an empty Image Descriptor parameter.  

<|ref|>text<|/ref|><|det|>[[144, 148, 810, 181]]<|/det|>
2. Upon receipt of a GetImage request from the IUT, the Lower Tester issues an appropriate GetImage response message.  

<|ref|>image<|/ref|><|det|>[[149, 188, 714, 455]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 462, 602, 478]]<|/det|>
<center>Figure 4.81: AVRCP/CT/CA/BV-13-C [Pull a Native Image - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 493, 844, 604]]<|/det|>
Expected Outcome Pass verdict The IUT issues a well- formatted GetImage request to the Lower Tester. The ConnectionID and Image Handle parameters in the GetImage request are present and valid. The Image Descriptor parameter in the GetImage request is empty.  

<|ref|>sub_title<|/ref|><|det|>[[114, 620, 544, 638]]<|/det|>
## AVRCP/TG/CA/BV-14-C [Pull a Native Image - TG]  

<|ref|>text<|/ref|><|det|>[[115, 648, 810, 690]]<|/det|>
Test Purpose Verify that the IUT can correctly respond to requests for an available image in native format.  

<|ref|>text<|/ref|><|det|>[[115, 698, 366, 738]]<|/det|>
Reference [9] 5.14, 4.4.6.2, 4.4.7.2, 4.5.8  

<|ref|>text<|/ref|><|det|>[[115, 747, 260, 762]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 773, 870, 870]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- There is an active Cover Art OBEX connection where the IUT is the OBEX server and the Lower Tester is the OBEX client.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[144, 70, 544, 87]]<|/det|>
- The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 94, 847, 127]]<|/det|>
- The Lower Tester has successfully retrieved a Cover Art Image Handle by using either of the following methods:  

<|ref|>text<|/ref|><|det|>[[201, 135, 875, 241]]<|/det|>
ALT 1: The Lower Tester issues a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player. The Lower Tester issues the GettemAttributes or GetFolderltems commands to the IUT. At least one item with Cover Art is available in the default folder on the Browsed Player at the IUT. ALT 2: An item with Cover Art is playing on the default Addressed Player at the IUT. The Lower Tester issues the GetElementAttributes command to the IUT.  

<|ref|>sub_title<|/ref|><|det|>[[116, 254, 259, 270]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 277, 857, 328]]<|/det|>
1. The Lower Tester issues a GetImage request to the IUT with the Image Handle parameter set to the handle retrieved during the set-up of the initial condition and an empty Image Descriptor parameter.  

<|ref|>text<|/ref|><|det|>[[144, 329, 810, 362]]<|/det|>
2. Upon receipt of a GetImage request from the Lower Tester, the IUT issues an appropriate GetImage response message.  

<|ref|>image<|/ref|><|det|>[[147, 368, 700, 636]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 643, 604, 658]]<|/det|>
<center>Figure 4.82: AVRCP/TG/CA/BV-14-C [Pull a Native Image - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 673, 281, 689]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 697, 238, 712]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 720, 822, 737]]<|/det|>
The IUT responds to the GetImage request from the Lower Tester with a native format Image.  

<|ref|>text<|/ref|><|det|>[[144, 744, 632, 761]]<|/det|>
The Image Descriptor parameter in the GetImage request is empty.  

<|ref|>sub_title<|/ref|><|det|>[[114, 776, 564, 795]]<|/det|>
## AVRCP/CT/CA/BV-15-C [Cover Art SDP record - CT]  

<|ref|>text<|/ref|><|det|>[[115, 804, 245, 820]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[141, 828, 879, 861]]<|/det|>
Verify that the IUT can retrieve the AVRCP SDP record to determine the PSM on which the Cover Art OBEX service is running.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 72, 268, 139]]<|/det|>
Reference [8] 8 [10] 3.4 [11] 5.4 Initial Condition  

<|ref|>text<|/ref|><|det|>[[115, 171, 125, 183]]<|/det|>  

<|ref|>text<|/ref|><|det|>[[142, 195, 732, 237]]<|/det|>
- An L2CAP connection for SDP exists between the IUT and the Lower Tester.  
- The IUT is acting as AVRCP CT role in category 1.  

<|ref|>text<|/ref|><|det|>[[115, 248, 260, 264]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 271, 830, 305]]<|/det|>
1. The Upper Tester triggers the IUT to issue an SDP query to the Lower Tester to retrieve the AVRCP Cover Art PSM from the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[142, 306, 829, 322]]<|/det|>
2. The Lower Tester issues an SDP response message conveying the AVRCP Cover Art PSM.  

<|ref|>text<|/ref|><|det|>[[142, 322, 856, 355]]<|/det|>
3. The IUT creates an L2CAP channel on the PSM associated with the AVRCP Cover Art and then issues an OBEX CONNECT request on it.  

<|ref|>text<|/ref|><|det|>[[142, 356, 830, 389]]<|/det|>
4. Upon receipt of an OBEX CONNECT request the Lower Tester issues an appropriate OBEX CONNECT response.  

<|ref|>image<|/ref|><|det|>[[145, 397, 699, 662]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 670, 617, 686]]<|/det|>
<center>Figure 4.83: AVRCP/CT/CA/BV-15-C [Cover Art SDP record - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 701, 285, 717]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 725, 238, 740]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 748, 681, 764]]<|/det|>
The IUT uses SDP to request the PSM associated with AVRCP Cover Art.  

<|ref|>text<|/ref|><|det|>[[142, 771, 876, 788]]<|/det|>
The IUT creates an L2CAP channel on the PSM published in the Lower Tester's AVRCP SDP record.  

<|ref|>text<|/ref|><|det|>[[144, 795, 754, 812]]<|/det|>
The IUT issues an OBEX CONNECT [0x80] request on the created L2CAP channel.  

<|ref|>sub_title<|/ref|><|det|>[[115, 828, 565, 847]]<|/det|>
## AVRCP/TG/CA/BV-16-C [Cover Art SDP record - TG]  

<|ref|>text<|/ref|><|det|>[[115, 856, 245, 872]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 880, 850, 913]]<|/det|>
Verify that the IUT correctly publishes an AVRCP SDP record indicating support for the Cover Art feature and the PSM on which the Cover Art OBEX service is running.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 267, 139]]<|/det|>
Reference [8] 8 [10] 3.4 [11] 5.4 Initial Condition  

<|ref|>text<|/ref|><|det|>[[115, 172, 125, 184]]<|/det|>  

<|ref|>text<|/ref|><|det|>[[142, 196, 730, 237]]<|/det|>
- An L2CAP connection for SDP exists between the IUT and the Lower Tester.- The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[115, 248, 260, 264]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 271, 870, 305]]<|/det|>
1. The Lower Tester issues an SDP query to the IUT to retrieve the AVRCP Cover Art PSM from the IUT.  

<|ref|>text<|/ref|><|det|>[[142, 306, 760, 322]]<|/det|>
2. The IUT issues an SDP response message conveying the AVRCP Cover Art PSM.  

<|ref|>text<|/ref|><|det|>[[142, 323, 833, 356]]<|/det|>
3. The Lower Tester issues an OBEX CONNECT request on an L2CAP channel created on the PSM associated with AVRCP Cover Art obtained from the IUT after Step 2.  

<|ref|>text<|/ref|><|det|>[[142, 356, 844, 389]]<|/det|>
4. Upon receipt of an OBEX CONNECT request the IUT issues an appropriate OBEX CONNECT response.  

<|ref|>image<|/ref|><|det|>[[144, 396, 712, 644]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 652, 618, 667]]<|/det|>
<center>Figure 4.84: AVRCP/TG/CA/BV-16-C [Cover Art SDP record - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 682, 287, 698]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 707, 237, 722]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 730, 816, 763]]<|/det|>
The IUT responds with an appropriate SDP response, which contains the requested attribute containing the L2CAP PSM associated with AVRCP Cover Art.  

<|ref|>text<|/ref|><|det|>[[144, 765, 768, 782]]<|/det|>
The OBEX CONNECT response from the IUT is well- formatted and indicates success.  

<|ref|>sub_title<|/ref|><|det|>[[115, 802, 649, 820]]<|/det|>
## AVRCP/CT/CA/BV-17-C [UIDs Changed during Cover Art - CT]  

<|ref|>text<|/ref|><|det|>[[115, 830, 245, 846]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 854, 861, 903]]<|/det|>
Verify that when there is an OBEX Cover Art connection and the Lower Tester is a database aware player, the IUT disconnects OBEX connection when Lower Tester issues a UIDs Changed notification.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 223, 88]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 96, 366, 113]]<|/det|>
[8] 6.10.3.3, 6.10.4.2, 6.10.4.3  

<|ref|>text<|/ref|><|det|>[[144, 121, 207, 136]]<|/det|>
[9] 4.5.8  

<|ref|>text<|/ref|><|det|>[[115, 146, 259, 161]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 171, 660, 188]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 195, 801, 229]]<|/det|>
- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.  

<|ref|>text<|/ref|><|det|>[[144, 231, 864, 265]]<|/det|>
- There is an active Cover Art OBEX connection where the IUT is the OBEX client and the Lower Tester is the OBEX server.  

<|ref|>text<|/ref|><|det|>[[144, 268, 543, 284]]<|/det|>
The IUT is acting as AVRCP CT role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 291, 866, 325]]<|/det|>
- The Browsed Player and the default Addressed Player at the Lower Tester are the same player, called the Cover Art Player.  

<|ref|>text<|/ref|><|det|>[[144, 332, 812, 349]]<|/det|>
- At least one item with Cover Art is available in the default folder on the Cover Art Player.  

<|ref|>text<|/ref|><|det|>[[144, 355, 470, 371]]<|/det|>
- The Cover Art Player is database-aware.  

<|ref|>text<|/ref|><|det|>[[144, 378, 833, 412]]<|/det|>
- The IUT has registered for a UIDs Changed notification via the AVRCP RegisterNotification command.  

<|ref|>text<|/ref|><|det|>[[115, 435, 259, 450]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[140, 459, 848, 491]]<|/det|>
1. The Lower Tester issues a Register Notification response message to the IUT with the EventID parameter set to EVENT_UIDS_CHANGED.  

<|ref|>text<|/ref|><|det|>[[140, 492, 861, 525]]<|/det|>
2. As a result of receiving notification, the IUT issues an OBEX DISCONNECT request to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[140, 526, 840, 560]]<|/det|>
3. The Lower Tester sends an appropriate OBEX DISCONNECT response to the IUT, and upon successful response, the OBEX connection is disconnected.  

<|ref|>text<|/ref|><|det|>[[140, 560, 844, 593]]<|/det|>
4. The IUT issues an AVRCP RegisterNotification command to the Lower Tester with the EventID parameter set to EVENT_UIDS_CHANGED to register again for notification of UID changes.  

<|ref|>text<|/ref|><|det|>[[140, 594, 861, 643]]<|/det|>
5. The Lower Tester issues an appropriate AVRCP RegisterNotification interim response to the IUT. Note that the OBEX DISCONNECT transaction in Steps 2–3 and the Register notification transaction in Steps 4–5 can occur in either order.  

<|ref|>text<|/ref|><|det|>[[140, 644, 830, 676]]<|/det|>
6. Subsequent to successful disconnection, the IUT issues an OBEX CONNECT request to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[140, 677, 810, 710]]<|/det|>
7. The Lower Tester sends an appropriate OBEX CONNECT response to the IUT, and upon successful response, the OBEX connection is established.  

<|ref|>text<|/ref|><|det|>[[140, 711, 825, 744]]<|/det|>
8. The IUT issues a request for a Cover Art Image Handle to the Lower Tester using either the AVRCP GetFolderItems or GetItemAttributes command.  

<|ref|>text<|/ref|><|det|>[[140, 745, 797, 778]]<|/det|>
9. The Lower Tester sends an appropriate response to the command from Step 8, which if successful, contains a Cover Art Image Handle.  

<|ref|>text<|/ref|><|det|>[[140, 778, 866, 812]]<|/det|>
10. The IUT sends a GetImage or GetLinkedThumbnail request to the Lower Tester with the Image Handle parameter set to the handle received in Step 9.  

<|ref|>text<|/ref|><|det|>[[140, 812, 872, 845]]<|/det|>
11. The Lower Tester sends an appropriate GetImage or GetLinkedThumbnail response message to the IUT, which if successful, contains the requested image.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[146, 70, 712, 480]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 487, 683, 503]]<|/det|>
<center>Figure 4.85: AVRCP/CT/CA/BV-17-C [UIDs Changed during Cover Art – CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[116, 519, 285, 534]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[145, 543, 238, 558]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[145, 565, 655, 582]]<|/det|>
The IUT issues a well- formed and valid OBEX DISCONNECT request.  

<|ref|>text<|/ref|><|det|>[[144, 590, 830, 622]]<|/det|>
The IUT issues a well- formed RegisterNotification command with the EventID parameter set to EVENT_UIDS_CHANGED.  

<|ref|>text<|/ref|><|det|>[[145, 626, 627, 642]]<|/det|>
The IUT issues a well- formed and valid OBEX CONNECT request.  

<|ref|>text<|/ref|><|det|>[[144, 650, 777, 666]]<|/det|>
The IUT issues a well- formed and valid GetFolderltems or GetItemAttributes command.  

<|ref|>text<|/ref|><|det|>[[144, 673, 861, 707]]<|/det|>
The IUT issues a well- formed and valid GetImage request, with the Image Handle parameter set to the handle supplied by the Lower Tester.  

<|ref|>sub_title<|/ref|><|det|>[[115, 728, 818, 747]]<|/det|>
## AVRCP/CT/CA/BV-18-C [Database-Unaware Folder Change during Cover Art – CT]  

<|ref|>text<|/ref|><|det|>[[116, 756, 244, 771]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 779, 879, 812]]<|/det|>
Verify that when there is an OBEX Cover Art connection and the Lower Tester is a database- unaware player, then when the IUT changes folder, OBEX is disconnected by the IUT.  

<|ref|>text<|/ref|><|det|>[[116, 818, 223, 833]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 840, 412, 857]]<|/det|>
[8] 6.6.1, 6.10.4.1, 6.10.4.2, 6.10.4.3  

<|ref|>text<|/ref|><|det|>[[144, 864, 252, 879]]<|/det|>
[9] 4.5.8, 4.5.9=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 96, 870, 304]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- There is an active Cover Art OBEX connection where the IUT is the OBEX client and the Lower Tester is the OBEX server.- The IUT is acting as AVRCP CT role in category 1.- The Browsed Player and the default Addressed Player at the Lower Tester are the same player, called the Cover Art Player.- At least one item with Cover Art is available in the default folder on the Cover Art Player.- The Cover Art Player is database- unaware but supports browsing.  

<|ref|>sub_title<|/ref|><|det|>[[115, 320, 259, 336]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[140, 343, 870, 729]]<|/det|>
Test Procedure1. The Upper Tester triggers the IUT to issue a request for a Cover Art Image Handle to the Lower Tester using either the AVRCP GetFolderltems or GetItemAttributes command.2. The Lower Tester sends an appropriate response to the command from Step 1, which if successful, contains a Cover Art Image Handle.3. The IUT issues an AVRCP ChangePath command to the Lower Tester to navigate to another part of the virtual filesystem.4. The Lower Tester issues an appropriate ChangePath response message to the IUT.5. Upon receipt of a successful ChangePath response, the IUT issues an OBEX DISCONNECT request.6. The Lower Tester sends an appropriate OBEX DISCONNECT response to the IUT, and upon successful response, the OBEX connection is disconnected.7. Subsequent to successful disconnection, the IUT issues an OBEX CONNECT request to the Lower Tester.8. The Lower Tester sends an appropriate OBEX CONNECT response to the IUT, and upon successful response, the OBEX connection is established.9. The IUT issues a request for a Cover Art Image Handle to the Lower Tester using either the AVRCP GetAllFolderltems or GetItemAttributes commands.10. The Lower Tester sends an appropriate response to the command from Step 9, which if successful, contains a Cover Art Image Handle.11. The IUT sends a GetImage or GetLinkedThumbnail request to the Lower Tester with the Image Handle parameter set to the handle received in Step 10.12. The Lower Tester sends an appropriate GetImage or GetLinkedThumbnail response to the IUT, which if successful, contains the requested image.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[145, 70, 714, 483]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[142, 495, 813, 510]]<|/det|>
<center>Figure 4.86: AVRCP/CT/CA/BV-18-C [Database-Unaware Folder Change during Cover Art – CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[116, 526, 288, 542]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 550, 240, 565]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 573, 777, 590]]<|/det|>
The IUT issues a well- formed and valid GetFolderItems or GetItemAttributes command.  

<|ref|>text<|/ref|><|det|>[[144, 597, 605, 613]]<|/det|>
The IUT issues a well- formed and valid ChangePath command.  

<|ref|>text<|/ref|><|det|>[[144, 621, 655, 637]]<|/det|>
The IUT issues a well- formed and valid OBEX DISCONNECT request.  

<|ref|>text<|/ref|><|det|>[[144, 644, 627, 660]]<|/det|>
The IUT issues a well- formed and valid OBEX CONNECT request.  

<|ref|>text<|/ref|><|det|>[[144, 668, 857, 700]]<|/det|>
The IUT issues a well- formed and valid GetImage or GetLinkedThumbnail request, with the Image Handle parameter set to the handle supplied by the Lower Tester after OBEX reconnection.  

<|ref|>sub_title<|/ref|><|det|>[[115, 718, 860, 737]]<|/det|>
## AVRCP/TG/CA/BI-01-C [Retrieval of Cover Art attribute with no OBEX connection – TG]  

<|ref|>text<|/ref|><|det|>[[116, 745, 245, 761]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 769, 817, 801]]<|/det|>
Verify that when the Lower Tester attempts to retrieve the Cover Art attribute when no OBEX connection exists, the IUT does not return an image handle.  

<|ref|>text<|/ref|><|det|>[[115, 808, 223, 844]]<|/det|>
Reference [8] 6.10.4.2=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 96, 881, 277]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- No OBEX connection exists.- The IUT is acting as AVRCP TG role in category 1.- The Tester has successfully issued a SetBrowsedPlayer command to the player specified in [6] as the browsable player.- The Tester has successfully issued any necessary ChangePath commands to navigate to a folder on the Browsed Player of the IUT, containing at least one item with Cover Art [6].  

<|ref|>text<|/ref|><|det|>[[115, 296, 260, 312]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 320, 848, 353]]<|/det|>
The Lower Tester issues a GetFolderltems command to the IUT, with the scope parameter set to Virtual Media Player Filesystem, and the attribute list containing only the Cover Art attribute.  

<|ref|>image<|/ref|><|det|>[[150, 360, 714, 605]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 614, 839, 630]]<|/det|>
<center>Figure 4.87: AVRCP/TG/CA/BI-01-C [Retrieval of Cover Art attribute with no OBEX connection – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 645, 701, 732]]<|/det|>
Expected OutcomePass verdictThe IUT issues a well- formed GetFolderltems response.The number of returned items in the response is 0 and the Item List is empty.  

<|ref|>sub_title<|/ref|><|det|>[[115, 749, 864, 782]]<|/det|>
## AVRCP/TG/CA/BI-04-C [Retrieval of Cover Art attribute with no OBEX connection using GetItemAttributes - TG]  

<|ref|>text<|/ref|><|det|>[[115, 793, 245, 808]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 816, 866, 848]]<|/det|>
Verify that the IUT does not return an image handle, when the Lower Tester attempts to retrieve the Cover Art attribute using GetItemAttributes when no OBEX connection exists.  

<|ref|>text<|/ref|><|det|>[[115, 854, 223, 890]]<|/det|>
Reference [8] 6.10.4.3=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 96, 880, 279]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- No OBEX connection exists.- The IUT is acting as AVRCP TG role in category 1.- The Tester has successfully issued a SetBrowseredPlayer command to the player specified in the IXIT [6] as the browsable player.- The Tester has successfully issued any necessary ChangePath commands to navigate to a folder on the Browsed Player of the IUT, containing at least one item with Cover Art [6].  

<|ref|>text<|/ref|><|det|>[[115, 296, 259, 312]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 320, 877, 353]]<|/det|>
The Lower Tester issues a valid GeltlemAttributes command to the IUT with the scope parameter set to Virtual Media Player Filesystem and the AttributeID list containing only the Cover Art AttributeID.  

<|ref|>image<|/ref|><|det|>[[150, 360, 714, 606]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 613, 800, 641]]<|/det|>
<center>Figure 4.88: AVRCP/TG/CA/BI-04-C [Retrieval of Cover Art attribute with no OBEX connection using GeltlemAttributes - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 659, 285, 675]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 684, 238, 699]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 707, 567, 723]]<|/det|>
The IUT issues a well- formed GeltlemAttributes response.  

<|ref|>text<|/ref|><|det|>[[142, 730, 881, 763]]<|/det|>
The GeltlemAttributes response does not contain an Attribute Value for the Cover Art attribute for any elements.  

<|ref|>sub_title<|/ref|><|det|>[[115, 780, 863, 813]]<|/det|>
## AVRCP/TG/CA/BI-05-C [Retrieval of Cover Art attribute with no OBEX connection using GetElementAttributes - TG]  

<|ref|>text<|/ref|><|det|>[[115, 823, 244, 839]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 847, 866, 879]]<|/det|>
Verify that the IUT does not return an image handle, when the Lower Tester attempts to retrieve the Cover Art attribute using GetElementAttributes when no OBEX connection exists.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 223, 88]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 97, 206, 113]]<|/det|>
[8] 6.6.1  

<|ref|>text<|/ref|><|det|>[[115, 123, 260, 138]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 147, 803, 261]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control channel between the IUT and the Lower Tester is established.- No OBEX connection exists.- The IUT is acting as AVRCP TG role in category 1.- An item with Cover Art is currently playing on the default Addressed Player on the IUT.  

<|ref|>text<|/ref|><|det|>[[115, 273, 260, 288]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 296, 816, 329]]<|/det|>
The Lower Tester issues a valid GetElementAttributes command to the IUT with the identifier parameter set to Playing and the AttributeID list containing only the Cover Art AttributeID.  

<|ref|>image<|/ref|><|det|>[[149, 336, 714, 584]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 592, 800, 619]]<|/det|>
<center>Figure 4.89: AVRCP/TG/CA/BI-05-C [Retrieval of Cover Art attribute with no OBEX connection using GetElementAttributes - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 636, 290, 652]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 661, 238, 676]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 684, 595, 700]]<|/det|>
The IUT issues a well- formed GetElementAttributes response.  

<|ref|>text<|/ref|><|det|>[[140, 707, 857, 724]]<|/det|>
The GetElementAttributes response does not contain an Attribute Value for the Cover Art attribute.  

<|ref|>sub_title<|/ref|><|det|>[[115, 739, 688, 758]]<|/det|>
## AVRCP/TG/CA/BI-06-C [Request of Unsupported Image Type - TG]  

<|ref|>text<|/ref|><|det|>[[115, 767, 863, 810]]<|/det|>
- Test PurposeVerify that when the IUT receives a request for an unsupported image type it can respond correctly.  

<|ref|>text<|/ref|><|det|>[[115, 818, 223, 834]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 842, 207, 857]]<|/det|>
[9] 4.5.8=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 96, 870, 420]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- There is an active Cover Art OBEX connection where the IUT is the OBEX server and the Lower Tester is the OBEX client.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester is aware of the currently valid Media Item UIDs on the IUT. This can be achieved by executing AVRCP/TG/MCN/CB/BV-02-C [GetFolderItems - TG].- The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.- The Lower Tester has successfully issued any necessary ChangePath commands to navigate to a folder on the Browsed Player of the IUT containing at least one item with Cover Art [6].- The Lower Tester has issued a GetItemAttributes command to the IUT with the scope parameter set to Virtual Media Player Filesystem and valid entries for UID, UIDcounter, Number of Attributes and AttributeID list. The AttributeID list contains the Cover Art AttributeID.- The Lower Tester issues a GetImageProperties to receive the imaging properties supported by the IUT.  

<|ref|>sub_title<|/ref|><|det|>[[116, 451, 259, 467]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 475, 870, 541]]<|/det|>
The Lower Tester issues a well- formed GetImage request to the IUT, with the Image Handle set to a valid handle discovered during the setup of the initial condition, and an Image Descriptor parameter describing an image format unsupported by the IUT, according to the imaging properties received in the Initial Conditions.  

<|ref|>image<|/ref|><|det|>[[152, 550, 707, 816]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 825, 711, 841]]<|/det|>
<center>Figure 4.90: AVRCP/TG/CA/BI-06-C [Request of Unsupported Image Type - TG] MSC </center>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 285, 88]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 97, 238, 112]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 120, 511, 136]]<|/det|>
The IUT issues a well- formed GetImage response.  

<|ref|>text<|/ref|><|det|>[[144, 143, 828, 160]]<|/det|>
The GetImage response contains a well- formed OBEX error code (e.g., 'Not Acceptable', etc.).  

<|ref|>sub_title<|/ref|><|det|>[[112, 176, 840, 195]]<|/det|>
## AVRCP/TG/CA/BI-07-C [Request of Unsupported Image Type without browsing - TG]  

<|ref|>text<|/ref|><|det|>[[115, 204, 245, 219]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 227, 863, 245]]<|/det|>
Verify that when the IUT receives a request for an unsupported image type it can respond correctly.  

<|ref|>text<|/ref|><|det|>[[115, 253, 223, 269]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 277, 207, 292]]<|/det|>
[9] 4.5.8  

<|ref|>text<|/ref|><|det|>[[115, 302, 259, 318]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[141, 328, 872, 515]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control channel between the IUT and the Lower Tester is established.- There is an active Cover Art OBEX connection where the IUT is the OBEX server and the Lower Tester is the OBEX client.- The IUT is acting as AVRCP TG role in category 1.- An item with Cover Art is currently playing on the Addressed Player on the IUT. The tester issues the getElementAttributes command to the IUT.- The Lower Tester issues a GetImageProperties to receive the imaging properties supported by the IUT.  

<|ref|>text<|/ref|><|det|>[[115, 528, 259, 543]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 551, 870, 616]]<|/det|>
The Lower Tester issues a well- formed GetImage request to the IUT, with the Image Handle set to a valid handle discovered during the setup of the initial condition, and an Image Descriptor parameter describing an image format unsupported by the IUT, according to the imaging properties received in the Initial Conditions.  

<|ref|>image<|/ref|><|det|>[[149, 625, 707, 892]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 900, 825, 916]]<|/det|>
<center>Figure 4.91: AVRCP/TG/CA/BI-07-C [Request of Unsupported Image Type withou t browsing - TG] MSC </center>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 288, 89]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 97, 238, 113]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 120, 510, 137]]<|/det|>
The IUT issues a well- formed GetImage response.  

<|ref|>sub_title<|/ref|><|det|>[[112, 151, 800, 170]]<|/det|>
## AVRCP/TG/CA/BI-08-C [Use GetFolderltems to request Cover Art attribute - TG]  

<|ref|>text<|/ref|><|det|>[[115, 179, 245, 195]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 202, 865, 253]]<|/det|>
Verify that when the Lower Tester attempts to retrieve the Cover Art attribute using GetFolderltems, and when no item in the selected folder has associated Cover Art, then the IUT does not return an image handle.  

<|ref|>text<|/ref|><|det|>[[115, 262, 223, 278]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 286, 230, 302]]<|/det|>
[8] 6.10.4.2  

<|ref|>text<|/ref|><|det|>[[144, 310, 207, 326]]<|/det|>
[9] 4.4.4  

<|ref|>text<|/ref|><|det|>[[115, 336, 260, 352]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 360, 890, 576]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester. The AVCTP control and browsing channels between the IUT and the Lower Tester are established.- There is an active Cover Art OBEX connection where the IUT is the OBEX server and the Lower Tester is the OBEX client.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in the IXIT [6] as the browsable player.- The Lower Tester has successfully issued any necessary ChangePath commands to navigate to a folder on the Browsed Player of the IUT, containing only items with no associated Cover Art as specified in the IXIT [6].  

<|ref|>text<|/ref|><|det|>[[115, 593, 259, 608]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 617, 842, 651]]<|/det|>
The Lower Tester issues a GetFolderltems command to the IUT with the scope parameter set to Virtual Media Player Filesystem and the attribute list containing the Cover Art attribute.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[150, 68, 714, 316]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 324, 794, 340]]<|/det|>
<center>Figure 4.92: AVRCP/TG/CA/BI-08-C [Use GetFoldertems to request Cover Art attribute – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 356, 288, 372]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 380, 238, 396]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 403, 785, 420]]<|/det|>
The IUT issues a well-formatted GetFoldertems response message to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 427, 755, 443]]<|/det|>
The GetFoldertems response message does not contain a Cover Art Image Handle.  

<|ref|>text<|/ref|><|det|>[[115, 454, 191, 469]]<|/det|>
- Notes  

<|ref|>text<|/ref|><|det|>[[142, 477, 842, 510]]<|/det|>
Note that although the test does not directly use the Cover Art OBEX connection it must exist for there to be valid Image Handles available on the TG (Imaging Responder).  

<|ref|>sub_title<|/ref|><|det|>[[112, 526, 819, 545]]<|/det|>
## AVRCP/TG/CA/BI-09-C [Use GettemAttributes to request Cover Art attribute – TG]  

<|ref|>text<|/ref|><|det|>[[115, 554, 245, 570]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 578, 879, 627]]<|/det|>
Verify that when the Lower Tester attempts to retrieve the Cover Art attribute using GettemAttributes, and when the selected item has no associated Cover Art, then the IUT does not return an image handle.  

<|ref|>text<|/ref|><|det|>[[115, 636, 223, 652]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 660, 230, 676]]<|/det|>
[8] 6.10.4.3  

<|ref|>text<|/ref|><|det|>[[144, 684, 207, 700]]<|/det|>
[9] 4.5.8  

<|ref|>text<|/ref|><|det|>[[115, 710, 260, 725]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 737, 872, 880]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control channel between the IUT and the Lower Tester is established.- There is an active Cover Art OBEX connection where the IUT is the OBEX server and the Lower Tester is the OBEX client.- The IUT is acting as AVRCP TG role in category 1.- The Lower Tester is aware of the currently valid Media Item UIDs on the IUT. This can be achieved by executing AVRCP/TG/MCN/CB/BV-02-C [GetFoldertems – TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[142, 70, 875, 142]]<|/det|>
- The Lower Tester has successfully issued a SetBrowsedPlayer command to the player specified in [6] as the browsable player.- The Lower Tester has successfully issued any necessary ChangePath commands to navigate to a folder on the Browsed Player on the IUT containing only items with no associated Cover Art [6].  

<|ref|>sub_title<|/ref|><|det|>[[115, 155, 259, 170]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 179, 863, 228]]<|/det|>
The Lower Tester issues a GettlemAttributes command to the IUT, with the scope parameter set to Virtual Media Player Filesystem, and valid entries for UID, UIDcounter, Number of Attributes and AttributeID list. The AttributeID list contains the Cover Art AttributeID.  

<|ref|>image<|/ref|><|det|>[[145, 237, 700, 483]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 491, 806, 506]]<|/det|>
<center>Figure 4.93: AVRCP/TG/CA/BI-09-C [Use GettlemAttributes to request Cover Art attribute – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 522, 288, 538]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 546, 250, 562]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 570, 800, 586]]<|/det|>
The IUT issues a well- formatted GettlemAttributes response message to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 594, 770, 610]]<|/det|>
The GettlemAttributes response message does not contain a Cover Art Image Handle.  

<|ref|>sub_title<|/ref|><|det|>[[115, 625, 852, 644]]<|/det|>
## AVRCP/TG/CA/BI-10-C [Use GetElementAttributes to request Cover Art attribute – TG]  

<|ref|>text<|/ref|><|det|>[[115, 653, 245, 668]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 676, 860, 725]]<|/det|>
Verify that when the Lower Tester attempts to retrieve the Cover Art attribute using GetElementAttributes with the Playing identifier, and when the selected element has no associated Cover Art, that the IUT does not return an image handle.  

<|ref|>text<|/ref|><|det|>[[115, 735, 228, 750]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 759, 206, 774]]<|/det|>
[8] 6.6.1  

<|ref|>text<|/ref|><|det|>[[115, 784, 259, 799]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 811, 870, 893]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP control channel between the IUT and the Lower Tester is established.- There is an active Cover Art OBEX connection where the IUT is the OBEX server and the Lower Tester is the OBEX client.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[144, 70, 544, 88]]<|/det|>
- The IUT is acting as AVRCP TG role in category 1.  

<|ref|>text<|/ref|><|det|>[[144, 94, 835, 112]]<|/det|>
- An item with no associated Cover Art is playing on the default Addressed Player at the IUT.  

<|ref|>text<|/ref|><|det|>[[116, 122, 260, 138]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 145, 857, 179]]<|/det|>
The Lower Tester issues a GetElementAttributes command to the IUT with the identifier parameter set to Playing and the AttributeID list containing the Cover Art AttributeID.  

<|ref|>image<|/ref|><|det|>[[150, 186, 714, 433]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[142, 440, 834, 457]]<|/det|>
<center>Figure 4.94: AVRCP/TG/CA/BI-10-C [Use GetElementAttributes to request Cover Art attribute – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[116, 472, 287, 488]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 497, 238, 512]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 520, 830, 537]]<|/det|>
The IUT issues a well- formatted GetElementAttributes response message to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 543, 800, 560]]<|/det|>
The GetElementAttributes response message does not contain a Cover Art Image Handle.  

<|ref|>sub_title<|/ref|><|det|>[[114, 575, 504, 596]]<|/det|>
### 4.12 Media Player Selection tests  

<|ref|>title<|/ref|><|det|>[[116, 599, 169, 616]]<|/det|>
#### 4.12.1  

<|ref|>sub_title<|/ref|><|det|>[[202, 606, 519, 625]]<|/det|>
## Listing of available Media Players  

<|ref|>text<|/ref|><|det|>[[116, 635, 245, 651]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 658, 847, 676]]<|/det|>
CT: Verify that the CT is able to request the list of available Media Players announced by the TG.  

<|ref|>text<|/ref|><|det|>[[144, 682, 684, 700]]<|/det|>
TG: Verify that the TG returns the complete list of available Media Players.  

<|ref|>text<|/ref|><|det|>[[116, 708, 228, 750]]<|/det|>
- Reference 
[5] 5.9, 6.9  

<|ref|>text<|/ref|><|det|>[[116, 759, 260, 775]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 785, 455, 802]]<|/det|>
- A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[116, 813, 325, 829]]<|/det|>
- Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[150, 836, 646, 904]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MPS/BV-04-C [Listing of available Media Players]</td></tr><tr><td>AVRCP/TG/MPS/BV-01-C [Listing of available Media Players]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 908, 506, 923]]<|/det|>
Table 4.6: Listing of available Media Players test cases=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 707, 137]]<|/det|>
- Test ProcedureCT: Initiate the action on the CT to list the Media Players available on the TG.TG: No action is required.  

<|ref|>text<|/ref|><|det|>[[115, 146, 655, 211]]<|/det|>
- Expected OutcomePass verdictThe CT displays the list of Media Players that are available on the TG.  

<|ref|>title<|/ref|><|det|>[[115, 225, 470, 243]]<|/det|>
#### 4.12.2 Availability of Media Players  

<|ref|>text<|/ref|><|det|>[[115, 253, 848, 364]]<|/det|>
- Test PurposeCT: Verify that the CT is able to access each Media Player announced as available by the TG.TG: Verify that each Media Player announced by the TG can be accessed without additional user interaction on the TG device.  

<|ref|>text<|/ref|><|det|>[[115, 368, 260, 404]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 420, 844, 478]]<|/det|>
- A connection for control is established.- The list of available Media Players is available on the CT. This can be retrieved by executing AVRCP/CT/MPS/BV-0 - Listing of available Media Players.  

<|ref|>text<|/ref|><|det|>[[115, 487, 325, 503]]<|/det|>
- Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[146, 512, 586, 577]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MPS/BV-05-C [Availability of Media Players]</td></tr><tr><td>AVRCP/TG/MPS/BV-08-C [Availability of Media Players]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[146, 584, 473, 598]]<|/det|>
Table 4.7: Availability of Media Players test cases  

<|ref|>text<|/ref|><|det|>[[115, 614, 260, 630]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[141, 637, 850, 672]]<|/det|>
CT: For each Media Player in the list of available Media Players, initiate an action on the CT, e.g., browsing or playing a title.  

<|ref|>text<|/ref|><|det|>[[144, 675, 335, 692]]<|/det|>
TG: No action is required.  

<|ref|>text<|/ref|><|det|>[[115, 701, 287, 718]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 726, 238, 741]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 750, 836, 783]]<|/det|>
An action can be performed on each of the available Media Players without any user interaction required on the TG device.  

<|ref|>title<|/ref|><|det|>[[115, 799, 647, 819]]<|/det|>
#### 4.12.3 PASS THROUGH functionality of Media Players  

<|ref|>text<|/ref|><|det|>[[115, 828, 245, 844]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 851, 700, 868]]<|/det|>
CT: Verify that the CT can send the PASS THROUGH commands to the TG.  

<|ref|>text<|/ref|><|det|>[[144, 875, 805, 925]]<|/det|>
TG: Verify that each Media Player on the TG reacts to the PASS THROUGH commands as announced in the IXIT [6] according to the operation_id list table in Section 6 Appendix A - Operation_id list tables.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 223, 88]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 97, 270, 113]]<|/det|>
[5] 5.9, 4.4.1, 4.5  

<|ref|>text<|/ref|><|det|>[[115, 123, 260, 138]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 147, 843, 205]]<|/det|>
- A connection for control is established.- The list of available Media Players is available on the CT. This can be retrieved by executing AVRCP/CT/MPS/BV-0 - Listing of available Media Players.  

<|ref|>text<|/ref|><|det|>[[115, 215, 325, 231]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 240, 765, 304]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MPS/BV-06-C [PASS THROUGH functionality of Media Players]</td></tr><tr><td>AVRCP/TG/MPS/BV-03-C [PASS THROUGH functionality of Media Players]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 310, 600, 325]]<|/det|>
Table 4.8: PASS THROUGH functionality of Media Players test cases  

<|ref|>text<|/ref|><|det|>[[115, 341, 260, 357]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 365, 881, 400]]<|/det|>
CT: Initiate the required user actions (e.g., press button) to perform all operations that are listed in the IXIT MediaPlayerFeature table for each Media Player in [6].  

<|ref|>text<|/ref|><|det|>[[144, 402, 333, 417]]<|/det|>
TG: No action is required.  

<|ref|>text<|/ref|><|det|>[[115, 428, 285, 444]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 453, 237, 468]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 475, 838, 525]]<|/det|>
The TG reacts to all performed PASS THROUGH commands sent from the CT according to the "Expected operation to be performed by the TG" of the section "operation_id list" in Section 6 Appendix A - Operation_id list tables without any user interaction on the TG.  

<|ref|>sub_title<|/ref|><|det|>[[115, 545, 772, 566]]<|/det|>
### 4.13 Media Content Navigation tests for Content Browsing  

<|ref|>title<|/ref|><|det|>[[115, 569, 177, 585]]<|/det|>
#### 4.13.1  

<|ref|>sub_title<|/ref|><|det|>[[202, 577, 486, 595]]<|/det|>
## Browsing of the current folder  

<|ref|>text<|/ref|><|det|>[[115, 605, 244, 620]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 628, 688, 667]]<|/det|>
CT: Verify that the CT is able to browse the current folder on the TG. TG: Verify that the TG correctly browses the current folder requested by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 678, 223, 694]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 702, 202, 718]]<|/det|>
[5] 5.13  

<|ref|>text<|/ref|><|det|>[[115, 728, 260, 743]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 755, 748, 795]]<|/det|>
- A connection for control is established.- An appropriate folder for browsing media content on the TG has been selected.  

<|ref|>text<|/ref|><|det|>[[115, 806, 325, 822]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 831, 645, 898]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MCN/CB/BV-08-C [Browsing of the current folder]</td></tr><tr><td>AVRCP/TG/MCN/CB/BV-01-C [Browsing of the current folder]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 902, 480, 916]]<|/det|>
Table 4.9: Browsing of the current folder test cases=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[141, 96, 872, 130]]<|/det|>
CT: Initiate the action on the CT to browse through the media content of the currently selected folder on the TG.  

<|ref|>text<|/ref|><|det|>[[144, 134, 333, 149]]<|/det|>
TG: No action is required.  

<|ref|>text<|/ref|><|det|>[[115, 160, 285, 175]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 184, 238, 199]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 207, 523, 223]]<|/det|>
The expected media content is displayed on the CT.  

<|ref|>title<|/ref|><|det|>[[115, 242, 325, 260]]<|/det|>
#### 4.13.2 Browsing up  

<|ref|>text<|/ref|><|det|>[[115, 270, 245, 285]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 294, 721, 310]]<|/det|>
CT: Verify that the CT is able to browse into the superordinate folder on the TG.  

<|ref|>text<|/ref|><|det|>[[140, 317, 825, 334]]<|/det|>
TG: Verify that the TG correctly browses into the superordinate folder as requested by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 344, 222, 359]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 367, 202, 382]]<|/det|>
[5] 5.13  

<|ref|>text<|/ref|><|det|>[[115, 393, 259, 408]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 420, 855, 460]]<|/det|>
- A connection for control is established.  
- A folder on the TG has been selected as current folder that actually has a superordinate folder.  

<|ref|>text<|/ref|><|det|>[[115, 471, 324, 487]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 495, 530, 560]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MCN/CB/BV-02-C [Browsing up]</td></tr><tr><td>AVRCP/TG/MCN/CB/BV-14-C [Browsing up]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[145, 567, 377, 581]]<|/det|>
Table 4.10: Browsing up test cases  

<|ref|>text<|/ref|><|det|>[[115, 597, 260, 612]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 621, 857, 655]]<|/det|>
CT: Initiate the action on the CT to change into the folder superior to the current folder in the folder hierarchy ('folder up').  

<|ref|>text<|/ref|><|det|>[[144, 658, 333, 673]]<|/det|>
TG: No action is required.  

<|ref|>text<|/ref|><|det|>[[115, 684, 285, 699]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 708, 238, 722]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 731, 574, 747]]<|/det|>
The CT indicates the superordinate folder as current folder.  

<|ref|>title<|/ref|><|det|>[[115, 766, 352, 784]]<|/det|>
#### 4.13.3 Browsing down  

<|ref|>text<|/ref|><|det|>[[115, 794, 245, 809]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 817, 877, 833]]<|/det|>
CT: Verify that the CT is able to change into a subfolder of the current folder on the TG and browse it.  

<|ref|>text<|/ref|><|det|>[[142, 841, 872, 874]]<|/det|>
TG: Verify that the TG correctly changes into a subfolder and returns its content as requested by the CT.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 74, 223, 88]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[145, 97, 203, 113]]<|/det|>
[5] 5.13  

<|ref|>text<|/ref|><|det|>[[115, 123, 260, 138]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 148, 857, 188]]<|/det|>
- A connection for control is established.- A folder on the TG has been selected as current folder that actually has at least one subfolder.  

<|ref|>text<|/ref|><|det|>[[115, 199, 325, 215]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[145, 224, 589, 288]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MCN/CB/BV-03-C [Browsing down]</td></tr><tr><td>AVRCP/TG/MCN/CB/BV-15-C [Browsing down]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[145, 295, 395, 310]]<|/det|>
Table 4.11: Browsing down test cases  

<|ref|>text<|/ref|><|det|>[[115, 325, 260, 341]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 349, 878, 383]]<|/det|>
CT: Initiate the action on the CT to change into one of the subfolders of the current folder in the folder hierarchy ('folder down').  

<|ref|>text<|/ref|><|det|>[[145, 385, 333, 401]]<|/det|>
TG: No action is required.  

<|ref|>text<|/ref|><|det|>[[115, 412, 287, 428]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 436, 238, 451]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 459, 560, 475]]<|/det|>
The CT indicates the selected subfolder as current folder.  

<|ref|>sub_title<|/ref|><|det|>[[115, 494, 750, 513]]<|/det|>
#### 4.13.4 Playing of a track from the Virtual Media Player Filesystem  

<|ref|>text<|/ref|><|det|>[[115, 522, 245, 538]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 546, 880, 579]]<|/det|>
CT: Verify that the CT is able to start playback of a track offered by the TG in the Virtual Media Player Filesystem and correctly displays the Now Playing list.  

<|ref|>text<|/ref|><|det|>[[144, 582, 870, 617]]<|/det|>
TG: Verify that the TG correctly plays a track from the Virtual Media Player Filesystem requested by the CT and updates the Now Playing folder accordingly.  

<|ref|>text<|/ref|><|det|>[[115, 621, 223, 636]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[145, 644, 201, 659]]<|/det|>
[5] 5.10  

<|ref|>text<|/ref|><|det|>[[145, 668, 260, 683]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[115, 685, 123, 696]]<|/det|>  

<|ref|>text<|/ref|><|det|>[[144, 707, 455, 723]]<|/det|>
A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[144, 730, 866, 764]]<|/det|>
A folder on the TG has been selected as current folder that actually contains at least one media track.  

<|ref|>text<|/ref|><|det|>[[115, 774, 325, 790]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[145, 799, 881, 863]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MC/N/CB/BV-10-C [Playing of a track from the Virtual Media Player Filesystem]</td></tr><tr><td>AVRCP/TG/MC/N/CB/BV-04-C [Playing of a track from the Virtual Media Player Filesystem]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 870, 677, 885]]<|/det|>
Table 4.12: Playing of a track from the Virtual Media Player Filesystem test cases=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 96, 775, 113]]<|/det|>
CT: Initiate the action on the CT to start playback of a track from the Virtual Filesystem.  

<|ref|>text<|/ref|><|det|>[[144, 120, 333, 137]]<|/det|>
TG: No action is required.  

<|ref|>text<|/ref|><|det|>[[115, 146, 285, 162]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 170, 238, 185]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 193, 475, 209]]<|/det|>
The desired media track is played on the TG.  

<|ref|>sub_title<|/ref|><|det|>[[115, 224, 454, 243]]<|/det|>
## 4.13.5 Change in media database  

<|ref|>text<|/ref|><|det|>[[115, 253, 245, 269]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 277, 714, 294]]<|/det|>
CT: Verify that the CT correctly handles a database change notified by the TG.  

<|ref|>text<|/ref|><|det|>[[144, 300, 832, 334]]<|/det|>
TG: Verify that the TG correctly handles a change within its media database (e.g., exchange of memory card).  

<|ref|>text<|/ref|><|det|>[[115, 338, 223, 353]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 360, 256, 376]]<|/det|>
[5], [8] 6.10.3.1  

<|ref|>text<|/ref|><|det|>[[115, 384, 260, 400]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 419, 460, 436]]<|/det|>
A Connection for control is established.  

<|ref|>text<|/ref|><|det|>[[144, 443, 842, 479]]<|/det|>
The CT has already accessed part of the database on the TG. This can be achieved e.g., by executing AVRCP/CT/MCN/CB/BV- 0 - Browsing of the current folder.  

<|ref|>text<|/ref|><|det|>[[115, 488, 324, 504]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[146, 512, 645, 576]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MCN/CB/BV-05-C [Change in media database]</td></tr><tr><td>AVRCP/TG/MCN/CB/BV-16-C [Change in media database]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[145, 583, 471, 597]]<|/det|>
Table 4.13: Change in media database test cases  

<|ref|>text<|/ref|><|det|>[[115, 614, 260, 630]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 638, 331, 654]]<|/det|>
CT: No action is required.  

<|ref|>text<|/ref|><|det|>[[144, 661, 682, 678]]<|/det|>
TG: Initiate the action on the TG to apply a change to the media database.  

<|ref|>text<|/ref|><|det|>[[115, 687, 285, 702]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 711, 238, 726]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 734, 803, 768]]<|/det|>
The CT indicates it correctly handles the database change on the TG, e.g., by updating the information displayed.  

<|ref|>sub_title<|/ref|><|det|>[[115, 782, 513, 801]]<|/det|>
## 4.13.6 Metadata from Virtual Filesystem  

<|ref|>text<|/ref|><|det|>[[115, 811, 245, 826]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 834, 870, 867]]<|/det|>
CT: Verify that the CT is able to request metadata information for a track other than currently playing one from the Virtual Filesystem.  

<|ref|>text<|/ref|><|det|>[[144, 872, 820, 906]]<|/det|>
TG: Verify that the TG correctly returns the metadata information for the track from the Virtual Filesystem list as requested by the CT.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 222, 88]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[145, 96, 312, 113]]<|/det|>
[5], [8] 5.13.2, 6.10.1.2  

<|ref|>text<|/ref|><|det|>[[115, 123, 260, 138]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 147, 456, 188]]<|/det|>
A connection for control is established. The TG is currently playing a track.  

<|ref|>text<|/ref|><|det|>[[115, 199, 325, 215]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 223, 706, 288]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MCN/CB/BV-06-C [Metadata from Virtual Filesystem]</td></tr><tr><td>AVRCP/TG/MCN/CB/BV-17-C [Metadata from Virtual Filesystem]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[145, 294, 512, 309]]<|/det|>
Table 4.14: Metadata from Virtual Filesystem test cases  

<|ref|>text<|/ref|><|det|>[[115, 325, 260, 341]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[140, 348, 863, 381]]<|/det|>
CT: Initiate the action on the CT to request metadata information for a track other than the currently playing one from the Virtual Filesystem.  

<|ref|>text<|/ref|><|det|>[[144, 384, 316, 400]]<|/det|>
TG: No action required.  

<|ref|>text<|/ref|><|det|>[[115, 411, 287, 427]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 435, 238, 450]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 458, 657, 475]]<|/det|>
The CT displays the correct metadata information for the desired track.  

<|ref|>sub_title<|/ref|><|det|>[[115, 495, 808, 515]]<|/det|>
## AVRCP/TG/MCN/CB/BV-07-C [Browsing of a folder if the player is not addressed]  

<|ref|>text<|/ref|><|det|>[[115, 523, 245, 539]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 546, 828, 580]]<|/det|>
TG: Verify that the CT is able to correctly browse the folder on a player that is not the currently addressed player as requested by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 584, 222, 599]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 607, 330, 623]]<|/det|>
[5], [8] 5.13, 6.9, 6.10.1.2  

<|ref|>text<|/ref|><|det|>[[115, 631, 260, 647]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 666, 456, 682]]<|/det|>
A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[144, 689, 795, 706]]<|/det|>
Multiple Players are available on the TG with at least one Player supporting Browsing.  

<|ref|>text<|/ref|><|det|>[[115, 717, 260, 732]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[140, 740, 839, 774]]<|/det|>
Initiate the action on the CT to select a Player as the currently addressed one, e.g., by playing a track. Then browse into a Player different from that addressed Player.  

<|ref|>text<|/ref|><|det|>[[115, 778, 252, 792]]<|/det|>
Test Condition  

<|ref|>text<|/ref|><|det|>[[140, 800, 879, 833]]<|/det|>
There is a Player available on the TG that supports browsing and the OnlyBrowsableWhenAddressed bit is not set in the Player Feature bitmask.  

<|ref|>text<|/ref|><|det|>[[115, 841, 287, 857]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 864, 238, 879]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 887, 806, 904]]<|/det|>
The CT is able to retrieve the media content of the browsed Player on the TG as requested.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[111, 70, 848, 88]]<|/det|>
## AVRCP/TG/MCN/CB/BI-08-C [Browsing of a folder in the player only when addressed]  

<|ref|>text<|/ref|><|det|>[[115, 97, 245, 112]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 120, 877, 153]]<|/det|>
TG: Verify that the TG is able to reject browsing requests when browsing of non- addressed players is not supported.  

<|ref|>text<|/ref|><|det|>[[115, 158, 223, 172]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 180, 330, 197]]<|/det|>
[5], [8] 5.13, 6.9, 6.10.1.2  

<|ref|>text<|/ref|><|det|>[[144, 204, 259, 219]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 240, 456, 256]]<|/det|>
A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[115, 267, 259, 282]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[140, 290, 839, 323]]<|/det|>
Initiate the action on the CT to select a Player as the currently addressed one, e.g., by playing a track. Then browse into a Player different from that addressed Player.  

<|ref|>text<|/ref|><|det|>[[115, 330, 252, 345]]<|/det|>
Test Condition  

<|ref|>text<|/ref|><|det|>[[140, 353, 879, 386]]<|/det|>
There is a Player available on the TG that supports browsing and the OnlyBrowsableWhenAddressed bit is set in the Player Feature bitmask.  

<|ref|>text<|/ref|><|det|>[[115, 394, 285, 410]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 418, 238, 433]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 440, 838, 474]]<|/det|>
The TG sends a properly formatted response PDU to the Lower Tester with status code \(= 0\times 13\) , Player Not Addressed.  

<|ref|>sub_title<|/ref|><|det|>[[115, 496, 857, 530]]<|/det|>
## AVRCP/CT/MCN/CB/BV-09-C [CT can retrieve the metadata Virtual Filesystem from TG with future SDP version]  

<|ref|>text<|/ref|><|det|>[[115, 540, 245, 555]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 563, 872, 597]]<|/det|>
Verify that the CT is able to request metadata information for a track other than currently playing one from the Virtual Filesystem when the TG supports a later profile version.  

<|ref|>text<|/ref|><|det|>[[115, 602, 223, 616]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 624, 311, 640]]<|/det|>
[5], [8] 5.13.2, 6.10.1.2  

<|ref|>text<|/ref|><|det|>[[115, 648, 259, 663]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 682, 850, 714]]<|/det|>
The Lower Tester supports an SDP version that is greater than the current published version, e.g., AVRCP v1.9.  

<|ref|>text<|/ref|><|det|>[[144, 721, 853, 755]]<|/det|>
The Lower Tester has all the bits in its Supported Features SDP attributes set, including those that are RFA.  

<|ref|>text<|/ref|><|det|>[[144, 759, 456, 775]]<|/det|>
A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[144, 783, 599, 800]]<|/det|>
The Lower Tester acting as TG is currently playing a track.  

<|ref|>text<|/ref|><|det|>[[115, 816, 259, 831]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[140, 839, 832, 872]]<|/det|>
Initiate the action on the CT to request metadata information for a track other than the currently playing one from the Virtual Filesystem.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 288, 89]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 97, 238, 113]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 120, 835, 153]]<|/det|>
The CT receives the correct metadata information for the desired track and can provide it to the Upper Tester.  

<|ref|>sub_title<|/ref|><|det|>[[115, 168, 652, 189]]<|/det|>
### 4.14 Media Content Navigation tests for Search  

<|ref|>title<|/ref|><|det|>[[115, 192, 166, 208]]<|/det|>
#### 4.14.1  

<|ref|>sub_title<|/ref|><|det|>[[202, 201, 349, 218]]<|/det|>
## Search request  

<|ref|>text<|/ref|><|det|>[[115, 228, 245, 244]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[141, 251, 864, 270]]<|/det|>
CT: Verify that the CT is able to correctly submit a search request to the TG and display the results.  

<|ref|>text<|/ref|><|det|>[[144, 275, 687, 293]]<|/det|>
TG: Verify that the TG correctly responds to a search requested by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 302, 225, 318]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 325, 230, 341]]<|/det|>
[5], [8] 5.12  

<|ref|>text<|/ref|><|det|>[[115, 350, 260, 366]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 378, 456, 394]]<|/det|>
A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[115, 405, 324, 421]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 429, 589, 493]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MCN/SRC/BV-08-C [Search request]</td></tr><tr><td>AVRCP/TG/MCN/SRC/BV-01-C [Search request]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[145, 500, 396, 514]]<|/det|>
Table 4.15: Search request test cases  

<|ref|>text<|/ref|><|det|>[[115, 531, 260, 547]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 554, 655, 572]]<|/det|>
CT: Initiate the action on the CT to Search for a media item on the TG.  

<|ref|>text<|/ref|><|det|>[[144, 579, 317, 595]]<|/det|>
TG: No action required.  

<|ref|>text<|/ref|><|det|>[[115, 605, 286, 621]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 629, 237, 644]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 652, 473, 668]]<|/det|>
The CT displays the expected search results.  

<|ref|>title<|/ref|><|det|>[[115, 682, 495, 701]]<|/det|>
#### 4.14.2 Browsing of the Search results  

<|ref|>text<|/ref|><|det|>[[115, 710, 245, 726]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[143, 734, 572, 750]]<|/det|>
CT: Verify that the CT is able to browse the Search results.  

<|ref|>text<|/ref|><|det|>[[143, 757, 846, 775]]<|/det|>
TG: Verify that the TG correctly returns the content of the Search results as requested by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 785, 225, 800]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 808, 245, 825]]<|/det|>
[5], [8] 5.13.3  

<|ref|>text<|/ref|><|det|>[[115, 834, 260, 849]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 861, 456, 877]]<|/det|>
A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[143, 885, 867, 920]]<|/det|>
A successful Search operation has been performed with the Search results still being valid. This can be achieved by executing AVRCP/CT/MCN/SRC/BV- 0 - Search request.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 325, 88]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 97, 706, 162]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MCN/SRC/BV-09-C [Browsing of the Search results]</td></tr><tr><td>AVRCP/TG/MCN/SRC/BV-05-C [Browsing of the Search results]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 168, 496, 184]]<|/det|>
Table 4.16: Browsing of the Search results test cases  

<|ref|>text<|/ref|><|det|>[[115, 199, 656, 285]]<|/det|>
Test ProcedureCT: Initiate the action on the CT to browse through the Search results.TG: No action required.Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 277, 480, 337]]<|/det|>
Pass verdictThe CT displays the expected Search results.  

<|ref|>title<|/ref|><|det|>[[115, 351, 436, 370]]<|/det|>
#### 4.14.3 Play from Search results  

<|ref|>text<|/ref|><|det|>[[115, 379, 830, 444]]<|/det|>
Test PurposeCT: Verify that the CT is able to request to play a track from the list of Search results.TG: Verify that the TG correctly plays the track from the Search result list requested by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 453, 352, 495]]<|/det|>
Reference[5], [8] 5.13.3, 6.11, 6.10.1.2  

<|ref|>text<|/ref|><|det|>[[115, 503, 260, 518]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 530, 868, 590]]<|/det|>
- A connection for control is established.- A successful Search operation has been performed with the Search results still being valid. This can be achieved by executing AVRCP/CT/MCN/SRC/BV-0 - Search request.  

<|ref|>text<|/ref|><|det|>[[115, 598, 325, 614]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 622, 647, 687]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MN/SRC/BV-10-C [Play from Search results]</td></tr><tr><td>AVRCP/TG/MN/SRC/BV-03-C [Play from Search results]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 693, 456, 708]]<|/det|>
Table 4.17: Play from Search results test cases  

<|ref|>text<|/ref|><|det|>[[115, 724, 707, 789]]<|/det|>
Test ProcedureCT: Initiate the action on the CT to play a media item from the Search results.TG: No action required.  

<|ref|>text<|/ref|><|det|>[[115, 797, 427, 862]]<|/det|>
Expected OutcomePass verdictThe TG plays the selected media item.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>title<|/ref|><|det|>[[114, 70, 481, 88]]<|/det|>
#### 4.14.4 Metadata from Search results  

<|ref|>text<|/ref|><|det|>[[115, 98, 245, 113]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 121, 872, 155]]<|/det|>
CT: Verify that the CT is able to request metadata information for a track other than currently playing one from the list of Search results.  

<|ref|>text<|/ref|><|det|>[[141, 158, 872, 193]]<|/det|>
TG: Verify that the TG correctly returns the metadata information for the track from the Search result list as requested by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 198, 223, 212]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 218, 243, 234]]<|/det|>
[5], [8] 5.13.3  

<|ref|>text<|/ref|><|det|>[[144, 242, 259, 257]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 282, 455, 298]]<|/det|>
A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[144, 305, 868, 340]]<|/det|>
A successful Search operation has been performed with the Search results still being valid. This can be achieved by executing AVRCP/CT/MCN/SRC/BV- 0 - Search request.  

<|ref|>text<|/ref|><|det|>[[115, 349, 325, 365]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 373, 706, 437]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MCN/SRC/BV-11-C [Metadata from Search results]</td></tr><tr><td>AVRCP/TG/MCN/SRC/BV-07-C [Metadata from Search results]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[145, 444, 485, 459]]<|/det|>
Table 4.18: Metadata from Search results test cases  

<|ref|>text<|/ref|><|det|>[[115, 475, 260, 490]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[140, 498, 866, 532]]<|/det|>
CT: Initiate the action on the CT to request metadata information for a track other than the currently playing one from the Search results.  

<|ref|>text<|/ref|><|det|>[[144, 535, 315, 550]]<|/det|>
TG: No action required.  

<|ref|>text<|/ref|><|det|>[[115, 561, 252, 576]]<|/det|>
Test Condition  

<|ref|>text<|/ref|><|det|>[[140, 584, 825, 618]]<|/det|>
The TG might or might not be currently playing a track. In case a track is currently playing, the metadata is not requested for the currently playing track.  

<|ref|>text<|/ref|><|det|>[[144, 622, 285, 636]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 644, 240, 659]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 667, 658, 683]]<|/det|>
The CT displays the correct metadata information for the desired track.  

<|ref|>sub_title<|/ref|><|det|>[[115, 712, 712, 733]]<|/det|>
### 4.15 Media Content Navigation tests for Now Playing  

<|ref|>title<|/ref|><|det|>[[115, 743, 635, 763]]<|/det|>
#### 4.15.1 Playing of a track from the Now Playing folder  

<|ref|>text<|/ref|><|det|>[[115, 773, 245, 788]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 796, 869, 830]]<|/det|>
CT: Verify that the CT is able to start playback of a track offered by the TG in the Now Playing folder and correctly displays the Now Playing list.  

<|ref|>text<|/ref|><|det|>[[140, 833, 830, 850]]<|/det|>
TG: Verify that the TG correctly plays a track from the Now Playing folder requested by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 861, 223, 876]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 884, 230, 900]]<|/det|>
[5], [8] 5.10=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 96, 545, 138]]<|/det|>
Initial Condition- A Connection for control is established.- The Now Playing list already contains media items.  

<|ref|>text<|/ref|><|det|>[[115, 147, 325, 163]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 172, 765, 237]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MCN/NP/BV-11-C [Playing of a track from the Now Playing folder]</td></tr><tr><td>AVRCP/TG/MCN/NP/BV-01-C [Playing of a track from the Now Playing folder]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 244, 593, 259]]<|/det|>
Table 4.19: Playing of a track from the Now Playing folder test cases  

<|ref|>text<|/ref|><|det|>[[115, 274, 260, 290]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 297, 741, 315]]<|/det|>
CT: Initiate the action on the CT to start playback of a track in the Now Playing list.  

<|ref|>text<|/ref|><|det|>[[144, 322, 313, 338]]<|/det|>
TG: No action required.  

<|ref|>text<|/ref|><|det|>[[115, 348, 285, 364]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 372, 238, 387]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 394, 470, 410]]<|/det|>
The TG starts playback of the selected track.  

<|ref|>text<|/ref|><|det|>[[144, 418, 700, 435]]<|/det|>
The CT correctly displays the Now Playing list and the currently playing item.  

<|ref|>title<|/ref|><|det|>[[115, 450, 630, 470]]<|/det|>
#### 4.15.2 Adding a Filesystem track to Now Playing list  

<|ref|>text<|/ref|><|det|>[[115, 479, 245, 495]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 502, 848, 520]]<|/det|>
CT: Verify that the CT is able to request adding a track offered by the TG in its Virtual Filesystem.  

<|ref|>text<|/ref|><|det|>[[144, 526, 784, 544]]<|/det|>
TG: Verify that the TG correctly adds the track selected by the CT to its Now Playing list.  

<|ref|>text<|/ref|><|det|>[[115, 553, 224, 568]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 576, 230, 592]]<|/det|>
[5], [8] 5.10  

<|ref|>text<|/ref|><|det|>[[115, 601, 260, 616]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 628, 457, 644]]<|/det|>
A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[144, 652, 778, 687]]<|/det|>
The CT has browsed into the Virtual Filesystem. This can be achieved by executing AVRCP/CT/MCN/CB/BV- 0 - Browsing of the current folder.  

<|ref|>text<|/ref|><|det|>[[115, 697, 325, 713]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 721, 763, 788]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MC/NP/BV-12-C [Adding a Filesystem track to Now Playing list]</td></tr><tr><td>AVRCP/TG/MC/NP/BV-08-C [Adding a Filesystem track to Now Playing list]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 792, 588, 808]]<|/det|>
Table 4.20: Adding a Filesystem track to Now Playing list test cases  

<|ref|>text<|/ref|><|det|>[[115, 824, 260, 839]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 847, 869, 864]]<|/det|>
CT: Initiate the action on the CT to add a track from the Virtual Filesystem to the Now Playing folder.  

<|ref|>text<|/ref|><|det|>[[144, 871, 315, 886]]<|/det|>
TG: No action required.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 280, 89]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 97, 238, 112]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 120, 770, 137]]<|/det|>
The CT correctly displays the Now Playing list containing the newly added media item.  

<|ref|>sub_title<|/ref|><|det|>[[115, 149, 653, 169]]<|/det|>
#### 4.15.3 Adding a Search result track to Now Playing list  

<|ref|>text<|/ref|><|det|>[[115, 178, 245, 195]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 201, 847, 241]]<|/det|>
CT: Verify that the CT is able to request adding a track offered by the TG in the Search result list. TG: Verify that the TG correctly adds the track selected by the CT to its Now Playing list.  

<|ref|>text<|/ref|><|det|>[[115, 251, 225, 288]]<|/det|>
Reference [5], [8] 5.10  

<|ref|>text<|/ref|><|det|>[[115, 300, 260, 316]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 328, 763, 388]]<|/det|>
- A connection for control is established.- The CT has successfully performed a Search. This can be achieved by executing AVRCP/CT/MCN/SRC/BV-0 - Search request.  

<|ref|>text<|/ref|><|det|>[[115, 396, 324, 412]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 420, 765, 484]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MCN/NP/BV-13-C [Adding a Search result track to Now Playing list]</td></tr><tr><td>AVRCP/TG/MCN/NP/BV-03-C [Adding a Search result track to Now Playing list]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 491, 605, 506]]<|/det|>
Table 4.21: Adding a Search result track to Now Playing list test cases  

<|ref|>text<|/ref|><|det|>[[115, 521, 260, 537]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 545, 861, 585]]<|/det|>
CT: Initiate the action on the CT to add a track from the Search result list to the Now Playing folder. TG: No action required.  

<|ref|>text<|/ref|><|det|>[[115, 595, 287, 611]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 619, 238, 634]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 641, 768, 659]]<|/det|>
The CT correctly displays the Now Playing list containing the newly added media item.  

#### 4.15.4 Local change of Now Playing list on TG  

<|ref|>text<|/ref|><|det|>[[115, 704, 245, 719]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 727, 875, 761]]<|/det|>
CT: Verify that the CT correctly updates the Now Playing list when it has been changed locally on the TG.  

<|ref|>text<|/ref|><|det|>[[144, 764, 840, 799]]<|/det|>
TG: Verify that the TG correctly announces a change in the Now Playing list that has been done locally on the TG.  

<|ref|>text<|/ref|><|det|>[[115, 802, 225, 817]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 824, 230, 840]]<|/det|>
[5], [8] 5.10=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 97, 644, 137]]<|/det|>
- A connection for control is established.- The Now Playing list on the TG contains at least one media item.  

<|ref|>text<|/ref|><|det|>[[115, 147, 325, 163]]<|/det|>
- Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[146, 173, 706, 237]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MCN/NP/BV-14-C [Local change of Now Playing list on TG]</td></tr><tr><td>AVRCP/TG/MCN/NP/BV-10-C [Local change of Now Playing list on TG]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[145, 244, 552, 259]]<|/det|>
Table 4.22: Local change of Now Playing list on TG test cases  

<|ref|>text<|/ref|><|det|>[[115, 274, 731, 360]]<|/det|>
- Test ProcedureCT: No action required.TG: Initiate the action on the TG to change the content of the Now Playing folder.- Expected OutcomePass verdictThe CT correctly displays the Now Playing list containing the newly selected media item(s).  

<|ref|>text<|/ref|><|det|>[[115, 368, 803, 410]]<|/det|>
Pass verdictThe CT correctly displays the Now Playing list containing the newly selected media item(s).  

#### 4.15.5 Metadata from Now Playing list  

<|ref|>text<|/ref|><|det|>[[115, 454, 245, 470]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 478, 870, 511]]<|/det|>
CT: Verify that the CT is able to request metadata information for a track other than currently playing one from the Now Playing list.  

<|ref|>text<|/ref|><|det|>[[140, 514, 866, 548]]<|/det|>
TG: Verify that the TG correctly returns the metadata information for the track from the Now Playing list as requested by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 551, 224, 565]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 574, 243, 590]]<|/det|>
[5], [8] 5.13.4  

<|ref|>text<|/ref|><|det|>[[144, 599, 258, 614]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[115, 620, 125, 630]]<|/det|>
-  

<|ref|>text<|/ref|><|det|>[[144, 640, 455, 655]]<|/det|>
- A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[115, 666, 325, 682]]<|/det|>
- Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[146, 690, 647, 755]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MC/NP/BV-15-C [Metadata from Now Playing list]</td></tr><tr><td>AVRCP/TG/MC/NP/BV-05-C [Metadata from Now Playing list]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[145, 761, 500, 776]]<|/det|>
Table 4.23: Metadata from Now Playing list test cases  

<|ref|>text<|/ref|><|det|>[[115, 792, 260, 807]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[140, 815, 864, 849]]<|/det|>
CT: Initiate the action on the CT to request metadata information for a track other than the currently playing one from the Now Playing folder.  

<|ref|>text<|/ref|><|det|>[[144, 852, 316, 867]]<|/det|>
TG: No action required.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 253, 88]]<|/det|>
Test Condition  

<|ref|>text<|/ref|><|det|>[[142, 96, 825, 130]]<|/det|>
The TG might or might not be currently playing a track. In case a track is currently playing, the metadata is not requested for the currently playing track.  

<|ref|>text<|/ref|><|det|>[[115, 135, 287, 150]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 158, 238, 173]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 180, 657, 197]]<|/det|>
The CT displays the correct metadata information for the desired track.  

<|ref|>title<|/ref|><|det|>[[115, 217, 513, 236]]<|/det|>
#### 4.15.6 Browsing the Now Playing folder  

<|ref|>text<|/ref|><|det|>[[115, 245, 245, 262]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 269, 603, 286]]<|/det|>
CT: Verify that the CT is able to browse the Now Playing folder.  

<|ref|>text<|/ref|><|det|>[[142, 293, 877, 311]]<|/det|>
TG: Verify that the TG correctly returns the content of the Now Playing folder as requested by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 319, 223, 335]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 342, 243, 359]]<|/det|>
[5], [8] 5.13.4  

<|ref|>text<|/ref|><|det|>[[115, 368, 259, 384]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 395, 459, 412]]<|/det|>
A Connection for control is established.  

<|ref|>text<|/ref|><|det|>[[144, 420, 507, 436]]<|/det|>
The Now Playing folder contains media items.  

<|ref|>text<|/ref|><|det|>[[115, 447, 323, 463]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[146, 472, 705, 535]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MCN/NP/BV-16-C [Browsing the Now Playing folder]</td></tr><tr><td>AVRCP/TG/MCN/NP/BV-12-C [Browsing the Now Playing folder]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 542, 507, 557]]<|/det|>
Table 4.24: Browsing the Now Playing folder test cases  

<|ref|>text<|/ref|><|det|>[[115, 572, 256, 589]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 596, 685, 614]]<|/det|>
CT: Initiate the action on the CT to browse through the Now Playing folder.  

<|ref|>text<|/ref|><|det|>[[144, 621, 316, 637]]<|/det|>
TG: No action required.  

<|ref|>text<|/ref|><|det|>[[115, 646, 286, 662]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 670, 238, 686]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 693, 644, 710]]<|/det|>
The CT displays the expected media items in the Now Playing folder.  

<|ref|>title<|/ref|><|det|>[[115, 725, 621, 745]]<|/det|>
#### 4.15.7 Adding a Playable Folder to Now Playing list  

<|ref|>text<|/ref|><|det|>[[115, 754, 245, 769]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 777, 848, 810]]<|/det|>
CT: Verify that the CT is able to request adding a Playable Folder offered by the TG in the Virtual Filesystem.  

<|ref|>text<|/ref|><|det|>[[144, 814, 850, 848]]<|/det|>
TG: Verify that the TG correctly adds the tracks from the Playable Folder selected by the CT to its Now Playing list.  

<|ref|>text<|/ref|><|det|>[[144, 851, 223, 866]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 874, 230, 890]]<|/det|>
[5], [8] 5.10=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 97, 780, 175]]<|/det|>
Initial Condition- A connection for control is established.- The CT has browsed into the Virtual Filesystem. This can be achieved by executing AVRCP/CT/MCN/CB/BV- 0 - Browsing of the current folder.- The current folder on the TG contains a Playable Folder.  

<|ref|>text<|/ref|><|det|>[[115, 189, 325, 205]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 213, 765, 279]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/MCN/NP/BV-17-C [Adding a Playable Folder to Now Playing list]</td></tr><tr><td>AVRCP/TG/MCN/NP/BV-13-C [Adding a Playable Folder to Now Playing list]</td></tr></table>

<|ref|>table_footnote<|/ref|><|det|>[[144, 285, 585, 301]]<|/det|>
Table 4.25: Adding a Playable Folder to Now Playing list test cases  

<|ref|>text<|/ref|><|det|>[[115, 316, 260, 331]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 339, 841, 374]]<|/det|>
CT: Initiate the action on the CT to add a Playable Folder from the Virtual Filesystem to the Now Playing folder.  

<|ref|>text<|/ref|><|det|>[[144, 377, 316, 393]]<|/det|>
TG: No action required.  

<|ref|>text<|/ref|><|det|>[[115, 403, 285, 419]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 428, 238, 443]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 450, 863, 468]]<|/det|>
The CT correctly displays the Now Playing list containing the media items from the Playable Folder.  

<|ref|>sub_title<|/ref|><|det|>[[115, 485, 504, 505]]<|/det|>
### 4.16 Volume Level Handling tests  

<|ref|>title<|/ref|><|det|>[[115, 510, 545, 530]]<|/det|>
#### 4.16.1 Monitoring the TG volume on the CT  

<|ref|>text<|/ref|><|det|>[[115, 544, 245, 560]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 567, 777, 585]]<|/det|>
CT: Verify that the CT is able to correctly receive Volume Changed events from the TG.  

<|ref|>text<|/ref|><|det|>[[142, 592, 695, 609]]<|/det|>
TG: Verify that the TG correctly announces local volume changes to the CT.  

<|ref|>text<|/ref|><|det|>[[115, 618, 223, 634]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 643, 220, 659]]<|/det|>
[5], [8] 5.8  

<|ref|>text<|/ref|><|det|>[[115, 668, 260, 684]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 695, 857, 736]]<|/det|>
Initial Condition- A connection for control is established.- Some media is playing on the TG so that the volume level change can be verified acoustically.  

<|ref|>text<|/ref|><|det|>[[115, 747, 325, 763]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 771, 705, 836]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/VLH/BV-04-C [Monitoring the TG volume on the CT]</td></tr><tr><td>AVRCP/TG/VLH/BV-01-C [Monitoring the TG volume on the CT]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 842, 533, 857]]<|/det|>
Table 4.26: Monitoring the TG volume on the CT test cases=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 630, 137]]<|/det|>
- Test ProcedureCategory 2 CT: No action required.Category 2 TG: Initiate the action on the TG to change the volume.  

<|ref|>text<|/ref|><|det|>[[115, 146, 287, 162]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 170, 238, 186]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 193, 842, 228]]<|/det|>
The category 2 CT correctly receives the Volume Changed events from the TG and updates any corresponding local state accordingly.  

<|ref|>text<|/ref|><|det|>[[144, 230, 477, 246]]<|/det|>
The volume on the category 2 TG is changed.  

<|ref|>title<|/ref|><|det|>[[115, 265, 405, 285]]<|/det|>
#### 4.16.2 Changing the volume  

<|ref|>text<|/ref|><|det|>[[115, 294, 245, 310]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 318, 700, 357]]<|/det|>
CT: Verify that the CT can correctly set the absolute volume on the TG.TG: Verify that the TG changes to the absolute volume requested by the CT.  

<|ref|>text<|/ref|><|det|>[[115, 367, 223, 383]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 391, 222, 407]]<|/det|>
[5], [8] 5.8  

<|ref|>text<|/ref|><|det|>[[115, 416, 260, 432]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 444, 857, 485]]<|/det|>
- A connection for control is established.- Some media is playing on the TG so that the volume level change can be verified acoustically.  

<|ref|>text<|/ref|><|det|>[[115, 495, 325, 511]]<|/det|>
- Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 520, 588, 585]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/VLH/BV-05-C [Changing the volume]</td></tr><tr><td>AVRCP/TG/VLH/BV-03-C [Changing the volume]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[145, 591, 435, 606]]<|/det|>
Table 4.27: Changing the volume test cases  

<|ref|>text<|/ref|><|det|>[[115, 621, 260, 637]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 645, 671, 661]]<|/det|>
Category 2 CT: Initiate the action on the CT to set the volume on the TG.  

<|ref|>text<|/ref|><|det|>[[144, 668, 400, 685]]<|/det|>
Category 2 TG: No action required.  

<|ref|>text<|/ref|><|det|>[[115, 695, 287, 711]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 719, 237, 735]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 742, 454, 758]]<|/det|>
The TG changes to the new volume level.  

<|ref|>sub_title<|/ref|><|det|>[[115, 775, 355, 795]]<|/det|>
### 4.17 Cover Art tests  

<|ref|>title<|/ref|><|det|>[[115, 806, 562, 825]]<|/det|>
#### 4.17.1 Retrieval of multiple Cover Art images  

<|ref|>text<|/ref|><|det|>[[115, 834, 630, 899]]<|/det|>
- Test PurposeCT: Verify that the CT can retrieve multiple Cover Art images.TG: Verify that the TG is able to provide multiple Cover Art images.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 223, 88]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 96, 344, 113]]<|/det|>
[8] 6.6.1, 6.10.4.2, 6.10.4.3  

<|ref|>text<|/ref|><|det|>[[144, 120, 507, 137]]<|/det|>
[9] 4.4.3, 4.4.6.2, 4.4.6.3, 4.5.1, 4.5.7, 4.5.8, 4.5.9  

<|ref|>text<|/ref|><|det|>[[115, 146, 260, 162]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 171, 864, 293]]<|/det|>
- One ACL connection exists between the CT and the TG.- The AVCTP control and browsing channels between the CT and the TG are established.- There is an active Cover Art OBEX connection where the TG is the OBEX server and the CT is the OBEX client.- A folder containing multiple media items with Cover Art on the TG has been selected and browsed to on the CT.  

<|ref|>text<|/ref|><|det|>[[115, 305, 325, 321]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[146, 330, 705, 394]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/CA/BV-04-C [Retrieval of multiple Cover Art images]</td></tr><tr><td>AVRCP/TG/CA/BV-01-C [Retrieval of multiple Cover Art images]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[146, 400, 543, 415]]<|/det|>
Table 4.28: Retrieval of multiple Cover Art images test cases  

<|ref|>text<|/ref|><|det|>[[115, 431, 260, 447]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 455, 838, 490]]<|/det|>
CT: Initiate the action on the CT to browse through the media content and retrieve the matching Cover Art in any format for all items in the current folder.  

<|ref|>text<|/ref|><|det|>[[144, 492, 333, 508]]<|/det|>
TG: No action is required.  

<|ref|>text<|/ref|><|det|>[[115, 518, 285, 534]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 543, 238, 557]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 565, 694, 582]]<|/det|>
The appropriate Cover Art is displayed on the CT for each item in the folder.  

<|ref|>sub_title<|/ref|><|det|>[[115, 600, 752, 620]]<|/det|>
### 4.17.2 Retrieval of Cover Art image for the currently playing track  

<|ref|>text<|/ref|><|det|>[[115, 628, 245, 644]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 652, 760, 669]]<|/det|>
CT: Verify that the CT can retrieve the Cover Art image for the currently playing track.  

<|ref|>text<|/ref|><|det|>[[144, 676, 800, 693]]<|/det|>
TG: Verify that the TG is able to provide the Cover Art image for the currently playing track.  

<|ref|>text<|/ref|><|det|>[[115, 702, 223, 717]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 725, 230, 741]]<|/det|>
[8] 6.10.4.2  

<|ref|>text<|/ref|><|det|>[[144, 749, 507, 765]]<|/det|>
[9] 4.4.3, 4.4.6, 2, 4.4.6.3, 4.5.1, 1, 4.5.7, 4.5.8, 4.4.5.9  

<|ref|>text<|/ref|><|det|>[[115, 776, 260, 791]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 802, 582, 819]]<|/det|>
One ACL connection exists between the CT and the TG.  

<|ref|>text<|/ref|><|det|>[[144, 826, 815, 844]]<|/det|>
The AVCTP control and browsing channels between the CT and the TG are established.  

<|ref|>text<|/ref|><|det|>[[144, 850, 860, 883]]<|/det|>
There is an active Cover Art OBEX connection where the TG is the OBEX server and the CTis the OBEX client.  

<|ref|>text<|/ref|><|det|>[[144, 888, 660, 904]]<|/det|>
A track with an associated Cover Art is currently playing on the TG.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 325, 88]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 97, 824, 162]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/CA/BV-02-C [Retrieval of Cover Art image for the currently playing track]</td></tr><tr><td>AVRCP/TG/CA/BV-05-C [Retrieval of Cover Art image for the currently playing track]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 168, 674, 184]]<|/det|>
Table 4.29: Retrieval of Cover Art image for the currently playing track test cases  

<|ref|>text<|/ref|><|det|>[[115, 199, 260, 215]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 222, 625, 240]]<|/det|>
CT: Initiate the action on the CT to display Cover Art, if necessary.  

<|ref|>text<|/ref|><|det|>[[144, 247, 333, 263]]<|/det|>
TG: No action is required.  

<|ref|>text<|/ref|><|det|>[[115, 273, 287, 288]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 297, 238, 312]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 319, 796, 337]]<|/det|>
The appropriate Cover Art is displayed on the CT for the track currently playing on the TG.  

<|ref|>sub_title<|/ref|><|det|>[[115, 351, 828, 389]]<|/det|>
#### 4.17.3 Retrieval of Cover Art image for the currently playing track without browsing  

<|ref|>text<|/ref|><|det|>[[115, 397, 245, 413]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 420, 696, 438]]<|/det|>
This test case is specific for devices that don't support the Browsing feature.  

<|ref|>text<|/ref|><|det|>[[144, 444, 763, 461]]<|/det|>
CT: Verify that the CT can retrieve the Cover Art image for the currently playing track.  

<|ref|>text<|/ref|><|det|>[[144, 468, 802, 485]]<|/det|>
TG: Verify that the TG is able to provide the Cover Art image for the currently playing track.  

<|ref|>text<|/ref|><|det|>[[115, 495, 225, 510]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 518, 228, 534]]<|/det|>
[8] 6.10.4.2  

<|ref|>text<|/ref|><|det|>[[144, 543, 507, 560]]<|/det|>
[9] 4.4.3, 4.4.6.2, 4.4.6.3, 4.5.1, 4.5.7, 4.5.8, 4.5.9  

<|ref|>text<|/ref|><|det|>[[115, 570, 260, 585]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 595, 584, 612]]<|/det|>
One ACL connection exists between the CT and the TG.  

<|ref|>text<|/ref|><|det|>[[144, 619, 692, 636]]<|/det|>
The AVCTP control channel between the CT and the TG is established.  

<|ref|>text<|/ref|><|det|>[[144, 643, 860, 676]]<|/det|>
There is an active Cover Art OBEX connection where the TG is the OBEX server and the CT is the OBEX client.  

<|ref|>text<|/ref|><|det|>[[144, 679, 660, 696]]<|/det|>
A track with an associated Cover Art is currently playing on the TG.  

<|ref|>text<|/ref|><|det|>[[115, 712, 325, 728]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[146, 736, 881, 830]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/ CA/BV-06-C [Retrieval of Cover Art image for the currently playing track without browsing]</td></tr><tr><td>AVRCP/TG/CA/BV-03-C [Retrieval of Cover Art image for the currently playing track without browsing]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 836, 787, 852]]<|/det|>
Table 4.30: Retrieval of Cover Art image for the currently playing track without browsing test cases=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 625, 140]]<|/det|>
- Test ProcedureCT: Initiate the action on the CT to display Cover Art, if necessary.TG: No action is required.  

<|ref|>text<|/ref|><|det|>[[115, 147, 799, 213]]<|/det|>
- Expected OutcomePass verdictThe appropriate Cover Art is displayed on the CT for the track currently playing on the TG.  

<|ref|>sub_title<|/ref|><|det|>[[115, 227, 600, 247]]<|/det|>
### 4.18 Connection establishment for control  

<|ref|>text<|/ref|><|det|>[[115, 254, 457, 270]]<|/det|>
Verify the connection establishment for control.  

<|ref|>sub_title<|/ref|><|det|>[[115, 282, 750, 301]]<|/det|>
### 4.18.1 Connection establishment for control initiated from the CT  

<|ref|>text<|/ref|><|det|>[[115, 308, 531, 324]]<|/det|>
Verify the connection establishment initiated from the CT.  

<|ref|>title<|/ref|><|det|>[[115, 333, 427, 349]]<|/det|>
#### 4.18.1.1 Connection establishment - CT  

<|ref|>text<|/ref|><|det|>[[115, 360, 727, 424]]<|/det|>
- Test PurposeCT: Verify that the CT can establish a connection for control towards the TG.TG: Verify that the TG accepts a connection establishment initiated from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 433, 288, 473]]<|/det|>
- Reference[2], [5], [7], [8] 4.1.1  

<|ref|>text<|/ref|><|det|>[[115, 482, 260, 498]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 509, 317, 551]]<|/det|>
- CT: Standby mode.- TG: Standby mode.  

<|ref|>text<|/ref|><|det|>[[115, 561, 325, 577]]<|/det|>
- Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 585, 648, 650]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/CEC/BV-01-C [Connection establishment - CT]</td></tr><tr><td>AVRCP/TG/CEC/BV-01-C [Connection establishment - CT]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 657, 504, 671]]<|/det|>
Table 4.31: Connection establishment - CT test cases  

<|ref|>text<|/ref|><|det|>[[115, 688, 260, 703]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 710, 816, 750]]<|/det|>
CT: Initiate the user action (e.g., press button) on the CT to establish a connection to the TG.TG: No user action is required.  

<|ref|>text<|/ref|><|det|>[[115, 760, 285, 776]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 784, 238, 799]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[142, 807, 847, 840]]<|/det|>
CT: It is possible to control the TG by the subsequent user action performed on the CT. It may be indicated that connection for control is established.  

<|ref|>text<|/ref|><|det|>[[144, 843, 616, 859]]<|/det|>
TG: It may be indicated that connection for control is established.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[114, 70, 752, 89]]<|/det|>
### 4.18.2 Connection establishment for control initiated from the TG  

<|ref|>text<|/ref|><|det|>[[114, 96, 532, 112]]<|/det|>
Verify the connection establishment initiated from the TG.  

<|ref|>title<|/ref|><|det|>[[115, 121, 428, 138]]<|/det|>
#### 4.18.2.1 Connection establishment - TG  

<|ref|>text<|/ref|><|det|>[[115, 148, 725, 213]]<|/det|>
- Test PurposeCT: Verify that the CT accepts a connection establishment initiated from the TG.TG: Verify that the TG can establish a connection for control towards the CT.  

<|ref|>text<|/ref|><|det|>[[115, 222, 288, 262]]<|/det|>
- Reference[2], [5], [7], [8] 4.1.1  

<|ref|>text<|/ref|><|det|>[[115, 270, 260, 285]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 297, 315, 339]]<|/det|>
- CT: Standby mode- TG: Standby mode  

<|ref|>text<|/ref|><|det|>[[115, 349, 325, 365]]<|/det|>
- Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[146, 373, 648, 437]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/CEC/BV-02-C [Connection establishment – TG]</td></tr><tr><td>AVRCP/TG/CEC/BV-02-C [Connection establishment – TG]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[146, 444, 500, 459]]<|/det|>
Table 4.32: Connection establishment - TG test cases  

<|ref|>text<|/ref|><|det|>[[115, 475, 266, 490]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 498, 370, 514]]<|/det|>
CT: No user action is required.  

<|ref|>text<|/ref|><|det|>[[144, 521, 817, 538]]<|/det|>
TG: Initiate the user action (e.g., press button) on the TG to establish a connection to the CT.  

<|ref|>text<|/ref|><|det|>[[115, 548, 286, 563]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 572, 238, 587]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 595, 848, 629]]<|/det|>
CT: It is possible to control the TG by the subsequent user action performed on the CT. It may be indicated that connection for control is established.  

<|ref|>text<|/ref|><|det|>[[144, 632, 616, 648]]<|/det|>
TG: It may be indicated that connection for control is established.  

<|ref|>title<|/ref|><|det|>[[115, 668, 686, 687]]<|/det|>
#### 4.18.3 Connection release for control initiated from the CT  

<|ref|>text<|/ref|><|det|>[[115, 694, 484, 710]]<|/det|>
Verify the connection release initiated from the CT.  

<|ref|>title<|/ref|><|det|>[[115, 719, 372, 735]]<|/det|>
#### 4.18.3.1 Connection release - CT  

<|ref|>text<|/ref|><|det|>[[115, 745, 666, 810]]<|/det|>
- Test PurposeCT: Verify that the CT releases the connection for control with the TG.TG: Verify that the TG accepts connection release initiated from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 820, 288, 857]]<|/det|>
- Reference[2], [5], [7], [8] 4,1.2=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 96, 497, 137]]<|/det|>
- CT: A connection for control is established.- TG: A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[115, 148, 325, 164]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 173, 590, 237]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/CRC/BV-01-C [Connection release - CT]</td></tr><tr><td>AVRCP/TG/CRC/BV-01-C [Connection release - CT]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 244, 459, 258]]<|/det|>
Table 4.33: Connection release - CT test cases  

<|ref|>text<|/ref|><|det|>[[115, 274, 260, 290]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 297, 805, 338]]<|/det|>
CT: Initiate the user action (e.g., press button) on the CT to release a connection to the TG. TG: No user action is required.  

<|ref|>text<|/ref|><|det|>[[115, 348, 287, 364]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 372, 238, 387]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 394, 595, 410]]<|/det|>
The user action on the CT releases the connection for control.  

<|ref|>text<|/ref|><|det|>[[144, 417, 840, 434]]<|/det|>
CT: The CT returns to standby mode. It may be indicated that connection for control is released.  

<|ref|>text<|/ref|><|det|>[[144, 441, 840, 458]]<|/det|>
TG: The TG returns to standby mode. It may be indicated that connection for control is released.  

<|ref|>sub_title<|/ref|><|det|>[[115, 474, 688, 494]]<|/det|>
### 4.18.4 Connection release for control initiated from the TG  

<|ref|>text<|/ref|><|det|>[[115, 500, 485, 517]]<|/det|>
Verify the connection release initiated from the TG.  

<|ref|>title<|/ref|><|det|>[[115, 526, 374, 542]]<|/det|>
#### 4.18.4.1 Connection release - TG  

<|ref|>text<|/ref|><|det|>[[115, 552, 245, 568]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 576, 664, 593]]<|/det|>
CT: Verify that the CT accepts connection release initiated from the TG.  

<|ref|>text<|/ref|><|det|>[[144, 600, 653, 616]]<|/det|>
TG: Verify that the TG releases the connection for control with the CT.  

<|ref|>text<|/ref|><|det|>[[115, 627, 222, 642]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 650, 289, 667]]<|/det|>
[2], [5], [7], [8] 4.1.2  

<|ref|>text<|/ref|><|det|>[[115, 676, 260, 691]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 703, 487, 744]]<|/det|>
CT: A connection for control is established.- TG: A connection for control is established.  

<|ref|>table<|/ref|><|det|>[[144, 780, 646, 844]]<|/det|>
<|ref|>table_caption<|/ref|><|det|>[[115, 754, 325, 770]]<|/det|>
Test Case Configuration   

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/CRC/BV-O2-C [Connection release - TG]</td></tr><tr><td>AVRCP/TG/CRC/BV-O2-C [Connection release - TG]</td></tr></table>

<|ref|>table_footnote<|/ref|><|det|>[[144, 850, 460, 864]]<|/det|>
Table 4.34: Connection release - TG test cases=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 821, 140]]<|/det|>
- Test ProcedureCT: No user action is required.TG: Initiate the user action (e.g., press button) on the TG to release the connection to the CT.  

<|ref|>text<|/ref|><|det|>[[115, 147, 840, 261]]<|/det|>
- Expected OutcomePass verdictThe user action on the TG releases the connection for control.CT: The CT returns to standby mode. It may be indicated that connection for control is released.TG: The TG returns to standby mode. It may be indicated that connection for control is released.  

<|ref|>sub_title<|/ref|><|det|>[[115, 275, 552, 296]]<|/det|>
### 4.19 Information collection for control  

<|ref|>text<|/ref|><|det|>[[115, 302, 488, 319]]<|/det|>
Verify that the CT can collect the information of TG.  

<|ref|>title<|/ref|><|det|>[[115, 330, 641, 350]]<|/det|>
#### 4.19.1 Information collection by UNIT INFO command  

<|ref|>text<|/ref|><|det|>[[115, 356, 535, 373]]<|/det|>
Verify Information collection by the UNIT INFO command.  

<|ref|>title<|/ref|><|det|>[[115, 381, 545, 399]]<|/det|>
#### 4.19.1.1 Information collection by UNIT INFO command  

<|ref|>text<|/ref|><|det|>[[115, 407, 725, 473]]<|/det|>
- Test Purpose CT: Verify that the CT can collect information of TG by UNIT INFO command. TG: Verify that the TG responds UNIT INFO command initiated by CT.  

<|ref|>text<|/ref|><|det|>[[115, 482, 280, 545]]<|/det|>
- Reference[2], [7] 4.1.3, 4.4.1[5], [8] 4.1.3, 4.2.1  

<|ref|>text<|/ref|><|det|>[[115, 555, 260, 571]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 582, 497, 624]]<|/det|>
- CT: A connection for control is established.- TG: A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[115, 633, 325, 650]]<|/det|>
- Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 658, 765, 724]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CTJCC/BV-01-C [Information collection by UNIT INFO command]</td></tr><tr><td>AVRCP/TG/IICC/BV-01-C [Information collection by UNIT INFO command]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 728, 601, 743]]<|/det|>
Table 4.35: Information collection by UNIT INFO command test cases  

<|ref|>text<|/ref|><|det|>[[115, 759, 260, 775]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 783, 864, 818]]<|/det|>
CT: Initiate the user action (e.g., press button) on the CT to collect information of TG by UNIT INFO command.  

<|ref|>text<|/ref|><|det|>[[144, 821, 369, 837]]<|/det|>
TG: No user action is required.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 257, 88]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[115, 97, 228, 113]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[113, 120, 802, 153]]<|/det|>
CT: It is indicated that UNIT INFO response is received from the TG. The method for indication depends on the device implementation.  

<|ref|>text<|/ref|><|det|>[[113, 156, 848, 192]]<|/det|>
TG: The UNIT INFO command is received from the CT and the UNIT INFO response is sent from the TG.  

<|ref|>text<|/ref|><|det|>[[115, 189, 172, 202]]<|/det|>
4.19.2  

<|ref|>sub_title<|/ref|><|det|>[[201, 207, 682, 225]]<|/det|>
## Information collection by SUBUNIT INFO command  

<|ref|>text<|/ref|><|det|>[[115, 232, 627, 249]]<|/det|>
Verify Information collection by the SUBUNIT INFO command transfer.  

<|ref|>title<|/ref|><|det|>[[115, 258, 580, 275]]<|/det|>
#### 4.19.2.1 Information collection by SUBUNIT INFO command  

<|ref|>text<|/ref|><|det|>[[115, 284, 758, 349]]<|/det|>
- Test Purpose CT: Verify that the CT can collect information of TG by SUBUNIT INFO command. TG: Verify that the TG responds SUBUNIT INFO command initiated by CT.  

<|ref|>text<|/ref|><|det|>[[115, 358, 225, 374]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[143, 382, 280, 399]]<|/det|>
[2], [7] 4.1.3, 4.4.2  

<|ref|>text<|/ref|><|det|>[[143, 406, 280, 422]]<|/det|>
[5], [8] 4.1.3, 4.2.2  

<|ref|>text<|/ref|><|det|>[[115, 432, 260, 448]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 459, 498, 500]]<|/det|>
- CT: A connection for control is established.  
- TG: A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[115, 511, 325, 527]]<|/det|>
- Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[146, 536, 765, 599]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/ICC/BV-02-C [Information collection by SUBUNIT INFO command]</td></tr><tr><td>AVRCP/TG/ICC/BV-02-C [Information collection by SUBUNIT INFO command]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[145, 605, 631, 620]]<|/det|>
Table 4.36: Information collection by SUBUNIT INFO command test cases  

<|ref|>text<|/ref|><|det|>[[115, 636, 260, 652]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 660, 855, 694]]<|/det|>
CT: Initiate the user action (e.g., press button) on the CT to collect information of TG by SUBUNIT INFO command.  

<|ref|>text<|/ref|><|det|>[[143, 697, 369, 713]]<|/det|>
TG: No user action is required.  

<|ref|>text<|/ref|><|det|>[[115, 724, 286, 739]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[143, 748, 238, 763]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[143, 770, 865, 803]]<|/det|>
CT: It is indicated that SUBUNIT INFO response is received from the TG. The method for indication depends on the device implementation.  

TG: The SUBUNIT INFO command is received from the CT and the SUBUNIT INFO response is sent by the TG.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[114, 71, 506, 92]]<|/det|>
## 4.20 PASS THROUGH commands  

<|ref|>text<|/ref|><|det|>[[114, 98, 535, 115]]<|/det|>
Verify that the PASS THROUGH command is transferred.  

<|ref|>sub_title<|/ref|><|det|>[[114, 127, 594, 146]]<|/det|>
## 4.20.1 Category 1 of PASS THROUGH command  

<|ref|>text<|/ref|><|det|>[[114, 152, 632, 170]]<|/det|>
Verify that the category 1 of PASS THROUGH command is transferred.  

<|ref|>sub_title<|/ref|><|det|>[[114, 178, 560, 196]]<|/det|>
## 4.20.1.1 PASS THROUGH command transfer - category 1  

<|ref|>text<|/ref|><|det|>[[114, 204, 896, 222]]<|/det|>
- Test Purpose CT: Verify that the CT can send PASS THROUGH command in category 1 to the TG. TG:  

<|ref|>text<|/ref|><|det|>[[140, 228, 848, 263]]<|/det|>
Verify that the TG reacts to the PASS THROUGH command in category 1 from the CT according to the operation_id list in Appendix A - Operation_id list tables.  

<|ref|>text<|/ref|><|det|>[[144, 266, 223, 281]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[114, 288, 285, 305]]<|/det|>
[2] 4.1.3, 4.6.1, 4.7  

<|ref|>text<|/ref|><|det|>[[144, 313, 285, 328]]<|/det|>
[7] 4.1.3, 4.6.1, 4.8  

<|ref|>text<|/ref|><|det|>[[144, 336, 312, 352]]<|/det|>
[5], [8] 4.1.3, 4.4.1, 4.5  

<|ref|>text<|/ref|><|det|>[[144, 360, 260, 375]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[114, 396, 125, 408]]<|/det|>  

<|ref|>text<|/ref|><|det|>[[144, 419, 485, 435]]<|/det|>
- CT: A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[144, 443, 848, 478]]<|/det|>
- TG: A connection for control is established. The TG should be ready to react to the command from the CT.  

<|ref|>text<|/ref|><|det|>[[114, 487, 325, 503]]<|/det|>
- Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 511, 765, 577]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/PTT/BV-01-C [PASS THROUGH command transfer – category 1]</td></tr><tr><td>AVRCP/TG/PTT/BV-01-C [PASS THROUGH command transfer – category 1</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 583, 621, 598]]<|/det|>
Table 4.37: PASS THROUGH command transfer - category 1 test cases  

<|ref|>text<|/ref|><|det|>[[114, 613, 260, 629]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 637, 880, 688]]<|/det|>
CT: Initiate the required user actions (e.g., press button) to perform all operations that are listed in the category 1 "operation_id list" table in Appendix A - Operation_id list tables and indicated as supported in Table 3: Operation_id of category 1 for CT in [3].  

<|ref|>text<|/ref|><|det|>[[144, 694, 368, 710]]<|/det|>
TG: No user action is required.  

<|ref|>text<|/ref|><|det|>[[114, 720, 285, 736]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 744, 238, 759]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 766, 819, 817]]<|/det|>
CT: The CT sends PASS THROUGH commands in category 1 to the TG that are listed in the category 1 "operation_id list" table in Appendix A - Operation id list tables and indicated as supported in Table 3: Operation_id of category 1 for CTin [3].  

<|ref|>text<|/ref|><|det|>[[144, 823, 880, 874]]<|/det|>
TG: The TG reacts to all performed PASS THROUGH commands in category 1 sent from the CT according to the "Expected operation to be performed by the TG" that are listed in the operation_id list table in Appendix A - Operation_id list tables.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[114, 70, 594, 89]]<|/det|>
## 4.20.2 Category 2 of PASS THROUGH command  

<|ref|>text<|/ref|><|det|>[[114, 95, 633, 112]]<|/det|>
Verify that the category 2 of PASS THROUGH command is transferred.  

<|ref|>sub_title<|/ref|><|det|>[[114, 121, 561, 138]]<|/det|>
## 4.20.2.1 PASS THROUGH command transfer - category 2  

<|ref|>text<|/ref|><|det|>[[115, 146, 896, 207]]<|/det|>
- Test Purpose CT: Verify that the CT can send PASS THROUGH command in category 2 to the TG. TG: Verify that the TG reacts to the PASS THROUGH command in category 2 from the CT according to the operation_id list table in Appendix A - Operation_id list tables.  

<|ref|>text<|/ref|><|det|>[[144, 209, 222, 223]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[115, 231, 312, 297]]<|/det|>
[2] 4.1.3, 4.6.1, 4.7  [7] 4.1.3, 4.6.1, 4.8  [5], [8] 4.1.3, 4.4.1, 4.5  

<|ref|>text<|/ref|><|det|>[[144, 304, 259, 319]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[115, 339, 123, 350]]<|/det|>
·  

<|ref|>text<|/ref|><|det|>[[144, 362, 485, 378]]<|/det|>
- CT: A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[144, 386, 850, 420]]<|/det|>
- TG: A connection for control is established. The TG should be ready to react to the command from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 430, 324, 446]]<|/det|>
- Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 455, 765, 519]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/PTT/BV-02-C [PASS THROUGH command transfer – category 2]</td></tr><tr><td>AVRCP/TG/PTT/BV-02-C [PASS THROUGH command transfer – category 2</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 525, 621, 541]]<|/det|>
Table 4.38: PASS THROUGH command transfer - category 2 test cases  

<|ref|>text<|/ref|><|det|>[[115, 556, 260, 572]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 580, 880, 630]]<|/det|>
CT: Initiate the required user actions (e.g., press button) to perform all operations that are listed in the operation_id list table in Appendix A - Operation_id list tables and indicated as supported in Table 4: Operation_id of category 2 for CT in [3].  

<|ref|>text<|/ref|><|det|>[[144, 637, 369, 653]]<|/det|>
TG: No user action is required.  

<|ref|>text<|/ref|><|det|>[[115, 662, 287, 678]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 686, 238, 701]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 708, 819, 759]]<|/det|>
CT: The CT sends PASS THROUGH commands in category 2 to the TG that are listed in the category 2 "operation_id list" table in Appendix A - Operation_id list tables and indicated as supported in Table 4: Operation_ id of category 2 for CT in [3].  

<|ref|>text<|/ref|><|det|>[[144, 765, 881, 815]]<|/det|>
TG: The TG reacts to all performed PASS THROUGH commands in category 2 sent from the CT according to the "Expected operation to be performed by the TG" that are listed in the operation_id list table in Appendix A - Operation_id list tables.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[114, 70, 594, 89]]<|/det|>
## 4.20.3 Category 3 of PASS THROUGH command  

<|ref|>text<|/ref|><|det|>[[114, 95, 633, 112]]<|/det|>
Verify that the category 3 of PASS THROUGH command is transferred.  

<|ref|>sub_title<|/ref|><|det|>[[114, 121, 560, 138]]<|/det|>
## 4.20.3.1 PASS THROUGH command transfer - category 3  

<|ref|>text<|/ref|><|det|>[[114, 146, 896, 207]]<|/det|>
- Test Purpose CT: Verify that the CT can send PASS THROUGH command in category 3 to the TG. TG: Verify that the TG reacts to the PASS THROUGH command in category 3 from the CT according to the operation_id list table in Appendix A - Operation_id list tables.  

<|ref|>text<|/ref|><|det|>[[144, 209, 223, 223]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[114, 231, 312, 297]]<|/det|>
[2] 4.1.3, 4.6.1, 4.7  [7] 4.1.3, 4.6.1, 4.8  [5], [8] 4.1.3, 4.4.1, 4.5  

<|ref|>text<|/ref|><|det|>[[144, 304, 259, 319]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[114, 339, 123, 350]]<|/det|>
·  

<|ref|>text<|/ref|><|det|>[[144, 362, 485, 378]]<|/det|>
- CT: A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[144, 386, 850, 420]]<|/det|>
- TG: A connection for control is established. The TG should be ready to react to the command from the CT.  

<|ref|>text<|/ref|><|det|>[[114, 430, 325, 446]]<|/det|>
- Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 455, 765, 519]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/PTT/BV-03-C [PASS THROUGH command transfer – category 3]</td></tr><tr><td>AVRCP/TG/PTT/BV-03-C [PASS THROUGH command transfer – category 3</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 526, 620, 541]]<|/det|>
Table 4.39: PASS THROUGH command transfer - category 3 test cases  

<|ref|>text<|/ref|><|det|>[[114, 557, 259, 572]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 580, 880, 630]]<|/det|>
CT: Initiate the required user actions (e.g., press button) to perform all operations that are listed in the operation_id list table in Appendix A - Operation_id list tables and indicated as supported in Table 5: Operation_id of category 3 for CT in [3].  

<|ref|>text<|/ref|><|det|>[[144, 637, 368, 653]]<|/det|>
TG: No user action is required.  

<|ref|>text<|/ref|><|det|>[[114, 662, 287, 678]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 686, 238, 701]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 708, 819, 759]]<|/det|>
CT: The CT sends PASS THROUGH commands in category 3 to the TG that are listed in the category 3 "operation_id list" table in Appendix A - Operation_id list tables and indicated as supported in Table 5: Operation_ id of category 3 for CT in [3].  

<|ref|>text<|/ref|><|det|>[[144, 766, 880, 815]]<|/det|>
TG: The TG reacts to all performed PASS THROUGH commands in category 3 sent from the CT according to the "Expected operation to be performed by the TG" that are listed in the operation_id list table in Appendix A - Operation_id list tables.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>title<|/ref|><|det|>[[114, 70, 594, 88]]<|/det|>
#### 4.20.4 Category 4 of PASS THROUGH command  

<|ref|>text<|/ref|><|det|>[[114, 95, 632, 112]]<|/det|>
Verify that the category 4 of PASS THROUGH command is transferred.  

<|ref|>title<|/ref|><|det|>[[114, 121, 561, 138]]<|/det|>
#### 4.20.4.1 PASS THROUGH command transfer - category 4  

<|ref|>text<|/ref|><|det|>[[115, 148, 245, 164]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 170, 761, 188]]<|/det|>
CT: Verify that the CT can send PASS THROUGH command in category 4 to the TG.  

<|ref|>text<|/ref|><|det|>[[142, 194, 875, 228]]<|/det|>
TG: Verify that the TG reacts to the PASS THROUGH command in category 4 from the CT according to the operation_id list table in Appendix A - Operation_id list tables.  

<|ref|>text<|/ref|><|det|>[[115, 233, 228, 248]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 255, 310, 321]]<|/det|>
[2] 4.1.3, 4.6.1, 4.7  [7] 4.1.3, 4.6.1, ad 4.8  [5], [8] 4.1.3, 4.4.1, 4.5  

<|ref|>text<|/ref|><|det|>[[115, 328, 260, 344]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 362, 485, 378]]<|/det|>
- CT: A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[144, 386, 848, 420]]<|/det|>
- TG: A connection for control is established. The TG should be ready to react to the command from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 430, 325, 446]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 455, 765, 519]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/PTT/BV-04-C [PASS THROUGH command transfer - category 4]</td></tr><tr><td>AVRCP/TG/PTT/BV-04-C [PASS THROUGH command transfer - category 4</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 525, 620, 540]]<|/det|>
Table 4.40: PASS THROUGH command transfer - category 4 test cases  

<|ref|>text<|/ref|><|det|>[[115, 556, 260, 572]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 580, 880, 629]]<|/det|>
CT: Initiate the required user actions (e.g., press button) to perform all operations that are listed in the operation_id list table in Appendix A - Operation_id list tables and indicated as supported in Table 6: Operation_id of category 4 for CT in [3].  

<|ref|>text<|/ref|><|det|>[[144, 637, 369, 652]]<|/det|>
TG: No user action is required.  

<|ref|>text<|/ref|><|det|>[[115, 662, 287, 678]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 686, 238, 701]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 708, 819, 759]]<|/det|>
CT: The CT sends PASS THROUGH commands in category 4 to the TG that are listed in the category 4 "operation_id list" table in Appendix A - Operation_id list tables and indicated as supported in Table 6: Operation _id of category 4 for CT in [3].  

<|ref|>text<|/ref|><|det|>[[144, 765, 880, 814]]<|/det|>
TG: The TG reacts to all performed PASS THROUGH commands in category 4 sent from the CT according to the "Expected operation to be performed by the TG" that are listed in the operation_id list table in Appendix A - Operation_id list tables.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 70, 641, 89]]<|/det|>
## 4.20.5 Press and hold of PASS THROUGH command  

<|ref|>text<|/ref|><|det|>[[115, 95, 633, 112]]<|/det|>
Verify that the category 1 of PASS THROUGH command is transferred.  

<|ref|>sub_title<|/ref|><|det|>[[115, 121, 596, 138]]<|/det|>
## 4.20.5.1 PASS THROUGH command transfer - press and hold  

<|ref|>text<|/ref|><|det|>[[115, 147, 892, 230]]<|/det|>
- Test Purpose CT: Verify that the CT can send PASS THROUGH commands where a button is pressed and held to the TG. TG: Verify that the TG reacts to the PASS THROUGH commands from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 235, 223, 250]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[143, 258, 428, 323]]<|/det|>
[2] 4.1.3, 4.6.1, 4.7  [7] 4.1.3, 4.6.1, 4.8  [5], [8] 4.1.3, 4.4.1, 4.5 Initial Condition  

<|ref|>text<|/ref|><|det|>[[115, 338, 125, 350]]<|/det|>
-  

<|ref|>text<|/ref|><|det|>[[143, 363, 852, 420]]<|/det|>
- CT: A connection for control is established.  
- TG: A connection for control is established. The TG should be ready to react to the command from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 430, 325, 447]]<|/det|>
- Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 455, 825, 520]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/PTT/BV-05-C [PASS THROUGH command transfer – press and hold]</td></tr><tr><td>AVRCP/TG/PTT/BV-05-C [PASS THROUGH command transfer – press and hold</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 525, 649, 541]]<|/det|>
Table 4.41: PASS THROUGH command transfer - press and hold test cases  

<|ref|>text<|/ref|><|det|>[[115, 556, 260, 572]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 580, 867, 630]]<|/det|>
CT: Initiate the required user actions (e.g., press button) to indicate that a button is being held down for a selected PASS THROUGH operation. The button should be held for longer than 2 seconds. Actions should then be performed to indicate that the button has been released.  

<|ref|>text<|/ref|><|det|>[[144, 637, 369, 653]]<|/det|>
TG: No user action is required.  

<|ref|>text<|/ref|><|det|>[[115, 663, 287, 678]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 687, 238, 702]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 709, 879, 760]]<|/det|>
CT: As long as the button is held down the CT sends PASS THROUGH commands with the state flag set to button press, and with an interval of no more than 2 seconds. When the button is released the CT sends a PASS THROUGH command with the state flag set to button release."  

<|ref|>text<|/ref|><|det|>[[144, 765, 632, 783]]<|/det|>
TG: The TG indicates that the button is being held down on the CT.  

<|ref|>sub_title<|/ref|><|det|>[[115, 801, 390, 821]]<|/det|>
### 4.21 Metadata Transfer  

<|ref|>text<|/ref|><|det|>[[115, 828, 654, 845]]<|/det|>
Verify that the IUT conforms to the requirements of the Metadata Transfer.  

<|ref|>title<|/ref|><|det|>[[115, 857, 444, 875]]<|/det|>
#### 4.21.1 Configuration commands  

<|ref|>text<|/ref|><|det|>[[115, 882, 747, 899]]<|/det|>
Verify the various configuration commands that are defined in the AVRCP specification.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[113, 70, 527, 88]]<|/det|>
## AVRCP/CT/CFG/BV-01-C [Get Capabilities - CT]  

<|ref|>text<|/ref|><|det|>[[115, 97, 559, 140]]<|/det|>
- Test PurposeVerify the Get Capabilities command issued from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 147, 264, 210]]<|/det|>
- Reference[7] 5.1.1[5], [8] 6.4.1  

<|ref|>text<|/ref|><|det|>[[115, 220, 260, 235]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 246, 732, 288]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.  

<|ref|>text<|/ref|><|det|>[[115, 298, 260, 314]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 321, 809, 370]]<|/det|>
The Upper Tester triggers the IUT to send a GetCapabilities command with the METADATA TRANSFER_GetCapabilities PDU containing any valid CapabilityID value. Upper Tester  

<|ref|>image<|/ref|><|det|>[[150, 365, 707, 630]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 637, 590, 653]]<|/det|>
<center>Figure 4.95: AVRCP/CT/CFG/BV-01-C [Get Capabilities - CT]_MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 668, 488, 733]]<|/det|>
- Expected OutcomePass verdictThe Lower Tester receives the GetCapabilities.  

<|ref|>sub_title<|/ref|><|det|>[[113, 747, 614, 765]]<|/det|>
## AVRCP/TG/CFG/BV-02-C [Get Capabilities response - TG]  

<|ref|>text<|/ref|><|det|>[[115, 775, 555, 817]]<|/det|>
- Test PurposeVerify the Get Capabilities response issued from the TG.  

<|ref|>text<|/ref|><|det|>[[115, 825, 235, 890]]<|/det|>
- Reference[7] 5.1.1[5], [8]. 6.4.1=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 96, 731, 137]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.  

<|ref|>text<|/ref|><|det|>[[115, 147, 260, 163]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 171, 754, 204]]<|/det|>
Test ProcedureThe Lower Tester sends a GetCapabilities message to the IUT with the METADATA TRANSFER_GetCapabilities PDU parameter value set to COMPANY_ID.  

<|ref|>image<|/ref|><|det|>[[152, 214, 707, 479]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 487, 655, 503]]<|/det|>
<center>Figure 4.96: AVRCP/TG/CFG/BV-02-C [Get Capabilities response - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 518, 285, 560]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 567, 857, 599]]<|/det|>
The Lower Tester receives from the IUT the supported COMPANY_IDs. The first COMPANY_ID is the Bluetooth SIG COMPANY_ID.  

<|ref|>sub_title<|/ref|><|det|>[[115, 615, 748, 633]]<|/det|>
## AVRCP/TG/CFG/BI-01-C [Get Capabilities invalid behavior response - TG]  

<|ref|>text<|/ref|><|det|>[[115, 642, 239, 657]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 665, 839, 682]]<|/det|>
Verify the Get Capabilities response issued from the TG when an invalid capability is requested.  

<|ref|>text<|/ref|><|det|>[[115, 692, 223, 707]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 716, 231, 732]]<|/det|>
[7] 5.1.1  

<|ref|>text<|/ref|><|det|>[[144, 740, 233, 755]]<|/det|>
[5], [8] 6.4.1  

<|ref|>text<|/ref|><|det|>[[115, 765, 260, 781]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 792, 730, 831]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the Lower Tester.  - The AVCTP connection between the IUT and the Lower Tester is completed.  

<|ref|>sub_title<|/ref|><|det|>[[115, 843, 260, 858]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 866, 875, 899]]<|/det|>
Test ProcedureThe Lower Tester sends a GetCapabilities message to the IUT within the METADATA TRANSFER_GetCapabilities PDU parameter value set to an invalid capability ID – for example 0x7F.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[152, 70, 707, 336]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 344, 756, 360]]<|/det|>
<center>Figure 4.97: AVRCP/TG/CFG/BI-01-C [Get Capabilities invalid behavior response – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 375, 287, 414]]<|/det|>
- Expected OutcomePass verdict  

<|ref|>text<|/ref|><|det|>[[144, 421, 839, 455]]<|/det|>
The IUT responds to the Lower Tester with the Error status Invalid Parameter indicating that the capability ID issued was invalid.  

<|ref|>title<|/ref|><|det|>[[115, 469, 570, 489]]<|/det|>
#### 4.21.2 Player Application Settings commands  

<|ref|>text<|/ref|><|det|>[[115, 494, 812, 528]]<|/det|>
Verify the player application settings commands that are defined in the METADATA TRANSFER specification.  

<|ref|>sub_title<|/ref|><|det|>[[115, 542, 740, 562]]<|/det|>
## AVRCP/CT/PAS/BV-01-C [List Player Application Setting Attributes - CT]  

<|ref|>text<|/ref|><|det|>[[115, 570, 735, 612]]<|/det|>
- Test PurposeVerify the List Player Application Setting Attributes command issued from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 620, 255, 685]]<|/det|>
- Reference[7] 5.2.1[5], [8] 6.5.1  

<|ref|>text<|/ref|><|det|>[[115, 694, 260, 710]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 719, 730, 761]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.  

<|ref|>text<|/ref|><|det|>[[115, 771, 260, 787]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 794, 847, 828]]<|/det|>
The Upper Tester triggers the IUT to send a ListPlayerApplicationSettingAttributes command. No parameter needs to be passed for this PDU.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[148, 70, 714, 344]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 352, 745, 368]]<|/det|>
<center>Figure 4.98: AVRCP/CT/PAS/BV-01-C [List Player Application Setting Attributes – CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 382, 750, 448]]<|/det|>
- Expected OutcomePass verdictThe Lower Tester receives the List Player Application Settings Attributes command.  

<|ref|>sub_title<|/ref|><|det|>[[115, 462, 741, 481]]<|/det|>
## AVRCP/TG/PAS/BV-02-C [List Player Application Setting Attributes – TG]  

<|ref|>text<|/ref|><|det|>[[115, 490, 732, 536]]<|/det|>
- Test PurposeVerify the List Player Application Setting Attributes response issued from the TG.  

<|ref|>text<|/ref|><|det|>[[115, 543, 234, 604]]<|/det|>
- Reference[7] 5.2.1[5], [8] 6.5.1  

<|ref|>text<|/ref|><|det|>[[115, 613, 260, 629]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 639, 731, 680]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 875, 130]]<|/det|>
The Lower Tester sends a ListPlayerApplicationSettingAttributes command to the IUT. No parameter needs to be passed for this PDU.  

<|ref|>image<|/ref|><|det|>[[150, 138, 714, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 412, 746, 428]]<|/det|>
<center>Figure 4.99: AVRCP/TG/PAS/BV-02-C [List Player Application Setting Attributes – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 444, 553, 508]]<|/det|>
- Expected OutcomePass verdictThe IUT returns a response with zero or more attributes.  

<|ref|>sub_title<|/ref|><|det|>[[115, 522, 770, 541]]<|/det|>
## AVRCP/CT/PAS/BV-03-C [Get Player Application Setting Attribute Text – CT]  

<|ref|>text<|/ref|><|det|>[[115, 550, 771, 616]]<|/det|>
- Test PurposeVerify the Get Player Application Settings Attribute Text command issued from the CT.  

<|ref|>text<|/ref|><|det|>[[144, 622, 235, 662]]<|/det|>
[7] 5.2.5  [5], [8] 6.5.5  

<|ref|>text<|/ref|><|det|>[[115, 673, 260, 688]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 699, 731, 740]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 842, 130]]<|/det|>
The Upper Tester triggers the IUT to send a GetPlayerApplicationSettingAttributeText command containing one or more attribute IDs.  

<|ref|>image<|/ref|><|det|>[[150, 137, 714, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 411, 778, 428]]<|/det|>
<center>Figure 4.100: AVRCP/CT/PAS/BV-03-C [Get Player Application Setting Attribute Text - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 444, 810, 510]]<|/det|>
- Expected OutcomePass verdictThe Get Player Application Setting Attribute Text command is received by the Lower Tester.  

<|ref|>sub_title<|/ref|><|det|>[[115, 522, 770, 542]]<|/det|>
## AVRCP/TG/PAS/BV-04-C [Get Player Application Setting Attribute Text - TG]  

<|ref|>text<|/ref|><|det|>[[115, 550, 759, 593]]<|/det|>
- Test PurposeVerify the Get Player Application Setting Attribute Text response issued from the TG.  

<|ref|>text<|/ref|><|det|>[[115, 600, 237, 664]]<|/det|>
- Reference[7] 5.2.5[5], [8] 6.5.5  

<|ref|>text<|/ref|><|det|>[[115, 673, 260, 689]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 699, 866, 781]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The Lower Tester is aware of the available attributes for the IUT. This can be retrieved from the result of AVRCP/TG/PAS/BV-02-C [List Player Application Setting Attributes - TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 848, 130]]<|/det|>
The Lower Tester sends a GetPlayerApplicationSettingAttributeText command to the IUT with an attribute ID listed in the available attributes for the IUT.  

<|ref|>image<|/ref|><|det|>[[149, 137, 714, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 411, 780, 428]]<|/det|>
<center>Figure 4.101: AVRCP/TG/PAS/BV-04-C [Get Player Application Setting Attribute Text - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 443, 287, 483]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 490, 818, 523]]<|/det|>
The IUT returns the values in UTF- 8 format as specified by the Lower Tester. The values are Manufacturer dependent.  

<|ref|>sub_title<|/ref|><|det|>[[115, 539, 712, 558]]<|/det|>
## AVRCP/CT/PAS/BV-05-C [List Player Application Setting Values - CT]  

<|ref|>text<|/ref|><|det|>[[115, 567, 714, 608]]<|/det|>
Test Purpose Verify the List Player Application Setting Values command issued from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 616, 248, 682]]<|/det|>
Reference [7] 5.2.2 [5], [8] 6.5.2  

<|ref|>text<|/ref|><|det|>[[115, 690, 260, 706]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 715, 866, 799]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The IUT is aware of the available attributes for the Lower Tester. This can be retrieved from the result of AVRCP/CT/PAS/BV-01-C [List Player Application Setting Attributes - CT].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 856, 129]]<|/det|>
The Upper Tester triggers the IUT to send a ListPlayerApplicationSettingValues command with an attribute ID listed in the available attributes for the Lower Tester.  

<|ref|>image<|/ref|><|det|>[[146, 137, 714, 411]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 419, 736, 435]]<|/det|>
<center>Figure 4.102: AVRCP/CT/PAS/BV-05-C [List Player Application Setting Values - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 690, 515]]<|/det|>
Expected Outcome  Pass verdict  The List Player Application Setting Values is received by the Lower Tester.  

<|ref|>sub_title<|/ref|><|det|>[[115, 529, 714, 549]]<|/det|>
## AVRCP/TG/PAS/BV-06-C [List Player Application Setting Values - TG]  

<|ref|>text<|/ref|><|det|>[[115, 557, 712, 600]]<|/det|>
Test Purpose  Verify the List Player Application Setting Values response issued from the TG.  

<|ref|>text<|/ref|><|det|>[[115, 608, 250, 671]]<|/det|>
Reference  [7] 5.2.2  [5], [8] 6.5.2  

<|ref|>text<|/ref|><|det|>[[115, 680, 260, 696]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 707, 866, 789]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The Lower Tester is aware of the available attributes for the IUT. This can be retrieved from the result of AVRCP/TG/PAS/BV-02-C [List Player Application Setting Attributes - TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 867, 129]]<|/det|>
The Lower Tester sends a ListPlayerApplicationSettingValues command to the IUT with an attribute ID listed in the available attributes for the IUT.  

<|ref|>image<|/ref|><|det|>[[146, 137, 714, 410]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 419, 737, 435]]<|/det|>
<center>Figure 4.103: AVRCP/TG/PAS/BV-06-C [List Player Application Setting Values - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 810, 515]]<|/det|>
Expected Outcome  Pass verdict  The IUT returns the list of setting values for that Attribute ID as defined by the manufacturer.  

<|ref|>sub_title<|/ref|><|det|>[[115, 529, 742, 549]]<|/det|>
## AVRCP/CT/PAS/BV-07-C [Get Player Application Setting Value Text - CT]  

<|ref|>text<|/ref|><|det|>[[115, 557, 712, 600]]<|/det|>
Test Purpose  Verify the Player Application Setting Value Text command issued from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 608, 250, 670]]<|/det|>
Reference  [7] 5.2.6  [5], [8] 6.5.6  

<|ref|>text<|/ref|><|det|>[[115, 680, 260, 696]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 706, 871, 805]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The IUT is aware of the available attributes and corresponding values for the Lower Tester. This can be retrieved from the result of AVRCP/CT/PAS/BV-01-C [List Player Application Setting Attributes - CT] and AVRCP/CT/PAS/BV-05-C [List Player Application Setting Values - CT].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[116, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 877, 145]]<|/det|>
Test ProcedureInitiated by the Upper Tester, the IUT sends a Get Player Application Setting Value Text command to the Lower Tester, with attribute and value IDs listed in the available attributes and corresponding values for the Lower Tester.  

<|ref|>image<|/ref|><|det|>[[150, 155, 714, 430]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 437, 761, 453]]<|/det|>
<center>Figure 4.104: AVRCP/CT/PAS/BV-07-C [Get Player Application Setting Value Text - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 468, 715, 533]]<|/det|>
Expected Outcome Pass verdict The Get Player Application Setting Value Text is received by the Lower Tester.  

<|ref|>sub_title<|/ref|><|det|>[[115, 546, 744, 565]]<|/det|>
## AVRCP/TG/PAS/BV-08-C [Get Player Application Setting Value Text - TG]  

<|ref|>text<|/ref|><|det|>[[115, 574, 740, 616]]<|/det|>
Test Purpose Verify the Get Player Application Setting Value Text response issued from the TG.  

<|ref|>text<|/ref|><|det|>[[115, 624, 250, 688]]<|/det|>
Reference [7] 5.2.6 [5], [8] 6.5.6  

<|ref|>text<|/ref|><|det|>[[115, 698, 260, 713]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 723, 872, 820]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The Lower Tester is aware of the available attributes and corresponding values for the IUT. This can be retrieved from the result of AVRCP/TG/PAS/BV- 02- C [List Player Application Setting Attributes - TG] and AVRCP/TG/PAS/BV- 06- C [List Player Application Setting Values - TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[116, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 833, 130]]<|/det|>
The Lower Tester sends a Get Player Application Setting Value Text command to the IUT, with attribute and value IDs listed in the available attributes and corresponding values for the IUT.  

<|ref|>image<|/ref|><|det|>[[145, 137, 714, 411]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 419, 763, 435]]<|/det|>
<center>Figure 4.105: AVRCP/TG/PAS/BV-08-C [Get Player Application Setting Value Text - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 287, 490]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 498, 825, 531]]<|/det|>
The IUT returns the values in UTF- 8 format as requested by the Lower Tester. The values are manufacturer dependent.  

<|ref|>sub_title<|/ref|><|det|>[[115, 546, 770, 565]]<|/det|>
## AVRCP/CT/PAS/BV-09-C [Get Current Player Application Setting Value - CT]  

<|ref|>text<|/ref|><|det|>[[115, 574, 768, 616]]<|/det|>
Test Purpose Verify the Get Current Player Application Setting Value command issued from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 624, 256, 686]]<|/det|>
Reference [7] 5.2.3 [5], [8] 6.5.3  

<|ref|>text<|/ref|><|det|>[[115, 697, 260, 712]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 723, 864, 805]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The IUT is aware of the available attributes on the Lower Tester. This can be retrieved from the result of AVRCP/CT/PAS/BV-01-C [List Player Application Setting Attributes - CT].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[116, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 96, 881, 130]]<|/det|>
Test ProcedureInitiated by the Upper Tester, the IUT sends a Get Current Player Application Setting Value command to the Lower Tester containing an attribute ID listed in the available attributes for the Lower Tester.  

<|ref|>image<|/ref|><|det|>[[147, 137, 714, 412]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 419, 782, 435]]<|/det|>
<center>Figure 4.106: AVRCP/CT/PAS/BV-09-C [Get Current Player Application Setting Value - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 777, 515]]<|/det|>
Expected OutcomePass verdictThe Lower Tester receives the Get Current Player Application Setting Value command.  

<|ref|>sub_title<|/ref|><|det|>[[115, 529, 772, 549]]<|/det|>
## AVRCP/TG/PAS/BV-10-C [Get Current Player Application Setting Value - TG]  

<|ref|>text<|/ref|><|det|>[[115, 557, 763, 600]]<|/det|>
Test PurposeVerify the Get Current Player Application Setting Value response issued from the TG.  

<|ref|>text<|/ref|><|det|>[[115, 608, 255, 671]]<|/det|>
Reference [7] 5.2.3 [5], [8] 6.5.3  

<|ref|>text<|/ref|><|det|>[[115, 680, 260, 696]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 706, 864, 789]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The Lower Tester is aware of the available attributes on the IUT. This can be retrieved from the result of AVRCP/TG/PAS/BV- 02- C [List Player Application Setting Attributes - TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 96, 872, 130]]<|/det|>
The Lower Tester sends a Get Current Player Application Setting Value command to the IUT with an attribute ID listed in the available attributes for the IUT.  

<|ref|>image<|/ref|><|det|>[[144, 137, 714, 412]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 419, 784, 436]]<|/det|>
<center>Figure 4.107: AVRCP/TG/PAS/BV-10-C [Get Current Player Application Setting Value - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 451, 840, 515]]<|/det|>
Expected Outcome  Pass verdict  The IUT returns the list of values for the requested Attribute IDs as defined by the manufacturer.  

<|ref|>sub_title<|/ref|><|det|>[[115, 529, 699, 549]]<|/det|>
## AVRCP/CT/PAS/BV-11-C [Set Player Application Setting Value - CT]  

<|ref|>text<|/ref|><|det|>[[115, 557, 705, 600]]<|/det|>
Test Purpose  Verify the Set Player Application Setting Value command issued from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 608, 252, 670]]<|/det|>
Reference  [7] 5.2.4  [5], [8] 6.5.4  

<|ref|>text<|/ref|><|det|>[[115, 680, 260, 696]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 706, 870, 806]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The IUT is aware of the available attributes and corresponding values for the Lower Tester. This can be retrieved from the result of AVRCP/CT/PAS/BV-01-C [List Player Application Setting Attributes - CT] and AVRCP/CT/PAS/BV-05-C [List Player Application Setting Values - CT].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 868, 145]]<|/det|>
Test ProcedureInitiated by the Upper Tester, the IUT sends a Set Player Application Setting Value command to the Lower Tester, with attribute and value IDs listed in the available attributes and corresponding values for the Lower Tester.  

<|ref|>image<|/ref|><|det|>[[146, 155, 714, 420]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 428, 727, 444]]<|/det|>
<center>Figure 4.108: AVRCP/CT/PAS/BV-11-C [Set Player Application Setting Value - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 459, 285, 498]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[142, 507, 870, 540]]<|/det|>
The Lower Tester receives the SetPlayerApplicationSettingValue command the correct attribute and value ID.  

<|ref|>sub_title<|/ref|><|det|>[[115, 555, 879, 590]]<|/det|>
## AVRCP/TG/PAS/BI-01-C [Get Player Application Settings Attribute Text invalid behavior - TG]  

<|ref|>text<|/ref|><|det|>[[115, 599, 245, 615]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[141, 622, 858, 655]]<|/det|>
Verify the behavior of the target when a Get Player Application Settings Attribute Text command is issued with an invalid parameter.  

<|ref|>text<|/ref|><|det|>[[115, 660, 223, 676]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 684, 234, 722]]<|/det|>
[7] 5.2.5  [5], [8] 6.5.5  

<|ref|>text<|/ref|><|det|>[[115, 733, 260, 750]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 764, 730, 806]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 72, 870, 145]]<|/det|>
- Test Procedure The Lower Tester sends a Get Player Application Setting Attribute Text command to the IUT with parameters Num Player Application Setting Attributes \(= 1\) and Player Application Setting Attribute ID \(1 = 0x7F\) .  

<|ref|>image<|/ref|><|det|>[[146, 155, 714, 420]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 428, 852, 456]]<|/det|>
<center>Figure 4.109: AVRCP/TG/PAS/BI-01-C [Get Player Application Settings Attribute Text invalid behavior – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 473, 287, 512]]<|/det|>
- Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 520, 840, 554]]<|/det|>
The IUT returns an error response with error code 0x01 indicating that an invalid parameter was passed.  

<|ref|>sub_title<|/ref|><|det|>[[115, 569, 848, 588]]<|/det|>
## AVRCP/TG/PAS/BI-02-C [List Player Application Setting Values invalid behavior – TG]  

<|ref|>text<|/ref|><|det|>[[115, 596, 240, 612]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 619, 835, 652]]<|/det|>
Verify the ability of the TG to respond to a List Player Application Setting Values command with invalid parameters.  

<|ref|>text<|/ref|><|det|>[[115, 657, 225, 720]]<|/det|>
- Reference [7] 5.2.2 [5], [8] 6.5.2  

<|ref|>text<|/ref|><|det|>[[115, 730, 260, 746]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 762, 731, 803]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 870, 130]]<|/det|>
The Lower Tester sends a List Player Application Setting Value command to the IUT with parameter Player Application Attribute \(\mathsf{ID} = 0\times 7\mathsf{F}\) .  

<|ref|>image<|/ref|><|det|>[[146, 137, 714, 410]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 419, 839, 436]]<|/det|>
<center>Figure 4.110: AVRCP/TG/PAS/BI-02-C [List Player Application Setting Values invalid behavior – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 287, 490]]<|/det|>
- Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 498, 840, 531]]<|/det|>
The IUT returns an error response with error code 0x01 indicating that an invalid parameter was passed.  

<|ref|>sub_title<|/ref|><|det|>[[115, 546, 877, 565]]<|/det|>
## AVRCP/TG/PAS/BI-03-C [Get Player Application Setting Value Text invalid behavior – TG]  

<|ref|>text<|/ref|><|det|>[[115, 574, 245, 590]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 597, 864, 630]]<|/det|>
Verify the ability of the TG to respond to a Get Player Application Setting Value Text command with invalid parameters.  

<|ref|>text<|/ref|><|det|>[[115, 635, 225, 650]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 657, 208, 673]]<|/det|>
[7] 5.2.6  

<|ref|>text<|/ref|><|det|>[[144, 681, 233, 697]]<|/det|>
[5], [8] 6.5.6  

<|ref|>text<|/ref|><|det|>[[115, 708, 259, 724]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 740, 864, 821]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The Lower Tester is aware of the available attributes for the IUT. This can be retrieved from the result of AVRCP/TG/PAS/BV-02-C [List Player Application Setting Attributes – TG].=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
## Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 859, 146]]<|/det|>
The Lower Tester sends a Get Player Application Setting Value Text command to the IUT. The attribute ID passed is listed in the available attributes for the IUT. The other parameter settings are Num Player Application Settings \(= 1\) and Player Application Setting Value \(= 0x7F\) .  

<|ref|>image<|/ref|><|det|>[[146, 155, 714, 430]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 437, 860, 452]]<|/det|>
<center>Figure 4.111: AVRCP/TG/PAS/BI-03-C [Get Player Application setting Value Text invalid behavior – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 467, 285, 483]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 492, 238, 507]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 515, 840, 547]]<|/det|>
The IUT returns an error response with error code 0x01 indicating that an invalid parameter was passed.  

<|ref|>sub_title<|/ref|><|det|>[[115, 563, 870, 596]]<|/det|>
## AVRCP/TG/PAS/BI-04-C [Get Current Player Application Setting Value invalid behavior – TG]  

<|ref|>text<|/ref|><|det|>[[115, 606, 245, 621]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 630, 852, 662]]<|/det|>
Verify the ability of the TG to respond to a Get Current Player Application Setting Value command with invalid parameters.  

<|ref|>text<|/ref|><|det|>[[115, 667, 228, 682]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 691, 234, 730]]<|/det|>
[7] 5.2.3  [5], [8] 6.5.3  

<|ref|>text<|/ref|><|det|>[[115, 741, 260, 756]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 773, 730, 814]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 96, 852, 130]]<|/det|>
The Lower Tester sends a Get Current Player Application Setting Value command to the IUT with parameters Num Player Application Settings \(= 1\) and Player Application Setting Value \(= 0x7F\) .  

<|ref|>image<|/ref|><|det|>[[146, 137, 714, 410]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[143, 419, 848, 447]]<|/det|>
<center>Figure 4.112: AVRCP/TG/PAS/BI-04-C [Get Current Player Application Setting Value invalid behavior – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 464, 285, 480]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 489, 238, 504]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[143, 512, 840, 545]]<|/det|>
The IUT returns an error response with error code 0x01 indicating that an invalid parameter was passed.  

<|ref|>sub_title<|/ref|><|det|>[[115, 560, 836, 578]]<|/det|>
## AVRCP/TG/PAS/BI-05-C [Set Player Application Setting Value invalid behavior – TG]  

<|ref|>text<|/ref|><|det|>[[115, 587, 245, 602]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[140, 610, 875, 642]]<|/det|>
Verify the ability of the TG to respond to a Set Player Application Setting Value command with invalid parameters.  

<|ref|>text<|/ref|><|det|>[[115, 648, 225, 663]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 671, 220, 686]]<|/det|>
[7] 5.2.4  

<|ref|>text<|/ref|><|det|>[[144, 695, 234, 710]]<|/det|>
[5], [8] 6.5.4  

<|ref|>text<|/ref|><|det|>[[115, 720, 260, 736]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 753, 730, 793]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 877, 145]]<|/det|>
The Lower Tester sends a Set Player Application Setting Value command to the IUT with parameters Num Player Application Setting \(= 1\) , Player Application Setting Attribute \(\mathrm{ID} = 0\mathrm{x}02\) and Player Application Setting Value \(= 0\mathrm{x}7\mathrm{F}\) .  

<|ref|>image<|/ref|><|det|>[[146, 155, 714, 420]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 428, 830, 444]]<|/det|>
<center>Figure 4.113: AVRCP/TG/PAS/BI-05-C [Set Player Application Setting Value invalid behavior – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 459, 287, 500]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 508, 839, 541]]<|/det|>
The IUT returns an error response with error code 0x01 indicating that an invalid parameter was passed.  

<|ref|>title<|/ref|><|det|>[[115, 554, 485, 572]]<|/det|>
#### 4.21.3 Media Information commands  

<|ref|>text<|/ref|><|det|>[[115, 579, 820, 596]]<|/det|>
Verify the media information commands related to play status as well as information about media.  

<|ref|>sub_title<|/ref|><|det|>[[114, 610, 517, 628]]<|/det|>
## AVRCP/CT/MDI/BV-01-C [Get Play Status - CT]  

<|ref|>text<|/ref|><|det|>[[115, 638, 558, 678]]<|/det|>
Test Purpose Verify the Get Play Status command issued from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 687, 260, 752]]<|/det|>
Reference [7] 5.4.1 [5], [8] 6.7.1  

<|ref|>text<|/ref|><|det|>[[115, 761, 260, 777]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 787, 648, 828]]<|/det|>
- One ACL connection exists between the IUT and the test system.- AVCTP connection exists between the IUT and the test system.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 96, 848, 130]]<|/det|>
Test ProcedureInitiated by the Upper Tester, the IUT sends a Get Play Status command to the Lower Tester. No parameters need to be passed for this command.  

<|ref|>image<|/ref|><|det|>[[146, 137, 714, 411]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 419, 588, 435]]<|/det|>
<center>Figure 4.114: AVRCP/CT/MDI/BV-01-C [Get play status - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 560, 515]]<|/det|>
Expected Outcome Pass verdict The Lower Tester receives the GetPlayStatus command.  

<|ref|>sub_title<|/ref|><|det|>[[115, 530, 520, 549]]<|/det|>
## AVRCP/TG/MDI/BV-02-C [Get Play Status - TG]  

<|ref|>text<|/ref|><|det|>[[115, 558, 245, 573]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 581, 870, 614]]<|/det|>
Verify the Get Play Status response issued from the TG. Test to be conducted for all three modes of play status on the TG - Playing, Paused, and Stop status.  

<|ref|>text<|/ref|><|det|>[[115, 619, 222, 634]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 642, 204, 657]]<|/det|>
[7] 5.4.1  

<|ref|>text<|/ref|><|det|>[[144, 666, 232, 681]]<|/det|>
[5], [8] 6.7.1  

<|ref|>text<|/ref|><|det|>[[115, 691, 259, 707]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 723, 648, 767]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the test system.- AVCTP connection exists between the IUT and the test system.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 865, 129]]<|/det|>
The Lower Tester sends a Get Play Status command to the IUT. No parameters need to be passed for this command.  

<|ref|>image<|/ref|><|det|>[[145, 137, 714, 412]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 420, 593, 436]]<|/det|>
<center>Figure 4.115: AVRCP/TG/MDI/BV-02-C [Get Play Status - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 451, 570, 515]]<|/det|>
- Expected OutcomePass verdictThe IUT returns the correct current play status of the MP.  

<|ref|>sub_title<|/ref|><|det|>[[115, 530, 580, 549]]<|/det|>
## AVRCP/CT/MDI/BV-03-C [Get Element Attributes - CT]  

<|ref|>text<|/ref|><|det|>[[115, 558, 608, 601]]<|/det|>
- Test PurposeVerify the Get Element Attributes command issued from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 609, 250, 672]]<|/det|>
- Reference[7] 5.3.1[5], [8] 6.6.1  

<|ref|>text<|/ref|><|det|>[[115, 681, 260, 696]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 707, 648, 749]]<|/det|>
- One ACL connection exists between the IUT and the test system.- AVCTP connection exists between the IUT and the test system.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[140, 96, 872, 114]]<|/det|>
Test ProcedureInitiated by the Upper Tester, the IUT sends a Get Element Attributes command to the Lower Tester.  

<|ref|>image<|/ref|><|det|>[[146, 121, 700, 388]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 395, 637, 411]]<|/det|>
<center>Figure 4.116: AVRCP/CT/MDI/BV-03-C [Get Element Attributes - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 426, 618, 491]]<|/det|>
Expected OutcomePass verdictThe Lower Tester receives the Get Element Attributes command.  

<|ref|>sub_title<|/ref|><|det|>[[115, 505, 582, 524]]<|/det|>
## AVRCP/TG/MDI/BV-04-C [Get Element Attributes - TG]  

<|ref|>text<|/ref|><|det|>[[115, 533, 775, 576]]<|/det|>
Test PurposeVerify the Get Element Attributes response for getting all attributes issued from the TG.  

<|ref|>text<|/ref|><|det|>[[115, 585, 262, 650]]<|/det|>
Reference[7] 5.3.1[5], [8] 6.6.1  

<|ref|>text<|/ref|><|det|>[[115, 658, 261, 674]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 684, 648, 725]]<|/det|>
- One ACL connection exists between the IUT and the test system.- AVCTP connection exists between the IUT and the test system.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 97, 875, 130]]<|/det|>
The Lower Tester sends a Get Element Attributes command to the IUT with the parameters Identifier \(=\) Playing and NumAttributes \(= 0\) .  

<|ref|>image<|/ref|><|det|>[[145, 138, 714, 411]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 420, 640, 436]]<|/det|>
<center>Figure 4.117: AVRCP/TG/MDI/BV-04-C [Get Element Attributes - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 451, 387, 515]]<|/det|>
Expected Outcome Pass verdict The IUT returns all attribute information.  

<|ref|>text<|/ref|><|det|>[[115, 525, 192, 540]]<|/det|>
Notes  

<|ref|>text<|/ref|><|det|>[[144, 549, 857, 581]]<|/det|>
NotesThe test case is used to retrieve all the elements (NumAttributes \(= 0 \times 00\) ) of a selected entry on the target.  

<|ref|>sub_title<|/ref|><|det|>[[115, 597, 582, 616]]<|/det|>
## AVRCP/TG/MDI/BV-05-C [Get Element Attributes - TG]  

<|ref|>text<|/ref|><|det|>[[115, 625, 818, 665]]<|/det|>
Test PurposeVerify the Get Element Attributes response for getting selected attributes issued from the TG.  

<|ref|>text<|/ref|><|det|>[[115, 675, 240, 739]]<|/det|>
Reference [7] 5.3.1 [5], [8] 6.6.1  

<|ref|>text<|/ref|><|det|>[[115, 749, 260, 764]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 775, 647, 815]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the test system.- AVCTP connection exists between the IUT and the test system.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 874, 130]]<|/det|>
The Lower Tester sends a Get Element Attributes command to the IUT with the parameters Identifier \(=\) Playing, NumAttributes \(=\) n and Attributeld \(=\) n Attribute Ids.  

<|ref|>image<|/ref|><|det|>[[145, 137, 714, 411]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 419, 639, 435]]<|/det|>
<center>Figure 4.118: AVRCP/TG/MDI/BV-05-C [Get Element Attributes - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 285, 466]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 475, 230, 490]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 498, 414, 514]]<|/det|>
The IUT returns attribute information.  

<|ref|>text<|/ref|><|det|>[[115, 525, 191, 540]]<|/det|>
Notes  

<|ref|>text<|/ref|><|det|>[[144, 548, 745, 565]]<|/det|>
NotesThe test case is used to retrieve specific elements of a selected entry on the target.  

<|ref|>sub_title<|/ref|><|det|>[[115, 580, 884, 614]]<|/det|>
## AVRCP/CT/MDI/BV-06-C [CT can retrieve the Metadata for the currently playing track from TG with future SDP version - Get Element Attributes]  

<|ref|>text<|/ref|><|det|>[[115, 623, 245, 639]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 647, 840, 680]]<|/det|>
Verify that the IUT, which does not support browsing, can retrieve the Metadata for the currently playing track when the TG supports a later profile version.  

<|ref|>text<|/ref|><|det|>[[115, 685, 223, 700]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 708, 210, 723]]<|/det|>
[7] 5.3.1  

<|ref|>text<|/ref|><|det|>[[144, 731, 232, 747]]<|/det|>
[5], [8] 6.6.1  

<|ref|>text<|/ref|><|det|>[[115, 758, 259, 773]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 790, 850, 824]]<|/det|>
The Lower Tester supports an SDP version that is greater than the current published version, e.g., AVRCP v1.9.  

<|ref|>text<|/ref|><|det|>[[144, 827, 852, 860]]<|/det|>
The Lower Tester has all the bits in its Supported Features SDP attributes set, including those that are RFA.  

<|ref|>text<|/ref|><|det|>[[173, 864, 456, 879]]<|/det|>
A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[173, 887, 599, 903]]<|/det|>
The Lower Tester acting as TG is currently playing a track.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[141, 96, 872, 114]]<|/det|>
Initiated by the Upper Tester, the IUT sends a Get Element Attributes command to the Lower Tester.  

<|ref|>image<|/ref|><|det|>[[145, 120, 713, 396]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[142, 403, 855, 430]]<|/det|>
<center>Figure 4.119: AVRCP/CT/MDI/BV-06-C [CT can retrieve the Metadata for the currently playing track from TG with future SDP version – Get Element Attributes] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 447, 285, 463]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 472, 238, 487]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[142, 495, 861, 527]]<|/det|>
The IUT is able to successfully retrieve Metadata from the Lower Tester and provide it to the Upper Tester.  

<|ref|>title<|/ref|><|det|>[[115, 541, 422, 559]]<|/det|>
#### 4.21.4 Notification commands  

<|ref|>text<|/ref|><|det|>[[115, 567, 409, 583]]<|/det|>
Verify the notification commands issued.  

<|ref|>sub_title<|/ref|><|det|>[[115, 597, 565, 616]]<|/det|>
## AVRCP/CT/NFY/BV-01-C [Register Notification - CT]  

<|ref|>text<|/ref|><|det|>[[115, 625, 590, 666]]<|/det|>
- Test PurposeVerify the Register Notification command issued from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 675, 240, 690]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 699, 210, 714]]<|/det|>
[7] 5.4.2  

<|ref|>text<|/ref|><|det|>[[144, 722, 234, 738]]<|/det|>
[5], [8] 6.7.2  

<|ref|>text<|/ref|><|det|>[[115, 748, 260, 763]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 774, 647, 815]]<|/det|>
- One ACL connection exists between the IUT and the test system.- AVCTP connection exists between the IUT and the test system.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[141, 96, 852, 114]]<|/det|>
Test ProcedureInitiated by the Upper Tester, the IUT sends a Register Notification command to the Lower Tester.  

<|ref|>image<|/ref|><|det|>[[146, 120, 714, 396]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 403, 624, 419]]<|/det|>
<center>Figure 4.120: AVRCP/CT/NFY/BV-01-C [Register Notification - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 433, 598, 500]]<|/det|>
Expected Outcome Pass verdict The Lower Tester receives the Register Notification command.  

<|ref|>sub_title<|/ref|><|det|>[[115, 513, 567, 533]]<|/det|>
## AVRCP/TG/NFY/BV-02-C [Register Notification - TG]  

<|ref|>text<|/ref|><|det|>[[115, 541, 586, 585]]<|/det|>
Test Purpose Verify the Register Notification response issued from the TG.  

<|ref|>text<|/ref|><|det|>[[115, 592, 235, 656]]<|/det|>
Reference [7] 5.4.2 [5], [8] 6.7.2  

<|ref|>text<|/ref|><|det|>[[115, 664, 260, 680]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 690, 647, 732]]<|/det|>
Initial Condition- One ACL connection exists between the IUT and the test system.- AVCTP connection exists between the IUT and the test system.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 839, 130]]<|/det|>
The Lower Tester sends a Register Notification command to the IUT with parameters EventID = 0x0002. The Playback Interval parameter is not needed.  

<|ref|>image<|/ref|><|det|>[[144, 137, 714, 411]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 419, 626, 435]]<|/det|>
<center>Figure 4.121: AVRCP/TG/NFY/BV-02-C [Register Notification - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 450, 285, 466]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 474, 238, 490]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 497, 595, 514]]<|/det|>
The IUT returns an INTERIM response with the current status.  

<|ref|>text<|/ref|><|det|>[[144, 521, 835, 555]]<|/det|>
After the track change happens, the IUT sends a CHANGED response indicating that the event EVENT_TRACK_CHANGED has been triggered.  

<|ref|>text<|/ref|><|det|>[[115, 560, 191, 574]]<|/det|>
Notes  

<|ref|>text<|/ref|><|det|>[[144, 581, 877, 599]]<|/det|>
NotesThe event used for the test is EVENT_TRACK_CHANGED (ID 0x02) which is registered with the IUT.  

<|ref|>sub_title<|/ref|><|det|>[[115, 621, 881, 656]]<|/det|>
## AVRCP/TG/NFY/BV-03-C [Register Notification EVENT_PLAYER_APPLICATION_SETTING_CHANGED - TG]  

<|ref|>text<|/ref|><|det|>[[115, 665, 245, 681]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 688, 876, 722]]<|/det|>
Verify the TG response for a register notification command for EVENT_PLAYER_APPLICATION_SETTING_CHANGED with all player application setting attributes.  

<|ref|>text<|/ref|><|det|>[[115, 727, 228, 742]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 750, 234, 789]]<|/det|>
[7] 5.4.2  [5], [8] 6.7.2  

<|ref|>text<|/ref|><|det|>[[115, 799, 260, 815]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 831, 647, 848]]<|/det|>
One ACL connection exists between the IUT and the test system.  

<|ref|>text<|/ref|><|det|>[[144, 856, 635, 873]]<|/det|>
AVCTP connection exists between the IUT and the test system.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 881, 130]]<|/det|>
The Lower Tester sends a Register Notification command to the IUT with parameters EventID = 0x08. The Playback Interval parameter is not needed.  

<|ref|>image<|/ref|><|det|>[[146, 137, 712, 412]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 419, 844, 448]]<|/det|>
<center>Figure 4.122: AVRCP/TG/NFY/BV-03-C [Register Notification EVENT_PLAYER_APPLICATION_SETTING_CHANGED - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 464, 285, 480]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 488, 238, 503]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 511, 595, 528]]<|/det|>
The IUT returns an INTERIM response with the current status.  

<|ref|>text<|/ref|><|det|>[[141, 534, 884, 568]]<|/det|>
Following the player application setting changes, the IUT sends a CHANGED response indicating that the event EVENT_PLAYER_APPLICATION_SETTING_CHANGED has been triggered.  

<|ref|>text<|/ref|><|det|>[[140, 572, 852, 589]]<|/det|>
The notification response contains all player application setting attributes with their current values.  

<|ref|>text<|/ref|><|det|>[[115, 599, 191, 614]]<|/det|>
Notes  

<|ref|>text<|/ref|><|det|>[[140, 621, 853, 655]]<|/det|>
The event used for the test is EVENT_PLAYER_APPLICATION_SETTING_CHANGED (ID 0x08), which is registered with the IUT.  

<|ref|>sub_title<|/ref|><|det|>[[115, 675, 696, 694]]<|/det|>
## AVRCP/TG/NFY/BV-04-C [Track Changed - No Selected Track - TG]  

<|ref|>text<|/ref|><|det|>[[115, 702, 668, 744]]<|/det|>
Test PurposeVerify the Track Changed INTERIM response when no track is selected.  

<|ref|>text<|/ref|><|det|>[[115, 753, 240, 817]]<|/det|>
Reference [7] 5.4.2 [5], [8] 6.7.2  

<|ref|>text<|/ref|><|det|>[[115, 826, 260, 842]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 853, 477, 895]]<|/det|>
- The IUT is active as AVRCP TG role.- No Track is currently selected on the IUT.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 792, 113]]<|/det|>
The Lower Tester issues a valid RegisterNotification for the EVENT_TRACK_CHANGED.  

<|ref|>image<|/ref|><|det|>[[144, 120, 712, 395]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 402, 732, 419]]<|/det|>
<center>Figure 4.123: AVRCP/TG/NFY/BV-04-C [Track Changed – No Selected Track – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 433, 287, 476]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 483, 795, 515]]<|/det|>
The IUT issues a correctly formatted RegisterNotification Interim Response for the EVENT_TRACK_CHANGED with the Identifier Parameter set to 0xFFFFFFFFFFFFFFFF.  

<|ref|>sub_title<|/ref|><|det|>[[115, 530, 657, 549]]<|/det|>
## AVRCP/TG/NFY/BV-05-C [Track Changed – Playing Track – TG]  

<|ref|>text<|/ref|><|det|>[[115, 558, 650, 600]]<|/det|>
Test Purpose Verify the Track Changed INTERIM response when a track is playing.  

<|ref|>text<|/ref|><|det|>[[115, 608, 259, 670]]<|/det|>
Reference [7] 5.4.2 [5], [8] 6.7.2  

<|ref|>text<|/ref|><|det|>[[115, 680, 260, 696]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 707, 535, 748]]<|/det|>
The IUT is active as AVRCP v1.3 or later TG role. A Track is currently playing on the IUT.  

<|ref|>text<|/ref|><|det|>[[115, 758, 260, 774]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 781, 792, 798]]<|/det|>
The Lower Tester issues a valid RegisterNotification for the EVENT_TRACK_CHANGERD.  

<|ref|>text<|/ref|><|det|>[[115, 808, 287, 844]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 854, 738, 888]]<|/det|>
The IUT issues a correctly formatted RegisterNotification Interim Response for the EVENT_TRACK CHANGED with the Identifier Parameter set to 0x0.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[112, 68, 787, 88]]<|/det|>
## AVRCP/TG/NFY/BV-06-C [Track Changed - Playing Track in NowPlaying - TG]  

<|ref|>text<|/ref|><|det|>[[115, 96, 245, 112]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[141, 120, 857, 154]]<|/det|>
Verify the Track Changed INTERIM response in the context of the Now Playing list when a track is playing.  

<|ref|>text<|/ref|><|det|>[[115, 157, 223, 172]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 180, 238, 197]]<|/det|>
[5], [8] 6.7.2  

<|ref|>text<|/ref|><|det|>[[144, 204, 259, 219]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 239, 535, 255]]<|/det|>
- The IUT is active as AVRCP v1.4 or later TG role.  

<|ref|>text<|/ref|><|det|>[[144, 263, 452, 279]]<|/det|>
- A track is currently playing on the IUT.  

<|ref|>text<|/ref|><|det|>[[115, 290, 259, 306]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 314, 777, 330]]<|/det|>
1. The Lower Tester retrieves the Now Playing list from the IUT with the GetFolderltems  

<|ref|>text<|/ref|><|det|>[[144, 331, 536, 347]]<|/det|>
Command/Response in the scope of NowPlaying.  

<|ref|>text<|/ref|><|det|>[[140, 347, 806, 364]]<|/det|>
2. The Lower Tester issues a valid RegisterNotification for the EVENT_TRACK_CHANGED.  

<|ref|>image<|/ref|><|det|>[[144, 370, 714, 646]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[142, 653, 796, 669]]<|/det|>
<center>Figure 4.124: AVRCP/TG/NFY/BV-06-C [Track Changed - Playing Track In NowPlaying - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 684, 285, 700]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 709, 237, 724]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 731, 740, 764]]<|/det|>
The IUT issues a correctly formatted RegisterNotification Interim Response for the EVENT_TRACK_CHANGED with:  

<|ref|>text<|/ref|><|det|>[[144, 774, 700, 815]]<|/det|>
- The Identifier Parameter set to a UID that is listed in the Now Playing list- That UID being the UID of the track that is currently played  

<|ref|>sub_title<|/ref|><|det|>[[115, 828, 803, 848]]<|/det|>
## AVRCP/TG/NFY/BV-07-C [Track Changed - Changing Track in NowPlaying - TG]  

<|ref|>text<|/ref|><|det|>[[115, 857, 255, 873]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 880, 755, 897]]<|/det|>
Verify the Track Changed INTERIM response when changing a track in NowPlaying.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 222, 88]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 97, 235, 114]]<|/det|>
[5], [8] 6.7.2  

<|ref|>text<|/ref|><|det|>[[115, 123, 260, 139]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 148, 787, 165]]<|/det|>
- The IUT is active as AVRCP v1.4 or later TG role and supports the browsing feature.  

<|ref|>text<|/ref|><|det|>[[144, 172, 468, 188]]<|/det|>
- A track is currently playing on the IUT.  

<|ref|>text<|/ref|><|det|>[[144, 195, 483, 211]]<|/det|>
- EVENT_TRACK_CHANGED is registered.  

<|ref|>text<|/ref|><|det|>[[115, 223, 260, 239]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 247, 780, 263]]<|/det|>
1. The Lower Tester retrieves the Now Playing list from the IUT with the GetFolderltems  

<|ref|>text<|/ref|><|det|>[[144, 264, 536, 280]]<|/det|>
Command/Response in the scope of NowPlaying.  

<|ref|>text<|/ref|><|det|>[[144, 281, 806, 297]]<|/det|>
2. The Lower Tester issues a valid RegisterNotification for the EVENT_TRACK_CHANGED.  

<|ref|>text<|/ref|><|det|>[[144, 298, 330, 313]]<|/det|>
3. The track is changed.  

<|ref|>text<|/ref|><|det|>[[144, 315, 728, 330]]<|/det|>
4. After receiving notification of the track change, the Lower Tester issues a valid  

<|ref|>text<|/ref|><|det|>[[170, 331, 586, 347]]<|/det|>
RegisterNotification for the EVENT_TRACK_CHANGED.  

<|ref|>image<|/ref|><|det|>[[144, 353, 712, 737]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[142, 744, 810, 761]]<|/det|>
<center>Figure 4.125: AVRCP/TG/NFY/BV-07-C [Track Changed – Changing Track in NowPlaying – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 776, 285, 792]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 801, 237, 816]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 823, 743, 840]]<|/det|>
The IUT returns the UID of the track in the Now Playing list that is currently played.  

<|ref|>text<|/ref|><|det|>[[144, 847, 765, 864]]<|/det|>
The IUT returns an interim response for each RegisterNotification command received.  

<|ref|>text<|/ref|><|det|>[[144, 870, 711, 887]]<|/det|>
The IUT returns the response for the EVENT_TRACK_CHANGED notification.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[113, 69, 667, 88]]<|/det|>
## AVRCP/TG/NFY/BV-08-C [Track Changed - Selected Track - TG]  

<|ref|>text<|/ref|><|det|>[[115, 96, 697, 140]]<|/det|>
- Test PurposeVerify the Track Changed INTERIM response when the track is SELECTED.  

<|ref|>text<|/ref|><|det|>[[115, 147, 260, 210]]<|/det|>
- Reference[7] 5.4.2[5], [8] 6.7.2  

<|ref|>text<|/ref|><|det|>[[115, 220, 260, 235]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[143, 246, 488, 287]]<|/det|>
- The IUT is active as AVRCP TG role.- A track is currently SELECTED on the IUT.  

<|ref|>text<|/ref|><|det|>[[115, 297, 260, 314]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[140, 320, 790, 338]]<|/det|>
The Lower Tester issues a valid RegisterNotification for the EVENT_TRACK_CHANGED.  

<|ref|>text<|/ref|><|det|>[[115, 347, 286, 363]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 371, 238, 386]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 393, 740, 409]]<|/det|>
The IUT issues a correctly formatted RegisterNotification Interim Response for the  

<|ref|>text<|/ref|><|det|>[[144, 411, 360, 427]]<|/det|>
EVENT_TRACK_CHANGED.  

<|ref|>text<|/ref|><|det|>[[144, 430, 795, 465]]<|/det|>
The Identifier Parameter is set to a value other than 0xFFFFFFFF for an IUT that supports AVRCP v1.3.  

<|ref|>text<|/ref|><|det|>[[144, 468, 745, 485]]<|/det|>
The Identifier Parameter is set to 0x0 for an IUT that supports AVRCP v1.4 or later.  

<|ref|>sub_title<|/ref|><|det|>[[115, 510, 688, 529]]<|/det|>
## AVRCP/TG/NFY/BI-01-C [Register for events invalid behavior - TG]  

<|ref|>text<|/ref|><|det|>[[115, 537, 245, 553]]<|/det|>
- Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 560, 628, 577]]<|/det|>
Verify that the TG can handle an invalid event ID sent from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 586, 225, 652]]<|/det|>
- Reference[7] 5.4.2[5], [8], 6.7.2  

<|ref|>text<|/ref|><|det|>[[115, 660, 260, 676]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 686, 648, 727]]<|/det|>
- One ACL connection exists between the IUT and the test system.- AVCTP connection exists between the IUT and the test system.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[143, 96, 875, 130]]<|/det|>
The Lower Tester sends a Register Notification command to the IUT with parameter EventID = 0xFF. The Playback Interval parameter is not needed.  

<|ref|>image<|/ref|><|det|>[[144, 137, 714, 412]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 420, 717, 436]]<|/det|>
<center>Figure 4.126: AVRCP/TG/NFY/BI-01-C [Register for events invalid behavior – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 451, 296, 491]]<|/det|>
Expected Outcome Pass verdict  

<|ref|>text<|/ref|><|det|>[[143, 498, 799, 515]]<|/det|>
The IUT returns the error code 0x01 indicating that an invalid parameter has been passed.  

<|ref|>title<|/ref|><|det|>[[115, 528, 377, 546]]<|/det|>
#### 4.21.5 Invalid commands  

<|ref|>text<|/ref|><|det|>[[115, 552, 593, 569]]<|/det|>
Verify that the TG can handle an invalid PDU ID sent from the CT.  

<|ref|>sub_title<|/ref|><|det|>[[115, 584, 500, 602]]<|/det|>
## AVRCP/TG/INV/BI-01-C [Invalid PDU ID – TG]  

<|ref|>text<|/ref|><|det|>[[115, 611, 625, 652]]<|/det|>
Test Purpose Verify that the TG can handle an invalid PDU ID sent from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 661, 225, 725]]<|/det|>
Reference [7] 5.7 [5], [8] 6.15  

<|ref|>text<|/ref|><|det|>[[115, 735, 260, 750]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 760, 730, 801]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 850, 130]]<|/det|>
The Lower Tester sends a Metadata Transfer Command to the IUT with a PDU ID = 0xFF and no command parameters.  

<|ref|>image<|/ref|><|det|>[[145, 138, 714, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 412, 580, 428]]<|/det|>
<center>Figure 4.127: AVRCP/TG/INV/BI-01-C [Invalid PDU ID - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 443, 880, 508]]<|/det|>
Expected Outcome  Pass verdict  The IUT returns an Error Response with error code 0x00 indicating that the PDU was not understood.  

<|ref|>sub_title<|/ref|><|det|>[[114, 522, 504, 541]]<|/det|>
## AVRCP/TG/INV/BI-02-C [General Reject - TG]  

<|ref|>text<|/ref|><|det|>[[115, 550, 535, 592]]<|/det|>
Test Purpose  Verify the General Reject response issued by the TG.  

<|ref|>text<|/ref|><|det|>[[115, 600, 250, 641]]<|/det|>
Reference [5], [8] 6.15.2  

<|ref|>text<|/ref|><|det|>[[115, 650, 260, 664]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 675, 860, 740]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- AVCTP control and browsing channels are established between the IUT and the Lower Tester.- The IUT is acting as AVRCP TG role in category 1 or 3.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 96, 841, 130]]<|/det|>
The Lower Tester sends an AVRCP specific Browsing command with an invalid PDU ID and the Browsing channel.  

<|ref|>image<|/ref|><|det|>[[147, 137, 714, 404]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[147, 411, 582, 428]]<|/det|>
<center>Figure 4.128: AVRCP/TG/INV/BI-02-C [General Reject - TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 443, 275, 459]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 467, 238, 483]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 490, 822, 507]]<|/det|>
The IUT issues a General Reject response with the error code indicating an invalid command.  

<|ref|>sub_title<|/ref|><|det|>[[115, 520, 537, 539]]<|/det|>
## 4.21.6 Basic Group Navigation commands  

<|ref|>text<|/ref|><|det|>[[115, 545, 594, 562]]<|/det|>
Verify that the Basic Group Navigation commands are transferred.  

<|ref|>title<|/ref|><|det|>[[115, 572, 418, 588]]<|/det|>
#### 4.21.6.1 Next Group command transfer  

<|ref|>text<|/ref|><|det|>[[115, 598, 633, 664]]<|/det|>
Test PurposeCT: Verify that the CT can send Next Group commands to the TG.TG: Verify that the TG reacts to Next Group command from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 672, 240, 688]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 696, 240, 735]]<|/det|>
[7] 5.6.1  [5], [8] 6.14.1  

<|ref|>text<|/ref|><|det|>[[115, 745, 260, 761]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 772, 850, 829]]<|/det|>
- CT: A connection for control is established.- TG: A connection for control is established. The TG should be ready to react to the command from the CT.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 325, 88]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 98, 648, 162]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/BGN/BV-01-C [Next Group command transfer]</td></tr><tr><td>AVRCP/TG/BGN/BV-01-C [Next Group command transfer]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[145, 169, 495, 184]]<|/det|>
Table 4.42: Next Group command transfer test cases  

<|ref|>text<|/ref|><|det|>[[115, 200, 260, 215]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 223, 785, 240]]<|/det|>
CT: Initiate the required user actions (e.g., press button) to perform Next Group function.  

<|ref|>text<|/ref|><|det|>[[145, 247, 368, 263]]<|/det|>
TG: No user action is required.  

<|ref|>text<|/ref|><|det|>[[115, 273, 287, 288]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 297, 238, 312]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 320, 425, 335]]<|/det|>
CT: The Next Group command is sent.  

<|ref|>text<|/ref|><|det|>[[144, 343, 852, 377]]<|/det|>
TG: The TG reacts to Next Group command sent from the CT to move to the first song in the next group.  

<|ref|>title<|/ref|><|det|>[[115, 389, 452, 405]]<|/det|>
#### 4.21.6.2 Previous Group command transfer  

<|ref|>text<|/ref|><|det|>[[115, 416, 245, 431]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[144, 439, 661, 456]]<|/det|>
CT: Verify that the CT can send Previous Group commands to the TG.  

<|ref|>text<|/ref|><|det|>[[144, 463, 662, 479]]<|/det|>
TG: Verify that the TG reacts to Previous Group command from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 489, 223, 504]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 513, 207, 529]]<|/det|>
[7] 5.6.2  

<|ref|>text<|/ref|><|det|>[[144, 538, 243, 554]]<|/det|>
[5], [8] 6.14.2  

<|ref|>text<|/ref|><|det|>[[115, 564, 260, 579]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 590, 485, 606]]<|/det|>
CT: A connection for control is established.  

<|ref|>text<|/ref|><|det|>[[144, 614, 850, 647]]<|/det|>
TG: A connection for control is established. The TG should be ready to react to the command from the CT.  

<|ref|>text<|/ref|><|det|>[[115, 658, 325, 673]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 682, 648, 747]]<|/det|>

<table><tr><td>Test Case</td></tr><tr><td>AVRCP/CT/BG/N/BV-02-C [Previous Group command transfer]</td></tr><tr><td>AVRCP/TG/BG/N/BV-02-C [Previous Group command transfer]</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[145, 753, 521, 767]]<|/det|>
Table 4.43: Previous Group command transfer test cases  

<|ref|>text<|/ref|><|det|>[[115, 784, 260, 799]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 807, 814, 824]]<|/det|>
CT: Initiate the required user actions (e.g., press button) toperform Previous Group function.  

<|ref|>text<|/ref|><|det|>[[144, 832, 369, 847]]<|/det|>
TG: No user action is required.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 845, 177]]<|/det|>
- Expected OutcomePass verdictCT: The Next Group command is sent.TG: The TG reacts to Previous Group command sent from the CT to move to the first song in the previous group.  

<|ref|>title<|/ref|><|det|>[[115, 190, 494, 208]]<|/det|>
#### 4.21.7 Continuation PDUs commands  

<|ref|>sub_title<|/ref|><|det|>[[115, 222, 644, 241]]<|/det|>
## AVRCP/CT/RCR/BV-01-C [Request continuing response - CT]  

<|ref|>text<|/ref|><|det|>[[115, 250, 534, 293]]<|/det|>
- Test PurposeVerify that the CT can handle fragmentation correctly.  

<|ref|>text<|/ref|><|det|>[[115, 300, 256, 365]]<|/det|>
- Reference[7] 5.5.1[5], [8] 6.8.1  

<|ref|>text<|/ref|><|det|>[[115, 374, 260, 390]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 400, 648, 440]]<|/det|>
- One ACL connection exists between the IUT and the test system.- AVCTP connection exists between the IUT and the test system.  

<|ref|>text<|/ref|><|det|>[[115, 451, 260, 467]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[142, 475, 835, 510]]<|/det|>
1. The IUT sends a Get Element Attributes command to the Lower Tester, which meets the test condition (see below).  

<|ref|>text<|/ref|><|det|>[[142, 510, 839, 544]]<|/det|>
2. The Lower Tester sends a 512-byte response with UTF-8 characters for the attribute string(s), along with the START indication (0x1) as packet type.  

<|ref|>text<|/ref|><|det|>[[142, 544, 735, 560]]<|/det|>
3. The IUT sends a Request Continuing Response command to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[142, 561, 584, 576]]<|/det|>
4. The Lower Tester sends Get Element Attributes response.  

<|ref|>text<|/ref|><|det|>[[142, 577, 848, 643]]<|/det|>
5. Repeat Steps 3 and 4, as necessary, until the IUT receives all of the remaining characters from the Lower Tester. The final Get Element Attributes response is indicated with 0x3 (END) for packet type. Any additional Get Element Attributes responses between the START (0x1) and END (0x3) should have a packet type of CONTINUE (0x2).=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>image<|/ref|><|det|>[[144, 70, 712, 336]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 345, 685, 360]]<|/det|>
<center>Figure 4.129: AVRCP/CT/RCB/BV-01-C [Request continuing response – CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 375, 253, 390]]<|/det|>
- Test Condition  

<|ref|>text<|/ref|><|det|>[[144, 399, 878, 449]]<|/det|>
The Lower Tester is configured so a GetElementAttributes command response is larger than the 512- byte limit on AV/C frames but the response is smaller than the Maximum number of accepted AV/C fragments valued specified in the IXIT [6].  

<|ref|>text<|/ref|><|det|>[[115, 458, 286, 473]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 483, 238, 497]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 504, 876, 538]]<|/det|>
Request(s) for continuing response packets are sent by the IUT, until the entire GetElementAttributes command response has been received via the control channel.  

<|ref|>text<|/ref|><|det|>[[144, 540, 875, 575]]<|/det|>
In the event that the lower test exceeds the Maximum number of accepted AV/C fragments value, the CT may send AbortContinuingResponse command before receiving the entire response.  

<|ref|>sub_title<|/ref|><|det|>[[115, 596, 646, 615]]<|/det|>
## AVRCP/TG/RCB/BV-02-C [Request continuing response – TG]  

<|ref|>text<|/ref|><|det|>[[115, 624, 546, 664]]<|/det|>
- Test PurposeVerify that the TG can handle fragmentation correctly.  

<|ref|>text<|/ref|><|det|>[[115, 674, 223, 690]]<|/det|>
- Reference  

<|ref|>text<|/ref|><|det|>[[144, 699, 231, 714]]<|/det|>
[7] 5.5.1  

<|ref|>text<|/ref|><|det|>[[144, 722, 233, 738]]<|/det|>
[5], [8] 6.8.1  

<|ref|>text<|/ref|><|det|>[[115, 748, 258, 764]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 774, 647, 813]]<|/det|>
- One ACL connection exists between the IUT and the test system.- AVCTP connection exists between the IUT and the test system.  

<|ref|>text<|/ref|><|det|>[[115, 825, 258, 840]]<|/det|>
- Test Procedure  

<|ref|>text<|/ref|><|det|>[[140, 849, 835, 880]]<|/det|>
1. The Lower Tester sends a Get Element Attributes command to the IUT, which meets the test condition (see below).  

<|ref|>text<|/ref|><|det|>[[140, 882, 848, 916]]<|/det|>
2. The IUT sends a 512-byte response with UTF-8 characters for the attribute string(s), along with the START indication (0x1) as packet type.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[144, 72, 748, 88]]<|/det|>
3. The Lower Tester sends a Request Continuing Response command to the IUT.  

<|ref|>text<|/ref|><|det|>[[144, 90, 700, 105]]<|/det|>
4. The IUT sends a Get Element Attributes response with more characters.  

<|ref|>text<|/ref|><|det|>[[144, 106, 868, 171]]<|/det|>
5. Repeat Steps 3 and 4, as necessary, until the Lower Tester receives all of the remaining characters from the IUT. The final Get Element Attributes response is indicated with 0x3 (END) for packet type. Any additional Get Element Attributes responses between the START (0x1) and END (0x3) should have a packet type of CONTINUE (0x2).  

<|ref|>image<|/ref|><|det|>[[145, 179, 712, 446]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[145, 453, 686, 469]]<|/det|>
<center>Figure 4.130: AVRCP/TG/CRR/BV-02-C [Request continuing response – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 483, 252, 499]]<|/det|>
- Test Condition  

<|ref|>text<|/ref|><|det|>[[140, 506, 875, 539]]<|/det|>
The IUT is configured so a GetElementAttributes command response is larger than the 512-byte limit on AV/C frames.  

<|ref|>text<|/ref|><|det|>[[115, 544, 287, 560]]<|/det|>
- Expected Outcome  

<|ref|>text<|/ref|><|det|>[[145, 567, 240, 582]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 590, 864, 640]]<|/det|>
For each GetElementAttributes command and continuing response packets sent to the IUT, the IUT responds with a GetElementAttributes response containing the proper fragmentation indication via the control channel.  

<|ref|>sub_title<|/ref|><|det|>[[113, 663, 621, 682]]<|/det|>
## AVRCP/CT/CRR/BV-03-C [Abort continuing response – CT]  

<|ref|>text<|/ref|><|det|>[[115, 691, 500, 733]]<|/det|>
- Test PurposeVerify that the CT aborts fragmentation correctly.  

<|ref|>text<|/ref|><|det|>[[115, 741, 240, 805]]<|/det|>
- Reference[7] 5.5.2[5], [8] 6.8.2  

<|ref|>text<|/ref|><|det|>[[115, 815, 260, 830]]<|/det|>
- Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 841, 647, 881]]<|/det|>
- One ACL connection exists between the IUT and the test system.- AVCTP connection exists between the IUT and the test system.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 97, 839, 131]]<|/det|>
1. The IUT sends a Get Element Attributes command to the Lower Tester, which meets the test condition (see below).  

<|ref|>text<|/ref|><|det|>[[144, 131, 840, 165]]<|/det|>
2. The Lower Tester sends a 512-byte response with UTF-8 characters for the attribute string(s), along with the START indication (0x1) as packet type.  

<|ref|>text<|/ref|><|det|>[[144, 165, 802, 199]]<|/det|>
3. The IUT either sends an Abort-Continuing Response command or a RequestContinuing-Response command to the Lower Tester.  

<|ref|>text<|/ref|><|det|>[[144, 199, 860, 249]]<|/det|>
4. Continuation occurs by the Lower Tester until the IXIT entry Maximum number of accepted AV/C fragments value [6] has been reached triggering the AbortContinuingResponse command response from the IUT.  

<|ref|>text<|/ref|><|det|>[[144, 248, 708, 265]]<|/det|>
5. The Lower Tester sends an AbortContinuingResponse command response.  

<|ref|>image<|/ref|><|det|>[[147, 272, 712, 538]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 545, 666, 561]]<|/det|>
<center>Figure 4.131: AVRCP/CT/RCR/BV-03-C [Abort continuing response - CT] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 576, 253, 592]]<|/det|>
Test Condition  

<|ref|>text<|/ref|><|det|>[[144, 600, 857, 650]]<|/det|>
The Lower Tester is configured so a GetElementAttributes command response is larger than the 512 byte limit on AV/C frames. The Lower Tester has sufficient response to satisfy the Maximum number of accepted AV/C fragments condition so the IUT can send the AbortContinuingResponse.  

<|ref|>text<|/ref|><|det|>[[115, 658, 285, 674]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 682, 238, 697]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 705, 881, 739]]<|/det|>
An AbortContinuingResponse command is sent by the IUT after the fragmented GetElementAttributes command response(s) are received.  

<|ref|>sub_title<|/ref|><|det|>[[115, 757, 624, 776]]<|/det|>
## AVRCP/TG/RCR/BV-04-C [Abort continuing response - TG]  

<|ref|>text<|/ref|><|det|>[[115, 785, 575, 826]]<|/det|>
Test PurposeVerify that the TG can accept abort fragmentation correctly.  

<|ref|>text<|/ref|><|det|>[[115, 835, 237, 897]]<|/det|>
Reference [7] 5.5.2 [5], [8] 6.8.2=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 88]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[144, 96, 648, 137]]<|/det|>
- One ACL connection exists between the IUT and the test system.- AVCTP connection exists between the IUT and the test system.  

<|ref|>text<|/ref|><|det|>[[115, 147, 260, 163]]<|/det|>
Test Procedure  

<|ref|>text<|/ref|><|det|>[[144, 171, 835, 205]]<|/det|>
1. The Lower Tester sends a Get Element Attributes command to the IUT, which meets the test condition (see below).  

<|ref|>text<|/ref|><|det|>[[144, 206, 850, 240]]<|/det|>
2. The IUT sends a 512-byte response with UTF-8 characters for the attribute string(s), along with the START indication (0x1) as packet type.  

<|ref|>text<|/ref|><|det|>[[144, 240, 722, 256]]<|/det|>
3. The Lower Tester sends an Abort Continuing Response command to the IUT.  

<|ref|>text<|/ref|><|det|>[[144, 257, 647, 273]]<|/det|>
4. The IUT sends an Abort Continuing Response to the Lower Tester.  

<|ref|>image<|/ref|><|det|>[[145, 280, 714, 547]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[144, 554, 666, 570]]<|/det|>
<center>Figure 4.132: AVRCP/TG/RCR/BV-04-C [Abort continuing response – TG] MSC </center>  

<|ref|>text<|/ref|><|det|>[[115, 585, 253, 600]]<|/det|>
Test Condition  

<|ref|>text<|/ref|><|det|>[[144, 608, 874, 641]]<|/det|>
The IUT is configured so a GetElementAttributes command response will be larger than the 512- byte limit on AV/C frames.  

<|ref|>text<|/ref|><|det|>[[115, 647, 285, 662]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[144, 670, 237, 685]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[144, 692, 857, 727]]<|/det|>
The IUT does not send any fragmented GetElementAttributes responses via the control channel to the Lower Tester, after an AbortContinuingResponse command is received.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 73, 427, 98]]<|/det|>
## 5 Test case mapping  

<|ref|>text<|/ref|><|det|>[[115, 111, 860, 144]]<|/det|>
The Test Case Mapping Table (TCMT) maps test cases to specific requirements in the ICS. The IUT is tested in all roles for which support is declared in the ICS document.  

<|ref|>text<|/ref|><|det|>[[115, 151, 479, 167]]<|/det|>
The columns for the TCMT are defined as follows:  

<|ref|>text<|/ref|><|det|>[[115, 174, 874, 256]]<|/det|>
Item: Contains a logical expression based on specific entries from the associated ICS document. Contains a logical expression (using the operators AND, OR, NOT as needed) based on specific entries from the applicable ICS document(s). The entries are in the form of y/x references, where y corresponds to the table number and x corresponds to the feature number as defined in the ICS document for AVRCP [3].  

<|ref|>text<|/ref|><|det|>[[115, 262, 745, 279]]<|/det|>
If a test case is mandatory within the respective layer, then the y/x reference is omitted.  

<|ref|>text<|/ref|><|det|>[[115, 286, 583, 303]]<|/det|>
Feature: A brief, informal description of the feature being tested.  

<|ref|>text<|/ref|><|det|>[[115, 310, 878, 360]]<|/det|>
Test Case(s): The applicable test case identifiers are required for Bluetooth Qualification if the corresponding y/x references defined in the Item column are supported. Further details about the function of the TCMT are elaborated in [4].  

<|ref|>text<|/ref|><|det|>[[115, 367, 532, 384]]<|/det|>
For the purpose and structure of the ICS/IXIT, refer to [4].  

<|ref|>table<|/ref|><|det|>[[114, 395, 883, 893]]<|/det|>

<table><tr><td>Item</td><td>Feature</td><td>Test Case(s)</td></tr><tr><td>AVRCP 1/1</td><td>Controller Service Discovery</td><td>AVRCP/CT/SGSIT/SERR/BV-01-C<br>AVRCP/CT/SGSIT/ATTR/BV-01-C<br>AVRCP/CT/SGSIT/ATTR/BY-05-C<br>AVRCP/CT/SGSIT/OFFS/BV-01-C<br>AVRCP/CT/SGSIT/OFFS/BV-02-C<br>AVRCP/CT/CGSIT/SFC/BV-01-C</td></tr><tr><td>AVRCP 1/1 AND AVRCP 2b/4</td><td>Controller SDP attribute:<br>BluetoothProfileDescriptorList – AVRCP v1.5</td><td>AVRCP/CT/SGSIT/ATTR/BV-03-C</td></tr><tr><td>AVRCP 1/1 AND AVRCP 2b / 5</td><td>Controller SDP attribute:<br>BluetoothProfileDescriptorList – AVRCP v 1.6</td><td>AVRCP/CT/SGSIT/ATTR/BV-04-C</td></tr><tr><td>AVRCP 2/7 OR AVRCP 2/8 OR AVRCP 2/9 OR AVRCP 2/10</td><td>PASS THROUGH operation supporting press and release</td><td>AVRCP/CT/PTH/BV-01-C</td></tr><tr><td>AVRCP 2/53</td><td>PASS THROUGH operation supporting press and hold</td><td>AVRCP/CT/PTH/BV-02-C</td></tr><tr><td>AVRCP 2/11</td><td>Get Capabilities</td><td>AVRCP/CT/CFG/BV-01-C</td></tr><tr><td>AVRCP 2/12</td><td>List Player Application Setting Attributes</td><td>AVRCP/CT/PAS/BV-01-C</td></tr><tr><td>AVRCP 2/13</td><td>List Player Application Setting Values</td><td>AVRCP/CT/PAS/BV-05-C</td></tr><tr><td>AVRCP 2/14</td><td>Get Current Player Application Setting Value</td><td>AVRCP/CT/PAS/BV-09-C</td></tr><tr><td>AVRCP 2/15</td><td>Set Player Application Setting Value</td><td>AVRCP/CT/PAS/BV-11-C</td></tr><tr><td>AVRCP 2/16</td><td>Get Player Application Setting Attribute Text</td><td>AVRCP/CT/PAS/BV-03-C</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[113, 68, 884, 899]]<|/det|>

<table><tr><td>Item</td><td>Feature</td><td>Test Case(s)</td></tr><tr><td>AVRCP 2/17</td><td>Get Player Application Setting Value Text</td><td>AVRCP/CT/PAS/BV-07-C</td></tr><tr><td>AVRCP 2/20</td><td>Get Element Attributes</td><td>AVRCP/CT/MDI/BV-03-C</td></tr><tr><td>AVRCP 2/21</td><td>Get Play Status</td><td>AVRCP/CT/MDI/BV-01-C</td></tr><tr><td>AVRCP 2/22 OR AVRCP 2/30 OR AVRCP 2/31 OR AVRCP 2/38 OR AVRCP 2/47</td><td>Register Notification</td><td>AVRCP/CT/NFY/BV-01-C</td></tr><tr><td>AVRCP 2/32</td><td>Connection Establishment for Browsing and Release</td><td>AVRCP/CT/CON/BV-01-C<br>AVRCP/CT/CON/BV-03-C<br>AVRCP/CT/SGSIT/ATTR/BV-02-C</td></tr><tr><td>AVRCP 2/28</td><td>Set Addressed Player</td><td>AVRCP/CT/MPS/BV-01-C</td></tr><tr><td>AVRCP 2/33</td><td>Set Browsed Player</td><td>AVRCP/CT/MPS/BV-03-C</td></tr><tr><td>AVRCP 2/29</td><td>Get Folder Items - Media Player List</td><td>AVRCP/CT/MPS/BV-08-C</td></tr><tr><td>AVRCP 2/35</td><td>Get Folder Items - Media Content</td><td>AVRCP/CT/MCN/CB/BV-01-C</td></tr><tr><td>AVRCP 2/34</td><td>Change Path</td><td>AVRCP/CT/MCN/CB/BV-04-C</td></tr><tr><td>AVRCP 2/36</td><td>Get Item Attributes</td><td>AVRCP/CT/MCN/CB/BV-07-C</td></tr><tr><td>AVRCP 2/40</td><td>Search</td><td>AVRCP/CT/MCN/SRC/BV-01-C</td></tr><tr><td>AVRCP 2/41</td><td>Get Folder Items - Search folder</td><td>AVRCP/CT/MCN/SRC/BV-03-C</td></tr><tr><td>AVRCP 2/41 AND AVRCP 2/36</td><td>Get Item Attributes - Search folder</td><td>AVRCP/CT/MCN/SRC/BV-05-C</td></tr><tr><td>AVRCP 2/45 OR AVRCP 2/37 OR AVRCP 2/42</td><td>Play Item</td><td>AVRCP/CT/MCN/NP/BV-01-C</td></tr><tr><td>AVRCP 2/46</td><td>Add To NowPlaying</td><td>AVRCP/CT/MCN/NP/BV-03-C</td></tr><tr><td>AVRCP 2/44</td><td>Get Folder Items - Now Playing folder</td><td>AVRCP/CT/MCN/NP/BV-05-C</td></tr><tr><td>AVRCP 2/44 AND AVRCP 2/36</td><td>Get Item Attributes - Now Playing folder</td><td>AVRCP/CT/MCN/NP/BV-08-C</td></tr><tr><td>AVRCP 2/50</td><td>Set Absolute Volume</td><td>AVRCP/CT/VLH/BV-01-C<br>AVRCP/CT/VLH/BI-03-C<br>AVRCP/CT/VLH/BI-04-C<br>AVRCP/CT/VLH/BV-05-C<br>AVRCP/CT/VLH/BV-06-C<br>AVRCP/CT/VLH/BV-07-C</td></tr><tr><td>AVRCP 2/51</td><td>Notify Volume Change</td><td>AVRCP/CT/VLH/BV-03-C</td></tr><tr><td>AVRCP 2/23</td><td>Request Continuing Response</td><td>AVRCP/CT/RCR/BV-01-C</td></tr><tr><td>AVRCP 2/24</td><td>Abort Continuing Response</td><td>AVRCP/CT/RCR/BV-03-C</td></tr><tr><td>AVRCP 2/29b</td><td>GetTotalNumberOfItems (MediaPlayerList)</td><td>AVRCP/CT/MPS/BV-11-C</td></tr><tr><td>AVRCP 2/35b</td><td>GetTotalNumberOfItems (MediaPlayerVirtual Filesystem)</td><td>AVRCP/CT/MCN/CB/BV-12-C</td></tr><tr><td>AVRCP 2/41b AND AVRCP 2/40</td><td>GetTotalNumberOfItems (Search)</td><td>AVRCP/CT/MCN/SRC/BV-07-C</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[113, 70, 884, 899]]<|/det|>

<table><tr><td>Item</td><td>Feature</td><td>Test Case(s)</td></tr><tr><td>AVRCP 2/44b</td><td>GetTotalNumberOfItems (NowPlayingList)</td><td>AVRCP/CT/MCN/NP/BV-10-C</td></tr><tr><td>AVRCP 2/54 AND AVRCP 2/35</td><td>Use GetFoldertems to request the Cover Art attribute</td><td>AVRCP/CT/CA/BV-01-C</td></tr><tr><td>AVRCP 2/54 AND AVRCP 2/36</td><td>Use GetItemAttributes to request the CoverArt attribute</td><td>AVRCP/CT/CA/BV-03-C</td></tr><tr><td>AVRCP 2/54 AND AVRCP 2/20</td><td>Use GetElementAttributes to request the Cover Art attribute</td><td>AVRCP/CT/CA/BV-05-C</td></tr><tr><td>AVRCP 2/54 AND AVRCP 2/55 AND AVRCP 2/56 AND (AVRCP 2/20 OR AVRCP 2/35 OR AVRCP 2/36)</td><td>Use an imaging property object</td><td>AVRCP/CT/CA/BV-07-C</td></tr><tr><td>AVRCP 2/54 AND AVRCP 2/56 AND (AVRCP 2/20 OR A VRCP 2/35 OR AVRCP 2/36)</td><td>Use GetImage with descriptor thumbnail</td><td>AVRCP/CT/CA/BV-09-C</td></tr><tr><td>AVRCP 2/54 AND AVRCP 2/57 AND (AVRCP 2/20 OR AVRCP 2/35 OR A VRCP 2/36)</td><td>Pull a thumbnail using GetLinkedThumbnail</td><td>AVRCP/CT/CA/BV-11-C</td></tr><tr><td>AVRCP 2/54 AND AVRCP 2/58 AND (AVRCP 2/20 OR AVRCP 2/35 OR A VRC P 2/36)</td><td>Pull a native image</td><td>AVRCP/CT/CA/BV-13-C</td></tr><tr><td>AVRCP 2/54 AND AVRCP 2/38 AND (AVRCP 2/35 OR AVRCP 2/36)</td><td>Retrieve Cover Art SDP record to determine PSM</td><td>AVRCP/CT/CA/BV-15-C</td></tr><tr><td>AVRCP 2/54 AND AVRCP 2/39 AND (AVRCP 2/35 OR AVRCP 2/36)</td><td rowspan="2">UIDs changed during Cover Art</td><td rowspan="2">AVRCP/CT/CA/BV-17-C</td></tr><tr><td>AVRCP 2/54 AND AVRCP 2/40 AND (AVRCP 2/35 OR AVRCP 2/36)</td></tr><tr><td>AVRCP 2/29</td><td>When IUT changes folder on a database unaware player, OBEX is disconnected</td><td>AVRCP/CT/CA/BV-18-C</td></tr><tr><td>AVRCP 2/29</td><td>Listing of Available Media Players</td><td>AVRCP/CT/MPS/BV-04-C</td></tr><tr><td>AVRCP 2/28</td><td>Availability of Media Players</td><td>AVRCP/CT/MPS/BV-05-C<br>AVRCP/CT/MPS/BV-06-C</td></tr><tr><td>AVRCP 2/35</td><td>Browsing of the Current Folder</td><td>AVRCP/CT/MCN/CB/BV-08-C</td></tr><tr><td>AVRCP 2/34</td><td>Browsing Up</td><td>AVRCP/CT/MCN/CB/BV-02-C</td></tr><tr><td>AVRCP 2/34</td><td>Browsing Down</td><td>AVRCP/CT/MCN/CB/BV-03-C</td></tr><tr><td>AVRCP 2/37</td><td>Playing of a track from the Virtual Media Player Filesystem</td><td>AVRCP/CT/MCN/CB/BV-10-C</td></tr><tr><td>AVRCP 2/32</td><td>Awareness of change in Media Database</td><td>AVRCP/CT/MCN/CB/BV-05-C</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[114, 70, 883, 920]]<|/det|>

<table><tr><td>Item</td><td>Feature</td><td>Test Case(s)</td></tr><tr><td>AVRCP 2/35 OR<br>AVRCP 2/36</td><td>Metadata from Virtual Filesystem</td><td>AVRCP/CT/MCN/CB/BV-06-C</td></tr><tr><td>AVRCP 2/35 OR<br>AVRCP 2 /36</td><td>CT can retrieve the Metadata Virtual Filesystem from TG with future SDP version</td><td>AVRCP/CT/MCN/CB/BV-09-C</td></tr><tr><td>AVRCP 2/40</td><td>Search request</td><td>AVRCP/CT/MCN/SRC/BV-08-C</td></tr><tr><td>AVRCP 2/41</td><td>Browsing of the Search results</td><td>AVRCP/CT/MCN/SRC/BV-09-C</td></tr><tr><td>AVRCP 2/42</td><td>Play from Search results</td><td>AVRCP/CT/MCN/SRC/BV-10-C</td></tr><tr><td>AVRCP 2/41 AND<br>AVRCP 2/36</td><td>Metadata from Search results</td><td>AVRCP/CT/MCN/SRC/BV-11-C</td></tr><tr><td>AVRCP 2/45</td><td>Playing of a track from the Now Playing folder</td><td>AVRCP/CT/MCN/NP/BV-11-C</td></tr><tr><td>AVRCP 2/46</td><td>Adding a track to Now Playing list</td><td>AVRCP/CT/MCN/NP/BV-12-C</td></tr><tr><td>AVRCP 2/46 AND<br>AVRCP 2/40</td><td>Adding a Search result track to Now Playing list</td><td>AVRCP/CT/MCN/NP/BV-13-C</td></tr><tr><td>AVRCP 2/47</td><td>Local change of Now Playing list on TG</td><td>AVRCP/CT/MCN/NP/BV-14-C</td></tr><tr><td>AVRCP 2/44 AND<br>AVRCP 2/36</td><td>Metadata from Now PlayingList</td><td>AVRCP/CT/MCN/NP/BV-15-C</td></tr><tr><td>AVRCP 2/44</td><td>Browsing the Now Playing folder</td><td>AVRCP/CT/MCN/NP/BV-16-C</td></tr><tr><td>AVRCP 2/51</td><td>Monitoring the CT Volume on the TG</td><td>AVRCP/CT/VLH/BV-04-C</td></tr><tr><td>AVRCP 2/48</td><td>Playable Folder</td><td>AVRCP/CT/MCN/NP/BV-17-C</td></tr><tr><td>AVRCP 2/25</td><td>Next Group</td><td>AVRCP/CT/BGN/BV-01-C</td></tr><tr><td>AVRCP 2/26</td><td>Previous Group</td><td>AVRCP/CT/BGN/BV-02-C</td></tr><tr><td>AVRCP 2/53</td><td>PASS THROUGH operations supporting press and hold</td><td>AVRCP/CT/PTT/BV-05-C</td></tr><tr><td>AVRCP 2/54 AND<br>AVRCP 2/32</td><td>Retrieval of multiple Cover Art images Retrieval of Cover Art image for the currently playing track</td><td>AVRCP/CT/CA/BV-04-C<br>AVRCP/CT/CA/BV-02-C</td></tr><tr><td>AVRCP 2/54</td><td>Retrieval of Cover Art image for the currently playing track without browsing</td><td>AVRCP/CT/CA/BV-06-C</td></tr><tr><td>AVRCP 2/1</td><td>Initiating connection establishment for control/ Accepting connection establishment for control initiated by CT</td><td>AVRCP/CT/CEC/BV-01-C</td></tr><tr><td>AVRCP 2/2</td><td>Accepting connection establishment for control initiated by TG/Initiating connection establishment for control</td><td>AVRCP/CT/CEC/BV-02-C</td></tr><tr><td>AVRCP 2/3</td><td>Initiating connection release for control/Accepting connection release for control initiated by CT</td><td>AVRCP/CT/CRC/BV-01-C</td></tr><tr><td>AVRCP 2/4</td><td>Accepting connection release for control initiated by TG/Initiating connection release for control</td><td>AVRCP/CT/CRC/BV-02-C</td></tr><tr><td>AVRCP 2/5</td><td>Sending/Receiving UNIT INFO command</td><td>AVRCP/CT/ICC/BV-01-C</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[115, 70, 882, 272]]<|/det|>
<|ref|>table_caption<|/ref|><|det|>[[115, 277, 358, 291]]<|/det|>
Table 5.1: Test case mapping for CT   

<table><tr><td>Item</td><td>Feature</td><td>Test Case(s)</td></tr><tr><td>AVRCP 2/6</td><td>Sending/Receiving SUBUNIT INFO command</td><td>AVRCP/CT/ICC/BV-02-C</td></tr><tr><td>AVRCP 2/7</td><td>Sending/receiving PASS THROUGH command in category 1</td><td>AVRCP/CT/PTT/BV-01-C</td></tr><tr><td>AVRCP 2/8</td><td>Sending/receiving PASS THROUGH command in category 2</td><td>AVRCP/CT/PTT/BV-02-C</td></tr><tr><td>AVRCP 2/9</td><td>Sending/receiving PASS THROUGH command in category 3</td><td>AVRCP/CT/PTT/BV-03-C</td></tr><tr><td>AVRCP 2/10</td><td>Sending/receiving PASS THROUGH command in category 4</td><td>AVRCP/CT/PTT/BV-04-C</td></tr></table>  

<|ref|>table<|/ref|><|det|>[[114, 301, 882, 920]]<|/det|>

<table><tr><td>Item</td><td>Feature</td><td>Test Case(s)</td></tr><tr><td>AV RCP 1/2</td><td>Target Service Discovery</td><td>AVRCP/TG/SGSIT/SERR/BV-01-C<br>AVRCP/TG/SGSIT/ATTR/BV-01-C<br>AVRCP/TG/SGSIT/ATTR/BY-06-C<br>AVRCP/TG/SGSIT/OFFS/BV-03-C<br>AVRCP/TG/SGSIT/OFFS/BV-04-C</td></tr><tr><td>AVRCP 1/2 AND<br>AVRCP 7/1</td><td>Successful Connection with future SDP Record value – AVRCP Target</td><td>AVRCP/TG/CGSIT/SFC/BV-02-C</td></tr><tr><td>AVRCP 1/2 AND<br>AVRCP 6/4</td><td>Controller SDP attribute:<br>BluetoothProfileDescriptorList – AVRCP v1.5</td><td>AVRCP/TG/SGSIT/ATTR/BV-04-C</td></tr><tr><td>AVRCP 1/2 AND<br>avRCP 7/5</td><td>Controller SDP attribute:<br>BluetoothProfileDescriptorList – AVRCP v2.6</td><td>AVRCP/TG/SGSIT/ATTR/BV-05-C</td></tr><tr><td>AVRCP 7/11</td><td>Get Capabilities Response</td><td>AVRCP/TG/CFG/BV-02-C<br>AVRCP/TG/CFG/BI-01-C</td></tr><tr><td>AVRCP 7/12</td><td>List Player Application Settings Attributes Response</td><td>AVRCP/TG/PAS/BV-02-C</td></tr><tr><td>AVRCP 7/13</td><td>List Player Application Setting Values Response</td><td>AVRCP/TG/PAS/BV-06-C<br>AVRCP/TG/PAS/BI-02-C</td></tr><tr><td>AVRCP 7/14</td><td>Get Current Player Application Settings Value Response</td><td>AVRCP/TG/PAS/BV-10-C<br>AVRCP/TG/PAS/BI-04-C</td></tr><tr><td>AVRCP 7/15</td><td>Set Player Application Setting Value Response</td><td>AVRCP/TG/PAS/BI-05-C</td></tr><tr><td>AVRCP 7/16</td><td>Get Player Application Setting Attribute Text Response</td><td>AVRCP/TG/PAS/BV-04-C<br>AVRCP/TG/PAS/BI-01-C</td></tr><tr><td>AVRCP 7/17</td><td>Get Player Application Setting Value Text Response</td><td>AVRCP/TG/PAS/BV-08-C<br>AVRCP/TG/PAS/BI-03-C</td></tr><tr><td>AVRCP 7/20</td><td>Get Element Attributes Response</td><td>AVRCP/TG/MDI/BV-04-C<br>AVRCP/TG/MDI/BV-05-C<br>AVRCP/TG/INV/BI-01-C</td></tr><tr><td>AVRCP 7/21</td><td>Get Play Status Response</td><td>AVRCP/TG/MDI/BV-02-C</td></tr><tr><td>AVRCP 2/20 AND<br>NOT AVRCP 2/32</td><td>Retrieve Metadata when TG supports a future version</td><td>AVRCP/CT/MDI/BV-06-C</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[113, 68, 884, 888]]<|/det|>

<table><tr><td>Item</td><td>Feature</td><td>Test Case(s)</td></tr><tr><td>AVRCP 7/22</td><td>Register Notification Response</td><td>AVRCP/TG/NFY/BI-01-C</td></tr><tr><td>AVRCP 7/22 AND AVRCP 7/20</td><td>Register Notification Response – Media Attributes for Current Media Item</td><td>AVRCP/TG/NFY/BV-02-C</td></tr><tr><td>AVRCP 7/30</td><td>Register Notification event</td><td>AVRCP/TG/NFY/BV-03-C</td></tr><tr><td>AVRCP 7/24</td><td>Track Changed – No Playing Track</td><td>AVRCP/TG/NFY/BV-04-C</td></tr><tr><td>AVRCP 7/24 AND NOT AVRCP 7/54</td><td>Track Changed – Playing or Selected Track</td><td>AVRCP/TG/NFY/BV-05-C AVRCP/TG/NFY/BV-08-C</td></tr><tr><td>AVRCP 7/24 AND AVRCP 7/54</td><td>Playing and Changing Track in NowPlaying</td><td>AVRCP/TG/NFY/BV-06-C AVRCP/TG/NFY/BV-07-C</td></tr><tr><td>AVRCP 7/31</td><td>Request Continuing Response</td><td>AVRCP/TG/RCR/BV-02-C</td></tr><tr><td>AVRCP 7/32</td><td>Abort Continuing Response</td><td>AVRCP/TG/RCR/BV-04-C</td></tr><tr><td>AVRCP 7/1 AND AVRCP 7/42 AND AVRCP 7/42a</td><td>Connection Establishment for Browsing</td><td>AVRCP/TG/CON/BV-02-C</td></tr><tr><td>AVRCP 7/1 AND AVRCP 7/4</td><td>Connection Establishment for Browsing</td><td>AVRCP/TG/CON/BV -05-C</td></tr><tr><td>AVRCP 7/42</td><td>Connection Release for Browsing</td><td>AVRCP/TG/CON/BV-04-C AVRCP/TG/SGSIT/ATTR/BV-02-C</td></tr><tr><td>AVRCP 7/37</td><td>Set Addressed Player</td><td>AVRCP/TG/MPS/BV-02-C AVRCP/TG/MPS/BI-01-C</td></tr><tr><td>AVRCP 7/43</td><td>Set Browsed Player</td><td>AVRCP/TG/MPS/BV-04-C AVRCP/TG/MPS/BI-02-C</td></tr><tr><td>AVRCP 7/40 AND AVRCP 7/41</td><td>Addressed Player Changed Notification</td><td>AVRCP/TG/MPS/BV-05-C</td></tr><tr><td>AVRCP 7/38</td><td>Media Player Item – Player Feature Bitmask</td><td>AVRCP/TG/MPS/BV-06-C</td></tr><tr><td>AVRCP 7/39 AND AVRCP 7/41</td><td>Available Players Changed Notification</td><td>AVRCP/TG/MPS/BV-07-C</td></tr><tr><td>AVRCP 7/38</td><td>Get Folder Items – Media Player List</td><td>AVRCP/TG/MPS/BV-09-C</td></tr><tr><td>AVRCP 7/41</td><td>Default Player</td><td>AVRCP/TG/MPS/BV-10-C</td></tr><tr><td>AVRCP 7/45</td><td>Get Folder Items – Media Content</td><td>AVRCP/TG/MCN/CB/BV-02-C</td></tr><tr><td>AVRCP 7/45 AND AVRCP 7/41</td><td>Get Folder Items – Media Content</td><td>AVRCP/TG/MCN/CB/BI-03-C</td></tr><tr><td>AVRCP 7/44</td><td>Change Path</td><td>AVRCP/TG/MCN/CB/BV-05-C AVRCP/TG/MCN/CB/BI-04-C AVRCP/TG/MCN/CB/BV-06-C</td></tr><tr><td>AVRCP 7/45</td><td>Get Folder Items- TG Get Folder</td><td>AVRCP/TG/MCN/CB/BI-01-C</td></tr><tr><td>AVRCP 7/44</td><td>Items -TG Get Folder Items -TG Get</td><td>AVRCP/TG/MCN/CB/BI-02-C</td></tr><tr><td>AVRCP 7/42</td><td>Item Attributes – Media Content</td><td>AVRCP/TG/MCN/CB/BI-03-C AVRCP/TG/MCN/CB/BV-08-C</td></tr><tr><td>AVRCP 7/46</td><td>Invalid UID counter</td><td>AVRCP/TG/MCN/CB/BI-05-C</td></tr><tr><td>AVRCP 7/42 AND AVRCP 7/48</td><td></td><td></td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[113, 70, 884, 896]]<|/det|>

<table><tr><td>Item</td><td>Feature</td><td>Test Case(s)</td></tr><tr><td>AVRCP 7/42 AND AVRCP 7/48 AND NOT AVRCP 7/49</td><td>Database Unaware Players</td><td>AVRCP/TG/MCN/CB/BV-09-C</td></tr><tr><td>AVRCP 7/41 AND AVRCP 7/43 AND NOT AVRCP 7/43a</td><td>Reject Browsing of a non-addressed Player</td><td>AVRCP/TG/MCN/CB/BI-08-C</td></tr><tr><td>AVRCP 7/42 AND AVRCP 7/49 AND AVRCP 7/48</td><td>Database Aware Players</td><td>AVRCP/TG/MCN/CB/BV-10-C AVRCP/TG/MCN/CB/BV-11-C</td></tr><tr><td>AVRCP 7/51</td><td>Search</td><td>AVRCP/TG/MCN/SRC/BV-02-C</td></tr><tr><td>AVRCP 7/52</td><td>Get Folder Items - Search folder</td><td>AVRCP/TG/MCN/SRC/BV-04-C</td></tr><tr><td>AVRCP 7/52 AND AVRCP 7/46</td><td>Get Item Attributes - Search folder</td><td>AVRCP/TG/MCN/SRC/BV-06-C</td></tr><tr><td>AVRCP 7/56 OR</td><td></td><td></td></tr><tr><td>AVRCP 7/47 OR AVRCP 7/53</td><td>Play Item</td><td>AVRCP/TG/MCN/NP/BV-02-C AVRCP/TG/MCN/NP/BI-01-C</td></tr><tr><td>AVRCP 7/57</td><td>Add To NowPlaying</td><td>AVRCP/TG/MCN/NP/BV-04-C AVRCP/TG/MCN/NP/BI-02-C</td></tr><tr><td>AVRCP 7/55</td><td>Get Folder Items - Now Playing folder</td><td>AVRCP/TG/MCN/NP/BV-06-C</td></tr><tr><td>AVRCP 7/58</td><td>NowPlaying Content Changed Notification</td><td>AVRCP/TG/MCN/NP/BV-07-C</td></tr><tr><td>AVRCP 7/55 AND AVRCP 7/46</td><td>Get Item Attributes - Now Playing folder</td><td>AVRCP/TG/MCN/NP/BV-09-C</td></tr><tr><td>AVRCP 7/61</td><td>Set Absolute Volume</td><td>AVRCP/TG/VLH/BV-02-C AVRCP/TG/VLH/BI-01-C AVRCP/TG/VLH/BI-02-C</td></tr><tr><td>AVRCP 7/62</td><td>Notify Volume Change</td><td>AVRCP/TG/VLH/BV-04-C</td></tr><tr><td>AVRCP 7/64</td><td>General Reject</td><td>AVRCP/TG/INV/BI-02-C</td></tr><tr><td>AVRCP 7/38b</td><td>GetTotalNumberOfItems (MediaPlayerList)</td><td>AVRCP/TG/MPS/BV-12-C</td></tr><tr><td>AVRCP 7/45b</td><td>GetTotalNumberOfItems (MediaPlayerVirtual Filesystem)</td><td>AVRCP/TG/MCN/CB/BV-13-C</td></tr><tr><td>AVRCP 7/52b AND AVRCP 7/43</td><td>GetTotalNumberOfItems (Search)</td><td>AVRCP/TG/MCN/SRC/BV-08-C</td></tr><tr><td>AVRCP 7/55b</td><td>GetTotalNumberOfItems (NowPlaying)</td><td>AVRCP/TG/MCN/NP/BV-11-C</td></tr><tr><td>AVRCP 7/67 AND AVRCP 7/45</td><td>Use GetFolderItems to request the Cover Art attribute</td><td>AVRCP/TG/CA/BV-02-C AVRCP/TG/CA/BI-08-C</td></tr><tr><td>AVRCP 7/67 AND AVRCP 7/46</td><td>Use GetItemAttributes to request the Cover Art attribute</td><td>AVRCP/TG/CA/BV-04-C AVRCP/TG/CA/BI-09-C</td></tr><tr><td>AVRCP 7/67 AND AVRCP 7/20</td><td>Use GetElementAttributes to request the Cover Art attribute</td><td>AVRCP/TG/CA/BV-06-C AVRCP/TG/CA/BI-10-C</td></tr><tr><td>AVRCP 7/67</td><td>Cover Art SDP record</td><td>AVRCP/TG/CA/BV-16-C</td></tr><tr><td>AVRCP 7/67 AND AVRCP 7/145</td><td>Retrieval of Cover Art attribute with no OBEX connection</td><td>AVRCP/TG/CA/BI-01-C</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[114, 70, 884, 920]]<|/det|>

<table><tr><td>Item</td><td>Feature</td><td>Test Case(s)</td></tr><tr><td>AVRCP 7/67 AND<br>AVRCP 7/46</td><td>Retrieval of Cover Art attribute with no OBEX connection using<br>GettlemAttributes</td><td>AVRCP/TG/CA/BI-04-C</td></tr><tr><td>AVRCP 7/67 AND<br>AVRCP 7 /20</td><td>Retrieval of Cover Art attribute with no OBEX connection using<br>GetElementAttributes</td><td>AVRCP/TG/CA/BI-05-C</td></tr><tr><td>AVRCP 7/67 AND<br>AVRCP 74</td><td>Request of Unsupported Image Type</td><td>AVRCP/TG/CA/BI-06-C</td></tr><tr><td>AVRCP 7/20 AND<br>AVRCP 7/67</td><td>Request of Unsupported Image Type without browsing</td><td>AVRCP/TG/CA/BI-07-C</td></tr><tr><td>(AVRCP 7/20 OR<br>AVRCP 7/42) AND<br>AVRCP 7/67</td><td>Use an imaging property object</td><td>AVRCP/TG/CA/BV-08-C</td></tr><tr><td>(AVRCP 7/20 OR<br>AVRCP 74) AND<br>AVRCP 7/67</td><td>Use GetImage with descriptor<br>thumbnail</td><td>AVRCP/TG/CA/BV-10-C</td></tr><tr><td>(AVRCP 7/20 OR<br>AVRCP 72) AND<br>AVRCP 7/67</td><td>Pull a thumbnail using<br>GetLinkedThumbnail</td><td>AVRCP/TG/CA/BV-12-C</td></tr><tr><td>(AVRCP 7/20 OR<br>AVRCP 71) AND<br>AVRCP 7/67</td><td>Pull a native image</td><td>AVRCP/TG/CA/BV-14-C</td></tr><tr><td>AVRCP 7/38</td><td>Listing of Available Media Players</td><td>AVRCP/TG/MPS/BV-01-C</td></tr><tr><td>AVRCP 7/37</td><td>Availability of Media Players</td><td>AVRCP/TG/MPS/BV-08-C<br>AVRCP/TG/MPS/BV-03-C</td></tr><tr><td>AVRCP 7/45</td><td>Browsing of the Current Folder</td><td>AVRCP/TG/MCN/CB/BV-01-C</td></tr><tr><td>AVRCP 7/44</td><td>Browsing Up</td><td>AVRCP/TG/MCN/CB/BV-14-C</td></tr><tr><td>AVRCP 7/44</td><td>Browsing Down</td><td>AVRCP/TG/MCN/CB/BV-15-C</td></tr><tr><td>AVRCP 7/47</td><td>Playing of a track from the Virtual<br>Media Player Filesystem</td><td>AVRCP/TG/MCN/CB/BV-04-C</td></tr><tr><td>AVRCP 7/49</td><td>Awareness of change in Media<br>Database</td><td>AVRCP/TG/MCN/CB/BV-16-C</td></tr><tr><td>AVRCP 7/45 OR<br>AVRCP 7/46</td><td>Metadata from Virtual Filesystem</td><td>AVRCP/TG/MCN/CB/BV-17-C</td></tr><tr><td>AVRCP 7/45 AND<br>AVRCP 7/41 AND<br>AVRCP 7/43a</td><td>Browsing of a Folder if the Player is<br>not the Addressed Player</td><td>AVRCP/TG/MCN/CB/BV-07-C</td></tr><tr><td>AVRCP 7/51</td><td>Search request</td><td>AVRCP/TG/MCN/SRC/BV-01-C</td></tr><tr><td>AVRCP 7/52</td><td>Browsing of the Search results</td><td>AVRCP/TG/MCN/SRC/BV-05-C</td></tr><tr><td>AVRCP 7/53</td><td>Play from Search results</td><td>AVRCP/TG/MCN/SRC/BV-03-C</td></tr><tr><td>AVRCP 7/52 AND<br>AVRCP 7/46</td><td>Metadata from Search results</td><td>AVRCP/TG/MCN/SRC/BV-07-C</td></tr><tr><td>AVRCP 7/56</td><td>Playing of a track from the Now<br>Playing folder</td><td>AVRCP/TG/MCN/NP/BV-01-C</td></tr><tr><td>AVRCP 7/57</td><td>Adding a track to Now Playing list</td><td>AVRCP/TG/MCN/NP/BV-08-C</td></tr><tr><td>AVRCP 7/57 AND<br>AVRCP 7/51</td><td>Adding a Search result track to Now<br>Playing list</td><td>AVRCP/TG/MCN/NP/BV-03-C</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[113, 70, 884, 847]]<|/det|>
<|ref|>table_caption<|/ref|><|det|>[[115, 850, 358, 864]]<|/det|>
Table 5.2: Test case mapping for TG   

<table><tr><td>Item</td><td>Feature</td><td>Test Case(s)</td></tr><tr><td>AVRCP 7/58</td><td>Local change of Now Playing list on TG</td><td>AVRCP/TG/MCN/NP/BV-10-C</td></tr><tr><td>AVRCP 7/55 AND AVRCP 7/46</td><td>Metadata from NowPlayingList</td><td>AVRCP/TG/MCN/NP/BV-05-C</td></tr><tr><td>AVRCP 7/55</td><td>Browsing the Now Playing folder</td><td>AVRCP/TG/MCN/NP/BV-12-C</td></tr><tr><td>AVRCP 7/62</td><td>Monitoring the CT Volume on the TG</td><td>AVRCP/TG/VLH/BV-01-C</td></tr><tr><td>AVRCP 7/61</td><td>Changing the Volume</td><td>AVRCP/TG/VLH/BV-03-C</td></tr><tr><td>AVRCP 7/59</td><td>Playable Folder</td><td>AVRCP/TG/MCN/NP/BV-13-C</td></tr><tr><td>AVRCP 7/34</td><td>Next Group</td><td>AVRCP/TG/BGN/BV-01-C</td></tr><tr><td>AVRCP 7/35</td><td>Previous Group</td><td>AVRCP/TG/BGN/BV-02-C</td></tr><tr><td>AVRCP 7/66</td><td>PASS THROUGH operations supporting press and hold</td><td>AVRCP/TG/PTT/BV-05-C</td></tr><tr><td>AVRCP 7/67 AND AVRCP 7/42</td><td>Retrieval of multiple Cover Art images Retrieval of Cover Art image for the currently playing track</td><td>AVRCP/TG/CA/BV-01-C AVRCP/TG/CA/BV-05-C</td></tr><tr><td>AVRCP 7/67</td><td>Retrieval of Cover Art image for the currently playing track without browsing</td><td>AVRCP/TG/CA/BV-03-C AVRCP/TG/SGSIT/ATTR/BV-03-C</td></tr><tr><td>AVRCP 7/2</td><td>Initiating connection establishment for control/ Accepting connection establishment for control initiated by CT</td><td>AVRCP/TG/CEC/BV-01-C</td></tr><tr><td>AVRCP 7/1</td><td>Accepting connection establishment for control initiated by TG/Initiating connection establishment for control</td><td>AVRCP/TG/CEC/BV-02-C</td></tr><tr><td>AVRCP 7/4</td><td>Initiating connection release for control/Accepting connection release for control initiated by CT</td><td>AVRCP/TG/CRC/BV-01-C</td></tr><tr><td>AVRCP 7/3</td><td>Accepting connection release for control initiated by TG/Initiating connection release for control</td><td>AVRCP/TG/CRC/BV-02-C</td></tr><tr><td>AVRCP 7/5</td><td>Sending/Receiving UNIT INFO command</td><td>AVRCP/TG/ICC/BV-01-C</td></tr><tr><td>AVRCP 7/6</td><td>Sending/Receiving SUBUNIT INFO command</td><td>AVRCP/TG/ICC/BV-02-C</td></tr><tr><td>AVRCP 7/7</td><td>Sending/receiving PASS THROUGH command in category 1</td><td>AVRCP/TG/PTT/BV-01-C</td></tr><tr><td>AVRCP 7/8</td><td>Sending/receiving PASS THROUGH command in category 2</td><td>AVRCP/TG/PTT/BV-02-C</td></tr><tr><td>AVRCP 7/9</td><td>Sending/receiving PASS THROUGH command in category 3</td><td>AVRCP/TG/PTT/BV-03-C</td></tr><tr><td>AVRCP 7/10</td><td>Sending/receiving PASS THROUGH command in category 4</td><td>AVRCP/TG/PTT/BV-04-C</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[114, 72, 663, 98]]<|/det|>
## 6 Appendix A - Operation_id list tables  

<|ref|>title<|/ref|><|det|>[[114, 111, 485, 133]]<|/det|>
#### 6.1 Operation_id of Category 1  

<|ref|>table<|/ref|><|det|>[[113, 130, 882, 880]]<|/det|>

<table><tr><td>operation_id</td><td>Expected operation to be performed by the TG</td></tr><tr><td>0 1 2 3 4 5 6 7</td><td>Input a numerical value.</td></tr><tr><td>8 9 angle</td><td>Input a numerical value.</td></tr><tr><td>backward</td><td>Input a numerical value.</td></tr><tr><td></td><td>Input a numerical value.</td></tr><tr><td></td><td>Input a numerical value.</td><td></td></tr><tr><td></td><td>Input a numerical value.</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>Input a numerical value.</td><td></td></tr><tr><td>Input a numerical value.</td><td></td><td></td></tr><tr><td></td><td>Input a numerical value.</td><td></td></tr></table><br><br><table><tr><td>&lt;fcel&gt;</td><td>&lt;nl&gt;</td></tr><tr><td>&lt;fcel&gt;</td><td>&lt;nl&gt;</td></tr><tr><td></td><td>&lt;nl&gt;</td></tr><tr><td>&lt;fcel&gt;</td><td></td></tr><tr><td>&lt;fcel&gt;</td><td>&lt;nl&gt;</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[115, 70, 880, 150]]<|/det|>

<table><tr><td>operation_id</td><td>Expected operation to be performed by the TG</td></tr><tr><td>stop</td><td>Stops playing back the content.</td></tr><tr><td>subpicture</td><td>Switches or rotates the sub pictures, if it has some sub pictures data.</td></tr></table>

<|ref|>table_caption<|/ref|><|det|>[[115, 157, 388, 170]]<|/det|>
Table 6.1: Operation_id List - Category 1

<|ref|>table_caption<|/ref|><|det|>[[115, 187, 485, 205]]<|/det|>
6.2 Operation_id of Category 2

<|ref|>table<|/ref|><|det|>[[115, 208, 883, 716]]<|/det|>

<table><tr><td>operation_id</td><td>Expected operation to be performed by the TG<br></td></tr><tr><td>0 1 2 3 4 5 6 7 8 9</td><td>Input a numerical value. Input a numerical value. Input a numerical value.</td></tr><tr><td>clear display</td><td>value. Input a numerical value. Input a numerical value. Input a numerical value.</td></tr><tr><td>information</td><td>numerical value. Input a numerical value. Input a numerical value.</td></tr><tr><td></td><td>Input a numerical value. Input a numerical value. Cancel the entered numerical value. Displays the information about current contents. For example, this<br>command may be used to display the channel number, broadcaster and broadcast time, or recorded date and time code. Used with 0-9</td></tr><tr><td></td><td>to input numerical value such as a sub channel in<br>US.</td></tr><tr><td></td><td>Fix the entered numerical value.</td></tr><tr><td></td><td>Displays help instructions.</td></tr><tr><td></td><td>Used to switch the input signal.<br>Puts the sound out, and may resume it alternatively or not.<br>Controls the power state of the device alternatively. This command</td></tr><tr><td>dot</td><td>may support to turn the device off only.<br>Used to switch the sound such as multiple language selection.</td></tr><tr><td>enter</td><td>Turns the volume to low.</td></tr><tr><td>help</td><td>Turns the volume to high.</td></tr><tr><td>input select</td><td></td></tr><tr><td>mute</td><td></td></tr><tr><td>power</td><td></td></tr><tr><td>sound select</td><td></td></tr><tr><td>volume down</td><td></td></tr><tr><td>volume up</td><td></td></tr></table>

<|ref|>table_caption<|/ref|><|det|>[[115, 723, 389, 735]]<|/det|>
Table 6.2: Operation_id List - Category 2

<|ref|>table_caption<|/ref|><|det|>[[115, 752, 485, 769]]<|/det|>
6.3 Operation_id of Category 3

<|ref|>table<|/ref|><|det|>[[115, 772, 880, 920]]<|/det|>

<table><tr><td>operation_id</td><td>Expected operation to be performed by the TG </td></tr><tr><td>0 1 2 3 4 5</td><td>Input a numerical value. Input a numerical value.</td></tr><tr><td></td><td>Input a numerical value.Input a numerical value.</td></tr><tr><td></td><td>Input a numerical value. Input a numerical value</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>

<|ref|>image<|/ref|><|det|>[[115, 945, 148, 976]]<|/det|>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[114, 70, 883, 570]]<|/det|>

<table><tr><td>operation_id</td><td>Expected operation to be performed by the TG</td></tr><tr><td>6 7 8 9 angle</td><td>Input a numerical value. Input a numerical value. Input a numerical value.</td></tr><tr><td>channel down</td><td>value. Input a numerical value. Switches the scene of the contents, if it has multi angle contents. Switches the channel, such as broadcast</td></tr><tr><td></td><td>channel, to lower one,<br>i.e., minus direction in number.</td></tr><tr><td></td><td>Switches the channel, such as broadcast channel, to upper one,<br>i.e., plus direction in number.</td></tr><tr><td>channel up</td><td>Cancel the entered numerical value.<br>Displays the information about current contents. For example, this command may be used to display the channel number, broadcaster and broadcast time, or recorded date and time code.</td></tr><tr><td>clear</td><td></td></tr><tr><td>display information</td><td>Used with 0–9 to input numerical value such as a sub channel in US.</td></tr><tr><td>dot</td><td>Fix the entered numerical value.<br>Displays help instructions.</td></tr><tr><td>enter</td><td>Used to switch the input signal.</td></tr><tr><td>help</td><td>Controls the power state of the device alternatively. This command may support to turn the device off only. Switches to the previously selected channel. For example, in case</td></tr><tr><td>input select</td><td>123 ch was switched to 246 ch, this command can be used as a switcher between 123 ch and 246 ch. Used to switch the sound such as multiple language selection. Switches or rotates the sub pictures, if it has some sub pictures<br>data.</td></tr><tr><td>power</td><td></td></tr><tr><td>previous channel</td><td></td></tr><tr><td>sound select</td><td></td></tr><tr><td>subpicture</td><td></td></tr></table>

<|ref|>table_caption<|/ref|><|det|>[[115, 577, 390, 589]]<|/det|>
Table 6.3: Operation_id List - Category 3

<|ref|>table_caption<|/ref|><|det|>[[114, 606, 486, 625]]<|/det|>
6.4 Operation_id of Category 4

<|ref|>table<|/ref|><|det|>[[115, 628, 883, 920]]<|/det|>

<table><tr><td>operation_id</td><td>Expected operation to be performed by the TG<br></td></tr><tr><td>0 1 2 3 4 5 6 7</td><td>Input a numerical value. Input a numerical value. Input a numerical value.</td></tr></table>

<|ref|>image<|/ref|><|det|>[[115, 945, 148, 976]]<|/det|>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[113, 68, 881, 750]]<|/det|>
<|ref|>table_caption<|/ref|><|det|>[[115, 755, 387, 769]]<|/det|>
Table 6.4: Operation_id List - Category 4   

<table><tr><td>operation_id</td><td>Expected operation to be performed by the TG</td></tr><tr><td></td><td>displayed with this command should be designed to be reached from the initial menu of the target.</td></tr><tr><td>display information</td><td>Displays the information about current contents. For example, this command may be used to display the channel number, broadcaster and broadcast time, or recorded date and time code.</td></tr><tr><td>dot</td><td>Used with 0–9 to input numerical value such as a sub channel in US.</td></tr><tr><td>down</td><td>Moves cursor lower direction.</td></tr><tr><td>enter</td><td>Fix the entered numerical value.</td></tr><tr><td>exit</td><td>Closes current menu and go back previous menu. This command may also be used to finish GUI operation, but a target is implemented to be finished GUI operation without this command.</td></tr><tr><td>favorite menu</td><td>Displays user preset menu. (Can be used as a shortcut.) For example, this command may be used to display the list of user preset channel. The menu displayed with this command should be designed to be reached from the initial menu of the target.</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[115, 72, 857, 98]]<|/det|>
## 7 Appendix B - Supplementary Interoperability Tests  

<|ref|>text<|/ref|><|det|>[[114, 111, 870, 176]]<|/det|>
This section provides a supplementary set of interoperability tests. These tests are aimed at scenarios that do not have a direct specification reference. The tests are recommended by the Bluetooth SIG to be run for improved interoperability, but they are not required to be executed as part of the Bluetooth Qualification program.  

<|ref|>sub_title<|/ref|><|det|>[[114, 190, 682, 211]]<|/det|>
### 7.1 CT Handles Different TG Volume Resolutions  

<|ref|>text<|/ref|><|det|>[[115, 216, 245, 231]]<|/det|>
Test Purpose  

<|ref|>text<|/ref|><|det|>[[142, 239, 863, 288]]<|/det|>
Verify that the CT IUT correctly handles large variations in volume resolution from TG devices and uses the Register Notification command again upon receiving the notification of a change in the TG volume.  

<|ref|>text<|/ref|><|det|>[[115, 298, 223, 313]]<|/det|>
Reference  

<|ref|>text<|/ref|><|det|>[[144, 321, 243, 337]]<|/det|>
[5], [8] 6.13.2  

<|ref|>text<|/ref|><|det|>[[115, 346, 260, 362]]<|/det|>
Initial Condition  

<|ref|>text<|/ref|><|det|>[[142, 374, 876, 481]]<|/det|>
- One ACL connection exists between the IUT and the Lower Tester.- The AVCTP connection between the IUT and the Lower Tester is completed.- The IUT is acting as AVRCP CT role in category 2.- The IUT used the Register Notification command to receive the notification of a change in the TG volume.  

<|ref|>text<|/ref|><|det|>[[115, 491, 324, 507]]<|/det|>
Test Case Configuration  

<|ref|>table<|/ref|><|det|>[[144, 515, 876, 579]]<|/det|>

<table><tr><td>Test Case</td><td>Test Dataset</td></tr><tr><td>AVRCP/CT/VLH/BV-06-C [Volume Control - Low resolution TG]</td><td>Low Resolution</td></tr><tr><td>AVRCP/CT/VLH/BV-07-C [Volume Control - Higher resolution TG]</td><td>Higher Resolution</td></tr></table>  

<|ref|>text<|/ref|><|det|>[[144, 586, 584, 600]]<|/det|>
Table 7.1: CT Handles Different TG Volume Resolutions test cases=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>text<|/ref|><|det|>[[115, 73, 260, 87]]<|/det|>
- Test Procedure  

<|ref|>image<|/ref|><|det|>[[173, 95, 875, 666]]<|/det|>
<|ref|>image_caption<|/ref|><|det|>[[143, 672, 626, 688]]<|/det|>
<center>Figure 7.1: CT Handles Different TG Volume Resolutions test cases MSC </center>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[93, 115, 896, 268]]<|/det|>

<table><tr><td rowspan="2">Round</td><td rowspan="2">Commanded Volume</td><td colspan="4">Low Resolution Test Dataset</td><td colspan="4">Higher Resolution Test Dataset</td></tr><tr><td>TG Volume</td><td>CT Volume 1</td><td>Local Volume</td><td>CT Volume 2</td><td>TG Volume</td><td>CT Volume 1</td><td>Local Volume</td><td>CT Volume 2 </td></tr><tr><td>1</td><td>0% (0x00)</td><td>0% (0x00)</td><td>0%</td><td>20% (0x19)</td><td>10% to 30%</td><td>0% (0x00)</td><td>0%</td><td>5% (0x06)</td><td>0% to 15%</td></tr><tr><td>2</td><td>50% (0x3F)</td><td>40% (0x33)</td><td>30% to 50%</td><td>60% (0x4C)</td><td>50% to 70%</td><td>50% (0x3F)</td><td>40% to 60%</td><td>55% (0x46)</td><td>45% to 65%</td></tr><tr><td>3</td><td>100% (0x7F)</td><td>100% (0x7F)</td><td>100%</td><td>80% (0x66)</td><td>70% to 90%</td><td>100% (0x7F)</td><td>100%</td><td>95% (0x79)</td><td>85% to 100%</td></tr></table>

<|ref|>table_footnote<|/ref|><|det|>[[93, 275, 461, 293]]<|/det|>
Table 7.2: CT Handles Different TG Volume Resolutions test parameters  

<|ref|>text<|/ref|><|det|>[[92, 311, 890, 440]]<|/det|>
1. Repeat Steps 2 through 6 for each round specified in Table 7.2 for the Test Dataset specified in Table 7.1. 
2. The Upper Tester triggers the IUT to send a SetAbsoluteVolume command with the Commanded Volume specified in Table 7.2. 
3. The Lower Tester responds with a SetAbsoluteVolume Response indicating its Absolute Volume is now the TG Volume specified in Table 7.2. 
4. The IUT reports its volume to the Upper Tester. 
5. The Lower Tester sends a volume changed notification to the IUT with the Local Volume specified in Table 7.2 as if a local volume change occurred.  

<|ref|>text<|/ref|><|det|>[[92, 450, 696, 472]]<|/det|>
Step 6 must precede Step 7. Steps 6 and 7 can precede, follow, or occur simultaneously, relative to Step 8:  

<|ref|>text<|/ref|><|det|>[[92, 479, 895, 545]]<|/det|>
6. The IUT uses the Register Notification command to receive the notification of a change in the TG volume. 
7. The Lower Tester sends a Register Notification response within TMTP indicating the INTERIM volume and that volume changes will be notified. 
8. The IUT reports its volume to the Upper Tester.  

<|ref|>text<|/ref|><|det|>[[69, 554, 205, 574]]<|/det|>
Expected Outcome  

<|ref|>text<|/ref|><|det|>[[93, 584, 166, 603]]<|/det|>
Pass verdict  

<|ref|>text<|/ref|><|det|>[[93, 612, 504, 633]]<|/det|>
In Step 4, the IUT's volume matches the CT Volume 1 given in Table 7.2.  

<|ref|>text<|/ref|><|det|>[[92, 642, 740, 664]]<|/det|>
The IUT uses the Register Notification command upon receiving the notification of a local change in the TG volume.  

<|ref|>text<|/ref|><|det|>[[93, 673, 504, 694]]<|/det|>
In Step 7, the IUT's volume matches the CT Volume 2 given in Table 7.2.=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>sub_title<|/ref|><|det|>[[114, 80, 694, 106]]<|/det|>
## 8 Revision history and acknowledgments  

<|ref|>text<|/ref|><|det|>[[115, 109, 248, 125]]<|/det|>
Revision History  

<|ref|>table<|/ref|><|det|>[[113, 141, 884, 895]]<|/det|>

<table><tr><td>Publication Number</td><td>Revision Number</td><td>Date</td><td>Comments</td></tr><tr><td>0</td><td>1.0.0</td><td>2003-02</td><td>Release for Voting Draft</td></tr><tr><td></td><td>1.2.0r0-1</td><td>2006-02-08</td><td>Editorial updates to conform to template and 1.2 or later spec<br>Fixed Abstract text on title page.</td></tr><tr><td>1</td><td>1.2.0</td><td>2006-06-07</td><td>Prepare for publication.</td></tr><tr><td>2</td><td>1.3.0</td><td>2006-10-11</td><td>-Changed document number to be in line with AVRCP specification version number;<br>-Inclusion of Metadata Transfer<br>-Include edits and change tracking;<br>-Merged two figures into one<br>Added missing entries to figure 3.1 and editorial clarifications</td></tr><tr><td>3</td><td>1.3.1</td><td>2007-03-22</td><td>Prepare for publication.</td></tr><tr><td>4</td><td>1.3.2</td><td>2008-04</td><td>TSE 2378: New Test cases AVRCP/TG/BGN/BV-01-1, AVRCP/CT/BGN/BV-01-1, AVRCP/TG/BGN/BV-02-1, AVRCP/CT/BGN/BV-02-1 (legacy test case IDs TP/BGN/BV-01-1, TP/BGN/BV-02-1) for next/previous group</td></tr><tr><td>5</td><td>1.4.0</td><td>2008-06</td><td>Added test cases for advanced control; added IXIT text.</td></tr><tr><td></td><td>1.4.1r0</td><td>2008-07-14</td><td>TSE 2524: AVRCP/CT/CFG/BV-01-C (legacy test case ID TP/CFG/BV-01-C): update Test Condition<br>TSE 2503: new test case AVRCP/CT/RCR/BV-01-C (legacy test case ID TP/RCR/BV-01-C)</td></tr><tr><td></td><td>1.4.1r1-2</td><td>2008-10-31</td><td>Corrected previous table entry; updated new test cases per review comments;<br>TSE 2719: New test case AVRCP/TG/NFY/BV-03-C (legacy test case ID TP/NFY/BV-03-C)</td></tr><tr><td>6</td><td>1.4.1</td><td>2008-12-01</td><td>Prepare for publication</td></tr><tr><td></td><td>1.4.2r0</td><td>2009-08-06</td><td>TSE 2697: new test cases AVRCP/TG/NFY/BV-04-C (legacy test case ID TP/NFY/BV-04-C) (v1.3, v1.4), AVRCP/TG/NFY/BV-05-C (legacy test case ID TP/NFY/BV-05-C) (v1.3), AVRCP/TG/NFY/BV-06-C (legacy test case ID TP/NFY/BV-06-C) (v1.4); updates to TCMT<br>TSE 2703: Rename duplicate test case TP/MCN/CB/BV-02-I to AVRCP/TG/MCN/SCR/BV-02-I and AVRCP/CT/MCN/CB/BV-02-I (legacy test case ID TP/MCN/SCR/BV-02-I)<br>TSE 3087: TCMT correction for AVRCP/TG/RCR/BV-02-C and AVRCP/TG/RCR/BV-04-C (legacy test case IDs TP/RCR/BV-02-C, TP/RCR/BV-04-C)</td></tr><tr><td>7</td><td>1.4.2</td><td>2009-08-06</td><td>Prepare for publication.</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[114, 68, 884, 858]]<|/det|>

<table><tr><td>Publication Number</td><td>Revision Number</td><td>Date</td><td>Comments</td></tr><tr><td></td><td>1.4.2a</td><td>2009-10-08</td><td>Add AVRCP/TG/BGN/BV-01-I, AVRCP/CT/BGN/BV-01-I, AVRCP/TG/BGN/BV-02-I, AVRCP/CT/BGN/BV-02-I (legacy test case IDs TP/BGN/BV-01-I and TP/BGN/BV-02-I) to TCMT</td></tr><tr><td></td><td>1.4.3r0</td><td>2011-01-04</td><td>TSE 2706: New test cases AVRCP/CT/PTH/BV-01-C, AVRCP/CT/PTH/BV-02-C, AVRCP/TG/PTP/BV-05-I, and AVRCP/CT/PTP/BV-05-I (legacy test case IDs TP/PTH/BV-01-C, TP/PTH/BV-02-C, TP/PTP/BV-05-I) TCMT<br>TSE 2738: AVRCP/TG/VLH/BI-01-C (test case ID TP/VLH/BI-01-C) change test condition TSE 2854: AVRCP/CT/MCN/CB/BV-01-C, AVRCP/TG/MCN/CB/BV-02-C, AVRCP/TG/MCN/CB/BI-01-C, AVRCP/CT/MCN/CB/BV-04-C, AVRCP/TG/MCN/CB/BV-05-C, AVRCP/TG/MCN/CB/BI-02-C, AVRCP/TG/MCN/CB/BI-04-C, AVRCP/TG/MCN/CB/BI-05-C, AVRCP/TG/MCN/CB/BV-07-C, AVRCP/TG/MCN/CB/BV-08-C, AVRCP/TG/MCN/CB/BV-09-C, AVRCP/TG/MCN/CB/BV-10-C, AVRCP/TG/MCN/CB/BV-11-C, AVRCP/TG/MCN/CB/BI-03-C, AVRCP/CT/MCN/SRC/BV-01-C, AVRCP/TG/MCN/SRC/BV-02-C, AVRCP/CT/MCN/SRC/BV-03-C, AVRCP/TG/MCN/SRC/BV-04-C, AVRCP/CT/MCN/SRC/BV-05-C, AVRCP/TG/MCN/SRC/BV-06-C, AVRCP/CT/MCN/NP/BV-05-C, AVRCP/TG/MCN/NP/BV-06-C (legacy test case IDs TP/MCN/CB/BV-01-C, TP/MCN/CB/BV-02-C, TP/MCN/CB/BI-01-C, TP/MCN/CB/BV-04-C, TP/MCN/CB/BV-05-C, TP/MCN/CB/BI-02-C, TP/MCN/CB/BI-04-C, TP/MCN/CB/BI-05-C, TP/MCN/CB/BV-06-C, TP/MCN/CB/BV-07-C, TP/MCN/CB/BV-08-C, TP/MCN/CB/BV-09-C, TP/MCN/CB/BV-10-C, TP/MCN/CB/BV-11-C, TP/MCN/CB/BI-03-C, TP/MCN/SRC/BV-01-C, TP/MCN/SRC/BV-02-C, TP/MCN/SRC/BV-03-C, TP/MCN/SRC/BV-04-C, TP/MCN/SRC/BV-05-C, TP/MCN/SRC/BV-06-C, TP/MCN/NP/BV-05-C, TP/MCN/NP/BV-06-C) Initial conditions. TSE 3092 New test case AVRCP/TG/VLH/BI-02-C (legacy test case ID TP/VLH/BI-02-C)<br>TSE 3488: AVRCP/TG/VLH/BI-01-C (legacy test case ID TP/VLH/BI-01-C); move pass verdict text</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[114, 70, 884, 875]]<|/det|>

<table><tr><td>Publication Number</td><td>Revision Number</td><td>Date</td><td>Comments</td></tr><tr><td></td><td></td><td></td><td>TSE 3920: AVRCP/TG/NFY/BV-04-C, AVRCP/TG/NFY/BV-05-C, AVRCP/TG/NFY/BV-06-C (legacy test case IDs TP/NFY/BV-04-C, TP/NFY/BV-05-C, TP/NFY/BV-06-C) Initial condition and test procedures<br>TSE 3041: AVRCP/TG/INV/BI-02-C (legacy test case ID TP/INV/BI-02-C): update TCMT<br>TSE 3105: AVRCP/CT/VLH/BI-03-C (legacy test case ID TP/VLH/BI-03-C): new test case<br>TSE 3106: AVRCP/CT/VLH/BI-04-C (legacy test case ID TP/VLH/BI-04-C): new test case<br>TSE 3244: TCMT: Change to AVRCP/TG/MCN/NP/BV-06-I and AVRCP/CT/MCN/NP/BV-06-I (legacy test case ID TP/MCN/NP/BV-06-I<br>TSE 3836: AVRCP/TG/VLH/BI-01-C (legacy test case ID TP/VLH/BI-01-C): update test condition<br>TSE 3851: AVRCP/TG/NFY/BV-04-C, AVRCP/T/G/NFY/BV-05-C (legacy test case IDs TP/NFY/BV-04, 05-C): Update TCMT</td></tr><tr><td></td><td>1.4.3r1</td><td>2011-01-26</td><td>Reviewer's comments—reorg test cases by number/-V, number -I. See ToC for changes.<br>TSE 2854. Remove AVRCP/TG/MCN/CB/BV-03-C (legacy test case ID TP/MCN/CB/BV-03-C) changes</td></tr><tr><td></td><td>1.4.3r2</td><td>2011-02-09</td><td>More test case reorg</td></tr><tr><td></td><td>1.4.3r3</td><td>2011-03-01</td><td>TSE 4193: AVRCP/TG/MCN/CB/BV-05-C) (legacy test case ID TP/MCN/CB/BV-05-C): Update Reference.<br>TSE 4194: AVRCP/CT/PAS/BV-01-C, AVRCP/TG/PAS/BV-02-C (legacy test case IDs TP/PAS/BV-01-C, TP/PAS/BV-02-C): Update Reference</td></tr><tr><td></td><td>1.4.3r4</td><td>2011-03-02</td><td>References changed<br>TSE 4187: AVRCP/TG/NFY/BV-03-C (legacy test case ID TP/NFY/BV-03-C): Update Reference<br>TSE 4188: AVRCP/CT/PAS/BV-07-C (legacy test case ID TP/PAS/BV-07-C): Update Reference</td></tr><tr><td>8</td><td>1.4.3</td><td>2011-07-21</td><td>Prepare for publication.</td></tr><tr><td></td><td>1.4.4r0-1</td><td>2011-09-13</td><td>TSE 3533: AVRCP/TG/NFY/BV-04-C (legacy test case ID TP/NFY/BV-04-C) Test conditions<br>TSE 4247 Add new test case AVRCP/TG/NFY/BV-07-C (legacy test case ID TP/NFY/BV-07-C)<br>TSE 4417: AVRCP/TG/MCN/CB/BV-09-C (legacy test case ID TP/MCN/CB/BV-09-C): change TCMT<br>TSE 4499: TCMT changes per TSE 2706 for AVRCP/CT/PTH/BV-01-C, AVRCP/CT/PTT/BV-05-I, AVRCP/TG/PTT/BV-05-I (legacy test case IDs TP/PTH/BV-01-C, TP/PTT/BV-05-I)</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[113, 70, 886, 900]]<|/det|>

<table><tr><td>Publication Number</td><td>Revision Number</td><td>Date</td><td>Comments</td></tr><tr><td></td><td></td><td></td><td>AC edits: TSE 4543: Initial condition and TCMT changes for AVRCP/CT/VLH/BI-03-C. AVRCP/CT/VLH/BI-04-C (legacy test case IDs TP/VLH/BI-03-C, TP/VLH/BI-04-C).<br>TSE 4408: Table 0 is removed. Revised TCMT accordingly</td></tr><tr><td>9</td><td>1.4.4r2</td><td>2012-03-12</td><td>TSE 4715: Update TCMT for AVRCP/TG/VLH/BI-02-C (legacy test case ID TP/VLH/BI-02-C)</td></tr><tr><td></td><td>1.5.0r0</td><td>2012-06-21</td><td>Changed references for AVRCP version 1.5. Adjusted section numbering in Sections 2 and 3 to better match with latest TS template.<br>TSE 4726: AVRCP/TG/INV/BI-01-C (legacy test case ID TP/INV/BI-01-C): Change TCMT TSE 4757: AVRCP/TG/MCN/CB/BI-01-C (legacy test case ID TP/MCN/CB/BI-01-C): Relax error code restrictions TSE 4809: AVRCP/TG/CON/BV-02-C (legacy test case ID TP/CON/BV-02-C): Change TCMT</td></tr><tr><td></td><td>1.5.0r1</td><td>2012-06-21</td><td>Updated TCMT entry for the General Reject feature to include the ICS item for AVRCP 1.5.</td></tr><tr><td>10</td><td>1.5.0</td><td>2012-07-24</td><td>Prepare for publication.</td></tr><tr><td></td><td>1.5.1r1</td><td>2012-10-19</td><td>TSE 4964: Edits to TCMT to reflect ESR06: AVRCP/TG/INV/BI-01-C (legacy test case id TP/INV/BI-01-C)<br>AVRCP/TG/NFY/BV-02-C (legacy test case ID TP/NFY/BV-02-C)<br>Added test case names where they were missing for TCMT consistency.<br>TG and CT test cases appearing in the wrong table were moved to the appropriate table (6.1-6.3 in Section 6).<br>Edited AVRCP/TG/INV/BI-02-C (legacy test case ID TP/INV/BI-02-C) Initial Condition. Edited references in Section 2.1 to include both<br>AVRCP v1.4 and 1.5.<br>TSE 4531: New Test - AVRCP/TG/CON/BV-05-C (legacy test case ID TP/CON/BV-05-C) TCMT<br>Changes to the objective for AVRCP/TG/CON/BV-02-C (legacy test case ID TP/COIN/BV-02-C) TCMT</td></tr><tr><td></td><td>1.5.1r2</td><td>2012-10-29</td><td>TSE 4974: Renamed AVRCP/TG/NFY/BV-04-C (legacy test case ID TP/NFY/BV-04-C) [Track Changed - No Playing Track] to No "Selected" Track, updated wording in objective.</td></tr><tr><td></td><td>1.5.1r3</td><td>2012-11-12</td><td>Added changed to TSE 4531, rename of AVRCP/TG/CON/BV-05-C (legacy test case ID TP/COIN/BV-05-C) to [Connection establishment for browsing - TG initiates control channel and CT initiates browsing channel]</td></tr><tr><td>11</td><td>1.5.1</td><td>2012-11-12</td><td>Prepare for Publication</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[114, 70, 884, 810]]<|/det|>

<table><tr><td>Publication Number</td><td>Revision Number</td><td>Date</td><td>Comments</td></tr><tr><td></td><td>1.5.2r1</td><td>2013-04-26</td><td>TSE 5016: New test case, AVRCP/TG/NFY/BV-08-C (legacy test case ID TP/NFY/BV-08-C) [Track Changed - Selected Track - TG]. Added before AVRCP/TG/NFY/BI-01-C (legacy test case ID TP/NFY/BI-01-C). Added new test case to TCMT as Track Changed - Playing Track.TSE 5086: Revisions to the test condition and pass verdict for AVRCP/CT/RCR/BV-01-C and AVRCP/CT/RCR/BV-03-C (legacy test case IDs TP/RCR/BV-01-C and TP/RCR/BV-03-C).</td></tr><tr><td></td><td>1.5.2r2</td><td>2013-05-02</td><td>Updated version and references for ESR06.(Later rejected in r4)</td></tr><tr><td></td><td>1.5.2r3</td><td>2013-05-23</td><td>Removed repeated objective sentence that appeared before the start of section 4.4.3.</td></tr><tr><td></td><td>1.5.2r4</td><td>2013-06-05</td><td>Rejected ESR06 Changes, updated change history and versioning.</td></tr><tr><td>12</td><td>1.5.2r5</td><td>2013-06-13</td><td>BTI Approved</td></tr><tr><td></td><td>1.6.0r0</td><td>2013-06-17</td><td>Integrated Cover Art and Number of Items</td></tr><tr><td></td><td>1.6.0r1</td><td>2013-07-18</td><td>Resolution of Comments</td></tr><tr><td></td><td>1.6.0r2</td><td>2013-08-06</td><td>Split up some test cases for browsing and non-browsing<br>Added new test cases for TG role<br>Adjusted TCMT<br>Resolution of comments</td></tr><tr><td></td><td>1.6.0r3</td><td>2013-08-13</td><td>Fixed OBEX client/server mistakes</td></tr><tr><td></td><td>1.6.0r4</td><td>2013-08-21</td><td>Fixed typos, MSCs and TCMT issues</td></tr><tr><td></td><td>1.6.0r5</td><td>2013-09-16</td><td>Moved to new Test Suite template, formatting and standard boilerplate text. Added missing AVRCP 1.6 references to test cases. Renumbered the BV/BI test case labels for Cover Art to be sequential for easier reference (also updated TCMT accordingly). Updated test feature labeling in Table 4.1. Added Section 5.14 of the AVRCP 1.6 specification as a reference to relevant Cover Art test cases. Updated MSCs for Cover Art test cases for consistent formatting and standard Tester and IUT placement. Updated Cover Art SDP test cases to abstract the process by which the Cover Art PSM is retrieved via SDP query.<br>Removed double-mapping of test cases<br>AVRCP/TG/MCN/NP/BI-01-C and<br>AVRCP/TG/MCN/NP/BI-02-C (legacy test case IDs TP/MCN/NP/BI-01-C and TP/MCN/NP/BI-02-C).</td></tr><tr><td></td><td>1.6.0r6</td><td>2014-04-07</td><td>Addressed BTI review comments</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[113, 69, 884, 814]]<|/det|>

<table><tr><td>Publication Number</td><td>Revision Number</td><td>Date</td><td>Comments</td></tr><tr><td></td><td>1.6.07</td><td>2014-04-15</td><td>TSE 5415: Edits to the test condition and TCMT for AVRCP/TG/MCN/CB/BV-07-I (legacy test case ID TP/MCN/CB/BV-07-I) [Browsing of a folder if the player is not addressed], updated wording to objective and pass verdict. This is now a TG only test case.<br>TSE 5432: Removal of &#x27;(UID 0x0&#x27;) and replaced when needed by &#x27;the currently playing media item&#x27; in AVRCP/CT/MCN/CB/BV-07-C, AVRCP/TG/MCN/CB/BV-08-C, AVRCP/CT/MCN/SRC/BV-05-C, AVRCP, and TG/MCN/SRC/BV-06-C (legacy test case IDs TP/MCN/CB/BV-07-C, TP/MCN/CB/BV-08-C, TP/MCN/SRC/BV-05-C, and TP/MCN/SRC/BV-06-C).<br>TSE 5560: Revises the pass verdict of AVRCP/TG/NFY/BV-08-C (legacy test case ID TP/NFY/BV-08-C) [Track Changed – Selected Track - TG] so that AVRCP 1.3 devices should send a value other than 0xFFFFFFFF.<br>TSE 5598: Corrects an error in the TCMT where AVRCP/TG/MPS/BI-01-C (legacy test case ID TP/MPS/BI-01-C) [SetAddressedPlayer – TG] was overwritten with a duplicate entry for TP/MCN/NP/BI-01-C [PlayItem_Invalid – TG] and AVRCP/TG/MPS/BI-02-C (legacy test case ID TP/MPS/BI-02-C) [SetBrowsedPlayer – TG] was overwritten with a duplicate entry for TP/MCN/NP/BI-O2-C [AddToNowPlaying_Invalid – TG].<br>Adopted by SIG BoD</td></tr><tr><td>13</td><td>1.6.0</td><td>2014-09-18</td><td>TSE 6255: Clarified first paragraph of Pass verdict in AVRCP/TG/VLH/BI-02-C (legacy test case ID TP/VLH/BI-02-C).<br>TSE 6256: Deleted second paragraph of Pass verdict in AVRCP/TG/VLH/BI-02-C (legACY test case ID TP/VLH/BI-02-C).<br>Prepared for TCRL 2015-1 publication</td></tr><tr><td>14</td><td>1.6.1</td><td>2015-07-14</td><td>TSE 6427: Corrected feature descriptions in TCMT for AVRCP/TG/MCN/CB/BI-02-C and AVRCP/TG/MCN/CB/BI-03-C (legacy test case IDs TP/MCN/CB/BI-02-C and TP/MCN/CB/BI-03-C)</td></tr><tr><td></td><td>1.6.2r00</td><td>2015-10-02</td><td>Updated version numbering to align with Specification</td></tr><tr><td></td><td>1.6.1.0r00</td><td>2015-10-28</td><td>version change from 1.6 to 1.6.1 for ESR09. With the specification taking a third identifying number, the TS version identifier moves to the fourth number and starts again at 0.<br>Prepared for TCRL 2015-2 publication</td></tr><tr><td>15</td><td>1.6.1.0</td><td>2015-12-22</td><td></td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[113, 70, 884, 895]]<|/det|>

<table><tr><td>Publication Number</td><td>Revision Number</td><td>Date</td><td>Comments</td></tr><tr><td></td><td>1.6.1.1r00</td><td>2016-02-29</td><td>TSE 6425: Added new section, test case<br>AVRCP/TG/MCN/CB/BI-08-C (legacy test case ID<br>TP/MCN/CB/BI-08-C) and added to TCMT.<br>TSE 6758: Deleted Sections 4.2.9.20-21 and TCMT entries for test cases TP/CA/BI-02-C and TP/CA/BI-03-C.<br>TSE 6924: Updated test purpose and pass verdict of test case AVRCP/CT/VLH/BV-01-I and<br>AVRCP/TG/VLH/BV-01-I (legacy test case ID<br>TP/VLH/BV-01-I).</td></tr><tr><td>16</td><td>1.6.1.1</td><td>2016-07-13</td><td>Prepared for TCRL 2016-1 publication.</td></tr><tr><td></td><td>1.6.1.2r00</td><td>2016-09-28</td><td>Converted to new Test Case ID conventions as<br>defined in TSTO v4.1</td></tr><tr><td></td><td>1.6.1.2r01</td><td>2016-10-10</td><td>TSE 7640: Added test cases AVRCP/CT/MDI/BV-06-I and AVRCP/CT/MCN/CB/BV-09-I to ensure that AVRCP profile version in SDP does not negatively impact User Experience due to poor SDP based decisions</td></tr><tr><td></td><td>1.6.1.2r02</td><td>2016-11-15</td><td>Fixed TC ID styles to show up in ToC. Regenerated ToC.</td></tr><tr><td>17</td><td>1.6.1.2</td><td>2016-12-13</td><td>Approved by BTI: Prepared for TCRL 2016-2 publication.</td></tr><tr><td></td><td>1.6.1.2 (2nd edition)</td><td>2016-12-19</td><td>TSE 8258: Corrected mapping for new test case<br>AVRCP/CT/MCN/CB/BV-09-I. Also fixed formatting issues affecting document generation.<br>Approved by BTI and re-issued for TCRL 2016-2 publication.</td></tr><tr><td></td><td>1.6,1.3r00</td><td>2018-11-05</td><td>Updated template.</td></tr><tr><td></td><td>1.6.2.0r00</td><td>2018-11-09</td><td>Updated version number from 1.6.1.3 to 1.6.2.0 to align with adoption of the specification 1.6.2.</td></tr><tr><td>18</td><td>1.6.2.0</td><td>2018-11-21</td><td>Approved by BTI: Prepared for TCRL 2018-2 publication.</td></tr><tr><td></td><td>1.6.2.1r00 - r02</td><td>2019-04-09 - 2019-06-21</td><td>TSE 11455 (rating 2): Updated steps 9 and 10 and MSC for test case AVRCP/CT/CA/BV-17-C.</td></tr><tr><td>19</td><td>1.6.2.1</td><td>2019-07-28</td><td>Approved by BTI: Prepared for TCRL 2019-1 publication.</td></tr><tr><td></td><td>1.6.2.2r00</td><td>2019-09-27</td><td>TSE 12549 (rating 1): Updated test cases<br>AVRCP/CT/MCN/CB/BV-01-C, -04-C, -07-C;<br>AVRCP/CT/MCN/SRC/BV-01-C,-05-C;<br>AVRCP/CT/MCN/NP/BV-05-C to fix the wording in the initial condition sections.</td></tr><tr><td>20</td><td>1.6.2.2</td><td>2020-01-07</td><td>Approved by BTI on 2019-11-17. Prepared for TCRL 2019-2 publication.</td></tr><tr><td></td><td>1.6.2.2ed2 r00-01</td><td>2021-04-16 - 2021-04-26</td><td>TSE 16800 (rating 1): Fixed formatting problem.<br>Added consistency checker fixes.</td></tr><tr><td></td><td>1.6.2.2 edition 2</td><td>2021-05-21</td><td>Approved by BTI on 2021-05-06. Prepared for edition 2 publication.</td></tr></table>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[114, 70, 883, 708]]<|/det|>

<table><tr><td>Publication Number</td><td>Revision Number</td><td>Date</td><td>Comments</td></tr><tr><td></td><td>p21r00-r06</td><td>2023-11-08 -<br>2024-04-24</td><td>TSE 23963 (rating 1): Converted -I tests to -C tests as appropriate, renumbering where duplicates resulted; updated the TCMT and TCRL accordingly.<br>TSE 24519 (rating 4): Added new GSIT section with new TCs AVRCP/CT/CGSIT/SFC/BV-01-C, AVRCP/CT/SGSIT/ATTR/BV-01-C - -05-C, AVRCP/CT/SGSIT/OFFS/BV-01-C and -02-C, AVRCP/CT/SGSIT/SERR/BV-01-C, AVRCP/TG/CGSIT/SFC/BV-02-C, AVRCP/TG/SGSIT/ATTR/BV-01-C - -06-C, AVRCP/TG/SGSIT/OFFS/BV-03-C and -04-C, and AVRCP/TG/SGSIT/SERR/BV-01-C. Updated the TCMT accordingly. Updated the Scope, added the SDP.TS to the references list, updated the TCID Conventions section, and removed the Conformance tests introduction and the Interoperability tests heading and reset heading levels accordingly.<br>TSE 25005 (rating 1): Updated the Other general information section within the test cases introduction. Updated to align the document with the latest standards.</td></tr><tr><td>21</td><td>p21</td><td>2024-07-01</td><td>Approved by BTI on 2024-05-22. Prepared for TCRL 2024-1 publication.</td></tr><tr><td></td><td>p22r00</td><td>2024-08-13</td><td>TSE 24771 (rating 4): Per E23562, added the following supplemental interoperability tests in a new section (Appendix B): AVRCP/CT/VLH/BV-06-C and -07-C. Updated the TCMT accordingly. Updated the acknowledgments.</td></tr><tr><td>22</td><td>p22</td><td>2024-10-08</td><td>Approved by BTI on 2024-09-11. Audio/Video Remote Control Profile (AVRCP) Specification Versions 1.5.1 and 1.6.3 adopted by the BoD on 2024-10-01. Prepared for TCRL 2024-2-addition publication.</td></tr><tr><td></td><td>p23r00</td><td>2024-10-17</td><td>TSE 25724 (rating 2): Updated the TCMT for AVRCP/TG/CGSIT/SFC/BV-02-C.<br>TSE 26436 (rating 2): Updated the pass verdict for AVRCP/TG/VLH/BI-01-C.</td></tr><tr><td>23</td><td>p23</td><td>2025-02-18</td><td>Approved by BTI on 2024-12-25. Prepared for TCRL 2025-1 publication.</td></tr></table>

<|ref|>title<|/ref|><|det|>[[115, 721, 264, 733]]<|/det|>
# Acknowledgments

<|ref|>table<|/ref|><|det|>[[115, 744, 880, 911]]<|/det|>

<table><tr><td>Name</td><td>Company</td></tr><tr><td>Mat Davidson</td><td>Apple Berner &</td></tr><tr><td>Dominik Sollfrank</td><td>Mattner Bluetooth</td></tr><tr><td>Tharon Hall</td><td>SIG, Inc. Bluetooth</td></tr><tr><td>Meagen Schuler</td><td>SIG, Inc. Broadcom</td></tr><tr><td>Alicia Courtney</td><td>Broadcom CSR</td></tr><tr><td>Ash Kapur</td><td></td></tr><tr><td>Jiny Bradshaw</td><td></td></tr></table>

<|ref|>image<|/ref|><|det|>[[115, 945, 148, 973]]<|/det|>=====================
BASE:  torch.Size([1, 256, 1280])
PATCHES:  torch.Size([6, 100, 1280])
=====================
<|ref|>table<|/ref|><|det|>[[113, 70, 882, 905]]<|/det|>
<table><tr><td>Name</td><td>Company</td></tr><tr><td>Gordon Downie Magnus</td><td>CSR CSR CSR Denso</td></tr><tr><td>Sommansson David</td><td>Ericsson Fujitsu</td></tr><tr><td>Trainor Miyajima Akira</td><td>Impulsesoft Impulsesoft</td></tr><tr><td>Morgan Lindqvist</td><td>Impulsesoft Matsushita</td></tr><tr><td>Masahiko Nakashima</td><td>Matsushita Mecel</td></tr><tr><td>Pragya Gupta Yogesh</td><td>Motorola Mindtree</td></tr><tr><td>Kamar Mhamai</td><td>Mindtree National</td></tr><tr><td>Nagarajan V Ilya</td><td>Analysis Center Nokia</td></tr><tr><td>Goldberg Tsuyoshi</td><td>Open Interface Parrot</td></tr><tr><td>Okada Thomas</td><td>Parrot Philips Philips</td></tr><tr><td>Karlsson Ross Bundy</td><td>Plantronics Siemens</td></tr><tr><td>Shwetha Mahadik Anil</td><td>Sony Sony Sony Sony</td></tr><tr><td>Vutukuru Stephen</td><td>Sony Sony Sony Sony</td></tr><tr><td>Raxter Thomas Block</td><td>Ericsson Sony Ericsson</td></tr><tr><td>Brian Gix François</td><td>Symbian Toshiba</td></tr><tr><td>Ferrand Sébastien</td><td>Toshiba Toshiba Toshiba</td></tr><tr><td>Henrio Christian</td><td>Toshiba UL</td></tr><tr><td>Bouffioux Laurent</td><td></td></tr><tr><td>Meunier Scott Walsh</td><td></td></tr><tr><td>Dimitri Toropov Wilhelm</td><td></td></tr><tr><td>Hagg Masakazu Hattori</td><td></td></tr><tr><td>Atsushi Ichise Harumi</td><td></td></tr><tr><td>Kawamura Yoshiyuki</td><td></td></tr><tr><td>Nezu Hiroyasu Noguchi</td><td></td></tr><tr><td>Masahiko Seki Dick</td><td></td></tr><tr><td>deJong Patric Lind Siân</td><td></td></tr><tr><td>James Makoto</td><td></td></tr><tr><td>Kobayashi Yoshinari</td><td></td></tr><tr><td>Kumaki Shuichi Sakurai</td><td></td></tr><tr><td>Ichiro Tomoda Makoto</td><td></td></tr><tr><td>Yamashita Daniel Ralley</td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr></table>