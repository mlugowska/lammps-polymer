import math

import MDAnalysis
import numpy as np
from numpy import ndarray
from scipy.spatial.distance import pdist

# ---------- READ DUMPFILES ----------------------
# tail with no branches
# DUMPFILE = '/home/b02/prometheus/N12_4_in_branch_52_total/T_4_to_1/2_eq_nvt/constant_temp_low_3.lammpsdump'
# DUMPFILE = '/home/b02/prometheus/N12/T_4_to_05/2_eq_npt/constant_temp_low_3.lammpsdump'
# data = MDAnalysis.Universe(DUMPFILE, atom_type='id type x y z charge mol')

# tail with branches
# DUMPFILE_BRANCHES = '/home/b02/prometheus/N12_8_in_branch_92_total/T_4_to_1/2_eq_nvt_d_0_9/constant_temp_low_3.lammpsdump'
# DUMPFILE_BRANCHES = '/home/b02/prometheus/N12_8_in_branch_92_total/T_4_single_molecule/constant_temp_high_1.lammpsdump'
# data_branches = MDAnalysis.Universe(DUMPFILE_BRANCHES, atom_type='id type x y z charge mol')


# ---------- CALCULATE MEAN DISTANCE FROM HEAD TO LAST TAIL'S ATOM ----------------------
# METHOD 1.
def dist(p1: ndarray, p2: ndarray) -> float:
    """
    Computes the average distance among two points in the 3-dimensional space.
    :param p1:
    :param p2:
    :return:
    """
    (x1, y1, z1), (x2, y2, z2) = p1, p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


# ---------- GET ATOMS POSITIONS (FROM ONE MOLECULE) ----------------------
# polymers = []
# # positions = data.atoms[1:11].positions
# for atom_id in range(0, 496800, 92):
#     positions_branches = data_branches.atoms[atom_id:atom_id + 10].positions
#
#     # mean_distance = dist(positions[0], positions[-1])
#     mean_distance_branches = dist(positions_branches[0], positions_branches[-1])
#     if mean_distance_branches < 10:
#         polymers.append(mean_distance_branches)
# print(polymers)
# mean = np.mean(polymers)
# #
# # print(f"Mean distance from head to last tail's atom: {mean_distance}")
# print(f"Mean distance from head to last tail's atom (branches): {mean}")


# METHOD 2.
def compute_average_distance(coords: ndarray) -> ndarray:
    """
    Computes the average distance among a set of n points in the d-dimensional space.

    :param coords: the query points in an array of shape (n,d),
                          where n is the number of points and d is the dimension.
    :return: the average distance among the points
    """
    return np.mean(pdist(coords))

# # selected_atoms = np.vstack((positions[0], positions[-1]))
# selected_atoms_branches = np.vstack((positions_branches[0], positions_branches[-1]))
#
# # print(f"Mean distance from head to last tail's atom: {compute_average_distance(selected_atoms)}")
# print(f"Mean distance from head to last tail's atom (branches): {compute_average_distance(selected_atoms_branches)}")
