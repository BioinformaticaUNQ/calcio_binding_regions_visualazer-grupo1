import sys
import json
import os
from shutil import copyfile

from Bio.PDB import PDBParser


def validate_pdb():
    try:
        path = sys.argv[1]
        ROOT_DIR_TO = os.path.dirname(os.path.abspath(__file__))[:-17]
        try:
            parser = PDBParser(PERMISSIVE=0)
            structure = parser.get_structure("name", path)
            copyfile(path, ROOT_DIR_TO + '/input.pdb')
            for model in structure:
                for chain in model:
                    for residue in chain:
                        if residue.resname == "CA":
                            print(json.dumps({
                                "code": 200,
                                "response": "OK: PDB file is correct"
                            }))
                            return

            print(json.dumps({
                "code": 204,
                "response": "ERROR: There are no calcium ion bonds in the protein"
            }))
        except:
            print(json.dumps({
                "code": 204,
                "response": "ERROR: The PDB format is not correct"
            }))
    except:
        print(json.dumps({
            "code": 204,
            "response": "ERROR: You must enter the path of the PDB"
        }))


validate_pdb()
