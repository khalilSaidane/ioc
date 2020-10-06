from fastapi import Depends, FastAPI

from dependencies import get_service
from service import Service

app = FastAPI()


@app.get("/items/")
async def read_query(service: Service = Depends(get_service(Service))):
    return {
        "name": service.get_name(),
        "age": service.get_age()
    }
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)