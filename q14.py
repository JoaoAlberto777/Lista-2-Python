def main():
    
    Numeros = set()
    
    print("Digite os 3 Números do Conjunto: ")
    for i in range(0,3):
        Num = int(input(f"Número {i+1}: "))
        Numeros.add(Num)

    if 3 in Numeros:
        print("O número '3' EXISTE no Conjunto!")
    if 3 not in Numeros:
        print("O número '3' NÃO EXISTE no Conjunto!")    
    print("Veja o Conjunto: ")
    print(Numeros, end=", ")

if __name__ == "__main__":
    main()