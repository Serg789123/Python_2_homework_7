__all__ = ['gen_name']

from random import randint, choice
from pathlib import Path

MIN_VALUE = 4
MAX_VALUE = 7
VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'

def gen_name(str_counts: int, file_name: str | Path) -> None:
    with open(file_name, 'a', encoding='UTF-8') as f:
        for _ in range(str_counts):
            name = ''
            flag = choice([-1, 1])
            for _ in range(randint(MIN_VALUE, MAX_VALUE)):
                if flag == -1:
                    name += choice(CONSONANTS)
                else:
                    name += choice(VOWELS)
                flag *= -1
            f.write(name.title() + '\n')

if __name__ == '__main__':
    gen_name(10, Path('names.txt'))
