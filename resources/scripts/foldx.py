import os
import sys
import shutil

path = sys.argv[1]

dirPath = 'temp'

try:
    shutil.rmtree(dirPath)
except OSError as e:
    print(f"Error:{e.strerror}")

try:
    os.mkdir(dirPath)

except OSError as e:
    print(f"Error:{e.strerror}")

os.system("./foldx/foldx --output-dir=./temp/ --command=MetalBinding --metal=-PREDICT --metal_element=CA --pdb=" + path)

