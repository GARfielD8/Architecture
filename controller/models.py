class Project:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class ProjectService:
    def __init__(self, repository):
        self.repository = repository

    def create_project(self, name, description):
        project = Project(name, description)
        self.repository.save(project)
        return project
