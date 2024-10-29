#Algoritmo de Dijkstra

nos = [1 ,2 ,3 ,4 ,5 ,6 ]
arestas = [(5, 4, 5), (5, 3, 10), (5, 6, 4), (4, 3, 2), (4, 1, 2)
           , (6, 4, 1), (6, 1, 5), (3, 1, 1), (3, 2, 3), (1, 2, 2)]

def Dijkstra():

    rotulo = []
    not_rotulo = []
    origem = int(input("Digite o nó de origem: "))
    destino = int(input("Digite o nó de destino: "))
    distancia = 0
    rotulo.append(origem)

    gera_rotulo(origem, rotulo, not_rotulo)

    return gera_rotulo

def gera_rotulo(origem, rotulo, not_rotulo):

    for i in range(1,len(nos)):
        if i == origem:
            not_rotulo.append(nos[len(nos)-1])
            pass
        else:
            not_rotulo.append(i)
    
    return print(rotulo, not_rotulo)

Dijkstra()

