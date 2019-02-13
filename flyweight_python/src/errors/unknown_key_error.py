class UnknownKeyError(Exception):

    _MESSAGE_PATTERN = "Attempted to get unknown key: "

    def __init__(self, key):

        message = self._prepare_message(key)

        super().__init__(message)
        self.key = key

    def _prepare_message(self, key):
        return "%s %s" % (self._MESSAGE_PATTERN, key)
