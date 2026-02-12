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

_You are here:_ [browser/composer front-end test cases](../) > **Test Cases
for Password Manager**

# Test Case Matrix for Password Manager

Maintained by: [Terri Preston](mailto:tpreston@netscape.com)

Couldn't find a particular test case here? I encourage you to send additions,
corrections and suggestions! In addition, feel free to check out the
corresponding [ test plan for Password
Manager](http://mozilla.org/quality/browser/front-end/testplans/password-
manager).

### Password Manager

The Password Manager is also known as Single Signon. btw, The phrase "signon
information" refers inclusively to username, password and site information
saved within the Password Manager. These test cases mainly describe the steps
for one web site, it is adviced that these testcases be repeated on as many
sites as possible.

### New Feature Tests: (Currently Inactive, please do not report bugs on these
test cases)

Feature/Function/Test Case | Description | Test Case Links  
---|---|---  
Master Password prompt |  Verify that the master password is visually distinctive from other password prompts (indicates the functionality and importance of the master password) | Waiting for implementation  
Replace Forgotten Master Password | Verify that the process to replace a forgotten master password is easier/more discoverable (though encrypted information should still be lost to the user who has forgotten their password). | Waiting for implementation  
  
## Active test cases for Seamonkey:

Feature/Function/Test Case | Description | Test Case Links  
---|---|---  
Save username and password, yes | Verify that the browser behaves correctly after selections are made in the save password dialog box | [password-dialog-yes](/quality/browser/front-end/testcases/password-manager/password-dialog-yes)  
Save username and password, never for this site | Verify that the browser behaves correctly after selections are made in the save password dialog box | [password-dialog-never](/quality/browser/front-end/testcases/password-manager/password-dialog-never)  
Save username and password, no | Verify that the browser behaves correctly after selections are made in the save password dialog box | [password-dialog-no](/quality/browser/front-end/testcases/password-manager/password-dialog-no)  
Activation, disable after saved | Verify that when the password manager has been disabled, it is no longer in use, even for passwords already saved | [disable-after-save](/quality/browser/front-end/testcases/password-manager/disableaftersave)  
Activiation, Http Authentication | Need a good working case for this, working on it |   
Actitvation, ftp | Need a good working case for this, working on it |   
Password Manager, multiple users | Verify that when you have saved multiple username's and password's for a website, you are later presented with those same choices | [multiple-users](/quality/browser/front-end/testcases/password-manager/multiple-users)  
Password Manager, multiple passwords | Verify that when you have saved a username and password for a website and you later change the password, that password manager picks up the new password | [multiple-pass](/quality/browser/front-end/testcases/password-manager/multiple-pass)  
Preferences disable | Verify that when you disable password manager from the preferences panel, you no longer are asked if you would like to save passwords and longer get prefilled info on sites | [pass-pref-disable](/quality/browser/front-end/testcases/password-manager/passprefdisable)  
Preferences enable | Verify that when you enable password manager from the preferences panel, you are asked if you would like to save usernames and passwords and get prefilled info on sites | [pass-pref-enable](/quality/browser/front-end/testcases/password-manager/passprefenable)  
Preferences, view saved passwords | Verify that when you have saved a username and password in password manager, this information can be viewed in the password manager through preferences | [view-saved-pass](/quality/browser/front-end/testcases/password-manager/viewsavedpass-pref)  
Preferences, view passwords never saved | Verify that when you have designated not to ever save a username and password in password manager, this information can be viewed in the password manager through preferences (expedia.com) | [view-never-save-pass](/quality/browser/front-end/testcases/password-manager/viewneversavedpass)  
Preferences, passwords saved, remove | Verify that you can remove a username and password for a given site and it will no longer autofill on that sight nor will it be listed in password manager (espn.com) | [remove-pass-saved](/quality/browser/front-end/testcases/password-manager/removesavedpass-pref)  
Preferences, passwords saved, remove all | Verify that you can remove all username and password information and it will no longer autofill nor will anything be listed in password manager | [remove-all-saved-pass](/quality/browser/front-end/testcases/password-manager/removeallsavedpass-pref)  
Preferences, passwords never saved, remove | Verify that you can remove a site and username from the passwords never saved section of password manager (ivillage.com) | [remove-never-saved-pass](/quality/browser/front-end/testcases/password-manager/removeneversavedpass-pref)  
Preferences, passwords never saved, remove all | Verify that you can remove all site and username information from the passwords never saved section of password manager (ivillage.com) | [remove-all-never-saved-pref](/quality/browser/front-end/testcases/password-manager/removeallneversaved-pref)  
Tasks, view saved passwords | Verify that when you have saved a username and password in password manager, this information can be viewed in the password manager through tasks | [view-saved-pass-task](/quality/browser/front-end/testcases/password-manager/viewsavedpasstask)  
Tasks, view passwords never saved | Verify that when you have designated not to ever save a username and password in password manager, this information can be viewed in the password manager through tasks (nbci.com) | [view-never-saved-pass-task](/quality/browser/front-end/testcases/password-manager/viewneversavedpasstask)  
Tasks, passwords saved, remove | Verify that you can remove a username and password for a given site and it will no longer autofill on that sight nor will it be listed in password manager (netscape.com) | [remove-saved-pass-task](/quality/browser/front-end/testcases/password-manager/removesavedpass-task)  
Tasks, passwords saved, remove all | Verify that you can remove all username and password information and it will no longer autofill nor will anything be listed in password manager (lycos.com) | [remove-all-saved-pass-task](/quality/browser/front-end/testcases/password-manager/removeallsavedpass-task)  
Tasks, passwords never saved, remove | Verify that you can remove a site and username from the passwords never saved section of password manager | [remove-pass-never-saved-task](/quality/browser/front-end/testcases/password-manager/removeneversavedtask)  
Tasks, passwords never saved, remove all | Verify that you can remove all site and username information from the passwords never saved section of password manager | [remove-all-never-saved-task](/quality/browser/front-end/testcases/password-manager/removeallneversaved-task)  
  
* * *

  * [Site Map](/sitemap)
  * [Security Updates](../../../../../security/)
  * [Contact Us](../../../../../contact/)
  * [Donate](/foundation/donate)

Portions of this content are (C) 1998-2009 by individual mozilla.org contributors; content available under a Creative Commons license | [Details](http://www.mozilla.org/foundation/licensing/website-content).

Last modified March 10, 2007 [Document History](http://bonsai-
www.mozilla.org/cvslog.cgi?file=mozilla-org/html/quality/browser/front-
end/testcases/password-manager/index.html&rev=&root=/www/)

