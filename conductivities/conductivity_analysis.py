import numpy as np
from matplotlib import pyplot as plt

N20 = [0.334125, 0.4404375, 0.5133375, 0.5680125, 0.6660803571]
N20_2 = [0.1063, 0.1063, 0.1296, 0.1481, np.nan]
N20_4 = [0.0010125, 0.0041, 0.0209, 0.0491, np.nan]
N20_8 = [0.0005, 0.00236925, 0.01134, 0.030223125, np.nan]

T = [1, 2, 3, 4, 7]

for molecule in [N20, N20_2, N20_4, N20_8]:
    plt.plot(T, molecule)
    plt.scatter(T, molecule)

plt.legend(['N20', 'N20_2', 'N20_4', 'N20_8'])
plt.xlabel('temperature, T')
plt.ylabel('conductivity, sigma')
