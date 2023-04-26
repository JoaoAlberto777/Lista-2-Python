def main():
    
    Numeros = set()
    
    print("Informe os números do conjunto: ")
    
    for i in range(0,5):
        valor = int(input(f"{i+1}° Numero: "))
        Numeros.add(valor)
    print("Valores Digitados: ")
    print(Numeros, end=", ")    
    print("")

    Remove = int(input("Informe qual numero deseja remover: "))

    if Remove in Numeros:
        Numeros.remove(Remove)

    print("Valores apos alteração: ")
    print(Numeros, end=", ")    
    print("")
if __name__ == "__main__":
    main()