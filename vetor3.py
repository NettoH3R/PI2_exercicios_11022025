import numpy as np
try:

    valores = np.array([int(input(f"Digite o {i+1}º valor inteiro: ")) for i in range(10)])

    valores_invertidos = valores[::-1]

    print("Vetor original:", valores)
    print("Vetor invertido:", valores_invertidos)


except:
    print("Valor Inadequado!")