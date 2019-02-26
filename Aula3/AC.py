def verifica_peca(p):
    return type(p)==tuple and\
           len(p)==2 and\
           type(p[0])==int and\
           type(p[1])==int and\
           0 <= p[0] <= 6 and\
           0 <= p[1] <= 6

def conecta(p1,p2):
    return p1[-1] == p2[0]

def ler_arquivo(nome_do_arquivo,i):
    with open (nome_do_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    linha = linhas[i]
    peca = linha.replace('\n','').split(',')
    return tuple([int(x) for x in peca])

def len_arquivo(nome_do_arquivo):
    with open (nome_do_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    return len(linhas)

lista = len_arquivo("domino.dat")
lista2=ler_arquivo("domino.dat",3)
print(lista)
print(lista2,'\n')

''''def verifica_sequencia():
    for i in range (len_arquivo("domino.dat")):
        valor = ler_arquivo("domino.dat",i)
        if verifica_peca2(valor)==False:
            return False
        else:
            return True
'''
'''def verifica_sequencia():
    for i in range (len_arquivo("domino.dat")):
        v = ler_arquivo("domino.dat",i)
        for i2 in range(len_arquivo("domino.dat")):
             v2 = ler_arquivo("domino.dat",i)
             if (v[0] == v2[0] or v[1] == v2[0] or v[0] == v2[1] or v[1] == v2[1])==False:
                 return False
             else:
                return True
                 
'''
'''def verifica_sequencia():
    for i in range (len_arquivo("domino.dat")):
        v = ler_arquivo("domino.dat",i)
        v2 = ler_arquivo("domino.dat",i+1)
        if (v[0] == v2[0] or v[1] == v2[0] or v[0] == v2[1] or v[1] == v2[1])==False:
            return False
        else:
            return True
'''

    
def verifica_sequencia(valor):
    for i in range (len_arquivo(valor)):
        v = ler_arquivo("domino.dat",i)
        if not verifica_peca(v):
            print("valor invalido")
            break
        v2 = ler_arquivo("domino.dat",i+1)
        if not verifica_peca(v2):
            print("valor invalido")
            break
        if not conecta(v,v2):
            return False
        else:
            return True

print(verifica_sequencia("domino.dat"))
            
