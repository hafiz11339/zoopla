from fastapi import  FastAPI
from routers import sold_properties,fetch_properties,suggestion,properties_for_sale,properties_details
app = FastAPI()
import uvicorn
app.include_router(sold_properties.router,prefix="/api/soldProperties",
    tags=["properties"]
    
    )
app.include_router(fetch_properties.router, prefix="/api/fetchProperties",
                   tags=["properties"]

                   )

app.include_router(suggestion.router, prefix="/api/getSuggestion",
                   tags=["suggestions"]

                   )


app.include_router(properties_for_sale.router, prefix="/api/getPropertiesForSale",
                   tags=["forSale"]

                   )

app.include_router(properties_details.router, prefix="/api/getDetailOfProperties",
                   tags=["propertyDetails"]

                   )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



