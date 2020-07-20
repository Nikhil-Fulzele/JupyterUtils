import os
import argparse

from load_dependencies_magic.utils import download_files


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


cell_parser = argparse.ArgumentParser(add_help=True)
cell_parser.add_argument('--alias', type=str, required=False)
cell_parser.add_argument('--override', default=False, type=str2bool, required=False)


def parse_cell(cell_info):

    load_nbloader = False
    buf = cell_info.getvalue().strip().split('\n')

    for line in buf:

        line = line.split()
        file_path = line[0]
        file_ext = file_path.split('.')[-1]

        args = cell_parser.parse_args(line[1:])
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

        download_files(file_path, alias)
        if file_ext == 'ipynb':
            load_nbloader = True

    return load_nbloader
