import os
import sys
from shutil import copyfile

path = sys.argv

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
copyfile(path[1], ROOT_DIR+'/temp/input.pdb')
