import numpy
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
print (data)
print(type(data))
print(data.shape)
print('first value in data:', data[0, 0])
print('middle value in data:', data[30, 20])
print(data[0:4, 0:10])
print(data[5:10, 0:10])
small = data[:3, 36:]
print('small is:')
print(small)

doubledata = data * 2.0
print('original:')
print(data[:3, 36:])
print('doubledata:')
print(doubledata[:3, 36:])

tripledata = doubledata + data

print('tripledata:')
print(tripledata[:3, 36:])

print('mean inflammation:', data.mean())
print('maximum inflammation:', data.max())
print('minimum inflammation:', data.min())
print('standard deviation:', data.std())

patient_0 = data[0, :] # 0 on the first axis, everything on the second
print('maximum inflammation for patient 0:', patient_0.max())

print('maximum inflammation for patient 2:', data[2, :].max())

print(data.mean(axis=0)) #media diaria de inflamacoes

print(data.mean(axis=0).shape) #quantidade de dias

print(data.mean(axis=1)) #media de inflamacao por paciente

print(data.mean(axis=1).shape) #quantidade de pacientes

import matplotlib.pyplot
image  = matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show() #o objetivo eh mostrar os dados na forma grafica

ave_inflammation = data.mean(axis=0)
ave_plot = matplotlib.pyplot.plot(ave_inflammation)
matplotlib.pyplot.show() #grafico da evolucao da inflamacao com o tempo

max_plot = matplotlib.pyplot.plot(data.max(axis=0))
matplotlib.pyplot.show() #grafico da inflamacao maxima no decorrer dos dias
min_plot = matplotlib.pyplot.plot(data.min(axis=0))
matplotlib.pyplot.show() #grafico da inflamacao minima no decorrer dos dias

import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(data.mean(axis=0))

axes2.set_ylabel('max')
axes2.plot(data.max(axis=0))

axes3.set_ylabel('min')
axes3.plot(data.min(axis=0))

fig.tight_layout()

matplotlib.pyplot.show() #plot da media, minimo e maxima inflamacao por tempo na mesma figura

#Check your understanding

mass = 47.5
age = 122
mass = mass * 2.0
age = age - 20

print 'Nova massa', mass
print 'Nova idade', age

#Sorting out references
#What does the following program print out?

first, second = 'Grace', 'Hopper'
third, fourth = second, first
print(third, fourth)

#the program print => third=second= Hopper and fourth=first= Grace, so, Hopper and Grace

#Slicing strings

element = 'oxygen'
print('first three characters:', element[0:3])
print('last three characters:', element[3:6])

#What is the value of element[:4]? Todos os elementos ate o quarto: 'oxyg'
#What about element[4:]? Todos os elementos a partir do quarto, 'en'
#Or element[:]? 'oxygen'

#What is element[-1]? Representa o ultimo elemento 'n'
#What is element[-2]? Representa o penultimo elemento 'e'
#Given those answers, explain what element[1:-1] does. Printa do elemento 1 ate o penultimo, neste caso, 'xyge'


#Thin slices
#The expression element[3:3] produces an empty string, i.e., a string that contains no characters. 
#If data holds our array of patient data, what does data[3:3, 4:4] produce? Um vetor vazio pois o intervalo de um elemento ate ele mesmo eh nulo.
#What about data[3:3, :]? Tambem eh vazio pois nao tem como definir qual eh o intervalo entre a posicao inicial nula ate o final do array. 


#Make your own plot
#Create a plot showing the standard deviation (numpy.std) of the inflammation data for each day across all patients.

std_inflammation = numpy.std(data,axis=0)
std_plot = matplotlib.pyplot.plot(std_inflammation)
matplotlib.pyplot.ylabel('standart deviation')
matplotlib.pyplot.xlabel('days')
matplotlib.pyplot.show()

