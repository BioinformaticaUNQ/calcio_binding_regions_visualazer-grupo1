import json
import sys

import pymol
from Bio.PDB import PDBParser

from foldx import get_fold_data

strict_parser = PDBParser(PERMISSIVE=0)

# Call the function below before using any PyMOL modules.

# THIS DOES NOT WORK ON macOS
pymol.finish_launching()

# Now we can import cmd

from pymol import cmd

path = sys.argv[1]
data = get_fold_data(path)
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
