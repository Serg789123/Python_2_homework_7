__all__ = ['rename']


import os
from pathlib import Path


def rename(new_name: str, count_len: int, old_extension: str, new_extension: str, interval: list[int]):
    count = 0
    for file in os.listdir():
        if file.endswith(old_extension):
            count += 1
            Path(file).rename(f"{file.split('.')[0][interval[0]:interval[1]]}{new_name}{count:0>{count_len}}.{new_extension}")

if __name__ == '__main__':
    rename('_new', 2, 'csv', 'txt',[1, 4])