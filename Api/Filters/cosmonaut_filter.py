from pydantic import BaseModel
from fastapi import Query

class CosmonautFilterQuery(BaseModel):
    limit: int = Query(0, description="Limit the number of results")
    order_type: int = Query(None, description="Order type represented as 0 or 1 (e.g., ascending or descending)")