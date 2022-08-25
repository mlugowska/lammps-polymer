BASE_PATH = '/home/b02/prometheus'
DIR_NAME = 'N12_4_in_branch_52_total'
T = '2'
b = {
    'N12': 43.27,
    # 'N12_2_in_branch_32_total': 60.0,
    # 'N12_4_in_branch_52_total': 70.54,
    # 'N12_8_in_branch_92_total': 85.32,

}
N_atoms = 1
all = False

FILE_PATH = f'{BASE_PATH}/{DIR_NAME}/T_4_to_{T}/4_vacf'
FILENAME = 'N52_vacf.out' if all else 'N52_vacf_counterion.out'
