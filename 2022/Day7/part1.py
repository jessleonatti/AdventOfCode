from directory import Directory


def change_directory(
    directory_name: str, current_directory: Directory, root: Directory
):
    if directory_name == "..":
        # Get parent directory
        return current_directory.get_parent_directory()

    if directory_name == "/":
        # Go to root directory
        return root

    # Go to subdirectory
    return current_directory.get_directory(directory_name)


def find_directories_with_less_than_size(current_directory: Directory, size):
    directories = []
    if current_directory.has_directories():
        # Look at subdirectories
        for subdirectory in current_directory.get_directories():
            subdirectories = find_directories_with_less_than_size(subdirectory, size)
            directories.extend(subdirectories)

    current_size = current_directory.get_total_size()
    if current_size <= size:
        directories.append(current_size)
    return directories


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    root = Directory("root")
    current_directory = root
    # Load file system
    for line in lines:
        line = line.strip()
        if line.startswith("$ cd"):
            # cd
            directory_name = line.split(" ")[2]
            current_directory = change_directory(
                directory_name, current_directory, root
            )
        elif line == "$ ls":
            pass
        elif line.startswith("dir"):
            # Directory
            name = line.split(" ")[1]
            current_directory.add_directory(name)
        else:
            # File
            file_size, file_name = line.split(" ")
            current_directory.add_file(file_name, file_size)

    # Find directories with size of at most 100,000
    directories = find_directories_with_less_than_size(root, 100000)
    print(f"total: {sum(directories)}")


if __name__ == "__main__":
    main()
