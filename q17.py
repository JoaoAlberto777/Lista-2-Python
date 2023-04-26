def main():
    
    Names = ()
    list_Names = []
    print("Digite os nomes: ")
    for i in range(0, 3):
        list_Names.append(str(input(f"{i+1}° Nome: ")))

    Names = tuple(list_Names)
    print(f"O nome 'Maria' apareceu {Names.count('Maria')} vez(es)")
    print("Tupla Finalizada: ")
    print(Names, end=", ")


if __name__ == "__main__":
    main()