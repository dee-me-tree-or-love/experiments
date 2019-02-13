class Path:
    def __init__(self, path=[], source=None, target=None):
        self.path = path
        self.source = source
        self.target = target

    def get_path(self):
        return self.path

    def is_reached(self):
        return self.path is not None

    def __str__(self):
        return "(%s)\n from %s\n to %s" % (
            list(map(lambda s: str(s), self.path)),
            str(self.source),
            str(self.target)
        )
