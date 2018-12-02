from invoke import task

from src.tasks.handlers.new_project_handler import NewProjectHandler


@task(help={'name': 'the name of a new project'})
def new_project(c, name):
    """
    Initialize new project in the experiments repo:
    1. Creates new branch for the project
    2. Adds the entry to the readme 
    3. Commits the changes to master
    """
    handler = NewProjectHandler(c, name)
    handler.handle()
