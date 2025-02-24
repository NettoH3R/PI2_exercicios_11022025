import numpy as np
try:

    valores = np.array([float(input(f"Digite o {i+1}º valor real: ")) for i in range(6)])

    media = np.mean(valores)
    maior = np.max(valores)
    menor = np.min(valores)

    print(f"Média: {media:.2f}")
    print(f"Maior valor: {maior:.2f}")
    print(f"Menor valor: {menor:.2f}")

except:
    print("Valor Inadequado!")