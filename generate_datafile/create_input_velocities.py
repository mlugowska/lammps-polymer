from typing import TextIO

from utils import vars


def write_velocities(file: TextIO, add_branch: bool) -> None:
    N = vars.N_ATOMS_TOTAL if add_branch else vars.N_ATOMS

    file.write("Velocities\n\n")
    for atom_id in range(1, N + 1):
        file.write(f"{atom_id} {0.0} {0.0} {0.0}\n")
    file.write("\n")
