# Julia O.

valor = float(input("Digite um valor: "))
continua = True

while continua == True:
    operacao = input("Digite a operação desejada:\n1 -\n2 +\n3 *\n4 /\nx - fim\n\nDigite a opção: ")
    if operacao in ["1", "2", "3", "4"]:
        
        if operacao == "1":
            numeroOp = float(input("Digite o número para a operação: "))
            resultado = valor - numeroOp
        
        elif operacao == "2":
            numeroOp = float(input("Digite o número para a operação: "))
            resultado = valor + numeroOp
                    
        elif operacao == "3":
            numeroOp = float(input("Digite o número para a operação: "))
            resultado = valor * numeroOp

        elif operacao == "4":
            numeroOp = float(input("Digite o número para a operação: "))
            if numeroOp != 0:
                resultado = valor / numeroOp
                
            else:
                print("não da para dividir por 0")

        valor_atual = resultado

    elif operacao == "X":
        continua = False
    else:
        print("Opção inválida, tente novamente.")

print(f"O resultado {valor_atual}")