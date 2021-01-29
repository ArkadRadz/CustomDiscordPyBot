import os


def check_if_dir_exists(target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

def check_if_file_exists(file_path):
    return os.path.exists(file_path)
