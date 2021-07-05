import sys
import json

from Bio.PDB import *

strict_parser = PDBParser(PERMISSIVE=0)
myPDB = None

try:
    path = sys.argv[1]
    try:
        myPDB = strict_parser.get_structure('name', path)
        print(json.dumps({
            "code":200,
            "response": myPDB
        }))
    except:
        print(json.dumps({
            "code":204,
            "response":"ERROR: El formato del PDB no es correcto"
        }))
except:
    print(json.dumps({
        "code":204,
        "response":"ERROR: Debe ingresar path del PDB"
    }))
