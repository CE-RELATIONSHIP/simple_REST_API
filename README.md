## Walkthrough

### Run Docker
`docker-compose up -d`

### Build Docker 
`docker-compose up --build -d`

### Delete Old DB then Build Docker
`.\window_scripts\clean_db.bat && docker-compose up --build -d`

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

### Run Robot Unittest
`robot --outputdir /path/to/output_directory my_test_suite.robot`
