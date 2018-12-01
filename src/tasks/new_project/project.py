class Project:
    __BRANCH_PREFIX = "exp-"

    def __init__(self, name):
        self.name = name
        self.branch_name = self.__get_branch_format(name)

    def __get_branch_format(self, name):
        return "%s%s" % (self.__BRANCH_PREFIX, name)

    def __str__(self):
        return '%s @ %s' % (self.name, self.branch_name)