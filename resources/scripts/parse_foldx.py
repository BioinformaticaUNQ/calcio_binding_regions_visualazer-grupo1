def get_atom(line):
    return line.split()[0].split("_")[0]


def get_number(line):
    return int(line.split()[0].split("_")[0][2:])


def get_energy(line):
    return line.split()[-1]


# El archivo predict_output.txt debe estar en la carpeta ./temp
def parse_file_foldx(file):
    read = file.read()
    lines = read.splitlines()
    elements = []
    for i in range(int(len(lines)/2)):
        element = {
            "atom": get_atom(lines[i * 2 + 1]),
            "number": get_number(lines[i * 2 + 1]),
            "energy": get_energy(lines[i * 2])
        }
        elements.append(element)
    return elements
