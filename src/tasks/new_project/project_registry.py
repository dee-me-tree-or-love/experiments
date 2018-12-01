class ProjectRegistry:
    """
    Keeps the records of the projects in the markdown table
    """

    __NEW_ENTRY_KEYWORD = "new_project_entry"
    __COMMENT_OPENNING = "<!--"
    __COMMENT_CLOSING = "-->"


    @classmethod
    def get_entry_placeholder(cls):
        """
        Prepares the placeholder line

        >>> ProjectRegistry.get_entry_placeholder()
        '<!-- (new_project_entry) -->'
        """
        return "%s (%s) %s" % (cls.__COMMENT_OPENNING, cls.__NEW_ENTRY_KEYWORD, cls.__COMMENT_CLOSING)


    @classmethod
    def find_placeholder_line_index(cls, text_lines):
        """
        Find the index of a line that matches the placeholder pattern

        >>> ProjectRegistry.find_placeholder_line_index([])
        Traceback (most recent call last):
          ...
        ValueError: '<!-- (new_project_entry) -->' is not in list

        >>> ProjectRegistry.find_placeholder_line_index(['<!-- (new_project_entry) -->'])
        0

        >>> ProjectRegistry.find_placeholder_line_index(['bob','<!-- (new_project_entry) -->','carla'])
        1

        """
        placeholder = cls.get_entry_placeholder()
        try:
            return text_lines.index(placeholder)
        except Exception as e:
            print(e)
            raise e


    @classmethod
    def add_project_to_lines(cls, project, text_lines):
        """
        Add the project to text lines and return the new lines

        >>> p = Project('quake')
        >>> ProjectRegistry.add_project_to_lines(p, ['bob','<!-- (new_project_entry) -->','carla'])
        ['bob', '| quake | exp-quake |\n', '<!-- (new_project_entry) -->', 'carla']

        """
        index = cls.find_placeholder_line_index(text_lines)
        registry_entry = cls.prepare_project_registry_entry(project)
        text_lines.insert(index, registry_entry)
        return text_lines


    @classmethod
    def prepare_project_registry_entry(cls, project):
        return '| %s | %s |\n' % (project.name, project.branch_name)


if __name__ == "__main__":
    import doctest
    from project import Project
    doctest.testmod()
