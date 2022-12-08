from dataclasses import dataclass
from typing import List, Optional, Union, Dict


@dataclass
class Directory:
    path: str
    children: List[Union["Directory", "File"]]


@dataclass
class File:
    path: str
    size: int


def calculate_size(item: Union[Directory, File], limit: Optional[int] = None) -> int:
    if type(item) == File:
        return item.size
    size = 0
    for child in item.children:
        size += calculate_size(child)
        if limit and size > limit:
            return 0
    return size


def calculate_size_2(paths: Dict[str, Union[Directory, File]], limit: Optional[int] = None) -> int:
    size = 0
    for item in paths.values():
        if type(item) == Directory:
            dsize = calculate_size(item)
            if limit and dsize <= limit:
                size += dsize
    return size


def calculate_space_3(paths: Dict[str, Union[Directory, File]]) -> Dict[str, int]:
    dirs = {}
    for item in paths.values():
        if type(item) == Directory:
            dirs[item.path] = calculate_size(item)
    dirs = dict(sorted(dirs.items(), key=lambda x: x[1]))
    return dirs



def process_comands(comands: List[str]) -> Dict[str, Union[Directory, File]]:
    paths = {}
    current_path = "/"
    for comand in comands:
        comand = comand.split(" ")
        if comand[0] == "$":
            if comand[1] == "cd":
                if comand[2] == "..":
                    current_path = "/".join(current_path.split("/")[0:-1])
                else:
                    current_path = f"{current_path}/{comand[2]}" if comand[2] != "/" else current_path
                    current_path = current_path.replace("//", "/")

                    if current_path not in paths:
                        paths[current_path] = Directory(path=current_path, children=[])
            else:
                continue  # no op on ls
        else:
            # dir x or <size> x
            tmp_current_path = f"{current_path}/{comand[1]}"
            tmp_current_path = tmp_current_path.replace("//", "/")

            if comand[0] == "dir":
                item = Directory(path=tmp_current_path, children=[])
            else:
                item = File(path=tmp_current_path, size=int(comand[0]))
            paths[current_path].children.append(item)
            paths[tmp_current_path] = item

    return paths


def select_folder_to_delete(dirs_sizes: Dict[str, int], space_to_free: int) -> int:
    for dirs_size in dirs_sizes.values():
        if dirs_size >= space_to_free:
            return dirs_size


if __name__ == "__main__":
    comands = open("src/day7/input").read().split("\n")
    paths = process_comands(comands)
    print(calculate_size_2(paths, limit=100000))
    disk_size = 70000000
    required_space = 30000000
    used_space = calculate_size(paths["/"])
    free_space = disk_size - used_space
    space_to_free = required_space - free_space
    dirs_w_space = calculate_space_3(paths)
    print(select_folder_to_delete(dirs_w_space, space_to_free))


