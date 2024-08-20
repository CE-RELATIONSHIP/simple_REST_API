## Walkthrough

### Run Docker
`docker-compose up -d`

### Default PhpMyAdmin
| Key | Config |
| --- | --- |
| server   | MYSQL_DATABASE |
| user     | MYSQL_USER |
| password | MYSQL_PASSWORD |

### CRUD API
| Method | Path | Body |
| --- | --- | --- |
| GET | /user | {} |
| GET | /user/&lt;uid&gt; | {} |
| POST | /user | {uid, name, age} |
| PUT | /user/&lt;uid&gt; | {name, age} |
| DELETE | /user/&lt;uid&gt; | {} |

## Simple API using Flask

### Run using flask
`python app/app.py`

### Run Docker
`docker-compose -f compose.yaml up`

### Run Unittest
`python -m unit_test`

### Run Robot Unittest
`robot --outputdir /path/to/output_directory my_test_suite.robot`
