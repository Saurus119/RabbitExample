from fastapi import APIRouter

from Api.Controllers.cosmonaut_controller import CosmonautAPI
from Shared.DataAccess.Services.cosmonaut_service import CosmonautService

# init objects so I can refer to their instance methods to register them with API.
cosmonaut_api = CosmonautAPI(CosmonautService)


def register_routes(router: APIRouter):
    "Register all routes for api."
    router.add_api_route("/cosmonauts", cosmonaut_api.get_cosmonauts, methods=["GET"])
    router.add_api_route("/cosmonauts", cosmonaut_api.create_cosmonaut, methods=["POST"])
    router.add_api_route("/cosmonauts/{cosmonaunt_id}", cosmonaut_api.delete_cosmonaut, methods=["DELETE"])
    router.add_api_route("/cosmonauts/{cosmonaunt_id}", cosmonaut_api.update_cosmonaut, methods=["PATCH"])
    return router