import os
import sys
import parse_foldx

path = sys.argv[1]

os.system("./foldx/foldx --output-dir=./temp/ --command=MetalBinding --metal=-PREDICT --metal_element=CA --pdb=" + path)

print(parse_foldx.parse_file_foldx(open("./temp/predict_output.txt", "r")))
