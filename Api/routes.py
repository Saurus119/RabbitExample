from fastapi import APIRouter
from fastapi.openapi.docs import get_swagger_ui_html

from Api.Controllers.cosmonaut_controller import CosmonautAPI
from Api.Controllers.rabbit_test_controller import RabbitTestController
from Shared.DataAccess.Services.cosmonaut_service import CosmonautService
from Shared.Rabbit_MQ.config import MessageExchangeClient

# init objects so I can refer to their instance methods to register them with API.
cosmonaut_api = CosmonautAPI(CosmonautService)
rabbit_api = RabbitTestController(MessageExchangeClient)

def register_routes(router: APIRouter):
    "Register all routes for api."
    router.add_api_route("/docs", get_swagger_ui_html(openapi_url="openapi.json", title="FastAPI - Swagger UI"), include_in_schema=False)

    router.add_api_route("/cosmonaunt", cosmonaut_api.get_cosmonauts, methods=["GET"])
    router.add_api_route("/cosmonaunt", cosmonaut_api.create_cosmonaut, methods=["POST"])
    router.add_api_route("/cosmonaunt/{cosmonaunt_id}", cosmonaut_api.delete_cosmonaut, methods=["DELETE"])
    router.add_api_route("/cosmonaunt/{cosmonaunt_id}", cosmonaut_api.update_cosmonaut, methods=["PATCH"])

    router.add_api_route("/publish", rabbit_api.get, methods=["GET"])    
    return router