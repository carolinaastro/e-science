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

print('mean inflammation:'data.mean())
print('maximum inflammation:', data.max())
print('minimum inflammation:', data.min())
print('standard deviation:', data.std())

patient_0 = data[0, :] # 0 on the first axis, everything on the second
print('maximum inflammation for patient 0:', patient_0.max())
