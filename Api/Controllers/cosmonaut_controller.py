import json

from typing import List
from typing_extensions import Annotated
from fastapi import Depends, Body

from Api.Enums.Api.query_order_type import OrderDBType
from Api.Encoders.json_encoder import CustomDatetimeEncoder
from Api.Filters import CosmonautFilterQuery
from Api.Models import Cosmonaut
from Shared.DataAccess.Models import CosmonautModel
from Shared.DataAccess.Services.cosmonaut_service import CosmonautService

class CosmonautAPI:
    def __init__(self, cosmonaut_service: CosmonautService):
        self.cosmonaunt_service = cosmonaut_service()

    async def get_cosmonauts(self, filter: Annotated[CosmonautFilterQuery, Depends(CosmonautFilterQuery)]) -> List[dict]:
        cosmonauts : List[CosmonautModel] = self.cosmonaunt_service.get(filter)
        
        try:
            ordered_by_info = f"Ordering DB: {OrderDBType(filter.order_type).name}"
        except Exception:
            ordered_by_info = "Invalid order type. Use either 1 as ASC or 2 as DESC"

        if cosmonauts:
            json_cosmonaunts = [cosm.to_dict() for cosm in cosmonauts]

        return {"message": f"CosmountAPI, limiting:{filter.limit}, {ordered_by_info}",
                 "data": json.dumps(json_cosmonaunts, cls=CustomDatetimeEncoder, separators=(',', ':'))
                }

    async def create_cosmonaut(self, cosmonaut: Cosmonaut) -> bool:
        new_cosmonaut = CosmonautModel.from_validation_model(cosmonaut)
        is_created = self.cosmonaunt_service.create(new_cosmonaut)
        return {"created": is_created}

    async def delete_cosmonaut(self, cosmonaunt_id: int):
        deleted_rows = self.cosmonaunt_service.delete(cosmonaunt_id)
        return {"message": f"Deleted cosmonaunts: {deleted_rows}", "IsDeleted": deleted_rows > 0}
    
    async def update_cosmonaut(self, cosmonaunt_id: int, name: Cosmonaut = Body(..., description="Rename cosmounat for specific ID.")):
        is_updated = self.cosmonaunt_service.update(cosmonaunt_id, name)
        return {"IsUpdated": is_updated}