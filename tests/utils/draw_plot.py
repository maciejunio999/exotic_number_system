import matplotlib.pyplot as plt
import numpy as np

def draw_plot(data, decibel=False):
    average_results = dict(sorted(data.items(), key=lambda x: x[1])) if decibel else {k: 10 * np.log10(v) for k, v in data.items()}

    plt.figure(figsize=(10, 5))
    plt.bar(list(average_results.keys()), list(average_results.values()))
    plt.ylabel('Różnica względem najszybszego (dB)' if decibel else 'Czas wykonania (s)')
    plt.title('Różnice czasów wykonania w skali decybelowej' if decibel else 'Czas wykonania funkcji (bezwzględna wartość)')
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()