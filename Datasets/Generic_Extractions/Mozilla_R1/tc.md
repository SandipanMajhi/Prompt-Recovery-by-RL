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

_You are here:_ [Browser/Composer front-end QA](../../) > [front-end test
cases](../) > **Test Case Matrix for Bookmarks**

# Test Case Matrix for Bookmarks

*References to 'the 4 standard locations' in these testcases refer to the Manage Bookmarks window, the toplevel Bookmarks menu, the Bookmarks panel in the Sidebar, and the Bookmarks popup menu on the bookmarks/personal toolbar. This is important, there will be a test later.

Feature/Function | sub-feature  
sub-function | Description | Test Case Name  
---|---|---|---  
Bookmarks Basic Functional(Acceptance) Tests  
Bookmarks | View Bookmarks | Verify that bookmarks appear at the standard(4) access points | [view-bookmarks](/quality/browser/front-end/testcases/bookmarks/view-bookmarks)  
Bookmarks | Add Bookmark | Verify that bookmarks are properly added to bookmarks file and appear in all access points. | [add-bookmark](/quality/browser/front-end/testcases/bookmarks/add-bookmark)  
Bookmarks | File Bookmark | Add a new bookmark into a specific location within the bookmarks hierarchy. | [file-bookmark](/quality/browser/front-end/testcases/bookmarks/file-bookmark)  
Manage Bookmarks | Create new bookmark | Verify new bookmarks can be created (not added). | [create-bookmark](/quality/browser/front-end/testcases/bookmarks/create-bookmark)  
Bookmarks | Delete Bookmark | Verify that bookmarks are properly deleted from bookmarks file and disappear from all access points. | [delete-bookmark](/quality/browser/front-end/testcases/bookmarks/delete-bookmark)  
Bookmarks | Add/Delete Personal Toolbar bookmark | Verify that items from the personal toolbar folder are properly added/deleted. | [add-delete-ptoolbar-bmark](/quality/browser/front-end/testcases/bookmarks/add-delete-ptoolbar-bmark)  
Manage Bookmarks | Create Folder | Verify new folder creation and nesting of new folders. | [create-folder](/quality/browser/front-end/testcases/bookmarks/create-folder)  
Bookmarks | Surf Bookmark | Verify that double-clicking on a bookmark causes it to be launched in a browser window | [surf-bookmark](/quality/browser/front-end/testcases/bookmarks/surf-bookmark)  
Bookmarks | Surf All Bookmarks | Verify that there are no 'dead' default links. | [surf-all-bookmarks](/quality/browser/front-end/testcases/bookmarks/surf-all-bookmarks)  
Manage Bookmarks | Edit item properties | Verify that changes to an item are saved without loss of item integrity. | [edit-properties](/quality/browser/front-end/testcases/bookmarks/edit-properties)  
Bookmarks Advanced Functional Testcases  
Manage Bookmarks | Delete Folder | Verify folder(s) are correctly deleted. | [delete-folder](/quality/browser/front-end/testcases/bookmarks/delete-folder)  
Manage Bookmarks | Show/Hide Folder | Verify that disclosure triangles/folder icons are in sync. | [show-hide-folder](/quality/browser/front-end/testcases/bookmarks/show-hide-folder)  
Manage Bookmarks | Create/Delete separator | Verify separators are properly added/deleted. | [create-delete-separator](/quality/browser/front-end/testcases/bookmarks/create-delete-separator)  
Manage Bookmarks | Save State | Verify that changes are saved over restart/crash | [save-state](/quality/browser/front-end/testcases/bookmarks/save-state)  
Manage Bookmarks | View item properties | Verify that view properties works as appropriate for bookmarks, folders, and separators(negative) | [view-properties](/quality/browser/front-end/testcases/bookmarks/view-properties)  
Manage Bookmarks | Rename bookmark inline - not implemented | Change the name of a bookmark without use of the bookmark properties dialog. | [rename-bookmark](/quality/browser/front-end/testcases/bookmarks/rename-bookmark)  
Manage Bookmarks | Custom Keywords | surf using user-defined 'custom keyword'. | [custom-keywords](/quality/browser/front-end/testcases/bookmarks/custom-keywords)  
Manage Bookmarks | Sort by columns | sort and reverse-sort per column | [sort-columns](/quality/browser/front-end/testcases/bookmarks/sort-columns)  
Manage Bookmarks | Resize columns | Verify that columns are resizable to show/hide more of entries | [resize-columns](/quality/browser/front-end/testcases/bookmarks/resize-columns)  
Manage Bookmarks | Show/Hide columns | Show and hide columns. | [show-hide-columns](/quality/browser/front-end/testcases/bookmarks/show-hide-columns)  
Manage Bookmarks | Drag & Drop to reorder columns - not implemented |  | reorder-columns  
Manage Bookmarks | Drag & Drop to reorder items |  | [reorder-item](/quality/browser/front-end/testcases/bookmarks/reorder-item)  
Manage Bookmarks | Drag & Drop to rearrange item hierarchy |  | [reorder-hierarchy](/quality/browser/front-end/testcases/bookmarks/reorder-hierarchy)  
Manage Bookmarks | Cut and Undo items |  | [cut-undo-redo-items](/quality/browser/front-end/testcases/bookmarks/cut-undo-redo-items)  
Manage Bookmarks | Copy-paste items |  | [copy-paste-items](/quality/browser/front-end/testcases/bookmarks/copy-paste-items)  
Manage Bookmarks | Paste items nested inot a folder |  | [paste-into-folder](/quality/browser/front-end/testcases/bookmarks/paste-into-folder)  
Manage Bookmarks | Delete multiple bookmarks | Verify that several bookmarks are deleted at one time. | [delete-multiple-bookmarks](/quality/browser/front-end/testcases/bookmarks/delete-multiple-bookmarks)  
Manage Bookmarks | Import bookmarks |  | import-bookmarks  
Manage Bookmarks | Export bookmarks |  | export-bookmarks  
Bookmarks Negative & Regression Tests  
Manage Bookmarks  
(negative/regresion test) | Prevent bad drops | Verify that it is NOT possible to drop an item onto itself or its immediate parent or child | [self-drop](/quality/browser/front-end/testcases/bookmarks/self-drop)  
  
* * *

  * [Site Map](/sitemap)
  * [Security Updates](../../../../../security/)
  * [Contact Us](../../../../../contact/)
  * [Donate](/foundation/donate)

Portions of this content are (C) 1998-2009 by individual mozilla.org contributors; content available under a Creative Commons license | [Details](http://www.mozilla.org/foundation/licensing/website-content).

Last modified December 2, 2006 [Document History](http://bonsai-
www.mozilla.org/cvslog.cgi?file=mozilla-org/html/quality/browser/front-
end/testcases/bookmarks/index.html&rev=&root=/www/)

