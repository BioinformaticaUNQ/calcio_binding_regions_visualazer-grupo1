import os
import sys

path = sys.argv[1]

os.system("./foldx/foldx --output-dir=./temp/ --command=MetalBinding --metal=-PREDICT --metal_element=CA --pdb=" + path)
