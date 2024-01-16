import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import uniform
from matplotlib.pyplot import bar, show, grid

N = 2000
x_val = uniform.rvs(loc=10, scale=10, size=N)

p_14_18 = np.sum((14 <= x_val) & (x_val <= 18)) / N
p_15 = np.sum(x_val <= 15) / N
p_17 = np.sum(x_val >= 17) / N

print(p_14_18)
print(p_15)
print(p_15 + p_17)

uniform_distinct = uniform(loc=10, scale=10)
print(1 - uniform_distinct.cdf(14) - (1 - uniform_distinct.cdf(18)))
print(uniform_distinct.cdf(15))
print(uniform_distinct.cdf(15) + (1 - uniform_distinct.cdf(17)))


plt.hist(x_val, bins=10, density=True, color="blue", edgecolor="black", alpha=0.7, label="Relative Häufigkeiten")

plt.grid()
plt.legend()
plt.show()
