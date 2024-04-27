from fastapi import APIRouter

from routers import sold_properties, fetch_properties, suggestion, properties_for_sale, properties_details

api_router = APIRouter()
api_router.include_router(sold_properties.router, prefix="/soldProperties",
                          tags=["properties"]

                          )
api_router.include_router(fetch_properties.router, prefix="/fetchProperties",
                          tags=["properties"]

                          )

api_router.include_router(suggestion.router, prefix="/getSuggestion",
                          tags=["suggestions"]

                          )

api_router.include_router(properties_for_sale.router, prefix="/getPropertiesForSale",
                          tags=["forSale"]

                          )

api_router.include_router(properties_details.router, prefix="/getDetailOfProperties",
                          tags=["propertyDetails"]

                          )
