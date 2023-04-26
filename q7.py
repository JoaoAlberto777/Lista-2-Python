def main():

    Num = []

    for i in range(0,5):
        Num.append(int(input(f"Digite o {i+1}º número: ")))
        
    Num_tupla = tuple(Num) 
    
    print("Numeros na tupla: ")
    print(Num_tupla)
    print("O primeiro valor da tupla é: ", Num_tupla[0])

if __name__ == "__main__":
    main()