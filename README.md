# RabbitExample

## Getting Started

Application is wrapped into the docker containers. Dockerfile and docker-compose file are placed at the root directory of the project.

To run the application (it is expected that you have installed Docker and can run Docker commands), follow these steps:

1. Navigate into the root folder.

2. Build the Docker images:

   ```bash
   docker-compose build
   docker-compose up
  - Probably you will get an error. Check Troubleshooting + Resolution section of README.


3. Check Resolution section because you need to manually run SQL script to create a database inside SQL docker server. Run the script.
4. Navigate to: [http://127.0.0.1:8000/docs#], create your demo data through the openapi UI.

## Troubleshooting and Data Modification
  If you encounter similar error during the execution of your application:
  `web | sqlalchemy.exc.ProgrammingError: (pyodbc.ProgrammingError) ('42S02', "[42S02] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Invalid object name 'Cosmonaunts'. `

## Resolution
  From witihn folder where docker files are placed run:
  - `docker exec -it <db_container_id> /opt/mssql-tools/bin/sqlcmd -S db -U sa -P StrongPassword!123 -d master -i /docker-entrypoint-initdb.d/docker_setup.sql`
  - should be trigered before you try any API call.