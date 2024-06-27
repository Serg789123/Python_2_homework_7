__all__ = ['gen_different_file']

from pathlib import Path
from random import choices, randint
from string import ascii_lowercase, digits
import os

def gen_files(ext: str, min_name: int=6, max_name: int=30, min_size: int=256,
              max_size: int=4096, file_count: int=42) -> None:
    for _ in range(file_count):
        while True:
            name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
            if not Path(f'{name}.{ext}').is_file():
                break
        data_bytes = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data_bytes)

def gen_different_file(dyr_: str | Path, **kwargs) -> None:
    if isinstance(dyr_, str):
        dyr_ = Path(dyr_)
    if not dyr_.is_dir():
        dyr_.mkdir(parents=True)
    os.chdir(dyr_)
    for ext, count in kwargs.items():
        gen_files(ext, file_count=count)

if __name__ == '__main__':
    gen_different_file('directori', txt=2, doc=4, bin=3)
