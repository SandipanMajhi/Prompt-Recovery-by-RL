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
for Browser Preferences**

# Test Case Matrix for Themes

by Patty Mac

**Objective** : Describe the detail test cases for themes.

**Categories** : Divide the test cases into following three categories:

  * Acceptance tests - Must pass all the test cases describe under this category.
  * Functional tests - Describe how testing is going to be done for each feature.

## Acceptance tests

Feature/Function/Test Case | Description | Test Case Link  
---|---|---  
Check for Themes | Verify both Classic and Modern exist under the themes preferences | [ThemeTest_Acc.html](/quality/browser/front-end/testcases/themes/themetest_acc)  
Testing under Classic theme | Verify Classic theme works as advertised | [Classic_Acc.html](/quality/browser/front-end/testcases/themes/classic_acc)  
Check the appearance of browser | Visually inspect menu bar, floating component bar and all the tool bars | [Classic_Acc2.html](/quality/browser/front-end/testcases/themes/classic_acc2)  
Testing under Modern theme | Verify Modern theme works as advertised | [Modern_Acc.html](/quality/browser/front-end/testcases/themes/modern_acc)  
Check the appearance of browser | Visually inspect menu bar, floating component bar and all the tool bars | [Modern_Acc2.html](/quality/browser/front-end/testcases/themes/modern_acc2)  
Checking View menu | Verify if themes exist under View menu | [ThemesVerify_Acc.html](/quality/browser/front-end/testcases/themes/themesverify_acc)  
  
## Functional test

Feature/Function/Test Case | Description | Test Case Link  
---|---|---  
Verify all the selectable items work under Classic theme | Click through all the items on menu bar, tool bars, and floating component bar under Classic theme | [Functional1.html](/quality/browser/front-end/testcases/themes/functional1)  
Verify all the selectable items on other applications under Classic theme | Click through all the items on menu bar and tool bars under AIM, Composer, Mail and Address book to see all the looks and feel are consistence under Classic theme | [Functional2.html](/quality/browser/front-end/testcases/themes/functional2)  
Verify all the selectable items work under Modern theme | Click through all the items on menu bar, tool bars, and floating component bar under Modern theme | [Functional3.html](/quality/browser/front-end/testcases/themes/functional3)  
Verify all the selectable items on other applications under Modern theme | Click through all the items on menu bar and tool bars under AIM, Composer, Mail and Address book to see all the looks and feel are consistence under Modern theme | [Functional4.html](/quality/browser/front-end/testcases/themes/functional4)  
Verify themes under View menu | Test all the items under "Apply Theme" under View menu 

  1. Selecting "Theme Preferences"
  2. Get New Themes
  3. Classic
  4. Modern

| [Functional5a.html](/quality/browser/front-
end/testcases/themes/functional5a)  
[Functional5b.html](/quality/browser/front-end/testcases/themes/functional5b)  
[Functional5c.html](/quality/browser/front-end/testcases/themes/functional5c)  
[Functional5d.html](/quality/browser/front-end/testcases/themes/functional5d)  
  
* * *

  * [Site Map](/sitemap)
  * [Security Updates](../../../../../security/)
  * [Contact Us](../../../../../contact/)
  * [Donate](/foundation/donate)

Portions of this content are (C) 1998-2009 by individual mozilla.org contributors; content available under a Creative Commons license | [Details](http://www.mozilla.org/foundation/licensing/website-content).

Last modified June 30, 2007 [Document History](http://bonsai-
www.mozilla.org/cvslog.cgi?file=mozilla-org/html/quality/browser/front-
end/testcases/Themes/index.html&rev=&root=/www/)

