def main():
    
    Dic = {} 
    
    print("Informa as chaves e valores para o Dicionário: ")
    for i in range(0,2):
        Dic.update({input("Digite a chave: "): input("Digite o valor dessa chave: ")})

    if 'Profissão' in Dic.keys():
        print("A chave 'Profissão' esta no Dicionário!")
    if 'Profissão' not in Dic.keys():
        print("'Profissão' NÃO esta no Dicionário!")    

    print("Veja o Dicionário: ")
    print(Dic)    

if __name__ == "__main__":
    main()