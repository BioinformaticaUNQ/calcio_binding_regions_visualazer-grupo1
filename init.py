import sys

from Bio.PDB import *

strict_parser = PDBParser(PERMISSIVE=0)
myPDB = None

try:
    path = sys.argv[1]
    try:
        myPDB = strict_parser.get_structure('name', path)
        print(myPDB)
    except:
        print("ERROR: El formato del PDB no es correcto")
except:
    print("ERROR: Debe ingresar path del PDB")
