saudation= 'hello'
#print saudation[0], saudation[1], saudation[2], saudation[3], saudation[4]
#for i in saudation:
# print saudation[i]
saudation= 'hello'
my_list = []
for i in saudation: #para os indices do string
    for c in i: #conteudo do indice
        my_list.extend(c) #a nova lista recebe os conteudos, formando uma nova lista
        
print my_list  #printar nova lista
'''
Tuples and exchanges
Explain what the overall effect of this code is:

left = 'L'
right = 'R'

temp = left #a variavel temp recebe o conteudo da variavel left, então temp = 'L'
left = right #a variavel left recebe o conteudo da variavel right, então left = 'R'

right = temp #a variavel right recebe o conteudo da variavel temp, então right = 'L'

temp= 'L'
left='R'
right= 'F'
Compare it to:

left, right = right, left #answer= 'R''R'
Do they always do the same thing? Which do you find easier to read?
#Não fazem sempre a mesma coisa, a primeira forma é mais facil de ler

'''      
