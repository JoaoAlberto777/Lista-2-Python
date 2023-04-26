def main():
    
    Num = set()
    
    print("Informe os 10 elementos para o conjunto: ")
    for i in range(0, 10):
        Numeros = int(input(f"{i+1}° Número: "))
        Num.add(Numeros)
    print("Lista dos Números: ")
    print(Num, end=", ")
    print("")

    lista = list(Num)
    for valor in lista:
        if valor % 2 == 0:
            lista.remove(valor)
    Num = set(lista)

    print("Lista sem Números Pares: ")
    print(Num, end=", ")
    print("")


if __name__ == "__main__":
    main()