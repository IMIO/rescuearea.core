*** Settings ***

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup   Run keywords  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***

Required field
    Enable autologin as  Manager
    Go to  ${PLONE_URL}/++add++ppi
    click button  Save
    Page Should Contain Element  css=dl.portalMessage.error
    Element should contain  css=dl.portalMessage.error  Description sheet
    Element should contain  css=dl.portalMessage.error  Additional information
    Element should contain  css=dl.portalMessage.error  Administration of PPI

Error tabs
    Enable autologin as  Manager
    Go to  ${PLONE_URL}/++add++ppi
    Input Text  form-widgets-title  SiteNamePPI
    Input Text  form-widgets-address-widgets-number  1
    Input Text  form-widgets-address-widgets-street  Rue de la Loi
    Input Text  form-widgets-address-widgets-zip_code  1000
    Input Text  form-widgets-address-widgets-commune  Bruxelles
    click button  Save
    Page Should Contain Element  css=dl.portalMessage.error
    Element should not contain  css=dl.portalMessage.error  Description sheet
    page should contain  Additional information
    page should contain  Administration of PPI

Buttons and tabs
    Enable autologin as  Manager
    Go to  ${PLONE_URL}/++add++ppi
    Page should contain  Site name
    Element Should Be Visible  css=button#next
    Element Should Not Be Visible  css=button#previous
    click element  css=button#next
    Page should contain  Adaptation of the emergency services in relation to the response plan
    Element Should Be Visible  css=button#next
    Element Should Be Visible  css=button#previous
    click element  css=button#next
    Page should contain  Vehicle stop/emergency reception point
    Element Should Be Visible  css=button#next
    Element Should Be Visible  css=button#previous
    click element  css=button#next
    Page should contain  Reflex measurements on arrival on site
    Element Should Be Visible  css=button#next
    Element Should Be Visible  css=button#previous
    click element  css=button#next
    Page should contain  Attention points for the return to normal
    Element Should Be Visible  css=button#next
    Element Should Be Visible  css=button#previous
    click element  css=button#next
    Page should contain  Appendix : Itinerary
    Element Should Be Visible  css=button#next
    Element Should Be Visible  css=button#previous
    click element  css=button#next
    Page should contain  PPI reference
    Element Should Be Visible  css=button#next
    Element Should Be Visible  css=button#previous
    click element  css=button#next
    Page should contain  Tags
    Element Should Be Visible  css=button#next
    Element Should Be Visible  css=button#previous
    click element  css=button#next
    Page should contain  Publishing Date
    Element Should Be Visible  css=button#next
    Element Should Be Visible  css=button#previous
    click element  css=button#next
    Page should contain  Creators
    Element Should Not Be Visible  css=button#next
    Element Should Be Visible  css=button#previous
    click element  css=button#previous
    Page should contain  Publishing Date
