# Dekla Parking Application

## Server

The server python application offers a CLI with several options for database configuration. The option `--help`, describes the CLI usage.

```
usage: app.py [-h] [--host HOST] [--port PORT] [--db-host DB_HOST]
              [--db-port DB_PORT] [--db-name DB_NAME] --db-password DB_PASSWORD
              --db-user DB_USER [--db-dbms DB_DBMS] [--dev-mode]

Set environment variables for database configuration.

options:
  -h, --help            show this help message and exit
  --host HOST           host where server is running
  --port PORT           port where server is running
  --db-host DB_HOST     host where database is running
  --db-port DB_PORT     port where database is running
  --db-name DB_NAME     name of the database
  --db-password DB_PASSWORD
                        password to access database
  --db-user DB_USER     user to access database
  --db-dbms DB_DBMS     DBMS of the database
  --dev-mode            starts server in development mode

```

The restful API documentation can be found in the `/docs` of the path of the API.