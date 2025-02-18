try:
    nota1 = float(input("Digite o valor da nota: "))
    nota2 = float(input("Digite o valor da nota 2: "))

    media = (nota1+nota2)/2

    if media >= 6:
        print(f"Aluno aprovado")

    else:
        print("Aluno reprovado")
except:
    print("Valor Inadequado!")