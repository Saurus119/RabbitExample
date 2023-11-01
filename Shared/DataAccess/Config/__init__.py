from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Shared import is_local_enviroment
from Shared.DataAccess.Config.local_connection import LocalDBConnection
from Shared.DataAccess.Config.docker_connection import DockerDBConnection


if is_local_enviroment():
    engine = create_engine(
        f"mssql+pyodbc://{LocalDBConnection.USERNAME}:{LocalDBConnection.PASSWORD}@{LocalDBConnection.SERVER}/{LocalDBConnection.DATABASE}?driver={LocalDBConnection.DRIVER}"
    )
else:
    engine = create_engine(
        f"mssql+pyodbc://{DockerDBConnection.USERNAME}:{DockerDBConnection.PASSWORD}@{DockerDBConnection.SERVER}/{DockerDBConnection.DATABASE}?driver={DockerDBConnection.DRIVER}"
    )

Session = sessionmaker(engine)
db_session = Session()