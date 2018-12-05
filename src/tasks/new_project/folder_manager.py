import os


class FolderManager:

    @classmethod
    def create_directory(cls, dir_name):
        try:
            os.mkdir(dir_name)

        except OSError:
            print("Could not create new directory \"%s\"" % dir_name)

        else:
            print("Created new directory \"%s\"" % dir_name)
