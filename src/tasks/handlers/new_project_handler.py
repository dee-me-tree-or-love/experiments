
from src.tasks.new_project.project import Project
from src.tasks.new_project.validation import Validator
from src.tasks.new_project.git_manager import GitManager
from src.tasks.new_project.readme_editor import ReadmeEditor
from src.tasks.new_project.project_registry import ProjectRegistry


class NewProjectHandler:
    def __init__(self, c, project_name):
        self.command_runner = c
        self.project_name = project_name

    def handle(self):
        """
        Initialize new project in the experiments repo.
        """

        project = self.prepare_project_object(self.project_name)

        self.create_new_project_branch(project)
        self.add_new_project_information_to_readme(project)
        self.stage_readme_changes()
        self.commit_readme_changes(project)

        self.announce_new_project_ready(project)

    def prepare_project_object(self, project_name):
        """
        Validates the project name and returns the new Project object.
        Throws the validation error if something is wrong
        """
        Validator.validate_project_name(project_name)
        project = Project(project_name)

        return project

    def create_new_project_branch(self, project):
        """
        Creates a new branch using the project's branch name
        """
        GitManager.create_new_branch(self.command_runner, project.branch_name)

    def add_new_project_information_to_readme(self, project):
        """
        Adds the new line to the readme with the project
        """
        readme_lines = ReadmeEditor.get_file_lines()
        readme_lines = ProjectRegistry.add_project_to_lines(
            project, readme_lines
        )
        ReadmeEditor.write_file_lines(readme_lines)

    def stage_readme_changes(self):
        GitManager.add_readme(self.command_runner)

    def commit_readme_changes(self, project):
        GitManager.commit(self.command_runner, "new project %s" % project.name)

    def announce_new_project_ready(self, project):
        """
        Writes the post-handling messages to the console
        """
        self.__output_console_message("------")
        self.__output_console_message(
            "Succesfully prepared \"%s\"" % project.name
        )
        self.__output_console_message(
            "Feel free to edit the README.md file to add more information"
        )
        self.__output_console_message(
            "When ready to start working, checkout the new branch \"%s\"" % project.branch_name
        )

    def __output_console_message(self, message):
        self.__run_command("echo \"%s\"" % message)

    def __run_command(self, command):
        self.command_runner.run(command)
