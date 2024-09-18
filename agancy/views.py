from controller.services import ProjectService
from agancy.repositories import ProjectRepository

repository = ProjectRepository()
service = ProjectService(repository)

def create_project_view(name, description):
    project = service.create_project(name, description)
    print(f'Проект "{project.name}" создан с описанием: {project.description}')

def list_projects_view():
    projects = service.get_all_projects()
    for project in projects:
        print(f'Проект: {project.name}, Описание: {project.description}')
