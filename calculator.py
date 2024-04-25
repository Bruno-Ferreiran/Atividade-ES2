while True:
    print("Selecione a operação:")
    print("1.Adicionar")
    print("2.Subtrair")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Potência")
    print("6.Sair")
    choice = input("Digite o número da operação desejada: ")

    if choice == '6':
        print("Saindo do programa...")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))