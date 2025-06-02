numero = (5, 8, 12, 8, 7, 8, 3)
#para ser uma tupla precisa estar entre parenteses !!
print("tupla original:" , numero)
#imprimido para o usuario a tupla original, sem manipulaçoes
print ("tamanho da tupla:" , len (numero)) 
print("acessado pelo indice ", numero[2])
#escolhendo qual indice sera mostrado atraves do indice,lembrando que comeca do zero
print("fazendo slincing do 2 ao 5", numero[2:5])
#ao slicing ele nao pega o ultimo item definido no recorte
print("quantas vezes o numero 8 repete", numero.count(8),"vezes")
print("posicao da primeira ocorrencia do numero 7:", numero.index(7))
minimo_tupla=min(numero)
print(minimo_tupla)
maximo_tupla=max(numero)
print("maior numero dentro da tupla é:", maximo_tupla)
print("maior numero dentro da tupla é:",sum(numero))
tupla_ordenada=sorted(numero)
print("os numeros em ordem ultilizando o metodo sorted", tupla_ordenada)
print("o numero 4 esta na tupla ?", 4 in numero)
numero2=(15,20)
tupla_concatenada=numero+numero2
print("a concatenaçao das tuplas 1 e 2 resultada na nova tupla:", tupla_concatenada)
tupla_duplicada=numero*2
print(tupla_duplicada)