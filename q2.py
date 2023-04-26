def main():
    Nomes = []

    for i in range(0,3):
        Nomes.append(str(input(f"Digite o {i+1}º nome :")))

    Nomes_tupla = tuple(Nomes) 
    print("Lista de nomes: ")
    for i in Nomes_tupla:
        print(i, end=", ")
    print("")
        
    Pos = int(input("Qual nome sera substituido? 1, 2 ou 3?"))
    New_nome = str(input("Digite o novo nome: "))

    lista = list(Nomes_tupla)
    Pos = Pos -1
    lista[Pos] = New_nome
    Nomes_tupla = tuple(lista)

    print("Nova lista: ")
    for i in Nomes_tupla:
        print(i, end=", ")

if __name__ == "__main__":
    main()