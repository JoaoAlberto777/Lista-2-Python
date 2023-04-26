def main():
    
    Dic = {}
    
    print("Informe os elemento (chave - valor): ")
    for i in range(0, 3):
        Dic.update(
            {input("Digite a chave: "): input("Digite o valor: ")})

    print(Dic)
    print("Chave 'Idade': ", Dic['Idade'])


if __name__ == "__main__":
    main()