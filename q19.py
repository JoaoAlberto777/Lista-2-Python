def main():
    
    Conj = set()
    Cont = 0
    
    print("Digite os Números no Conjunto: ")
    for contador in range(0, 5):
        Num = int(input("Digite um Número: "))
        Conj.add(Num)
        Cont += 1
    print("Números Digitados: ")
    print(Conj)
    print(f"Você Digitou '{Cont}' Números")

if __name__ == "__main__":
    main()