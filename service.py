from repo import RepoAge
from repo import RepoName


class BaseService:
    repos = {}


class Service(BaseService):

    repos = {
        "repo_name": RepoName,
        "repo_age": RepoAge
    }

    def __init__(self, repo_name: RepoName, repo_age: RepoAge):
        self.repo_age = repo_age
        self.repo_name = repo_name

    def get_name(self):
        return self.repo_name.get_name()

    def get_age(self):
        return self.repo_age.get_age()
