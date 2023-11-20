def create_file_with_size(filename,size_in_bytes):
    with open(filename,"wb") as file:
        file.write(b'\0'*size_in_bytes)
import os

curr_dir=os.getcwd()
"""
with open("day7/d7_1.txt") as file:
    os.chdir("D:\\test")
    for line in file:
        line=line.rstrip().split()
        if line[1]=="cd":
            os.chdir(f'{os.getcwd()}\\{line[2]}')
        elif line[0]=="dir":
            os.mkdir(line[1])
        elif line[0].isnumeric():
            create_file_with_size(line[1],int(line[0]))
"""
os.chdir("D:\\test")
def get_dir_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        # Size of files in this directory
        total_size += sum(os.path.getsize(os.path.join(dirpath, name)) for name in filenames if not os.path.islink(os.path.join(dirpath, name)))
    return total_size


def iterate_directory(path):
    total=0
    for dirpath, dirnames, filenames in os.walk(path):
        dir_size = get_dir_size(dirpath)
        print(dirpath, dir_size)
        if dir_size<=100000:
            total+=dir_size
    return total

# Example usage

""" part 1 solution print(iterate_directory(os.getcwd()))"""

base=70000000-get_dir_size(os.getcwd())
need=30000000
def iterate_directory_part2(path):
    mini=float("inf")
    for dirpath, dirnames, filenames in os.walk(path):
        dir_size = get_dir_size(dirpath)
        if base+dir_size>=need:
            mini=min(dir_size,mini)
            print(dir_size)
    return mini

"""part 2 solution print(iterate_directory_part2(os.getcwd()))"""