def main():
    
    Names = ()
    
    List_Name = []
    print("Digite 3 nomes: ")
    for i in range(0, 3):
        List_Name.append(str(input(f"Nome {i +1}: ")))

    Names = tuple(List_Name)
    if 'Maria' in Names:
        print("O Nome 'Maria' está na tupla !")
    if 'Maria' not in Names:
        print("'Maria' não está na tupla !")

    print("Nomes na Tupla: ")
    print(Names, end=", ")
    print("")

if __name__ == "__main__":
    main()