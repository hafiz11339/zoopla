from fastapi import Depends, FastAPI
from routers import sold_properties
app = FastAPI()
import uvicorn
app.include_router(sold_properties.router,prefix="/api/soldProperties",
    tags=["properties"]
    
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



