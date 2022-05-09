from typing import TextIO

from utils import vars


def write_masses(file: TextIO) -> None:
    file.write("Masses\n\n")
    for idx in range(1, vars.N_ATOM_TYPES + 1):
        file.write(f"{idx} {1}\n")
    file.write("\n")
