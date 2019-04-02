def soma(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] +soma(lista[1:])

print(soma([1,2,3,4,5,6,7]))

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
