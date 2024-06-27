__all__ = ['gen_files']

from random import choices, randint
from string import ascii_lowercase, digits

def gen_files(ext: str, min_name: int=6, max_name: int=30, min_size: int=256,
              max_size: int=4096, file_count: int=42) -> None:
    for _ in range(file_count):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
        data_bytes = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data_bytes)

if __name__ == '__main__':
    gen_files('bin', 6, 10, 256, 4096, 5)
