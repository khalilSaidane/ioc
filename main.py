from typing import Optional

from fastapi import Cookie, Depends, FastAPI

from dependencies import get_service
from service import Service

app = FastAPI()


@app.get("/items/")
async def read_query(service: Service = Depends(get_service(Service))):
    return {
        "name": service.get_name(),
        "age": service.get_age()
    }
