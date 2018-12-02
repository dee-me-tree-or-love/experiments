class GitManager:

    @classmethod
    def create_new_branch(cls, c, branch_name):
        """
        Creates the new branch with given name using the provided command runner
        """
        command = cls.__get_create_new_branch_command(branch_name)
        c.run(command)

    @classmethod
    def switch_to_branch(cls, c, branch_name):
        """
        Switches to branch with given name using the provided command runner
        """
        command = cls.__get_switch_to_branch_command(branch_name)
        c.run(command)

    @classmethod
    def add_readme(cls, c):
        """
        Adds the readme file to the staged index
        """
        command = cls.__get_add_readme_command()
        c.run(command)

    @classmethod
    def commit(cls, c, message):
        """
        Commits the changes in the index
        """
        command = cls.__get_commit_changes_command(message)
        c.run(command)

    @classmethod
    def push(cls, c):
        """
        Push the changes to the remote
        """
        command = cls.__get_push_command()
        c.run(command)

    @classmethod
    def __get_create_new_branch_command(cls, branch_name):
        command = "git branch %s" % branch_name
        print(command)
        return command

    @classmethod
    def __get_switch_to_branch_command(cls, branch_name):
        command = "git checkout %s" % branch_name
        print(command)
        return command

    @classmethod
    def __get_add_readme_command(cls):
        command = "git add README.md"
        print(command)
        return command

    @classmethod
    def __get_commit_changes_command(cls, message):
        command = "git commit -m \"%s\"" % message
        print(command)
        return command

    @classmethod
    def __get_push_command(cls):
        command = "git push"
        print(command)
        return command
