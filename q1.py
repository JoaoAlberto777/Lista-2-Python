def main():
    ListNum = []
    for i in range(0,5):
        ListNum.append(int(input(f"Digite o {i+1}º número: ")))

    print("Lista: ")
    for i in ListNum:
        print(i, end=", ") 
    print("")  
    ListNum.append(input("Digite outro número: ")) 
    
    print("Números da lista: ")
    for i in ListNum:
        print(i, end=", ")

if __name__ == "__main__":
    main()