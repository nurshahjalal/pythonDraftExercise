import os

filename = os.path.dirname(os.path.realpath(__file__))
print(filename)

files = os.path.join(filename, "..", "differentDirectory","anotherDirectory", "another.json" )
print(files)

with open(files) as f:
    print(f.read())