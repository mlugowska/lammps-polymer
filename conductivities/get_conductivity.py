from typing import Tuple, Union, Any

import pandas
import numpy

from conductivities.constants import N_atoms, b, BASE_PATH
from utils import vars


def calculate_vacf(filename: str, dir_name: str, t: str) -> float:
    # ---------- GET AREAS OF INTERESTS FROM FILE ----------
    file_path = f'{BASE_PATH}/{dir_name}/T_4_to_{t}/5_msd'
    try:
        file = open(f'{file_path}/{filename}')
    except FileNotFoundError:
        file_path = f'{BASE_PATH}/{dir_name}/T_4_to_{t}/4_vacf_npt'
        file = open(f'{file_path}/{filename}')

    lines = file.readlines()
    for idx, line in enumerate(lines):
        if 'Step Temp c_vacf[4] v_diff' \
           '' in line:
            start_index = idx + 1
            stop_index = idx + 1002
            columns = line.split(' ')

    # ---------- CREATE DATAFRAME of VACF -------------------
    df_vacf = pandas.DataFrame([row.split() for row in lines[start_index:stop_index]],
                               columns=columns[:-1]).astype('float64')
    # ---------- CALCULATE MEAN VACF -------------------
    return float(numpy.mean(df_vacf['v_diff']))


def calculate_atom_concentration(dir_name: str) -> float:
    n = N_atoms * vars.REPLICA_X * vars.REPLICA_Y * vars.REPLICA_Z
    v = b.get(dir_name) ** 3
    return n / v


def calculate_ionic_conductivities(t: str, filename: str, dir_name: str) -> Tuple[float, Union[float, Any]]:
    D = calculate_vacf(filename, dir_name, t)
    c = calculate_atom_concentration(dir_name)
    t = '0.5' if t == '05' else t
    return D, (c * ((-9) ** 2) * D) / float(t)
