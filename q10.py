def main():
    
    Grafo = {}
    
    Vert = input('Digite os vértices do grafo separados por um espaço: ').split()

    for chave in Vert:
        Grafo[chave] = []
        
    Num_Aresta = int(input("Quantidade de arestas do grafo: "))
    
    for i in range(0,Num_Aresta):
        partida, chegada = input('Digite os vértices da aresta separados por um espaço: ').split()

        Grafo[partida].append(chegada)
        Grafo[chegada].append(partida)

    print("Grafo Original: ")
    for v in Grafo:
        print(v, '->', Grafo[v])

    print("Apague Uma das Arestas: ")
    P_apagar, C_apagar = input("Informe o Par da Aresta a Ser Apagada: ").split()  
    if P_apagar in Grafo and C_apagar in Grafo:
        Grafo[P_apagar].remove(C_apagar)
        Grafo[C_apagar].remove(P_apagar)

    print("Novo Grafo: ")
    for v in Grafo:
        print(v, '->', Grafo[v])        

if __name__ == "__main__":
    main()