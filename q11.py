def main():
    
    List_Num = []

    print("Digite os 10 Elementos da Lista: ")
    for i in range(0, 10):
        List_Num.append(int(input(f"{i+1}° Número: ")))
        
    print("Números com Índice Par: ")
    for i in range(0,10):
        if i % 2 != 0:
            print(List_Num[i], end=", ")


if __name__ == "__main__":
    main() 