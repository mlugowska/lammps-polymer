import random
from typing import Tuple, TextIO, List, Dict

from utils import vars


def get_init_coords(branch: bool) -> Tuple[float, float, float]:
    """
    :param branch:
    :return: first atom coordinates: x, y z
    """
    x = random.uniform(0, 1)
    y = random.uniform(vars.SYSTEM_SIZE_MIN_Y + 0.5, vars.SYSTEM_SIZE_MIN_Y + 1) if branch else random.uniform(0, 1)
    z = random.uniform(vars.SYSTEM_SIZE_MIN + 0.5, vars.SYSTEM_SIZE_MIN + 1)
    return x, y, z


def get_last_atom_coords_from_file(lines: List[str], last_atom_id: int, last_atom_type: str = '') -> Tuple[float, float, float]:
    # file.seek(0)

    for line in lines:
        if line.startswith(f"{last_atom_id} {get_atom_type(atom_type=last_atom_type)} "):
            line_to_list = line.split(" ")
            return float(line_to_list[2]), float(line_to_list[3]), float(line_to_list[4])


def get_atom_type(atom_type: str = '') -> int:
    """
    :param atom_type:
    :return:
    """
    if atom_type == 'head':
        return 1
    if atom_type == 'tail':
        return 3
    return 2


def get_atom_charge(atom_type: str = 'counter') -> int:
    """
    :param atom_type: head, tail or empty for counter
    :return:
    """
    if atom_type == 'head':
        return 9
    if atom_type == 'tail':
        return -9
    return 0


def get_branch_atom_id(branch_atoms: dict, branch_id: int, branch_atom_number: int) -> int:
    if branch_id == vars.N_BRANCH_STEP + vars.N_HEADS:
        return branch_atom_number + vars.N_ATOMS
    return int(branch_atoms[branch_id - vars.N_BRANCH_STEP][-1].split(" ")[0]) + branch_atom_number


def write_atom(file: TextIO, atom_type: str, linear:bool, n_atoms, x, y, z):
    for atom_id in n_atoms:
        if linear:
            file.write(
                f"{atom_id} {get_atom_type(atom_type=atom_type)} {round(x, 5)} {round(y, 5)} {round(z, 5)} "
                f"{get_atom_charge(atom_type=atom_type)} {vars.MOLECULE_ID}\n")
            z += 1


def write_backbone_atoms(file: TextIO, add_branch: bool, linear: bool):
    file.write("Atoms\n\n")
    x, y, z = get_init_coords(add_branch)

    # HEAD
    head_ids = range(1, vars.N_HEADS + 1)
    write_atom(file=file, atom_type='head', linear=linear, n_atoms=head_ids, x=x, y=y, z=z)

    # COUNTER
    atom_ids = range(vars.N_HEADS + 1, vars.N + vars.N_HEADS + 1)
    write_atom(file=file, atom_type='', linear=linear, n_atoms=atom_ids, x=x, y=y, z=z + vars.N_HEADS)

    # TAIL
    atom_ids = range(vars.N + vars.N_HEADS + 1, vars.N_ATOMS + 1)
    write_atom(file=file, atom_type='tail', linear=linear, n_atoms=atom_ids, x=x, y=y, z=z + vars.N_HEADS + vars.N)


def create_branch_atoms(file: TextIO) -> Dict[int, List]:
    """
    :param file:
    :return: dict - key is id of an atom to which a branch will be added, value is a list of new atoms in branch
    """
    branch_atoms = dict()
    lines = file.readlines()

    for branch_id in range(vars.N_BRANCH_STEP + vars.N_HEADS, vars.N + vars.N_HEADS + 1, vars.N_BRANCH_STEP):
        branch_atoms[branch_id] = []

        x, y, z = get_last_atom_coords_from_file(lines, last_atom_id=branch_id, last_atom_type='')

        for branch_atom_number in range(1, vars.N_ATOM_IN_BRANCH + 1):
            y += 1
            atom_id = get_branch_atom_id(branch_atoms, branch_id, branch_atom_number)
            new_line = f"{atom_id} 2 {round(x, 5)} {round(y, 5)} {round(z, 5)} {get_atom_charge()} " \
                       f"{vars.MOLECULE_ID}\n"
            branch_atoms[branch_id].append(new_line)

    return branch_atoms


def write_branch_atoms(file: TextIO, branch_atoms_lines: Dict[int, List]):
    for key, values in branch_atoms_lines.items():
        for value in values:
            file.write(value)
    file.write("\n")
