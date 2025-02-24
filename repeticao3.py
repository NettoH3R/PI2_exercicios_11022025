try:
    inicio = int(input("Digite o primeiro valor: "))
    fim = int(input("Digite o segundo valor: "))


    if inicio < fim:
        soma = 0
        for i in range(inicio, fim + 1):
            soma += i

        print(f"A soma dos inteiros entre {inicio} e {fim} é: {soma}")

    else:
        print("O número final deve ser maio que o inicial")

except:
    print("Valor Inadequado!")