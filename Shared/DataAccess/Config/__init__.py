from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Shared.DataAccess.Config.local_connection import LocalDBConnection

engine = create_engine(
    f"mssql+pyodbc://{LocalDBConnection.USERNAME}:{LocalDBConnection.PASSWORD}@{LocalDBConnection.SERVER}/{LocalDBConnection.DATABASE}?driver={LocalDBConnection.DRIVER}"
    )

Session = sessionmaker(engine)
db_session = Session()