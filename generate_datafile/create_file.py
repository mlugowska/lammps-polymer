"""
Generate LAMMPS data file
"""
import os

from utils import vars
from create_atoms import write_branch_atoms, create_branch_atoms, write_backbone_atoms
from create_bonds import write_backbone_bonds, create_branch_bonds, write_branch_bonds
from specify_box_size import write_box_dimensions
from create_masses import write_masses
from create_input_velocities import write_velocities


def create_dir(path: str):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def get_file_mode(add_branch: bool) -> str:
    return "r+" if add_branch else "a"


def get_filename(add_branch: bool) -> str:
    if add_branch:
        create_dir(f"../data/N{vars.N_ATOMS}_{vars.N_ATOM_IN_BRANCH}_in_branch_{vars.N_ATOMS_TOTAL}_total")
        return f"../data/N{vars.N_ATOMS}_{vars.N_ATOM_IN_BRANCH}_in_branch_{vars.N_ATOMS_TOTAL}_total/N{vars.N_ATOMS_TOTAL}"
    create_dir(f"../data/N{vars.N_ATOMS}")
    return f"../data/N{vars.N_ATOMS}/N{vars.N_ATOMS}"


def main(add_branch: bool) -> None:
    with open(get_filename(add_branch), "w") as file:
        file.write("# LAMMPS data file\n\n")

        # ---- header ---- #
        file.write(f"{vars.N_ATOMS_TOTAL if add_branch else vars.N_ATOMS} atoms\n")
        file.write(f"{vars.N_BONDS_TOTAL if add_branch else vars.N_BONDS} bonds\n")
        file.write(f"{vars.N_ANGLES} angles\n")
        file.write(f"{vars.N_DIHEDRALS} dihedrals\n")
        file.write(f"{vars.N_IMPROPERS} impropers\n")
        file.write("\n")

        file.write(f"{vars.N_ATOM_TYPES} atom types\n")
        file.write(f"{vars.N_BOND_TYPES} bond types\n")
        file.write(f"{vars.N_ANGLE_TYPES} angle types\n")
        file.write(f"{vars.N_DIHEDRAL_TYPES} dihedral types\n")
        file.write(f"{vars.N_IMPROPER_TYPES} improper types\n")
        # file.write(f"{vars.N_EXTRA_BOND_PER_ATOM} extra bond per atom\n")
        file.write("\n")

        # ---- box dimensions ---- #
        write_box_dimensions(file, add_branch)

        # ---- masses ---- #
        write_masses(file)

        # ---- head atoms ---- #
        write_backbone_atoms(file, add_branch)

    with open(get_filename(add_branch), get_file_mode(add_branch)) as file_to_append:

        if add_branch:
            # ---- branch atoms ---- #
            branch_atoms_lines = create_branch_atoms(file_to_append)
            write_branch_atoms(file_to_append, branch_atoms_lines)

        # ---- velocities ---- #
        file_to_append.write("\n")
        write_velocities(file_to_append, add_branch)

        # ---- backbone bonds ---- #
        write_backbone_bonds(file_to_append)

        if add_branch:
            # ---- branch bonds ---- #
            branch_bonds = create_branch_bonds(branch_atoms_lines)
            write_branch_bonds(file_to_append, branch_bonds)

        file_to_append.write("\n")
