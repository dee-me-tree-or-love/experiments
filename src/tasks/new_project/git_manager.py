class GitManager:

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
    def __get_add_readme_command(cls, branch_name):
        command = "git add README.md"
        print(command)
        return command

    @classmethod
    def __get_commit_changes_command(cls, branch_name):
        command = "git commit"
        print(command)
        return command

    @classmethod
    def __get_push_command(cls, branch_name):
        command = "git push"
        print(command)
        return command


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
        command = cls.__get_add_readme_command(branch_name)
        c.run(command)

    @classmethod
    def commit(cls, c):
        """
        Commits the changes in the index
        """
        command = cls.__get_commit_changes_command(branch_name)
        c.run(command)

    @classmethod
    def push(cls, c):
        """
        Push the changes to the remote
        """
        command = cls.__get_push_command(branch_name)
        c.run(command)
