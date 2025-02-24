import numpy as np
try:

    valores = np.array([int(input(f"Digite o {i+1}º valor inteiro: ")) for i in range(10)])

    soma_positivos_pares = sum(valores[i] for i in range(0, 10, 2) if valores[i] > 0)

    print("Vetor original:", valores)
    print("Soma dos elementos positivos nas posições pares:", soma_positivos_pares)

except:
    print("Valor Inadequado!")