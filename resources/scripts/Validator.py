import sys
import json

from Bio.PDB import *


class Validator:

    def __init__(self):
        """Initialize the class."""
        self.strict_parser = PDBParser(PERMISSIVE=0)
        self.myPDB = None

    @staticmethod
    def validate_pdb():
        try:
            path = sys.argv[1]
            try:
                parser = PDBParser()
                structure = parser.get_structure("name", path)
                print(structure.get_residues())
                for model in structure:
                    for chain in model:
                        for residue in chain:
                            if residue.resname == "CA":
                                print("Formato Correcto")
                                return structure

                print("ERROR: No existen elementos de CA en la proteina.")
            except:
                print("ERROR: El formato del PDB no es correcto")
        except:
            print("ERROR: Debe ingresar path del PDB")
