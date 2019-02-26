pilha=[]
def push(p,elemento,tipo=str):
    if type(elemento)==tipo:
        p.append(elemento)


def pop(p):
    return p.pop() if len(p) >0 else None
## 2 listas 1 pilha
def palindrono(s):
    lista=list(s)
    tamanho=len(lista)
    lista_direita=()
    meio=tamanho//2
    for c in lista:
        push(pilha,c)
        if len(pilha)==meio:
            pass
    for valor in range(-1):
        aplica=lista.index(valor)
        lista_direita.append(aplica)
        meio=-meio-1
    return lista_direita
    

s='ovoooo'
print(palindrono(s))
