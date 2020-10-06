from typing import Type

from fastapi import Depends

from repo import BaseRepo
from service import BaseService


def get_db():
    return "db"


def get_repository(**kwargs):
    def _get_repo(session: str = Depends(get_db)):
        d = {}
        for key, val in kwargs.items():
            d.update({key: val(session)})
        return d

    return _get_repo


def get_service(service_type: Type[BaseService]):
    def _get_service(repo=Depends(get_repository(**service_type.repos))):
        print(repo)
        return service_type(**repo)

    return _get_service
