def main():
    
    Dic = {}
    
    print("Digite: (Chave - Valor)")
    for i in range(0, 2):
        Dic.update({input(f"Digite a Chave {i+1}: ")
                          :input(f"Digite o Valor {i+1}: ")})
        
    print("Agora Informa a Cidade em Que Você Nasceu: ")
    Dic.update({"Cidade": input("Digite a Cidade: ")})

    print(Dic)


if __name__ == "__main__":
    main()