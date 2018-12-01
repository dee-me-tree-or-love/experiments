class ReadmeEditor: 
    
    __README_FILE_NAME = "README.md"

    @classmethod
    def get_file_lines(cls):
        f = open(cls.__README_FILE_NAME, "r")
        lines = f.readlines()
        f.close()
        return lines

    @classmethod
    def write_file_lines(cls, lines):
        f = open(cls.__README_FILE_NAME, "w")
        lines = "".join(lines)
        f.write(lines)
        f.close()


if __name__ == '__main__':
    print(ReadmeEditor.get_file_lines())
    ReadmeEditor.write_file_lines(["test"])
    