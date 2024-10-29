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
    predecessor = 0
    ultimo_rotulo = origem
    rotulo.append(origem)

    gera_rotulo(origem, rotulo, not_rotulo)

    minimos = []
    while ultimo_rotulo != destino:
        
        for j in not_rotulo:
            x = min(distancia, distancia + arestas[ultimo_rotulo,j])

    return gera_rotulo

Dijkstra()

