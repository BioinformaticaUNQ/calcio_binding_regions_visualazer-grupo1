import sys
import pymol

# Call the function below before using any PyMOL modules.

# THIS DOES NOT WORK ON macOS
pymol.finish_launching()

# Now we can import cmd

from pymol import cmd

try:
    path = sys.argv[1]
    try:
        myPDB = strict_parser.get_structure('name', path)
        cmd.load(path)
        cmd.show("sticks")
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
