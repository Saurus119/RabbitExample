from typing import List
from sqlalchemy.exc import PendingRollbackError

from Api.Enums.Api.query_order_type import OrderDBType
from Api.Models import Cosmonaunt
from Shared.DataAccess.Services.Config.config_service import DBService
from Shared.DataAccess.Models.cosmonaut_db import CosmonauntModel

class CosmonautService(DBService):
    
    def __init__(self) -> None:
        super().__init__()

    def get(self, filter) -> List[CosmonauntModel]:
        query = self.db.query(CosmonauntModel)

        if filter.order_type:
            try:
                if OrderDBType(filter.order_type).name.lower() == 'asc':
                    query = query.order_by(CosmonauntModel.Date.asc())
                elif OrderDBType(filter.order_type).name.lower() == 'desc':
                    query = query.order_by(CosmonauntModel.Date.desc())
            except AttributeError as e:
                print("Invalid order type from user. Data are not ordered.")

        if filter.limit:
            query = query.limit(filter.limit)

        try:
            cosmonaunts = query.all()
        except PendingRollbackError as exc:
            cosmonaunts = []
            self.db.rollback()
        
        # TODO: Maybe missmatch between SQL alchemy model and DB definition? extra characters are added.
        for cosm in cosmonaunts:
            cosm.Name = cosm.Name.strip()

        return cosmonaunts
    
    def create(self, cosmonaunt: CosmonauntModel) -> bool:
        try:
            self.db.add(cosmonaunt)
            self.db.commit()
            return True
        except Exception:
            return False
        
    def delete(self, cosmonaunt_id: int) -> int:
        deleted_rows = (
                self.db.query(CosmonauntModel)
                .filter(CosmonauntModel.Id == cosmonaunt_id)
                .delete()
        )
        self.db.commit()

        return deleted_rows
    
    def update(self, cosmonaunt_id: int, name: Cosmonaunt) -> bool:
        selected_cosmonaunt = (
            self.db.query(CosmonauntModel)
            .filter(CosmonauntModel.Id == cosmonaunt_id)
            .first()
        )

        if selected_cosmonaunt:
            selected_cosmonaunt.Name = name
            self.db.commit()
            return True
        
        return False



