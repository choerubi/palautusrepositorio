*** Settings ***
Resource  resource.robot
Resource    login.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  maija
    Set Password  maija1234
    Set Password Confirmation  maija1234
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ma
    Set Password  maija1234
    Set Password Confirmation  maija1234
    Submit Credentials
    Registration Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  maija
    Set Password  ma
    Set Password Confirmation  ma
    Submit Credentials
    Registration Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  maija
    Set Password  maijamaija
    Set Password Confirmation  maijamaija
    Submit Credentials
    Registration Should Fail With Message  Password does not meet the requirements

Register With Nonmatching Password And Password Confirmation
    Set Username  maija
    Set Password  maija1234
    Set Password Confirmation  maija4567
    Submit Credentials
    Registration Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Credentials
    Registration Should Fail With Message  Username already in use

Login After Successful Registration
    Set Username  matti
    Set Password  matti1234
    Set Password Confirmation  matti1234
    Submit Credentials
    Registration Should Succeed
    Go To Login Page
    Set Username  matti
    Set Password  matti1234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  pekka
    Set Password  pekka1234
    Set Password Confirmation  pekka4567
    Submit Credentials
    Registration Should Fail With Message  Passwords do not match
    Go To Login Page
    Set Username  pekka
    Set Password  pekka1234
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Registration Should Succeed
    Main Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle1234
    Go To Register Page
