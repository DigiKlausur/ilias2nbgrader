import os
from shutil import copy

def copyfiles(src, dst):
    for root, dirs, files in os.walk(src):
        dst_root = os.path.relpath(root, start=src)
        for file in files:
            os.makedirs(os.path.join(dst, dst_root), exist_ok=True)
            copy(os.path.join(root, file), os.path.join(dst, dst_root, file))
        for d in dirs:
            os.makedirs(os.path.join(dst, dst_root, d), exist_ok=True)