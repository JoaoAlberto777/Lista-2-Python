def main():
    
    List = []
    print("Digite 10 números para a lista: ")
    for i in range(0,10):
        List.append(int(input(f"Número {i+1}: ")))

    print("Lista dos Números Digitados: ")
    for i in List:
        print(i, end=", ")    

if __name__ == "__main__":
    main()