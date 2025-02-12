try:
    maca = print("Digite o número de maçãs compradas. \n")

    if 0 <= maca < 12 :
        print(f"Número de maçãs Compradas: {maca} \n Valor Total: {(maca*1.3):.2f}")

    elif maca > 12 :
        print(f"Número de maçãs Compradas: {maca} \n Valor Total: {(maca*1.3):.2f}")
    
except:
    print("Valor Invalido!")