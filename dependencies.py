from typing import Type, List

from fastapi import Depends

from repo import BaseRepo
from service import BaseService


def get_db():
    return "db"


def get_repository(*repos):
    print("-" * 50, repos)

    def _get_repo(session: str = Depends(get_db)):
        """

        :param session:
        :return: List of instantiated repositories that will be injected in the service
        """
        instantiated_repositories = []
        for repo in repos:
            instantiated_repositories.append(repo(session))
        return instantiated_repositories

    return _get_repo


def get_service(service_type: Type[BaseService]):
    def _get_service(repos: Type[List[BaseRepo]] = Depends(get_repository(*service_type.repos))):
        print("*" * 50, repos)
        return service_type(*repos)

    return _get_service
