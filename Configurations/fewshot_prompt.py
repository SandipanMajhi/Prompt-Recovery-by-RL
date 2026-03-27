FEW_SHOT_PROMPT = """Given a Bluetooth feature, test case name, item, and references, design test cases that include the following sections:

1. **Test Purpose**: A clear description of the test case's objective and the feature being tested.
2. **Initial Condition**: The initial state of the system or device before the test is performed.
3. **Test Procedure**: A step-by-step guide on how to perform the test, including any necessary setup, execution, and observation of the test results.
4. **Expected Outcome**: The desired result of the test, including any expected error messages, system responses, or other relevant outcomes.

You must produce your test case in the following format.
### Test Purpose:
<test purpose content>

### Initial Condition:
<initial condition content>

### Test Procedure:
<test procedure content>

### Expected Outcome:
<expected outcome content>

Only output your test case in the above output format with sections mentioned in markdown format and nothing else.
---

Below are examples of well-formed test cases. Study their structure, tone, and level of detail carefully before generating a new one.

---

## Example 1

Feature and Test Case Name: Multi BIG Broadcast Configuration Multi BIG Configuration
Item: Bluetooth
References: BAP Specification
Broadcast Audio Announcements-
To associate a PA, used to expose broadcast Audio Stream parameters, with a broadcast Audio
Stream, the Broadcast Source shall transmit EA PDUs that include the data defined in Table 3.14.
Implementations or higher-layer specifications may define additional service data that follows the
Broadcast_ID parameter to be included in the EA PDUs transmitted by the Broadcast Source.
The AD data format shown in Table 3.14 is defined in Volume 3, Part C, Section 11 in [1].
|Parameter|Col2|Size (Octets)|Description|
|---|---|---|---|
|Length|Length|1|Length of Type and Value fields for AD data type|
|Type: «Service Data - 16-bit UUID»|Type: «Service Data - 16-bit UUID»|1|Defined in Bluetooth Assigned Numbers [2]|
|Value|Value|Varies|2-octet Service UUID followed by the Broadcast_ID and any additional service data|
||Broadcast Audio Announcement Service UUID|2|Defined in Bluetooth Assigned Numbers [2]|
||Broadcast_ID|3|See Section 3.7.2.1.1|

### Test Purpose:
Verify that a Broadcast Source IUT can configure two broadcast Audio Streams over two BIGs that have different Broadcast_ID.

### Initial Condition:
- The IUT is a Broadcast Source and has a BASE set to the TSPX_BASE IXIT entry in [7].
- The IUT can create multiple BIGs.
- The Lower Tester is a Broadcast Sink.

### Test Procedure:
1. The Upper Tester orders the IUT to configure at least two broadcast audio streams in different BIGs using the broadcast Audio Stream Config Settings 16_2 and the Codec Specific Configuration values 16_2_1.
2. The Upper Tester orders the IUT to enter Periodic Advertising mode with configured BASE information in the AdvData field of AUX_SYNC_IND and optionally AUX_CHAIN_IND PDUs for each BIG.
3. The IUT enters Periodic Advertising Synchronizability mode including Service Data AD data type containing the Broadcast Audio Announcement Service UUID and Broadcast_ID in the service data for each BIG.
4. The Lower Tester scans for advertisements with the Broadcast Audio Announcement Service UUID.
For each advertisement train discovered from the IUT:
5. The Lower Tester synchronizes to the PA associated with the broadcast Audio Stream established by the IUT by using the Periodic Advertising Synchronization Establishment procedure.

### Expected Outcome:
Pass verdict
In Step 2, the AdvData field of AUX_SYNC_IND and optionally AUX_CHAIN_IND PDUs contains the configured BASE information.
In Step 3, the IUT transmits the PA synchronization information in the SyncInfo field of the Extended Header field of AUX_ADV_IND PDUs.
- The AUX_ADV_IND PDUs include the Service Data AD Type in the AdvData field with the Service UUID equal to the Broadcast Audio Announcement Service UUID.
- The additional service data includes Broadcast_ID which is different for each BIG.

---

## Example 2

Feature and Test Case Name: Get Folder Items – Media Content GetFolderItems – TG
Item: Bluetooth
References: AVRCP Specification
GetFolderItems-
|Command|Command Parameters|Response Parameters|
|---|---|---|
|GetFolderItems|Scope, Start Item, End Item, Attribute Count, Attribute List|Status, UID Counter, Number of Items, Item List|
This PDU can be used to retrieve a listing of the contents of a folder. The CT may specify a range of entries to be returned. This means that a CT which can only display a limited number of items can obtain a listing one part at a time as the user scrolls the display. If possible, the returned list should resemble the order used on the local display on the TG, but should list all folder items before media element items to facilitate browsing on the CT.
To allow the CT to request specific Metadata Attributes be returned along with each media element in the folder listing, the command shall include a filter specifying which metadata attributes are requested to be returned by the TG. The TG should provide the available attribute values in the response. The TG is not required to provide a value for all requested attributes.
The CT should not issue a GetFolderItems command to an empty folder. If the TG receives a GetFolderItems command for an empty folder, then the TG shall return the error (= Range Out of Bounds) in the status field of the GetFolderItems response.

### Test Purpose:
Verify the GetFolderItems response issued by the TG while the BrowsedPlayer is other than the AddressedPlayer.

### Initial Condition:
- One ACL connection exists between the IUT and the Lower Tester.
- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.
- The IUT is acting as AVRCP TG role in category 1.
- The Lower Tester has retrieved a list of available players. This can be achieved by executing AVRCP/TG/MPS/BV-09-C [GetFolderItems – TG].
- The IUT has at least two media player applications available.

### Test Procedure:
1. The Lower Tester sets the addressed and browsed players on the IUT to valid PlayerID values.
2. The Lower Tester sends a GetFolderItems command to the IUT with the VirtualFilesystem as Scope parameter and valid entries for Start Item, End Item, AttributeCount and AttributeList.

### Expected Outcome:
Pass verdict
The IUT responds with a correctly formatted list of only Folder Items and Media Items of the current folder on PlayerB.

---

Now, given the feature, item and references provided below, generate a new test case strictly following the format above.
"""