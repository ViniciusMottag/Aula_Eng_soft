cont = 1
lista=[]
while True:
    nome=input('%dº nome: '%cont)
    if nome =='@':
        break
    lista.append(nome)
    cont += 1

max_tamanho=0
for i,nome in enumerate(lista):
    if len(nome)>max_tamanho:
        max_tamanho=len(nome)
        max_nome =nome
        max_i = i
        
print("Maior nome: %s, com %d letras, na posição %d "%(max_nome,max_tamanho,max_i))
    
