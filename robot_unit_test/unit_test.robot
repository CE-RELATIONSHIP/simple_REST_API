*** Settings ***
Library    RequestsLibrary
Suite Setup    Create Session    my_api    http://127.0.0.1:80
Suite Teardown    Delete All Sessions

*** Variables ***
# Define the base URL and any common variables
# ${BASE_URL}    http://127.0.0.1:80
${USER_ENDPOINT}    /user
${EXISTING_UID}    1
${NEW_UID}    2
${NEW_USER}    {"uid": ${NEW_UID}, "name": "John Doe", "age": 30}
${UPDATED_USER}    {"name": "Jane Doe", "age": 25}

*** Test Cases ***

Get All Users
    [Documentation]    Test to retrieve all users.
    ${response}=    GET    ${USER_ENDPOINT}
    Should Be Equal As Numbers    ${response.status_code}    200
    Log    ${response.json()}

Create New User
    [Documentation]    Test to create a new user.
    ${headers}=  create dictionary   Content-Type=application/json
    ${response}=    POST    ${USER_ENDPOINT}    ${NEW_USER}
    Should Be Equal As Numbers    ${response.status_code}    200
    Log    ${response.json()}
    
Get Specific User
    [Documentation]    Test to retrieve a specific user by UID.
    ${response}=    GET    ${USER_ENDPOINT}/${EXISTING_UID}
    Should Be Equal As Numbers    ${response.status_code}    200
    Log    ${response.json()}


Update Existing User
    [Documentation]    Test to update an existing user by UID.
    ${response}=    PUT    ${USER_ENDPOINT}/${EXISTING_UID}    ${UPDATED_USER}
    Should Be Equal As Numbers    ${response.status_code}    200
    Log    ${response.json()}

Delete User
    [Documentation]    Test to delete a user by UID.
    ${response}=    DELETE    ${USER_ENDPOINT}/${NEW_UID}
    Should Be Equal As Numbers    ${response.status_code}    200

*** Keywords ***
GET
    [Arguments]    ${endpoint}
    ${response}=    GET On Session    my_api    ${endpoint}
    RETURN    ${response}

POST
    [Arguments]    ${endpoint}    ${json_body}
    ${response}=    Post On Session    my_api    ${endpoint}    json=${json_body}
    RETURN    ${response}

PUT
    [Arguments]    ${endpoint}    ${json_body}
    ${response}=    Put On Session    my_api    ${endpoint}    json=${json_body}
    RETURN    ${response}

DELETE
    [Arguments]    ${endpoint}
    ${response}=    Delete On Session    my_api    ${endpoint}
    RETURN    ${response}
