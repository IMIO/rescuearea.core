*** Settings ***

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers

*** Test Cases ***

Required field
    Enable autologin as  Manager
    Go to  ${PLONE_URL}/++add++ppi_e
    click button  Save
    Page Should Contain Element  css=dl.portalMessage.error

Buttons and tabs
    Enable autologin as  Manager
    Go to  ${PLONE_URL}/++add++ppi_e
    Page should contain  Title
    Element Should Be Visible  css=button#next
    Element Should Not Be Visible  css=button#previous
    click element  css=button#next
    Page should contain   Dates and times start
    Element Should Be Visible  css=button#next
    Element Should Be Visible  css=button#previous
    click element  css=button#next
    Page should contain   Modified itinerary
    Element Should Be Visible  css=button#next
    Element Should Be Visible  css=button#previous
    click element  css=button#next
    Page should contain  Multidiciplinary
    Element Should Be Visible  css=button#next
    Element Should Be Visible  css=button#previous
    click element  css=button#next
    Page should contain  On-site intervention request management
    Element Should Be Visible  css=button#next
    Element Should Be Visible  css=button#previous
    click element  css=button#next
    Page should contain  Access to the site
    Element Should Be Visible  css=button#next
    Element Should Be Visible  css=button#previous
    click element  css=button#next
    Page should contain  Preliminary actions to be undertaken
    Element Should Be Visible  css=button#next
    Element Should Be Visible  css=button#previous
    click element  css=button#next
    Page should contain  Appendices
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

Add ppie
    Enable autologin as  Manager
    Go to  ${PLONE_URL}/++add++ppi_e
    Input Text  form-widgets-IDublinCore-title  TitlePPIE
    click button  Save
    Page Should Contain Element  css=div.portalMessage.info
    Element should contain  css=div.portalMessage.info  Item created
