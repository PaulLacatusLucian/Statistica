from matplotlib.pyplot import bar, show, hist, grid, legend, xticks
from math import comb

import numpy as np

N = 2000
werter_x = [0, 1]
p_x = [0.5, 0.5]

# a
simulated_values = np.random.choice(werter_x, 4, p_x)
print(simulated_values)
z = np.sum(simulated_values == 1)
print(z)

werter_z = []

for i in range(N):
    simulated_value = np.random.choice(werter_x, 4, p_x)
    z = np.sum(simulated_value == 1)
    werter_z.append(z)

werter_z = np.array(werter_z)
z_0 = np.sum(werter_z == 0)
z_1 = np.sum(werter_z == 1)
z_2 = np.sum(werter_z == 2)
z_3 = np.sum(werter_z == 3)
z_4 = np.sum(werter_z == 4)

print(f"Z=0 hat die relative Hfg = {z_0 / N}")
print(f"Z=1 hat die relative Hfg = {z_1 / N}")
print(f"Z=2 hat die relative Hfg = {z_2 / N}")
print(f"Z=3 hat die relative Hfg = {z_3 / N}")
print(f"Z=4 hat die relative Hfg = {z_4 / N}")

# b
theoretic_Z_0 = 1 / 2 * 1 / 2 * 1 / 2 * 1 / 2
theoretic_Z_1 = comb(4, 1) * (1 / 2 * 1 / 2 * 1 / 2 * 1 / 2)
theoretic_Z_2 = comb(4, 2) * (1 / 2 * 1 / 2 * 1 / 2 * 1 / 2)
theoretic_Z_3 = comb(4, 1) * (1 / 2 * 1 / 2 * 1 / 2 * 1 / 2)
theoretic_Z_4 = 1 / 2 * 1 / 2 * 1 / 2 * 1 / 2

print(f"\nTheoretische Wsch\n")
print(f"P(Z = 0): {theoretic_Z_0:.4f}")
print(f"P(Z = 1): {theoretic_Z_1:.4f}")
print(f"P(Z = 2): {theoretic_Z_2:.4f}")
print(f"P(Z = 3): {theoretic_Z_3:.4f}")
print(f"P(Z = 4): {theoretic_Z_4:.4f}")

# c

z, count = np.unique(werter_z, return_counts=True)
d = dict([(z[i], count[i] / N) for i in range(0, len(z))])

bar(
    z,
    count / N,
    width=0.9,
    color="red",
    edgecolor="black",
    label=" relative Haufigkeiten ",
)

grid()
show()

# d

z_grosserAls1 = np.sum(werter_z > 1) / N
th_grosserAls1 = theoretic_Z_2 + theoretic_Z_3 + theoretic_Z_4

print(f"\nRel P(Z > 1): {z_grosserAls1:.4f}")
print(f"Th P(Z > 1): {th_grosserAls1:.4f}")
