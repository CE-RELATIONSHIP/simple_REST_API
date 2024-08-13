## Walkthrough

### Script to make db directory
`makefile.bat`

### Run Docker
`docker-compose up -d`

### Default PhpMyAdmin
server   : MYSQL_DATABASE
user     : MYSQL_USER
password : MYSQL_PASSWORD

### CRUD API
GET /user {}
GET /user/uid  {}                                
POST /user {uid, name, age}
PUT /user/uid {name, age}
DELETE /user/uid {}

## Simple API using Flask

### Run using flask
`python app/app.py`

### Run Docker
`docker-compose -f compose.yaml up`

### Run Unittest
`python -m unit_test`
