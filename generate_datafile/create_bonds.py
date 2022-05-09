from typing import TextIO, List

from utils import vars


def add_bond_id(bonds: List[str]):
    bond_ids = list(range(vars.N_BONDS + 1, vars.N_BONDS_TOTAL + 1))
    new_bonds = []

    for idx, bond_id in enumerate(bond_ids):
        new_bonds.append(bonds[idx].replace("bond_id", f"{bond_id}"))
    return new_bonds


def create_branch_bonds(branch_atoms: dict[int, List]):
    # ostatni bond ma id vars.N_BONDS
    bonds_list = []

    for key, values in branch_atoms.items():
        for value_id, value in enumerate(values):

            atom_id = int(value.split(" ")[0])

            if value_id == 0:
                new_bond = f"bond_id {vars.MOLECULE_ID} {key} {atom_id}\n"
            else:
                new_bond = f"bond_id {vars.MOLECULE_ID} {atom_id - 1} {atom_id}\n"
            bonds_list.append(new_bond)
    bonds = add_bond_id(bonds_list)
    return bonds


def write_backbone_bonds(file: TextIO) -> None:
    file.write("Bonds\n\n")
    for bond_id in range(1, vars.N_BONDS + 1):
        file.write(f"{bond_id} {vars.MOLECULE_ID} {bond_id} {bond_id + 1}\n")


def write_branch_bonds(file: TextIO, branch_bonds: List[str]):
    for bond in branch_bonds:
        file.write(bond)
    file.write("\n")
