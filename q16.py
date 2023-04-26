def main():
    
    List_Num = []
    
    print("Digite os 10 Números da Lista: ")
    for i in range(0, 10):
        List_Num.append(int(input(f"{i+1}° Número: ")))
    print("Lista Original: ")

    for i in List_Num:
        print(i, end=", ")
    print("")
    print("Lista Multiplicada: ")
    novaLista = []
    for num in List_Num:
        multi = num * 2
        novaLista.append(multi)
    for i in novaLista:
        print(i, end=", ")


if __name__ == "__main__":
    main()