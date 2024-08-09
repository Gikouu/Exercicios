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

#Separando números ímpares de listas

def encontra_impares(lista):

    if not lista:
        return []
    
    impares_restantes = encontra_impares(lista[1:])
    if lista[0] % 2 != 0:
        return impares_restantes + [lista[0]]
    else:
        return impares_restantes
    
#Música do elefante

def incomodam(n):
    if n <=0:
        return ""
    else:
        return incomodam(n-1) + "incomodam "

def elefantes(k):
    if k<=1:
        return ""
    
    elif k == 2:
        return elefantes(k-1) + "Um elefante incomoda muita gente\n{} elefantes {}muito mais\n".format(k, incomodam(k))
        
    else:
        return elefantes(k-1) + "{} elefantes incomodam muita gente\n{} elefantes {}muito mais\n".format(k-1,k,incomodam(k))

#Soma de Fibonacci

def fibonacci(x:int):
    if x < 2:
        return x 
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    
#Fatorial

def fatorial(x:int):
    if x <=1:
        return 1
    else:
        return fatorial(x-1) * x

#Retornas maiusculas

def maiusculas(frase:str):
    letrasM = ''
    for palavra in frase:
        if ord(palavra) >= 65 and ord(palavra) <= 90:
            letrasM += str(palavra)
    
    return letrasM

#Retorna o menor nome de uma lista de nomes

def menor_nome(nomes:list):
    menor = nomes[0]
    for nome in nomes:
        nome_c = nome.strip()
        if len(nome_c) < len(menor):
            menor = nome_c

    return menor.capitalize()
