#Tamanho da matriz

def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    return print(linhas,"X",colunas, sep='')

#Soma de matrizes

def soma_matrizes(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        matriz_soma = []

        for i in range(len(m1)):
            linha = []
            
            for j in range(len(m1[i])):
                valor = m1[i][j] + m2[i][j]
                linha.append(valor)
            matriz_soma.append(linha)

        return matriz_soma
    else:

        return False

#Imprimir Matriz

def imprime_matriz(matriz):
    for i in range(len(matriz)):

        for j in range(len(matriz[i])):

            if j == len(matriz[i])-1:
                print(matriz[i][j], end = '')
            else:
                print(matriz[i][j], end = ' ')

        print()

#As matrizes são multiplicaveis

def sao_multiplicaveis(m1, m2):
    if len(m1[0]) == len(m2):
        return True
    
    else:
        return False

#Somando listas com recursos recursivos

def soma_lista(lista):
    soma = 0
    if len(lista) == 1:
        soma += lista[0]
        return soma
    else:
        soma += lista[0]
        lista = lista[1:]
        return soma + soma_lista(lista)

