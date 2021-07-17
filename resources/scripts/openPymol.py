import json
import os
import sys

import pymol
from Bio.PDB import PDBParser

from parse_foldx import parse_file_foldx

from pymol import cmd

strict_parser = PDBParser(PERMISSIVE=0)

# Call the function below before using any PyMOL modules.

# THIS DOES NOT WORK ON macOS
pymol.finish_launching()

# Now we can import cmd

path = sys.argv[1]

# Es necesario ejecutar previamente get_fold_data
# data = get_fold_data(path)
ROOT_DIR_TO = os.path.dirname(os.path.abspath(__file__))[:-17]
data = parse_file_foldx(open(ROOT_DIR_TO + "predict_output.txt", "r"))

# Se puede dejar estos parametros como variables en una funcion para que queden a criterio del usuario.
amstrom = "5"
color = "red"

try:

    try:
        myPDB = strict_parser.get_structure('name', path)
        cmd.load(path)
        for i in data:
            cmd.color(color, "byres all within " + amstrom + " of resi " + str(i["number"]))

    except Exception as e:
        print(e)

except:
    print(json.dumps({
        "code": 204,
        "response": "ERROR: You must enter the path of the PDB"
    }))
