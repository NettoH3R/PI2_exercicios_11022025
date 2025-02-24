import numpy as np
try:

    valores = np.array([int(input(f"Digite o {i+1}º valor inteiro: ")) for i in range(10)])

    impares = valores[valores % 2 != 0]

    print("Valores ímpares:")
    print(impares)

except:
    print("Valor Inadequado!")