class ProjectRepository:
    def __init__(self):
        self.projects = []

    def save(self, project):
        self.projects.append(project)

    def get_all(self):
        return self.projects
