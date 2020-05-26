import os
from shutil import copy, move

def copyfiles(src, dst, exclude=[]):
    for root, dirs, files in os.walk(src):
        dst_root = os.path.relpath(root, start=src)
        for file in files:
            extension = file.split('.')[-1]
            if extension not in exclude:
                os.makedirs(os.path.join(dst, dst_root), exist_ok=True)
                copy(os.path.join(root, file), os.path.join(dst, dst_root, file))
        for d in dirs:
            os.makedirs(os.path.join(dst, dst_root, d), exist_ok=True)

def movefiles(src, dst, exclude=[]):
    for root, dirs, files in os.walk(src):
        dst_root = os.path.relpath(root, start=src)
        for file in files:
            extension = file.split('.')[-1]
            if extension not in exclude:
                os.makedirs(os.path.join(dst, dst_root), exist_ok=True)
                move(os.path.join(root, file), os.path.join(dst, dst_root, file))
        for d in dirs:
            os.makedirs(os.path.join(dst, dst_root, d), exist_ok=True)