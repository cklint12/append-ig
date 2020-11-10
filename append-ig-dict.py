import os
import time
start_time = time.time()

os.chdir(r'D:\Codes\append-ig\test-folder-master')
master = os.listdir(r'D:\Codes\append-ig\test-folder-master')
local = os.listdir(r'D:\Codes\append-ig\test-folder-local')


def list_to_dict(directory):
    """
    A helper file that turns a list into a dictionary
    """
    dir_dict = {}
    for img in directory:
        dir_dict[img] = img
    return dir_dict


def append_ig_dir(master_dict, local_dir):
    for img in local_dir:
        if img in master_dict:
            os.rename(img, img.replace(".jpg", "-ig.jpg"))


def remove_ig_dir(directory):
    for img in directory:
        if "ig" not in img:
            pass
        else:
            os.replace(img, img.replace("-ig.jpg", ".jpg"))


# remove_ig_dir(master)


master_dir_dict = list_to_dict(master)
append_ig_dir(master_dir_dict, local)

print("--- %s seconds ---" % (time.time() - start_time))
