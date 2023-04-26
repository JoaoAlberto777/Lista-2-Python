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

    print("Grafo Finalizado: ")
    for v in Grafo:
        print(v, '->', Grafo[v])

    if 'C' in Grafo['A']:
        print('A aresta (A, C) está presente no grafo')
    else:
        print('A aresta (A, C) NÃO está presente no grafo')
if __name__ == "__main__":
    main()