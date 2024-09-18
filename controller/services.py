from models import *

class ProjectService:
    def __init__(self, repository):
        self.repository = repository

    def create_project(self, name, description):
        project = Project(name, description)
        self.repository.save(project)
        return project

    def get_all_projects(self):
        return self.repository.get_all()
