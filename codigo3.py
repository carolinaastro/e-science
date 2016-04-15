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
