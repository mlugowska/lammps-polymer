import os
import MDAnalysis
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from scipy.spatial.distance import pdist


PATH_DUMPS = '/home/b02/Desktop/1xhead/T1/dummps'
dumpfiles = os.listdir(PATH_DUMPS)

data = MDAnalysis.Universe(f'{PATH_DUMPS}/{dumpfiles[0]}', atom_type='id type x y z charge mol')

heads = data.select_atoms(sel='type 1')


def dist(coor):
    n_coor = len(coor)
    dist = np.zeros((n_coor, n_coor))
    r = np.arange(n_coor)
    dist[r[:, None] < r] = pdist(coor)
    return dist


dist_array = dist(heads.positions)
# df_dist = pd.DataFrame(dist_array, columns=heads.ids, index=heads.ids)

# dist_array = dist_array[dist_array != 0]
arr = np.sort(dist_array)[0]
arr = arr[arr != 0]
current_group = [arr[0]]

groups = []
for index, distance in enumerate(arr):
    if distance - current_group[-1] <= 1.0:
        current_group.append(distance)  # Dodajemy element do bieżącej grupy
    else:
        groups.append(current_group)  # Dodajemy bieżącą grupę do listy grup
        current_group = [distance]  # Tworzymy nową grupę z bieżącego elementu

groups.append(current_group)