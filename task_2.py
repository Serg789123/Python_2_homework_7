""" Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами."""

from package.modul_gen_different_file import gen_different_file
from package.modul_gen_name import gen_name
from package.modul_rename import rename
from package.modul_gen_files import gen_files
from package.modul_write_file import write_file
from package.modul_sort_files import sort_files
from package.modul_read_oll_begin import read_oll_begin
from package.modul_num_files import num_files



if __name__ == '__main__':
    rename('_new', 2, 'txt', 'csv', [1, 4])