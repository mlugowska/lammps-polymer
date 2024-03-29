# ================================ MONOMER DEFINITION ==============================
# --------------------------- BACKBONE ---------------------------------------------
N = 10  # backbone (without head and anti-ion
N_HEADS = 11  # number of heads positively charged
N_ANTIIONS = N_HEADS  # number of anti-ions negatively charged
N_ATOMS = N + N_HEADS + N_ANTIIONS  # number of all atoms
N_BONDS = N + N_HEADS - 1

# --------------------------- BRANCH -----------------------------------------------
N_BRANCH_STEP = 1  # add branch every X atoms (without heads)
N_ATOM_IN_BRANCH = 4  # how many atoms in each branch
N_ATOMS_IN_BRANCHES = (N // N_BRANCH_STEP) * N_ATOM_IN_BRANCH if N_ATOM_IN_BRANCH else 0
N_ATOMS_TOTAL = N_ATOMS + N_ATOMS_IN_BRANCHES

# --------------------------- BONDS IN BRANCHES ------------------------------------
N_BONDS_IN_BRANCH = N_ATOM_IN_BRANCH
N_BONDS_IN_BRANCHES = (N // N_BRANCH_STEP) * N_BONDS_IN_BRANCH
N_BONDS_TOTAL = N_BONDS + N_BONDS_IN_BRANCHES

# --------------------------- ANGLES, DIHEDRALS, IMPROPERS -------------------------
N_ANGLES = 0
N_DIHEDRALS = 0
N_IMPROPERS = 0

# --------------------------- TYPES ------------------------------------------------
N_ATOM_TYPES = 3
N_BOND_TYPES = 1
N_ANGLE_TYPES = 0
N_DIHEDRAL_TYPES = 0
N_IMPROPER_TYPES = 0
N_EXTRA_BOND_PER_ATOM = 3

# --------------------------- MOLECULES --------------------------------------------
MOLECULE_ID = 1

# ================================ SYSTEM BOX ======================================
SYSTEM_SIZE_MIN, SYSTEM_SIZE_MAX = - N_ATOMS - 1, 5
SYSTEM_SIZE_MIN_Y, SYSTEM_SIZE_MAX_Y = - N_ATOM_IN_BRANCH - 1, 2
