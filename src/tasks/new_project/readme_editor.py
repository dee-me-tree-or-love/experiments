class ReadmeEditor:

    __README_FILE_NAME = "README.md"

    @classmethod
    def get_file_lines(cls):
        f = open(cls.__README_FILE_NAME, "r")
        lines = f.readlines()
        f.close()
        cls.__output_progress_message(
            "got all lines of %s" % cls.__README_FILE_NAME
        )
        return lines

    @classmethod
    def write_file_lines(cls, lines):
        f = open(cls.__README_FILE_NAME, "w")
        lines = "".join(lines)
        f.write(lines)
        f.close()
        cls.__output_progress_message(
            "wrote all lines to %s" % cls.__README_FILE_NAME
        )

    @classmethod
    def __output_progress_message(cls, message):
        print(message)


if __name__ == '__main__':
    print(ReadmeEditor.get_file_lines())
    ReadmeEditor.write_file_lines(["test"])
