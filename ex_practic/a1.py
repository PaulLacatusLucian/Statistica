import numpy as np

# Funktion, um das Ergebnis eines Roulette-Spiels zu simulieren
def roulette_game():
    # Zufällige Zahl zwischen 0 und 37 (37 Möglichkeiten)
    result = np.random.randint(0, 38)
    
    # Wenn die Glückszahl 15 ist und das Ergebnis ebenfalls 15 ist, gewinnen wir 175 €
    if result == 15:
        return 175
    else:
        return -5

# Anzahl der Spiele
num_games = 10

# Liste für die Ergebnisse der einzelnen Spiele
results = []

# Simulation der Spiele
for _ in range(num_games):
    results.append(roulette_game())

# Durchschnittlichen Gewinn/Verlust berechnen
average_result = np.mean(results)

print(f"Nach {num_games} Spielen betrug der durchschnittliche Gewinn/Verlust: {average_result} €")
