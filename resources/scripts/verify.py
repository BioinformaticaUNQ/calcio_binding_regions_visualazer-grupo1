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
            "response": "OK: PDB file is correct"
        }))
    except:
        print(json.dumps({
            "code":204,
            "response":"ERROR: The PDB format is not correct"
        }))
except:
    print(json.dumps({
        "code":204,
        "response":"ERROR: You must enter the path of the PDB"
    }))
