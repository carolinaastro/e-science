import numpy
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
print (data)
print(type(data))
print(data.shape)
print('first value in data:', data[0, 0])
print('middle value in data:', data[30, 20])
