*** Settings ***
Suite Setup    Open Browser    https://www.katalon.com/    firefox
Suite Teardown    Close Browser
Resource    seleniumLibrary.robot

*** Variables ***
${undefined}    https://www.katalon.com/

*** Test Cases ***
Test Case
    open    https://mail.163.com/
    selectFrame    index=2
    click    id=auto-id-1556809284468
    type    id=auto-id-1556809284468    13819492036
    type    id=auto-id-1556809284471    12345678
    click    id=dologin
    