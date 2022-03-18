from typing import List
from lib.model import *
from os import listdir
from os.path import isfile, join

import music_tag



def get_files_from_dir(dir:str) -> List:

    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
    return onlyfiles


def try_read():
    file_list = get_files_from_dir(TEST_DIR)

    for i in file_list:
        f = music_tag.load_file(".\\test_folder\\1.flac")

        # dict access returns a MetadataItem
        title_item = f['title']

        # MetadataItems keep track of multi-valued keys
        title_item.values  # -> ['440Hz']

        # A single value can be extracted
        title_item.first  # -> '440Hz'
        title_item.value  # -> '440Hz'

    # MetadataItems can also be cast to a string
    str(title_item)  # -> '440Hz'


if __name__ == '__main__':
    get_dir()