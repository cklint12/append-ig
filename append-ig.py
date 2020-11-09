import os

os.chdir(r'D:\Codes\append-ig\test-folder-master')
master = os.listdir(r'D:\Codes\append-ig\test-folder-master')
local = os.listdir(r'D:\Codes\append-ig\test-folder-local')


# For testing
def compare_test(local_dir, master_dir):
    for image_local in local:
        for image_master in master:
            if image_local == image_master:
                print(image_master)


def append_ig_dir(local_dir, master_dir):
    for image_local in local:
        for image_master in master:
            if image_local == image_master:
                append_ig(image_local)


def append_ig(file_name):
    if "ig" in file_name:
        pass
    else:
        os.rename(file_name, file_name.replace(".jpg", "-ig.jpg"))


def remove_ig_dir(directory):
    for img in directory:
        if "ig" not in img:
            pass
        else:
            os.replace(img, img.replace("-ig.jpg", ".jpg"))


remove_ig_dir(master)

# append_ig_dir(local, master)
