import os


def check_if_dir_exists(target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
