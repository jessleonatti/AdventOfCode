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


def find_directories_with_less_than_size(
    current_directory: Directory, size, next_best_size
):
    if current_directory.has_directories():
        # Look at subdirectories
        for subdirectory in current_directory.get_directories():
            next_best_size = find_directories_with_less_than_size(
                subdirectory, size, next_best_size
            )

    current_size = current_directory.get_total_size()
    if current_size >= size and current_size <= next_best_size:
        next_best_size = current_size
    return next_best_size


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

    total_storage = 70000000
    total_used = root.get_total_size()
    total_unused = total_storage - total_used
    size_for_update = 30000000
    space_needed = size_for_update - total_unused

    # Find smallest directory to be deleted to meet the space needed
    next_best_size = find_directories_with_less_than_size(
        root, space_needed, total_used
    )
    print(f"next best size: {next_best_size}")


if __name__ == "__main__":
    main()
