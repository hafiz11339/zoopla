from fastapi import FastAPI
from routers import sold_properties, fetch_properties, suggestion, properties_for_sale, properties_details

app = FastAPI()
import uvicorn
from routers import api_router

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
