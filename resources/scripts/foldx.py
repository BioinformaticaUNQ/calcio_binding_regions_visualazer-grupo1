import json
import os


def generate_fold_data():
    try:
        os.system(
            "resources/scripts/foldx/foldx --command=MetalBinding --metal=-PREDICT --metal_element=CA --pdb=input.pdb")
        return (json.dumps({
            "code": 200,
            "response": "fold data generated"
        }))
    except:
        return (json.dumps({
            "code": 204,
            "response": "fold cannot generated"
        }))


generate_fold_data()
