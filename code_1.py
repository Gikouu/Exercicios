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

#Uma função que conta as vogais ou consoantes dependendo da opção escolhida

def conta_letras(frase:str, contar:str="vogais"):
    contador = 0
    if contar == 'consoantes':
        for letra in frase:
            if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u' and letra != ' ':
                contador += 1
    else:
        for letra in frase:
            if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
                contador += 1

    return contador

#Função que retorna a menor palavra na ordem lexicográfica

def primeiro_lex(lista:list[str]):
    menor = lista[0]
    for palavra in lista:
        if palavra < menor:
            menor = palavra

    return menor

#Criando triângulo + perimetro + tipo

class Triangulo:
    def __init__(self , a , b , c) -> None:

        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self) -> int:

        return self.a + self.b + self.c

    def tipo_lado(self) -> str:

        if self.a == self.b and self.a == self.c:
            return 'equilátero'
        elif self.a != self.b and self.a != self.c and self.b != self.c:
            return 'escaleno'
        else:
            return 'isósceles'
        
    def retangulo(self) -> bool:

        if (self.a * self.a + self.b * self.b) == (self.c * self.c):
            return True
        else:
            return False

    def semelhantes(self, Triangulo):
        lados = []
        lados_2 = []
        razao = []
        check = True

        lados_2.append(Triangulo.a)
        lados_2.append(Triangulo.b)
        lados_2.append(Triangulo.c)
        lados.append(self.a)
        lados.append(self.b)
        lados.append(self.c)

        for i in range(3):
            elemento = lados[i] / lados_2[i]
            razao.append(elemento)

        for i in range(2):
            if razao[i] == razao[i+1]:
                check = True
            else:
                check = False
        
        if check == True:
            return True
        else:
            return False

#Confere ordenação da lista

def selecao_direta(lista):
    fim = len(lista)
    for i in range(fim - 1):
        posicao_do_minimo = i
        for j in range(i + 1, fim):
            if lista[j] < lista[posicao_do_minimo]:
                posicao_do_minimo = j
        lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
    return lista

def copia_lista(lista):
    lista_copia = []
    for i in range(len(lista)):
        lista_copia.append(lista[i])
    return lista_copia

def ordenada(lista):
    lista_normal = copia_lista(lista)
    lista_ordenada = selecao_direta(lista)
    for i in range(len(lista)):
        if lista_normal[i] == lista_ordenada[i]:
            pass
        else:
            return False
    return True

#Busca sequencial

def  busca(lista, elemento):

    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False

#Gerador de listas com números aleatórios

import random

def lista_grande(n):
    lista = []
    for i in range(n):
        numero_aleatorio = random.randint(1, 100)
        lista.append(numero_aleatorio)
    return lista
