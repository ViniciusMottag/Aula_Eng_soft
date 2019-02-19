def max2(a,b,c):
    return a if a>b else b    

def max3(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >=c:
        return b
    else:
        return c
print(max3(9,9,7))

def max3v2(a,b,c):
    return max2(max2(a,b),c)

l1 =[1,2,3,4]
def min_lista(lista):
    menor= lista[0]
    for elemento in lista:
        if elemento < menor:
            menor = elemento
    return menor
print(min_lista(l1))

def is_list(obj):
    if type(obj)==list:
        return True
    else:
        return False
lista=[2]
print(is_list(lista))

def soma_primeiro_ultimo(lista):
    return lista[0] + lista[-1]
print ("Soma ods elemtnos da lista"+lista+"="+soma_primeiro_ultimo(lista))

def mean(lista):
    soma = 0
    for elementos in lista:
        soma = soma + elementos
    return soma/len(lista)
print(mean(lista))


lista=[1,2,'avc','cd',2,3]
def extrai_strings(lista):
    l_string=[]
    for elemento in lista:
        if type(elemento)==str:
            l_string.append(elemento)
    return l_string
print(extrai_strings(lista))

def verifica_peca(valor):
    for elemento in valor:
        if elemento >6 or type(elemento)==str or len(valor)>2 or elemento <0 or type(elemento)==float:
            return False
        else:
            return True
p1=(-1,0)
print(verifica_peca(p1))

def verifica_peca2(p):
    return type(p)==tuple and\
           len(p)==2 and\
           type(p[0])== int and\
           type(p[1])== int and\
           0 <= p[0] <=6 and\
           0 <= p[1] <= 6
