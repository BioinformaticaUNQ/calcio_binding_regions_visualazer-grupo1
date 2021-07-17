import shutil
import os

dirPath = 'temp'
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR_TO_DELETE = os.path.dirname(os.path.abspath(__file__))[:-17]
try:
    shutil.rmtree(ROOT_DIR+"/"+dirPath)
except OSError as e:
    print(f"Error:{e.strerror}")

for e in ["CA_MB_input.pdb", "metal_orphan.txt", "MB_input.fxout", "predict_output.txt", "input.pdb"]:
    if os.path.exists(ROOT_DIR_TO_DELETE + e):
        os.remove(ROOT_DIR_TO_DELETE + e)

try:
    os.mkdir(ROOT_DIR+"/"+dirPath)

except OSError as e:
    print(f"Error:{e.strerror}")
