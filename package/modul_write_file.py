__all__ = ['write_file']

from random import randint, uniform  # uniform - для float
from pathlib import Path

MIN_NUM = -1000
MAX_NUM = 1000


def write_file(num_str: int, f_name: str | Path) -> None:
    with open(f_name, 'a', encoding='UTF_8') as f:
        for _ in range(num_str):
            f.write(f'{randint(MIN_NUM, MAX_NUM)} | {uniform(MIN_NUM, MAX_NUM)}\n')


if __name__ == '__main__':
    write_file(10, Path('numbers.txt'))
