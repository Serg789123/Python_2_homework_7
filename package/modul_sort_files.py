__all__ = ['modul_sort_files', 'modul_gen_different_file']


from pathlib import Path
from random import choices, randint
from string import ascii_lowercase, digits
import os

def sort_files(path: str | Path, groups: dict[str: list[str]]=None) -> None:
    if not groups:
        groups = {
        Path('video'): ['avi', 'mov', 'mp4', 'mkv'],
        Path('images'): ['bmp', 'jpeg', 'jpg', 'png']
        }
    os.chdir(path)
    reverse_groups = {}
    for target_dir, ext_list in groups.items():
        if not target_dir.is_dir():
             target_dir.mkdir()
        for ext in ext_list:
            reverse_groups[f'.{ext}'] = target_dir
    print(reverse_groups)
    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups:
            file.replace(reverse_groups[file.suffix] / file.name)

def gen_files(ext: str, min_name: int=6, max_name: int=30, min_size: int=256,
              max_size: int=4096, file_count: int=42) -> None:
    for _ in range(file_count):
        while True: # безконечный цикл
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
    gen_different_file('directori', avi=2, doc=4, bin=3, jpg=5, mkv=6, png=3)
    sort_files(Path(r'Absolute Path'))
