pilha=[]

def push(p,elemento,tipo=str):
    if type(elemento)==tipo:
        p.append(elemento)


def pop(p):
    return p.pop() if len(p) >0 else None

def palindrono(s):
    n=0
    nega=-1
    lista=list(s)
    tamanho=len(lista)
    resultado=tamanho%2
    if resultado==0:#se a pilha for de tamanho par
        for c in lista:
            push(pilha,c)
        if pilha[-1]==pilha[0]:
            return True
        else:
            return False
    else:#se a pilha for de tamanho impar
        for c in lista:
            push(pilha,c)
        for c in lista:
            if pilha[n]==pilha[nega]:
                pass
            else:
                return False
            n=n+1
            nega=nega-1
        return True
            

            
s='testt'
print(palindrono(s))

