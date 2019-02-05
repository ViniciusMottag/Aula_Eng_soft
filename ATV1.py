qtd_l=int(input('Digite o tamanho da lista: '))
lista=[0,]*qtd_l

for i in range(qtd_l):
    lista[i]=int(input("Valor %d: "%(i+1)))

soma = 0
#soma_str=''

for i in lista:
    soma+=i
    #soma_str+=str(i)+'+'
#soma_str=soma_str[:-1]
soma_str=str(lista)[1:-1].replace(',','+')
print("A soma %s resulta em %d"%(soma_str,soma)