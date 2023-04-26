def main():
    
    Grafo = {}
    
    Vert = input('Digite os vértices do grafo separados por um espaço: ').split()

    for chave in Vert:
        Grafo[chave] = []
    Num_Aresta = int(input("Quantas arestas vai ter o grafo: "))
    for i in range(0,Num_Aresta):
        partida, chegada = input('Digite os vértices da aresta separados por um espaço: ').split()

        Grafo[partida].append(chegada)
        Grafo[chegada].append(partida)

    print("Grafo Finalizado: ")
    for v in Grafo:
        print(v, '->', Grafo[v])
if __name__ == "__main__":
    main()