#Algoritmo de Dijkstra

nos = [1 ,2 ,3 ,4 ,5 ,6 ]
arestas = [(5, 4, 5), (5, 3, 10), (5, 6, 4), (4, 3, 2), (4, 1, 2)
           , (6, 4, 1), (6, 1, 5), (3, 1, 1), (3, 2, 3), (1, 2, 2)]

def obter_arestas(arestas, ultimo_rotulo):
    index = 0
    arestas_sep = []

    for u, v, distancia in arestas:
        if (u == ultimo_rotulo):
            arestas_sep.append(arestas[index])
            index += 1
        else:
            index += 1

    return arestas_sep

def gera_rotulo(origem, rotulo, not_rotulo):

    for i in range(1,len(nos)):
        if i == origem:
            not_rotulo.append(nos[len(nos)-1])
            pass
        else:
            not_rotulo.append(i)
    
    return rotulo, not_rotulo

def Dijkstra():

    rotulo = []
    not_rotulo = []
    origem = int(input("Digite o nó de origem: "))
    destino = int(input("Digite o nó de destino: "))
    distancia = 0
    predecessor = []
    ultimo_rotulo = origem
    rotulo.append(origem)

    gera_rotulo(origem, rotulo, not_rotulo)

    minimos = []
    custo_caminhos = []

    while ultimo_rotulo != destino:

        caminhos = obter_arestas(arestas, ultimo_rotulo)
        menor = caminhos[0][2]
        nó = caminhos[0][1]

        for i in range(0,len(caminhos)):
            
            custo = min(caminhos[i][2], (distancia + caminhos[i][2]))
            caminho = ultimo_rotulo, 
            if custo <= menor:
                menor = custo
                nó = caminhos[i][1]
                caminho = ultimo_rotulo, nó
                predecessor.append(caminho)

        ultimo_rotulo = nó
        custo_caminhos.append(menor)


        

    return gera_rotulo, custo_caminhos, predecessor

print(Dijkstra())


