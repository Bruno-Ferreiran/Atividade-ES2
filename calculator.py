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

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
        print(num1, "^", num2, "=", power(num1, num2))
    else:
        print("Entrada inválida")