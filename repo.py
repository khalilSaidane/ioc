class BaseRepo:
    def __init__(self, db):
        self.db = db


class RepoName(BaseRepo):

    def get_name(self):
        return "khalil"


class RepoAge(BaseRepo):

    def get_age(self):
        return 24
