You are currently viewing a snapshot of www.mozilla.org taken on April 21,
2008. Most of this content is highly out of date (some pages haven't been
updated since the project began in 1998) and exists for historical purposes
only. If there are any pages on this archive site that you think should be
added back to www.mozilla.org, please [file a
bug](https://bugzilla.mozilla.org/enter_bug.cgi?product=Websites&component=www.mozilla.org).

Skip to main content

# [Mozilla](/ "Return to home page")

  * [About](../../../../../about/ "Getting the most out of your online experience")
  * [Developers](../../../../../developer/ "Using Mozilla's products for your own applications")
  * [Store](http://store.mozilla.org/?r=mozorg1 "Shop for Mozilla products on CD and other merchandise")
  * [Support](../../../../../support/ "Installation, trouble-shooting, and the knowledge base")
  * [Products](../../../../../products/ "All software Mozilla currently offers")

search mozilla:

* * *

  * [**Roadmap**](/roadmap "Roadmap")
  * [**Projects**](../../../../../projects/ "Projects")
  * [**Coding**](../../../../../developer/ "For developers")
    * [ Module Owners](/owners "Module Owners")
    * [ Hacking](../../../../../hacking/ "Hacking")
    * [ Get the Source](http://developer.mozilla.org/en/docs/Download_Mozilla_Source_Code "Get the Source")
    * [ Build It](http://developer.mozilla.org/en/docs/Build_Documentation "Building Mozilla")
  * [**Testing**](../../../../../quality/ "Testing")
    * [ Releases](/download "Downloads of mozilla.org software releases")
    * [ Nightly Builds](../../../../../developer/#builds "Latest mozilla builds for testers")
    * [ Report A Problem](https://bugzilla.mozilla.org/ "For testers to report bugs")
  * [**Tools**](/tools "Tools for mozilla developers")
    * [ Bugzilla](https://bugzilla.mozilla.org/ "Bug tracking system for mozilla testers.")
    * [ Tinderbox](http://tinderbox.mozilla.org/showbuilds.cgi?tree=Firefox "Latest status of mozilla builds")
    * [ Bonsai](http://bonsai.mozilla.org/cvsqueryform.cgi "Latest checkins")
    * [ LXR](http://lxr.mozilla.org/seamonkey/ "Source cross reference")
  * [**FAQs**](/faq "Frequently Asked Questions.")

* * *

_You are here:_ [browser/composer front-end test cases](../) > **Test Case
Matrix for History**

# Test Case Matrix for History

Global History Basic Functional (Acceptance) Testcases Feature/Function | sub-feature  
sub-function | Description | Test Case Name  
---|---|---|---  
Global History | Record sites | Verify that visited links are recorded. | [record-links](/quality/browser/front-end/testcases/history/record-links)  
Global History | Record after redirect | Verify that the correct link is recorded after a server redirect. | [record-redirect](/quality/browser/front-end/testcases/history/record-redirect)  
Global History | Load recorded url | Verify that double-clicking on a history link causes it to be launched in a browser window. | [surf-history](/quality/browser/front-end/testcases/history/surf-history)  
Global History | Delete one entry | Delete a History entry | [delete-link](/quality/browser/front-end/testcases/history/delete-link)  
Global History | Delete multiple entries | Delete multiple History entries | [delete-multiple-links](/quality/browser/front-end/testcases/history/delete-multiple-links)  
Global History | Erase all | Clear all of history | [clear-history](/quality/browser/front-end/testcases/history/clear-history)  
Global History |  |  |   
Global History Advanced Functional Testcases Feature/Function | sub-feature  
sub-function | Description | Test Case Name  
---|---|---|---  
Global History | Change grouping | Change the History View to Group by Day|Site|None | [change-group](/quality/browser/front-end/testcases/history/change-group)  
Global History | Sort by columns | sort and reverse-sort per column | [sort-columns](/quality/browser/front-end/testcases/history/sort-columns)  
Global History | Resize columns | Verify that columns are resizable to show/hide more of entries | [resize-columns](/quality/browser/front-end/testcases/history/resize-columns)  
Global History | Show/Hide columns | Show and hide columns. | [show-hide-columns](/quality/browser/front-end/testcases/history/show-hide-columns)  
Global History  
(Negative test) | Don't record everything | Verify that things that aren't supposed to be added to history aren't (eg chorme:/// url's) | do-not-record-links  
Global History  
(Regression test) | Don't show 302 redirect | Don't ever show 302 redirects in history | [Bug 102043](https://bugzilla.mozilla.org/show_bug.cgi?id=102043)  
Session History Basic Functional (Acceptance) Testcases Feature/Function | sub-feature  
sub-function | Description | Test Case Name  
---|---|---|---  
Session History | Go menu list | Verify correct recently visited sites are in go menu. | [gomenu-list](/quality/browser/front-end/testcases/history/gomenu-list)  
Session History | Back and Forward button dropdowns | Verify recently visited sites are in Back and Forward button dropdown menu and work. | [button-dropdown](/quality/browser/front-end/testcases/history/button-dropdown)  
Session History | Surf Go menuitems | Verify browser goes back and forward to recently visited sites | [surf-golinks](/quality/browser/front-end/testcases/history/surf-golinks)  
Session History | Back and forward with frames | Verify browser goes back and forward correctly from page with frames. | [frame-history](/quality/browser/front-end/testcases/history/frame-history)  
Session History | New session | Verify that a new session is started with a new browser window or a restart. | [new-session](/quality/browser/front-end/testcases/history/new-session)  
Session History Advanced Functional Testcases Feature/Function | sub-feature  
sub-function | Description | Test Case Name  
---|---|---|---  
Session History | Back and forward with named anchors | Verify browser goes back and forward correctly from sites that use named anchors | [anchor-history](/quality/browser/front-end/testcases/history/anchor-history)  
Session History  
(Regression Test) | Retain scroll position | Verify that browser remembers scroll state when returning to pages in SH | Bug XXXXX  
  
* * *

  * [Site Map](/sitemap)
  * [Security Updates](../../../../../security/)
  * [Contact Us](../../../../../contact/)
  * [Donate](/foundation/donate)

Portions of this content are (C) 1998-2009 by individual mozilla.org contributors; content available under a Creative Commons license | [Details](http://www.mozilla.org/foundation/licensing/website-content).

Last modified November 26, 2006 [Document History](http://bonsai-
www.mozilla.org/cvslog.cgi?file=mozilla-org/html/quality/browser/front-
end/testcases/history/index.html&rev=&root=/www/)

