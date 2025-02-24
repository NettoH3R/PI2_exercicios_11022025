try:

    idade = int(input("Digite sua idade: "))

    if 5 <= idade <= 7:
        valor = "Infantil A"
    elif 8 <= idade <= 10:
        valor = "Infantil B"
    elif 11 <= idade <= 13:
        valor = "Juvenil A"
    elif 14 <= idade <= 17:
        valor = "Juvenil B"
    elif idade >= 18:
        valor = "Adulto"
    else:
        print("Idade fora da faixa de classificação")

    print(f"você está na categoria: {valor}")

except:
    print("Valor Inadequado!")