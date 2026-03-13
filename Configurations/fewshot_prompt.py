FEW_SHOT_PROMPT = """Given the following feature, item and references you have to design testcases for it.
Your test case must have the following sections section title, Test Purpose, Initial Condition, Test Procedure and Expected Outcome.

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

## Example 1 (Bluetooth – TG Role, Simple Command Verification)

Feature and Test Case Name: AVRCP Media Player Selection PlayerFeatureBitmask – TG
Item: Bluetooth
References: AVRCP Specification

### Test Purpose:
Verify the PlayerFeatureBitmask issued by the TG.

### Initial Condition:
- One ACL connection exists between the IUT and the Lower Tester.
- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.
- The IUT is acting as AVRCP TG role in category 1.
- There is an IXIT feature list for each Media Player application on the TG.

### Test Procedure:
The Lower Tester sends a GetFolderItems command to the IUT.

### Expected Outcome:
Pass verdict
The features announced in each Media Player's feature bitmask are according to the Media Player's IXIT entry.

---

## Example 2 (Bluetooth – TG Role, Invalid Parameter Handling)

Feature and Test Case Name: AVRCP Player Application Settings SetAddressedPlayer – TG
Item: Bluetooth
References: AVRCP Specification

### Test Purpose:
Verify the SetAddressedPlayer response issued by the TG when an invalid player is requested.

### Initial Condition:
- One ACL connection exists between the IUT and the Lower Tester.
- The AVCTP control and browsing channels between the IUT and the Lower Tester are established.
- The IUT is acting as AVRCP TG role in category 1.
- The Lower Tester has retrieved the valid PlayerIds of the IUT. This can be retrieved by executing AVRCP/TG/MPS/BV-09-C [GetFolderItems – TG].

### Test Procedure:
The Lower Tester sends a SetAddressedPlayer command to the IUT with an invalid PlayerID.

### Expected Outcome:
Pass verdict
The IUT responds with an 'Invalid Player Id' status response.

---

## Example 3 (Bluetooth – CT Role, Multi-Step Procedure)

Feature and Test Case Name: AVRCP Media Browsing GetTotalNumberOfItems – CT 
Item: Bluetooth
References: AVRCP Specification

### Test Purpose:
Verify the GetTotalNumberOfItems command issued by the IUT (CT) for the Media Player List scope.

### Initial Condition:
- One ACL connection exists between the IUT and the Lower Tester.
- AVCTP control and browsing channels between the IUT and the Lower Tester are established.
- The IUT is acting as AVRCP CT role in category 1.

### Test Procedure:
1. The Upper Tester triggers the IUT to issue a GetTotalNumberOfItems command to the Lower Tester with the scope parameter set to Media Player List.
2. Upon receipt of a GetTotalNumberOfItems command from the IUT, the Lower Tester issues an appropriate GetTotalNumberOfItems response message.

### Expected Outcome:
Pass verdict
The IUT issues a GetTotalNumberOfItems command to the Lower Tester with the scope parameter set to Media Player List.

---

## Example 4 (Bluetooth – CT Role, Invalid Response Behavior)

Feature and Test Case Name: AVRCP Absolute Volume Control SetAbsoluteVolume invalid behavior – CT
Item: Bluetooth
References: AVRCP Specification

### Test Purpose:
Verify the behavior of the CT receiving a SetAbsoluteVolume Response with the top bit (bit 7) set.

### Initial Condition:
- One ACL connection exists between the IUT and the Lower Tester.
- The AVCTP connection between the IUT and the Lower Tester is completed.
- The IUT is acting as AVRCP CT role in category 2.
- The EVENT_VOLUME_CHANGED notification is registered at the IUT.

### Test Procedure:
1. The Upper Tester triggers the IUT to issue a Valid Set Absolute Volume command to the Lower Tester.
2. The Lower Tester issues the response for Set Absolute Volume with the top bit (bit 7) of the absolute volume parameter set.

### Expected Outcome:
Pass verdict
The IUT ignores the top bit (bit 7) and considers only the lower seven bits for the current value for volume.

---

## Example 5 (Mozilla – Browser Session History Verification)

Feature and Test Case Name: Browser Session History Session History Go Menu List Verification
Item: Mozilla
References: Mozilla QA Browser Front-End Test Cases

### Test Purpose:
Verify that links are properly added to the session history and displayed in the browser's Go menu as the user navigates between pages.

### Initial Condition:
- The browser session history must be empty before starting this test. Restart the browser or open a new window to ensure a clean state.
- Confirm the session history is empty by checking that the Go menu lists no sites.

### Test Procedure:
1. Follow the Netscape link (http://home.netscape.com).
2. Follow the Netscape People link (http://people.netscape.com/claudius).
3. Wait for the redirect (approximately 15 seconds).
4. Follow the Mozilla QA link (http://www.mozilla.org/quality).
5. Follow the Mozilla link (http://www.mozilla.org/).
6. Click the browser Back button.

### Expected Outcome:
After step 1: The Go menu lists the title of the first page visited ("Netcenter").
After step 2: The Go menu lists "Netcenter" and "How Claudius Got His Groove Back".
After step 3: The Go menu additionally lists the redirect destination page title.
After step 4: The Go menu additionally lists "Mozilla QA Home Page".
After step 5: The Go menu additionally lists "Mozilla.org".
After step 6: The Go menu order remains the same as after step 5.
In all steps, the currently visited page is checked off in the Go menu list.

---

Now, given the feature, item and references provided below, generate a new test case strictly following the format above.
"""