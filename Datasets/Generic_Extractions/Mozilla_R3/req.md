# Firefox:Password Manager:UI

From MozillaWiki

Jump to navigation Jump to search

## Contents

  * 1 Goals
  * 2 Existing UI Touchpoints
  * 3 UI Design / Mockups
    * 3.1 Notification Bar
    * 3.2 Password Management
    * 3.3 Other

# Goals

Specific items from the [Firefox3/Product Requirements
Document](/Firefox3/Product_Requirements_Document "Firefox3/Product
Requirements Document"):

  * P1 / PASS-001a -- Only let the user save the password after they know the login has succeeded
  * P2 / PASS-001c -- Improve usefulness of password manager
  * P2 / PASS-001d -- Improve discoverability of autofill UI for multiple accounts on the same site
  * P2 / PASS-001e, f -- Improve "Show passwords" window. EG, searching.
  * P2 / PASS-001g -- Simplify and promote the use of Master Password

  
Other (some overlap):

  * Get rid of popup modal dialogs where possible
  * Opportunities to unify UI
  * Make management and use of multiple logins less confusing

**Out of scope** for this pass:

  * P2 / PASS-003a -- Generate random passwords for user
  * Investigate the possibility of authentication-in-chrome for new content authentications schemes to use (OpenID too?)

# Existing UI Touchpoints

  * Authentication provided by user 
    * Master Password popup 
      * Enable/Disable Master Password pref
      * Change Master Password Dialog
    * HTTP authentication popup
    * Proxy authentication popup
    * Form fields in content
  * Controlling what Firefox remembers 
    * Saving user-provided authentication (except Master Password)
    * Blocking Firefox from certain places ("Never for this site")
    * Deleting existing logins 
      * "Show Passwords" window in prefs
      * Shift-delete in an autocomplete field (only when multiple logins exist)
      * "Show Exceptions" window in prefs
    * Clear Private Data 
      * Saved Passwords
      * Authenticated Sessions

# UI Design / Mockups

(incomplete)

## Notification Bar

  * Replaces modal "Remember Password? Yes/No/Never" with a notification bar (ala popup-blocked notification bar)
  * Replaces "Use Password Mananger to remember this password" checkbox on HTTP auth popup

  * Visual appearance of the notification bar, color, transparency, vertical height?
  * Overlay vs. pushing content down vs. pushing UI up
  * How to dismiss the bar: close button vs. clicking anywhere else (content-only?) vs. forced choice. How to undo?
  * Confirmation of saving/updating the stored password?
  * How to deal with multiple notification bars being requested

## Password Management

  * Allowing filtering list of stored logins
  * Allow editing some fields in-place?
  * Sort list by eTLD
  * The primary column ('hostname') should be JUST the hostname. 
    * ...and port, if non-standard?
    * No 'http[s]://'.
    * ...Leave ftp:// there since it's uncommon (?)
    * ...Create a separate protocol column? And/or a column to indicate secure-only?

## Other

  * Presenting cases where there are multiple logins 
    * For HTTP auth, need a "simple" bugfix to allow using a dropdown in the username field to select from multiple accounts
    * Not sure what more to do with form fields. 
      * Mutate textfield into an editable menubox (so the dropdown widget gives a visual cue)?
      * Autofilling the last-used value (instead of leaving it blank) might help a little bit. Instead of seeing nothing ("firefox is broken") seeing one login might shift you to thinking that it's working, but you somehow can select a different value. OTOH, this is probably just wishful thinking :)
  * Automatic login? We would need to design a second bar that lets users undo the automatic log in

Retrieved from
"[https://wiki.mozilla.org/index.php?title=Firefox:Password_Manager:UI&oldid=61587](https://wiki.mozilla.org/index.php?title=Firefox:Password_Manager:UI&oldid=61587)"

## Navigation menu

###  Personal tools

  * [Log in](/index.php?title=Special:UserLogin&returnto=Firefox%3APassword+Manager%3AUI "You are encouraged to log in; however, it is not mandatory \[o\]")
  * [Request account](/Special:RequestAccount "You are encouraged to create an account and log in; however, it is not mandatory")

###  Namespaces

  * [Page](/Firefox:Password_Manager:UI "View the content page \[c\]")
  * [Discussion](/index.php?title=Talk:Firefox:Password_Manager:UI&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[t\]")

English

###  Views

  * [Read](/Firefox:Password_Manager:UI)
  * [View source](/index.php?title=Firefox:Password_Manager:UI&action=edit "This page is protected.
You can view its source \[e\]")

  * [View history](/index.php?title=Firefox:Password_Manager:UI&action=history "Past revisions of this page \[h\]")

More

###  Search

[](/Main_Page "Visit the main page")

###  Navigation

  * [Main page](/Main_Page "Visit the main page \[z\]")
  * [Product releases](/Releases)
  * [New pages](/Special:NewPages)
  * [Recent changes](/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [Recent uploads](/Special:NewFiles)
  * [Help](/MozillaWiki:Help "The place to find out")

###  How to Contribute

  * [Contribute to Mozilla](/Contribute)
  * [Community Portal](//community.mozilla.org)
  * [Community Participation Guidelines](//www.mozilla.org/en-US/about/governance/policies/participation/)

###  MozillaWiki

  * [About](/MozillaWiki:About)
  * [Team](/MozillaWiki:Team)
  * [Policies](/MozillaWiki:Policies)
  * [Report a wiki bug](//bugzilla.mozilla.org/enter_bug.cgi?product=Websites&component=wiki.mozilla.org)

###  Around Mozilla

  * [Mozilla Support](//support.mozilla.org/)
  * [Give product Feedback](//connect.mozilla.org/)
  * [Mozilla Developer Network](//developer.mozilla.org/)
  * [Planet Mozilla](//planet.mozilla.org/)

###  Tools

  * [What links here](/Special:WhatLinksHere/Firefox:Password_Manager:UI "A list of all wiki pages that link here \[j\]")
  * [Related changes](/Special:RecentChangesLinked/Firefox:Password_Manager:UI "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Firefox:Password_Manager:UI&oldid=61587 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Firefox:Password_Manager:UI&action=info "More information about this page")

  * This page was last edited on 9 July 2007, at 21:38.

  * [Privacy policy](/MozillaWiki:Privacy_policy)
  * [About MozillaWiki](/MozillaWiki:About)
  * [Mobile view](https://wiki.mozilla.org/index.php?title=Firefox:Password_Manager:UI&mobileaction=toggle_view_mobile)

  * [](https://www.mediawiki.org/)




# Firefox3/Product Requirements Document

From MozillaWiki

< [Firefox3](/Firefox3 "Firefox3")

Jump to navigation Jump to search

The Firefox 3 PRD Spreadsheet is still available
[here](http://spreadsheets.google.com/pub?key=p4kVYBRbEKKiemLr9CI-tZw). This
page will also be kept up to date. Please link relevant bugs and design
documents in the "Bugs/Design links" column.

This page is being updated, but the following link is current and allows some
useful data manipulation:

[PRD Data](http://people.mozilla.com/~mconnor/PRD.html)

## Contents

  * 1 Add-ons
    * 1.1 P1
    * 1.2 P2
    * 1.3 P3
  * 2 Content handling
    * 2.1 P1
    * 2.2 P2
    * 2.3 P3
  * 3 Distribution
    * 3.1 P1
    * 3.2 P2
    * 3.3 P3
  * 4 Gecko/Platform
    * 4.1 P1
    * 4.2 P2
    * 4.3 P3
  * 5 User support
    * 5.1 P1
    * 5.2 P2
    * 5.3 P3
  * 6 OS platform integration
    * 6.1 P1
    * 6.2 P2
    * 6.3 P3
  * 7 Password, Identity
    * 7.1 P1
    * 7.2 P2
    * 7.3 P3
  * 8 Places
    * 8.1 P1
    * 8.2 P2
    * 8.3 P3
  * 9 Site-Specific Preferences
    * 9.1 P2
  * 10 Security, Privacy
    * 10.1 P1
    * 10.2 P2
    * 10.3 P3
  * 11 Search
    * 11.1 P2
    * 11.2 P3
  * 12 Visual Refresh
    * 12.1 P1
    * 12.2 P2
    * 12.3 P3
  * 13 Tabbed browsing
    * 13.1 P1
    * 13.2 P2
    * 13.3 P3
  * 14 Installer
    * 14.1 P1
    * 14.2 P2
    * 14.3 P3

# Add-ons

## P1

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
ADD-003e | Complete | Unify add-ons management system and add plugin management system | Michael Wu | [bug 382367](https://bugzilla.mozilla.org/show_bug.cgi?id=382367) for backend changes. [bug 339056](https://bugzilla.mozilla.org/show_bug.cgi?id=339056) for frontend changes. [bug 391730](https://bugzilla.mozilla.org/show_bug.cgi?id=391730) for tracking remaining work.  
ADD-003h | Complete | Support shipping of localized user-facing addon text | Dave Townsend | [bug 257155](https://bugzilla.mozilla.org/show_bug.cgi?id=257155) [Implementation Spec](/User:Mossop:Fx-Docs:LocalizedAddonText "User:Mossop:Fx-Docs:LocalizedAddonText")  
  
## P2

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
ADD-001a | Complete | Add-ons can be installed in fewer mouse clicks | Dave Townsend | [bug 252830](https://bugzilla.mozilla.org/show_bug.cgi?id=252830) removed whitelist steps AMO is integrated into the Manager, but that was not part of the original req.  
ADD-001b |  | Ensure user understands the risks about installing extensions | Mike Connor |   
ADD-001c | Complete | Clarify XPi install dialogs and user interactions | Mike Connor | [Mockups](/Firefox:Add-ons_Manager_UI#Scary_Confirmation "Firefox:Add-ons Manager UI")  
ADD-01d | Complete | Remove extension installation whitelist | Dave Townsend | [bug 252830](https://bugzilla.mozilla.org/show_bug.cgi?id=252830) note: the (xpinstall) whitelist is for both plugins and extensions  
ADD-002a | Complete | Allow Add-on configuration UI to be accessed from main application configuration UI | Robert Strong | [bug 384956](https://bugzilla.mozilla.org/show_bug.cgi?id=384956) (same as ADD-002b)  
ADD-002b | Complete | Improve discoverability of Add-on configuration UI | Robert Strong | [bug 384956](https://bugzilla.mozilla.org/show_bug.cgi?id=384956) (same as ADD-002a)  
ADD-003a | Complete | Add visual indication to browser UI when Add-on updates are available | Dave Townsend | Fx3 fix implemented in [bug 394645](https://bugzilla.mozilla.org/show_bug.cgi?id=394645), will re-evaluate whether this is enough for Fx4  
ADD-003b | Complete | Add permanent button for restarting Firefox | Dão Gottwald | [bug 369075](https://bugzilla.mozilla.org/show_bug.cgi?id=369075). The button now appears in a notification only when needed.  
ADD-003d |  | Simplify language and unify terminology related to Add-ons | Robert Strong |   
ADD-003g | Complete | Support displaying information about the update in the updater | Dave Townsend | [bug 297903](https://bugzilla.mozilla.org/show_bug.cgi?id=297903) Would be more useful with [bug 102699](https://bugzilla.mozilla.org/show_bug.cgi?id=102699)  
ADD-003j | cut | Support add-on conflict resolution | Dave Townsend | [bug 382312](https://bugzilla.mozilla.org/show_bug.cgi?id=382312) [Proposed Implementation](/User:Mossop:Fx-Docs:AddonConflictResolution "User:Mossop:Fx-Docs:AddonConflictResolution") \- needs review by submitter (shaver?)  
ADD-005b |  | Promote the existence of Add-ons that could help the user accomplish their current task |  | Same as ADD-005d  
ADD-005c |  | Help documents should link to related Add-on categories on addons.mozilla.org |  |   
ADD-006a | Complete | Ship the [FUEL JavaScript library](/FUEL "FUEL") | John Resig & Mark Finkle | [bug 380168](https://bugzilla.mozilla.org/show_bug.cgi?id=380168)  
  
## P3

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
ADD-001e | At risk | Install Add-on without requiring a browser restart |  | Requires backend changes to do this reasonably  
ADD-003c | At risk | Simplify task flow for updating single addons |  | ??? This was add button for single extension update check  
ADD-003f | At risk | Allow addons to control other types of extensions and ensuring that model is extensible |  | ??? Needs definition from submitter  
ADD-003i | At risk | Support for use of some kind of service for extension dependency resolution |  | [Previous spec](/Extension_Manager:Extension_Dependencies "Extension Manager:Extension Dependencies")  
ADD-004a | Complete | Making signing a requirement or higher value in install experience |  |   
ADD-004b | At risk | Providing a lower priv model for certain classes of extension |  | Requires backend changes  
ADD-005a | At risk | Improve quality of results from Plugin Finders |  | Same as CON-002b - AMO and Plugin Finder Service  
ADD-005d | At risk | Small "Add-on" button on managers, dialogs, etc. which links directly to related Add-on categories in AMO |  | [bug 384125](https://bugzilla.mozilla.org/show_bug.cgi?id=384125)  
  
# Content handling

## P1

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
CON-001a | Complete | Support web services as protocol handlers | Dan Mosedale, Myk Melez, Shawn Wilsher | [bug 380415](https://bugzilla.mozilla.org/show_bug.cgi?id=380415) and dependents [Feature Requirements](/User:Dmose:Fx-Docs:ContentTypeProcessing "User:Dmose:Fx-Docs:ContentTypeProcessing")  
CON-002a | Needs def | Should be able to play all popular media formats when plugins/codecs are installed |  |   
CON-002b | Needs def | It should be easy to locate and install missing plugins |  |   
CON-002d | Needs def | Support all media types on all platforms as best we can |  |   
CON-003a | In Progress | Simplify content handling UI | Dan Mosedale | [bug 377782](https://bugzilla.mozilla.org/show_bug.cgi?id=377782), [Feature Requirements](/User:Dmose:Fx-Docs:ContentTypeProcessing "User:Dmose:Fx-Docs:ContentTypeProcessing")  
CON-003b | Complete | Create an easy-to-use MIME type handling configuration system | Myk Melez | [bug 377782](https://bugzilla.mozilla.org/show_bug.cgi?id=377782), [Feature Requirements](/User:Dmose:Fx-Docs:ContentTypeProcessing "User:Dmose:Fx-Docs:ContentTypeProcessing")  
  
## P2

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
CON-001b |  | Minimize/remove local MIME type database for local applications | Dan Mosedale | [bug 372853](https://bugzilla.mozilla.org/show_bug.cgi?id=372853)  
CON-002c | `needs spec` cut | Identify ways to mitigate plugin crashes | Johnny? |   
CON-004a | Complete | Revised downloads manager | Shawn Wilsher | [bug 377792](https://bugzilla.mozilla.org/show_bug.cgi?id=377792), [Feature Requirements](/User:Dmose:Fx-Docs:DownloadManager "User:Dmose:Fx-Docs:DownloadManager")  
CON-005b | Complete | Easier retrieval of files that a user has downloaded in the past | Shawn Wilsher | [bug 377793](https://bugzilla.mozilla.org/show_bug.cgi?id=377793)  
CON-006a | Complete | Integrate download manager with third-party virus scanners and malware protection | Rob Arnold | [bug 103487](https://bugzilla.mozilla.org/show_bug.cgi?id=103487)  
CON-007a | Complete | Support pause/resume for downloads. Improve download handling across multiple sessions | Michael Wu | [bug 377243](https://bugzilla.mozilla.org/show_bug.cgi?id=377243), [bug 230870](https://bugzilla.mozilla.org/show_bug.cgi?id=230870)  
CON-008a |  | Create document-parsing framework for detecting microformats | Michael Kaply | [Feature Requirements](/User:Mkaply:Fx-Docs:Microformats "User:Mkaply:Fx-Docs:Microformats")  
CON-008b |  | Create API for developers to leverage the microformat detection framework | Michael Kaply | [Feature Requirements](/User:Mkaply:Fx-Docs:Microformats "User:Mkaply:Fx-Docs:Microformats")  
CON-011a |  | Include Firebug as part of some distribution of Firefox | Mike Connor | [Tracking Page](/Firebug "Firebug")  
  
## P3

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
CON-001c | At risk | Properly handle streaming content types - embedded or handed off to a helper app |  |   
CON-003c | At risk | Ability to show or sniff content on demand and view in plaintext or HTML or other format instead |  |   
CON-005c | At risk | Simplified (not window) UI for managing downloads |  |   
CON-007b | At risk | Download manager can be extended in a way that feels tightly integrated |  |   
CON-009a |  | Display microformats in content area | Michael Kaply | [Feature Requirements](/User:Mkaply:Fx-Docs:Microformats "User:Mkaply:Fx-Docs:Microformats")  
CON-009b |  | Allow user to configure microformat handlers | Michael Kaply | [Feature Requirements](/User:Mkaply:Fx-Docs:Microformats "User:Mkaply:Fx-Docs:Microformats")  
CON-009c |  | Support hCard, hCal, and geo | Michael Kaply | [Feature Requirements](/User:Mkaply:Fx-Docs:Microformats "User:Mkaply:Fx-Docs:Microformats")  
CON-009e |  | Allow web developers to override microformat display attributes | Michael Kaply | [Feature Requirements](/User:Mkaply:Fx-Docs:Microformats "User:Mkaply:Fx-Docs:Microformats")  
CON-010a | At risk | Simplify the print preview dialog |  |   
  
# [Distribution](/Firefox3/Distro_Requirements "Firefox3/Distro Requirements")

## P1

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
DIST-001a | On Track | Settings from distros will need to be persisted across minor (and ideally for major) updates made to Firefox via Automatic Update Service (AUS) | Dan Mills | [Functional Reqs](/Firefox3/Distro_Requirements "Firefox3/Distro Requirements")  
DIST-001b | On Track | Branding will not be easily removable by end users except through a full uninstall of the branded Firefox | Dan Mills |   
DIST-001c | On Track | Security and stability releases/upgrades to Firefox will be smoothly delivered without requiring customized partner builds to be generated | Dan Mills |   
DIST-001d | On Track | When end users use a distro, settings from the distro will need to be persisted when a new OS user invokes Firefox for the first time and/or when a new Firefox user profile is created | Dan Mills |   
DIST-001e | On Track | All customizations of text must include full support of Unicode (UTF-8) | Dan Mills |   
DIST-001f | On Track | Support an indicator that a particular build is a partner build rather than a vanilla Mozilla distribution from inside Firefox (about box) | Dan Mills |   
DIST-002a | On Track | Ability to customize vanilla Firefox with a group of settings | Dan Mills |   
DIST-002b | On Track | Support for creating distributions that support Windows (.exe) | Dan Mills |   
DIST-002d | On Track | Support for creating distributions of any existing Firefox locale build | Dan Mills |   
DIST-003a | On Track | Support of low-touch customization features through low-touch interface (web UI, customization tool, etc...) | Dan Mills | [P1 Customization Checklist](/Firefox3/Distro_Requirements#Customization_Checklist "Firefox3/Distro Requirements")  
  
## P2

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
DIST-002c |  | Support for creating distributions that support Mac (.DMG) and Linux (.tar) | Dan Mills |   
DIST-003b |  | Support for high-touch customization features through tools | Dan Mills |   
DIST-004a |  | Ability to create a “master switch” that can disable a distro | Dan Mills |   
DIST-004b |  | Ability to repatriate a distro to vanilla settings remotely by Mozilla or partner (e.g. in the case of default by partner) | Dan Mills |   
DIST-004c |  | Support of low-touch customization features | Dan Mills | [P2 Customization Checklist](/Firefox3/Distro_Requirements#Customization_Checklist "Firefox3/Distro Requirements")  
  
## P3

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
DIST-001g |  | Support attributes on Firefox setup installer in order to distinguish various partner builds from vanilla builds | Dan Mills |   
DIST-001h |  | Support of low-touch customization features | Dan Mills | [P3 Customization Checklist](/Firefox3/Distro_Requirements#Customization_Checklist "Firefox3/Distro Requirements")  
  
# Gecko/Platform

## P1

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
GKO-004a | Complete | Pass ACID 2 test | David Baron | Fixed by reflow branch, see GKO-009b  
GKO-007a | on track, some ui patches are already there, targeted for M11 | Add UI elements for enabling offline app usage | Dave Camp | [bug 394392](https://bugzilla.mozilla.org/show_bug.cgi?id=394392)  
GKO-007b | On track for M11  
/mw22 - need to ask | Add backend elements for offline app support | Dave Camp | [bug 367447](https://bugzilla.mozilla.org/show_bug.cgi?id=367447)  
GKO-008a | Complete | Cairo graphics | Vlad Vukicevic | [bug 322938](https://bugzilla.mozilla.org/show_bug.cgi?id=322938)  
GKO-008b | Complete | Cocoa widgets on Mac | Josh Aas |   
GKO-008c | Only chrome->chrome frame trees are linked for Gecko1.9, see comment 67 and further in the mentioned bug | Linking Content/Chrome Frame Trees | Robert O'Callahan | [bug 130078](https://bugzilla.mozilla.org/show_bug.cgi?id=130078)  
GKO-008g | Complete | nxTextFrame migration to Thebes | Robert O'Callahan | [bug 367177](https://bugzilla.mozilla.org/show_bug.cgi?id=367177)  
GKO-008h | Complete | Frame Display Lists | Robert O'Callahan | [bug 317375](https://bugzilla.mozilla.org/show_bug.cgi?id=317375)  
GKO-009b | Complete | Reflow branch | David Baron | [bug 300030](https://bugzilla.mozilla.org/show_bug.cgi?id=300030)  
GKO-009c | Complete | Caret painting rewrite | Blake Kaplan | [bug 287813](https://bugzilla.mozilla.org/show_bug.cgi?id=287813)  
GKO-015a | Complete | Cross-domain XMLHttpRequest | Jonas Sicking | [bug 389508](https://bugzilla.mozilla.org/show_bug.cgi?id=389508)  
GKO-016b | Complete | Killing nested event queues, threadmanager | darinf | [bug 326273](https://bugzilla.mozilla.org/show_bug.cgi?id=326273)  
GKO-016c | Complete | Graydon's Cycle Collector | Graydon/Peterv | [bug 333078](https://bugzilla.mozilla.org/show_bug.cgi?id=333078)  
  
## P2

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
GKO-002a |  | Change "Do you want to resend the request?" dialog to an error page | Mike Beltzner |   
GKO-005a |  | Save web pages as PDF documents | Stuart Parmenter | [bug 162659](https://bugzilla.mozilla.org/show_bug.cgi?id=162659)  
GKO-006a |  | Native form controls and HTML content for Mac OS | Josh Aas |   
GKO-008d |  | Hoist plugins to toplevel children | Robert O'Callahan | [bug 339548](https://bugzilla.mozilla.org/show_bug.cgi?id=339548)  
GKO-008e |  | Widget removal | Robert O'Callahan | [bug 352093](https://bugzilla.mozilla.org/show_bug.cgi?id=352093)  
GKO-008f |  | View Removal | Robert O'Callahan |   
GKO-009a | Complete | Fix units in Gecko | Eli Friedman |   
GKO-016e |  | Cache item pinning for offline support | Dave Camp | [bug 396222](https://bugzilla.mozilla.org/show_bug.cgi?id=396222)?  
GKO-018 |  | Support for Quartz Netscape Plugin API (NPAPI) |  |   
GKO-019 | Complete | Support for ContentEditable | Peterv | [bug 237964](https://bugzilla.mozilla.org/show_bug.cgi?id=237964)  
  
## P3

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
GKO-001a |  | Printed pages should break without breaking lines |  |   
GKO-009d |  | Residual style handling | Blake Kaplan |   
GKO-010a |  | XUL Transform support | Vlad Vukicevic |   
GKO-014a | At risk | SVG as image format |  |   
GKO-016d | At risk | XPCOM restart in-process | Benjamin Smedberg |   
GKO-016f | At risk | Offline web browsing | Dave Camp, Robert O'Callahan |   
GKO-017a | Help Wanted | ATK support rearchitecture | Stan Shebs? |   
GKO-017b | Help Wanted | Mac OS X accessibility support | Aaron Leventhal? |   
  
# User support

## P1

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
HELP-002b | In Progress | Make it easier for users to solve their problems and engage with our support community | JT Batson |   
HELP-003a | In Progress | Make it easier to get rapid feedback on problems being encountered by users | JT Batson |   
  
## P2

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
  
## P3

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
HELP-006a |  | Showcase breadth of customization updates |  |   
HELP-001a | Need def | Improve the user support environment from beginning to end |  |   
HELP-002a | At risk | Support reporting multiple types of problems |  |   
HELP-002c | At risk | Recommend relevant documentation/information to user when a problem is submitted |  |   
HELP-003b |  | Provide some sort of feedback/information/status to people who have reported issues |  |   
HELP-004a |  | Better integration with online, real-time support resources |  |   
HELP-005a | At risk | Context sensitive help: Topics should be immediately relevant to users |  |   
  
# OS platform integration

## P1

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
OSPI-002a | In Progress | Collect crash stack data and report it to central server | Ted Mielczarek | [Socorro design](/Breakpad:Current_Implementation#Server_Side "Breakpad:Current Implementation")  
OSPI-002b | In Progress | Improve usability of crash report UI | Ted Mielczarek, Dave Camp | [bug 358082](https://bugzilla.mozilla.org/show_bug.cgi?id=358082), [bug 380540](https://bugzilla.mozilla.org/show_bug.cgi?id=380540)  
OSPI-004a | Complete | Integrate with Windows Vista parental controls | Jim Mathies | [bug 355554](https://bugzilla.mozilla.org/show_bug.cgi?id=355554)  
  
## P2

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
OSPI-001b | Complete | Version detection for Windows - Vista vs XP since we may want to have a different theme for each. Installation configuration piece | Mike Beltzner | Will not use CSS selectors  
OSPI-005a | Complete | Growl alert notifications for Mac OS X | Shawn Wilsher | [Bug 362685](https://bugzilla.mozilla.org/show_bug.cgi?id=362685)  
OSPI-006a | Complete | Handle OS Shutdown sanely on Windows/Linux (dataloss/odd UI) | Michael Wu | [Bug 333907](https://bugzilla.mozilla.org/show_bug.cgi?id=333907)  
OSPI-008a | In progress | Support IAccessible2 on Windows | Aaron Leventhal, Alexander Surkov | [Bug 368873](https://bugzilla.mozilla.org/show_bug.cgi?id=368873)  
OSPI-001a | cut | Build system should create a MSI/MSP bundle (Windows only) | Jim Mathies | [Bug 231062](https://bugzilla.mozilla.org/show_bug.cgi?id=231062)  
  
## P3

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
OSPI-003a | cut | Allow IT administrators to create group profile policies via the Windows Group Policy Object (GPO) |  | [Bug 267888](https://bugzilla.mozilla.org/show_bug.cgi?id=267888)  
OSPI-007a | In Progress | Support ATK (accessibility API) on Linux | Aaron Leventhal, Ginn Chen | [Bug 368881](https://bugzilla.mozilla.org/show_bug.cgi?id=368881)  
  
# Password, Identity

## P1

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
PASS-001a | Complete | Only ask the user to save the password after they know the login has succeeded | Justin Dolske | [bug 226735](https://bugzilla.mozilla.org/show_bug.cgi?id=226735)  
PASS-001b | Complete | Store more precise URIs for autofilling user IDs and passwords | Mike Connor | [bug 360493](https://bugzilla.mozilla.org/show_bug.cgi?id=360493)  
  
## P2

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
PASS-001c |  | Improve usefulness of password manager | Justin Dolske |   
PASS-001d |  | Improve discoverability of autofill UI for multiple accounts on the same site | Justin Dolske | [bug 376668](https://bugzilla.mozilla.org/show_bug.cgi?id=376668)  
PASS-001e |  | Improve the way password lists are sorted and add the ability to search or filter | Justin Dolske | [bug 376682](https://bugzilla.mozilla.org/show_bug.cgi?id=376682)  
PASS-001f |  | Improve usability of password manager list | Justin Dolske | [bug 376682](https://bugzilla.mozilla.org/show_bug.cgi?id=376682)  
PASS-001g | cut | Simplify and promote the use of Master Password | Justin Dolske |   
PASS-003a | cut | Generate hashed passwords for increased security (ref: pwdhash) | Justin Dolske, Robert Sayre | [bug 376674](https://bugzilla.mozilla.org/show_bug.cgi?id=376674)  
PASS-003c | cut | OS-level secure password storage integration | Justin Dolske | [bug 106400](https://bugzilla.mozilla.org/show_bug.cgi?id=106400)  
  
## P3

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
PASS-002a | At risk | Support Microsoft CardSpace on Windows | Justin Dolske |   
PASS-002b | At risk | Support OpenID | Justin Dolske |   
PASS-002c | At risk | Provide a simple identity management UI |  |   
PASS-003b | At risk | Out-of-band login support | Robert Sayre |   
  
# Places

## P1

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
PLCS-001a | Complete: code changes landed, community/extension outreach ongoing | Provide platform support to enable syncing of Places data-model objects to a remote server | Places Team | [bug 374518](https://bugzilla.mozilla.org/show_bug.cgi?id=374518)  
PLCS-001c | Complete | Provide platform support to support generic annotations | Places Team | [bug 374943](https://bugzilla.mozilla.org/show_bug.cgi?id=374943)  
PLCS-001d | Complete: code changes landed, outreach ongoing | Ensure that Places includes a usable and robust API for extensibility | Places Team | [bug 374520](https://bugzilla.mozilla.org/show_bug.cgi?id=374520)  
PLCS-002a | In Progress. Places Organizer landed but does not have support for downloads | Unified user interface that improves the usability and discoverability of features | Places Team | [bug 374521](https://bugzilla.mozilla.org/show_bug.cgi?id=374521)  
PLCS-002b | Complete | Parity with Firefox 2 Bookmarks/History UI | Places Team | [bug 355737](https://bugzilla.mozilla.org/show_bug.cgi?id=355737)  
PLCS-003a | Complete | Protection and safeguarding against data loss | Places Team | [bug 374526](https://bugzilla.mozilla.org/show_bug.cgi?id=374526)  
PLCS-003b | Complete | Bookmark data is never lost between browsing sessions | Places Team | [bug 374527](https://bugzilla.mozilla.org/show_bug.cgi?id=374527)  
PLCS-003c | Complete | Provide backup and restore functionality for bookmarks | Places Team | [bug 374528](https://bugzilla.mozilla.org/show_bug.cgi?id=374528)  
PLCS-003d | Complete | Make it easy for users to export their bookmarks for use in another application | Places Team | [bug 374529](https://bugzilla.mozilla.org/show_bug.cgi?id=374529)  
PLCS-005a | Complete | Improve performance (as measured by memory use, transactional speed, and Ts) of bookmark and history storage and retrieval operations | Places Team | [bug 374532](https://bugzilla.mozilla.org/show_bug.cgi?id=374532)  
  
## P2

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
PLCS-001b | deprioritize | Build a sync client on the new sync infrastructure | Places Team | [bug 374519](https://bugzilla.mozilla.org/show_bug.cgi?id=374519)  
PLCS-002c | Complete; "Starring" UI | Provide some UI that allows users to mark a URI as "interesting" | Places Team | ~~[bug 374522](https://bugzilla.mozilla.org/show_bug.cgi?id=374522)~~  
PLCS-002d | Complete | Provide some UI that allows users to annotate a URI with tags | Places Team | ~~[bug 374524](https://bugzilla.mozilla.org/show_bug.cgi?id=374524)~~  
PLCS-004a |  | Index web page content into a DB that can be queried | Places Team | [bug 342913](https://bugzilla.mozilla.org/show_bug.cgi?id=342913)  
PLCS-004b |  | Allow users to search on all available URI metadata | Places Team | [bug 374530](https://bugzilla.mozilla.org/show_bug.cgi?id=374530)  
  
## P3

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
PLCS-002e | At risk | Provide some UI that allows users to annotate a URI with free-form notes |  | [bug 374525](https://bugzilla.mozilla.org/show_bug.cgi?id=374525)  
PLCS-004c | cut | Support SQL queries of the bookmarks database in the Error Console |  | [bug 374531](https://bugzilla.mozilla.org/show_bug.cgi?id=374531)  
  
# [Site-Specific Preferences](/Site-Specific_Preferences "Site-Specific
Preferences")

## P2

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
PREF-001a | Complete | Create framework for persisting and applying per-site settings across sessions and tabs | Myk Melez | [bug 378547](https://bugzilla.mozilla.org/show_bug.cgi?id=378547)  
PREF-001b | Complete | Persist zoom for sites | Myk Melez | [bug 378549](https://bugzilla.mozilla.org/show_bug.cgi?id=378549)  
  
# Security, Privacy

## P1

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
SPI-001a | Complete | Better UI indication of encryption, identity, previous interaction/knowledge of site and security/privacy context | Johnathan Nightingale | [bug 377076](https://bugzilla.mozilla.org/show_bug.cgi?id=377076)  
SPI-001b | Complete | Support website identity validation mechanism (ref: EV Certificates) | Johnathan Nightingale/NSS Team | [bug 383183](https://bugzilla.mozilla.org/show_bug.cgi?id=383183)  
SPI-001g | Complete | Simplify dialogs around certificate errors | Johnathan Nightingale/Kaie | [bug 327181](https://bugzilla.mozilla.org/show_bug.cgi?id=327181)  
SPI-001i | Complete | Chromeless popup windows should have some forced chrome | Johnathan Nightingale | [bug 337344](https://bugzilla.mozilla.org/show_bug.cgi?id=337344)  
SPI-003b | In Progress 

  * Backend complete
  * User notification and Add-ons manager integration in progress

| Countermeasures for Java/plugin/extension vulnerabilities (disable, warn, offer updates) | Michael Wu | [bug 271559](https://bugzilla.mozilla.org/show_bug.cgi?id=271559) and [bug 330511](https://bugzilla.mozilla.org/show_bug.cgi?id=330511). [bug 391731](https://bugzilla.mozilla.org/show_bug.cgi?id=391731) for tracking remaining work.  
SPI-003c | Public discussion happening | Content restriction - Allow web authors to restrict scripts in headers | Jonas Sicking and Robert Sayre |   
  
## P2

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
SPI-001d | Complete, by virtue of SPI-001b & SPI-001k | User should be able to determine the "identity" of a website when that information is available | Johnathan Nightingale | [bug 377076](https://bugzilla.mozilla.org/show_bug.cgi?id=377076), [bug 383183](https://bugzilla.mozilla.org/show_bug.cgi?id=383183)  
SPI-001e | Complete, by virtue of SPI-001k | Provide UI for displaying summary of security signals | Johnathan Nightingale | [bug 377076](https://bugzilla.mozilla.org/show_bug.cgi?id=377076)  
SPI-001f | WIP Patch | Simplify the UI around presenting certificates | Johnathan Nightingale | [bug 380775](https://bugzilla.mozilla.org/show_bug.cgi?id=380775)  
SPI-001h | Complete | Improve dialogs/alerts related to security | Johnathan Nightingale | [bug 341472](https://bugzilla.mozilla.org/show_bug.cgi?id=341472)  
SPI-001j | Patch in Review | Unify terminology and metaphors for "blocked malicious content" | Johnathan Nightingale | [bug 399233](https://bugzilla.mozilla.org/show_bug.cgi?id=399233)  
SPI-001k | Complete | Enhanced Security Tab in Page Info | Johnathan Nightingale | [bug 377076](https://bugzilla.mozilla.org/show_bug.cgi?id=377076)  
SPI-002a | deprioritized | Create a "private browsing mode" for Firefox - local client only | Michael Ventnor | [Functional Spec](/PrivateBrowsing "PrivateBrowsing") [bug 248970](https://bugzilla.mozilla.org/show_bug.cgi?id=248970)  
SPI-002b | At risk | Indicate privacy status in primary UI |  | [Functional Spec](/PrivateBrowsing "PrivateBrowsing")  
SPI-003a | In progress | Blacklisting of malicious websites | Johnathan Nightingale (front end) / Dave Camp (back end) | [bug 380932 for front end](https://bugzilla.mozilla.org/show_bug.cgi?id=380932)  
SPI-003d |  | Tighten the same-origin policy for local files (file: URLs, trusted, security) | DVeditz |   
SPI-003f | In progress for malware sites | Extend Phishing Protection to include malware sites and Add-ons |  | [bug 380932](https://bugzilla.mozilla.org/show_bug.cgi?id=380932)  
  
## P3

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
SPI-001c | At risk | Indicate security and privacy status in secondary UI |  |   
SPI-002c | At risk | create pluggable architecture that supports private browsing |  |   
SPI-003e | At risk | Content restriction - Everything else involved with the content restriction proposal |  |   
SPI-003g | At risk | Sanitizing content sinks for full content, not just fragments |  |   
  
# Search

No P1s

## P2

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
SRCH-001b | Complete | Support search engine shortcut keys | Ryan Flint | [bug 378553](https://bugzilla.mozilla.org/show_bug.cgi?id=378553)  
SRCH-001d | Complete | Resizable search bar | Neil Deakin | [bug 267831](https://bugzilla.mozilla.org/show_bug.cgi?id=267831)  
SRCH-001e | Complete | Replace answers.com with Wikipedia |  | [bug 380785](https://bugzilla.mozilla.org/show_bug.cgi?id=380785), added not replaced  
  
## P3

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
SRCH-001a | At risk | Easy-to-understand UI |  |   
SRCH-001c | Needs def | Rich search results | Gavin Sharp |   
SRCH-002a | At risk | Ability to declare a default search engine |  |   
SRCH-002b | At risk | Ability to use a temporary search engine and then restore the default |  |   
  
# Visual Refresh

## P1

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
VIS-001a | On Track | Deliver new Firefox theme | Mike Beltzner | OS X Theme:[bug 397723](https://bugzilla.mozilla.org/show_bug.cgi?id=397723)  
VIS-001b | In Progress | Revise Firefox chrome | Mike Beltzner |   
  
## P2

No P2's

## P3

No P3's

# Tabbed browsing

## P1

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
TAB-006a | On track | Data-loss issue related to tabs/windows | Mike Connor | [bug 175124](https://bugzilla.mozilla.org/show_bug.cgi?id=175124)  
  
## P2

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
TAB-001a | At risk | Quickly group similar tabs together |  |   
TAB-002a | At risk | Quickly find the tab you're looking for |  | [bug 385211](https://bugzilla.mozilla.org/show_bug.cgi?id=385211)? [bug 395980](https://bugzilla.mozilla.org/show_bug.cgi?id=395980)?  
TAB-003a | At risk | Tear-off tabs (80% solution) |  | [bug 225680](https://bugzilla.mozilla.org/show_bug.cgi?id=225680)  
TAB-003d | At risk | Improve discoverability and usability of undo close tab |  | [bug 357235](https://bugzilla.mozilla.org/show_bug.cgi?id=357235)  
TAB-004d | Complete | Scrolling through tabs on tabstrip animation | Dão Gottwald and Michael Ventnor | [bug 347363](https://bugzilla.mozilla.org/show_bug.cgi?id=347363)  
  
## P3

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
TAB-003b | At risk | Try to do more intelligent things with the Tab title space |  |   
TAB-003c | At risk | Resizable tabs |  |   
TAB-004a | At risk | Transitioning between tabs animation |  |   
TAB-004b | needs review | Opening/closing tabs animation | Dão Gottwald (closing only) | [bug 380960](https://bugzilla.mozilla.org/show_bug.cgi?id=380960)  
TAB-004c | At risk | Reordering tabs animation |  | [bug 410972](https://bugzilla.mozilla.org/show_bug.cgi?id=410972)  
TAB-005a | At risk | Add a pref to allow users to stop animations and plugins on background tabs |  |   
TAB-005b | At risk | Improve user control over undo close tab and session history |  |   
  
# Installer

## P1

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
INST-001a | Complete | Support a .exe installer on Windows | Robert Strong | NSIS Installer implemented for Firefox 2.0  
INST-001b | Complete | Support a DMG installer on Mac OS X |  |   
INST-001c | Complete | Support for "scripted" installations (ie, command line options) | Robert Strong | Support for specifying a configuration file added for Firefox 2.0. [Specification](/Installer:Command_Line_Arguments "Installer:Command Line Arguments")  
INST-001d | Complete | Support for silent install (no UI) | Robert Strong | Support for silent installs added for Firefox 2.0. [Specification](/Installer:Command_Line_Arguments "Installer:Command Line Arguments")  
INST-003a | Complete | Uninstall should offer removal of profiles (for user performing uninstall) | Robert Strong | ~~[bug 398434](https://bugzilla.mozilla.org/show_bug.cgi?id=398434)~~  
INST-003b | Complete | Uninstall should remove all Windows registry entries | Robert Strong | ~~[bug 393149](https://bugzilla.mozilla.org/show_bug.cgi?id=393149)~~ , ~~[bug 389244](https://bugzilla.mozilla.org/show_bug.cgi?id=389244)~~ , and ~~[bug 369997](https://bugzilla.mozilla.org/show_bug.cgi?id=369997)~~  
INST-004a | Complete | Install as a non-admin user on Vista | Robert Strong | ~~[bug 370571](https://bugzilla.mozilla.org/show_bug.cgi?id=370571)~~  
  
## P2

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
INST-005a | In Progress | Support reading in a localizable string with a partner name | Robert Strong | ~~[bug 399665](https://bugzilla.mozilla.org/show_bug.cgi?id=399665)~~ , [bug 399921](https://bugzilla.mozilla.org/show_bug.cgi?id=399921), and [bug 399928](https://bugzilla.mozilla.org/show_bug.cgi?id=399928)  
INST-006a | At risk | Ability to allow optional installation (check/uncheck) of bundled add-ons  |  | [bug 400034](https://bugzilla.mozilla.org/show_bug.cgi?id=400034)  
  
## P3

ID | Status | Requirement | Assignee | Bug/Design links  
---|---|---|---|---  
INST-007a | Complete | Support replacing images in the wizard | Robert Strong | ~~[bug 399381](https://bugzilla.mozilla.org/show_bug.cgi?id=399381)~~  
  
Retrieved from
"[https://wiki.mozilla.org/index.php?title=Firefox3/Product_Requirements_Document&oldid=87477](https://wiki.mozilla.org/index.php?title=Firefox3/Product_Requirements_Document&oldid=87477)"

## Navigation menu

###  Personal tools

  * [Log in](/index.php?title=Special:UserLogin&returnto=Firefox3%2FProduct+Requirements+Document "You are encouraged to log in; however, it is not mandatory \[o\]")
  * [Request account](/Special:RequestAccount "You are encouraged to create an account and log in; however, it is not mandatory")

###  Namespaces

  * [Page](/Firefox3/Product_Requirements_Document "View the content page \[c\]")
  * [Discussion](/index.php?title=Talk:Firefox3/Product_Requirements_Document&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[t\]")

English

###  Views

  * [Read](/Firefox3/Product_Requirements_Document)
  * [View source](/index.php?title=Firefox3/Product_Requirements_Document&action=edit "This page is protected.
You can view its source \[e\]")

  * [View history](/index.php?title=Firefox3/Product_Requirements_Document&action=history "Past revisions of this page \[h\]")

More

###  Search

[](/Main_Page "Visit the main page")

###  Navigation

  * [Main page](/Main_Page "Visit the main page \[z\]")
  * [Product releases](/Releases)
  * [New pages](/Special:NewPages)
  * [Recent changes](/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [Recent uploads](/Special:NewFiles)
  * [Help](/MozillaWiki:Help "The place to find out")

###  How to Contribute

  * [Contribute to Mozilla](/Contribute)
  * [Community Portal](//community.mozilla.org)
  * [Community Participation Guidelines](//www.mozilla.org/en-US/about/governance/policies/participation/)

###  MozillaWiki

  * [About](/MozillaWiki:About)
  * [Team](/MozillaWiki:Team)
  * [Policies](/MozillaWiki:Policies)
  * [Report a wiki bug](//bugzilla.mozilla.org/enter_bug.cgi?product=Websites&component=wiki.mozilla.org)

###  Around Mozilla

  * [Mozilla Support](//support.mozilla.org/)
  * [Give product Feedback](//connect.mozilla.org/)
  * [Mozilla Developer Network](//developer.mozilla.org/)
  * [Planet Mozilla](//planet.mozilla.org/)

###  Tools

  * [What links here](/Special:WhatLinksHere/Firefox3/Product_Requirements_Document "A list of all wiki pages that link here \[j\]")
  * [Related changes](/Special:RecentChangesLinked/Firefox3/Product_Requirements_Document "Recent changes in pages linked from this page \[k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](javascript:print\(\); "Printable version of this page \[p\]")
  * [Permanent link](/index.php?title=Firefox3/Product_Requirements_Document&oldid=87477 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Firefox3/Product_Requirements_Document&action=info "More information about this page")

  * This page was last edited on 20 March 2008, at 07:09.

  * [Privacy policy](/MozillaWiki:Privacy_policy)
  * [About MozillaWiki](/MozillaWiki:About)
  * [Mobile view](https://wiki.mozilla.org/index.php?title=Firefox3/Product_Requirements_Document&mobileaction=toggle_view_mobile)

  * [](https://www.mediawiki.org/)

