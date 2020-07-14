import os
import sys
import argparse

from IPython.core.magic import register_line_cell_magic
from io import StringIO

from load_ipynb_local import NotebookFinder
from utils import download_files

ACCEPTED_FILE_EXT = ['ipynb', 'csv', 'py', 'txt']


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


parser_cell = argparse.ArgumentParser(add_help=True)
parser_cell.add_argument('--alias', type=str, required=False)
parser_cell.add_argument('--override', default=False, type=str2bool, required=False)

parse_line = argparse.ArgumentParser(add_help=True)
parser_cell.add_argument('--remote', default="", type=str, required=False)


def parse_cell(cell_info):
    load_nbloader = False
    buf = cell_info.getvalue().strip().split('\n')
    for line in buf:

        line = line.split()
        file_path = line[0]
        file_ext = file_path.split('.')[-1]
        if file_ext not in ACCEPTED_FILE_EXT:
            raise Exception(f"Illegal file type : {file_ext}. Currently it supports only .ipynb, .csv, .py and .txt")

        args = parser_cell.parse_args(line[1:])
        params = vars(args)
        alias = file_path.split('/')[-1] if not params['alias'] else params['alias']

        is_file_name_exists = os.path.isfile(alias)

        if is_file_name_exists and not params['override']:
            print(f"Skipping file with name {alias} since it already exists and override is False.")
        else:
            if is_file_name_exists:
                print(f"Loading {file_path} and overriding the existing file with name {alias}")
            else:
                print(f"Loading {file_path} and saving it as {alias}")

        download_files(file_path, alias, file_type=file_ext)
        if file_ext == 'ipynb':
            load_nbloader = True

    return load_nbloader


@register_line_cell_magic
def load_dependencies(line, cell=None):
    if not line:
        load_nbloader = True
    else:
        sio = StringIO(cell)
        load_nbloader = parse_cell(sio)

    if load_nbloader:
        sys.meta_path.append(NotebookFinder())

