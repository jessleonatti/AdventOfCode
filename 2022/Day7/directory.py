class Directory:
    def __init__(self, name, parent=None):
        self._name = name
        self._parent = parent
        self._files = []
        self._directories = {}

    def get_name(self):
        return self._name

    def get_parent_directory(self):
        return self._parent

    def has_directories(self):
        return not self._directories == {}

    def get_directory(self, name):
        return self._directories[name]

    def get_directories(self):
        return self._directories.values()

    def add_directory(self, name):
        self._directories[name] = Directory(name=name, parent=self)

    def add_file(self, file_name, file_size):
        self._files.append(File(file_name, file_size))

    def get_total_size(self):
        total_file_size = sum([int(file.size) for file in self._files])
        total_directories_size = sum(
            [
                int(directory.get_total_size())
                for directory in self._directories.values()
            ]
        )
        return total_file_size + total_directories_size


class File:
    def __init__(self, name, file_size):
        self.name = name
        self.size = file_size
