import os
import shutil
from pathlib import Path

src_folder = 'E:/PythonProjects/yjy-python/curtis-python/file/file_dir/source_dir'
des_folder = "E:/PythonProjects/yjy-python/curtis-python/file/file_dir/target_dir"


def categorizeFile(src_folder, des_folder):
    files = os.listdir(src_folder)
    print(files)
    for file in files:
        src_path = src_folder + "/" + file
        if os.path.isfile(src_path):
            des_path = des_folder + "/" + src_path.split(".")[-1]
            if not os.path.exists(des_path):
                os.makedirs(des_path)
            shutil.move(src_path, des_path)
        else:
            categorizeFile(src_path, des_folder)


# categorizeFile(src_folder, des_folder)




