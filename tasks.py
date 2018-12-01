from invoke import task

from src.tasks.new_project.project import Project
from src.tasks.new_project.validation import Validator
from src.tasks.new_project.git_manager import GitManager
from src.tasks.new_project.readme_editor import ReadmeEditor
from src.tasks.new_project.project_registry import ProjectRegistry


def add_new_project_information_to_readme(c, project):
    readme_lines = ReadmeEditor.get_file_lines()
    readme_lines = ProjectRegistry.add_project_to_lines(project, readme_lines)
    ReadmeEditor.write_file_lines(readme_lines)

    GitManager.add_readme(c)
    GitManager.commit(c)
    GitManager.push(c)


@task(help={'name': 'the name of a new project'})
def new_project(c, name):
    """
    Initialize new project in the experiments repo
    """
    Validator.validate_project_name(name)
    project = Project(name)

    GitManager.create_new_branch(c, project.branch_name)

    add_new_project_information_to_readme(c, project)

    GitManager.switch_to_branch(c, project.branch_name)

    c.run("echo \"heyo %s\"" % project)
