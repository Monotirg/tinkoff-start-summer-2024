def show_dir(directories, indent=0):
    sorted_directories = sorted(directories.keys())
    for directory in sorted_directories:
        print("  " * indent + directory)
        show_dir(directories[directory], indent + 1)

n = int(input())
directories = dict()
for _ in range(n):
    path = input().split('/')
    carry = directories
    for subdir in path[1:]:
        if subdir not in carry:
            carry[subdir] = dict()
        carry= carry[subdir]

directories = {path[0]: directories}
show_dir(directories)
