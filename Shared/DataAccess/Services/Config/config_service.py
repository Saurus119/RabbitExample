from Shared.DataAccess.Config import db_session

class DBService:

    def __init__(self) -> None:
        self.db = db_session