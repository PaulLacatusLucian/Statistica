import numpy as np
from scipy.stats import binom

# Wahrscheinlichkeiten für die verschiedenen Fehlerkategorien
p_no_error = 0.80
p_minor_error = 0.15
p_major_error = 0.05

# a) Simulierte Werte für X
N = 100
simulated_values = np.random.choice([0, 1, 2], size=N, p=[p_no_error, p_minor_error, p_major_error])

# b) Mittlere Anzahl M der Waren mit großen Fehlern
nr = np.sum(simulated_values == 2)
mean_2 = nr / N
print(f"Die mittlere Anzahl M der Waren mit großen Fehlern beträgt: {mean_2}")

# c) Theoretische Wahrscheinlichkeiten
# 1) Wahrscheinlichkeit, dass höchstens 3 Waren große Fehler haben:
p_less_than_3 = binom.cdf(3, 100, p_major_error)
print(f"Die theoretische Wahrscheinlichkeit, dass höchstens 3 Waren große Fehler haben, beträgt: {p_less_than_3}")

# 2) Wahrscheinlichkeit, dass genau 10 Waren große Fehler haben:
p_exactly_10 = binom.pmf(10, 100, p_major_error)
print(f"Die theoretische Wahrscheinlichkeit, dass genau 10 Waren große Fehler haben, beträgt: {p_exactly_10}")

# 3) Wahrscheinlichkeit, dass mindestens 4 Waren große Fehler haben:
p_at_least_4 = 1 - binom.cdf(3, 100, p_major_error)
print(f"Die theoretische Wahrscheinlichkeit, dass mindestens 4 Waren große Fehler haben, beträgt: {p_at_least_4}")
