import matplotlib.pyplot as plt
import pandas

# podstawowe dane
n = 'N12_2_in_branch_32_total'
n_bin = 10000
T = '1'
PATH = '/home/b02/prometheus'
all = False

dane_wszystkie = pandas.read_csv(f'{PATH}/{n}/T_4_to_{T}/3_rdf_npt/rdf_lammps.dat', delimiter=' ', skiprows=4, header=None)

if all:
    pairs = ('11', '12', '22', '23', '13', '33')
    ys = [dane_wszystkie.loc[:, 2], dane_wszystkie.loc[:, 4], dane_wszystkie.loc[:, 6], dane_wszystkie.loc[:, 8],
          dane_wszystkie.loc[:, 10], dane_wszystkie.loc[:, 12]]
else:
    pairs = ('11', '13', '33')
    ys = [dane_wszystkie.loc[:, 2], dane_wszystkie.loc[:, 10], dane_wszystkie.loc[:, 12]]
x = dane_wszystkie.loc[:, 1]

# tworzenie wykresu rdf
plt.figure(figsize=(18, 11))

for y in ys:
    import statsmodels.api as sm

    y_lowess = sm.nonparametric.lowess(y, x, frac=0.07)  # 7% lowess smoothing
    plt.plot(y_lowess[:, 0], y_lowess[:, 1])  # some noise removed

plt.legend(pairs, loc='upper right')
plt.title(f'RDF {n} T={T}')
plt.xlabel("r", fontsize=15)
plt.ylabel("g(r)", fontsize=15)

plt.savefig(f'RDF_{n}_T_{T}_3%.png' if all else f'RDF_{n}_T_{T}_ion_3%.png')
