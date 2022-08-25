from typing import List

from conductivities.constants import b
from conductivities.get_conductivity import calculate_ionic_conductivities
import matplotlib.pyplot as plt

t = ['4', '2']


def get_filename(system_name: str) -> str:
    all = False

    if system_name == 'N12':
        return f'{system_name}_vacf.out' if all else f'{system_name}_vacf_counterion.out'
    return f'N{system_name[-8:-6]}_vacf.out' if all else f'N{system_name[-8:-6]}_vacf_counterion.out'


def get_conductivities() -> List[List]:
    D_list = list()
    sigma_list = list()
    conductivities = list()

    for system, box in b.items():
        filename = get_filename(system_name=system)
        for temperature in t:
            D, sigma = calculate_ionic_conductivities(t=temperature, filename=filename, dir_name=system)
            D_list.append(round(D, 4))
            sigma_list.append(round(sigma, 4))
    conductivities.append(D_list)
    conductivities.append(sigma_list)
    return conductivities


conductivities = get_conductivities()
print(conductivities)

# plot sigma

# plt.plot(t, conductivities[1][:3])
# plt.plot(t, conductivities[1][3:6])
# plt.plot(t, conductivities[1][6:9])
# plt.plot(t, conductivities[1][9:])
#
# plt.legend(['N12', 'N12_2', 'N12_4', 'N12_8'])
# plt.xlabel('temperature, T')
# plt.ylabel('conductivity, sigma')
#
# plt.savefig('sigma.png')
# plt.clf()
#
# # plot diffusion
#
# plt.plot(t, conductivities[0][:3])
# plt.plot(t, conductivities[0][3:6])
# plt.plot(t, conductivities[0][6:9])
# plt.plot(t, conductivities[0][9:])
#
# plt.legend(['N12', 'N12_2', 'N12_4', 'N12_8'])
# plt.xlabel('temperature, T')
# plt.ylabel('diffusion coeff, D')
#
# plt.savefig('D.png')


