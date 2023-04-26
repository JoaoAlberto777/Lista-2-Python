def main():
    
    Dic = {}
    
    print("Informe os Elementos(chave - valor): ")
    chave = input("Digite a chave: ")
    valor= input("Digite o valor dessa chave: ")

    Dic.update({chave: valor})
    print("Dicionario: ")
    print(Dic)
    print("")

    chave2 = input("Digite outra chave: ")
    valor2= input("Digite o valor dessa nova chave: ")
    Dic.update({chave2: valor2})

    print("Dicionario: ")
    print(Dic)
    print("")


if __name__ == "__main__":
    main()