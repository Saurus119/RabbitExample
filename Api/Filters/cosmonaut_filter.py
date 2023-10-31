from pydantic import BaseModel
from fastapi import Query
from typing import Optional

class CosmonautFilterQuery(BaseModel):
    limit: Optional[int] = Query(None, description="Limit the number of results")
    order_type: Optional[int] = Query(None, description="Order type represented as 0 or 1 (e.g., ascending or descending)")
