
# read a file from different directory using realtive path

import os, sys, pathlib

dirname = os.path.dirname(__file__)
print(dirname)
file_loc = "differentDirectory/anotherDirectory/another.json"

filename = os.path.join(dirname,file_loc)
print(filename)

with open(filename) as f:
    txt = f.read()
    print(txt)