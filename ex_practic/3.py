from random import randrange
from scipy.stats import binom
import numpy as np
from matplotlib.pyplot import bar, show, grid

x_y_werte = [-2, -1, 1, 2, 3]
p_x_y = [0.2, 0.2, 0.2, 0.2, 0.2]
N = 2000000

# a
daten1 = np.random.choice(x_y_werte, N, p=p_x_y)
daten2 = np.random.choice(x_y_werte, N, p=p_x_y)

sums = [0] * N
sums = np.array(sums)
for i in range(N):
    sums[i] = daten1[i] + daten2[i]

z, count = np.unique(sums, return_counts=True)

for i in range(11):
    print(f"X+Y={z[i]} hat relative Hfg = {count[i] / N}")

# b
bar(
    z,
    count / N,
    width=0.9,
    color="red",
    edgecolor="black",
    label="relative Haufigkeiten",
)
grid()
show()

# c
p_greater_2 = count[7] + count[8] + count[9] + count[10]
print(p_greater_2 / N)

print(np.sum(sums > 2) / N)

# b2
prob = {}
th_p_greater_2 = 0
for i in range(len(x_y_werte)):
    for j in range(len(x_y_werte)):
        z = x_y_werte[i] + x_y_werte[j]
        p = p_x_y[i] * p_x_y[j]
        if prob.get(z):
            prob[z] += p
        else:
            prob[z] = p
        if z > 2:
            th_p_greater_2 += p

for k in prob:
    print(f"P(x+y={k}) hat die theoretische wahrscheinlichkeit = {prob[k]}")

print(f"P(X+Y>2 {th_p_greater_2}")
