import os
import parse_foldx
import clear


def get_fold_data(path):
    clear
    os.system("./foldx/foldx --output-dir=./temp/ --command=MetalBinding --metal=-PREDICT --metal_element=CA --pdb=" + path)
    return parse_foldx.parse_file_foldx(open("./temp/predict_output.txt", "r"))
