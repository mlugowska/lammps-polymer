import os

import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist

PATH_TXT = '/home/b02/Desktop/1xhead/T1/dummps'
txtfiles = [cluster_file for cluster_file in os.listdir(PATH_TXT) if '1.9_clusters' in cluster_file]


def dist(coor):
    n_coor = len(coor)
    dist = np.zeros((n_coor, n_coor))
    r = np.arange(n_coor)
    dist[r[:, None] < r] = pdist(coor)
    return dist


avg_cluster_size = []
avg_cluster_dist = []
for file in txtfiles:
    df = pd.read_csv(f'{PATH_TXT}/{file}', sep=' ', header=0)
    df.columns = ["Cluster Size", "Center of Mass.X", "Center of Mass.Y", "Center of Mass.Z", '']
    df.drop(columns='', inplace=True)

    avg_cluster_size.append(df['Cluster Size'].mean())

    positions = np.vstack((df['Center of Mass.X'], df['Center of Mass.Y'], df['Center of Mass.Z'])).transpose()
    dist_array = dist(positions)
    avg_cluster_dist.append(dist_array.mean())

