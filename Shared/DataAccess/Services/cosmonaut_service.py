from typing import List

from Api.Enums.Api.query_order_type import OrderDBType
from Api.Models import Cosmonaut
from Shared.DataAccess.Services.Config.config_service import DBService
from Shared.DataAccess.Models.cosmonaut_db import CosmonautModel

class CosmonautService(DBService):
    
    def __init__(self) -> None:
        super().__init__()

    def get(self, filter) -> List[CosmonautModel]:
        query = self.db.query(CosmonautModel)

        if filter.order_type:
            try:
                if OrderDBType(filter.order_type).name.lower() == 'asc':
                    query = query.order_by(CosmonautModel.Date.asc())
                elif OrderDBType(filter.order_type).name.lower() == 'desc':
                    query = query.order_by(CosmonautModel.Date.desc())
            except AttributeError as e:
                print("Invalid order type from user. Data are not ordered.")

        if filter.limit:
            query = query.limit(filter.limit)

        return query.all()
    
    def create(self, cosmonaunt: CosmonautModel) -> bool:
        try:
            self.db.add(cosmonaunt)
            self.db.commit()
            return True
        except Exception:
            return False
        
    def delete(self, cosmonaunt_id: int) -> int:
        deleted_rows = (
                self.db.query(CosmonautModel)
                .filter(CosmonautModel.Id == cosmonaunt_id)
                .delete()
        )
        self.db.commit()

        return deleted_rows
    
    def update(self, cosmonaunt_id: int, name: Cosmonaut) -> bool:
        selected_cosmonaunt = (
            self.db.query(CosmonautModel)
            .filter(CosmonautModel.Id == cosmonaunt_id)
            .first()
        )

        if selected_cosmonaunt:
            selected_cosmonaunt.Name = name
            self.db.commit()
            return True
        
        return False



