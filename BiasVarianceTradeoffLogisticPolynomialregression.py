import sys
import numpy
import matplotlib.pyplot as plt
from nltk.compat import raw_input

x = []
y = []
vs_x = []
vs_y = []

with open('training_x.txt', 'r') as f:
    for line in f:
        x.append(line.split('\n')[0])

with open('training_y.txt', 'r') as f:
    for line in f:
        y.append(line.split('\n')[0])

with open('cv_x.txt', 'r') as f:
    for line in f:
        vs_x.append(line.split('\n')[0])

with open('cv_y.txt', 'r') as f:
    for line in f:
        vs_y.append(line.split('\n')[0])

x = numpy.array(x, dtype=float)
x = numpy.column_stack((numpy.ones(len(x)), x))
x = numpy.matrix(x)
vs_x = numpy.array(vs_x, dtype=float)
vs_x = numpy.column_stack((numpy.ones(len(vs_y)), vs_x))
vs_x = numpy.matrix(vs_x)

y = numpy.matrix(y, dtype=float)
vs_y = numpy.matrix(vs_y, dtype=float)

def CalculateTheta(xData , yData):
    Coefficients = numpy.dot((numpy.dot((numpy.dot(xData.getT(), xData)).getI(), xData.getT())), yData.getT())
    return numpy.array(Coefficients)

def CalculateError(theta, yData, xData):
    sumSqError=0
    for i in range(0, numpy.size(yData)):
        sumSqError += ((numpy.math.pow((yData[0,i] - (theta[0] + (theta[1] * xData[i, 1]))), 2)) / ( 2 * numpy.size(yData)))
    return (sumSqError)

def CalculateError2(theta, yData, xData):
    sumSqError=0
    for i in range(0, numpy.size(yData)):
        sumSqError += ((numpy.math.pow((yData[0,i] - (theta[0] + (theta[1] * xData[i, 1]) + (theta[2] * xData[i, 2]) +(theta[3] * xData[i, 3]) +(theta[4] * xData[i, 4]) +(theta[5] * xData[i, 5]) +(theta[6] * xData[i, 6]))), 2)) / ( 2 * numpy.size(yData)))
    return (sumSqError)

def ExponentialList(power, list):
    return [i ** power for i in list]

TrainingError = []
ValidationError = []

for i in range(0, 11):
    xData = x[0:i+2, :]
    yData = y[:,0:i+2]
    TrainingError.append(CalculateError(CalculateTheta(xData, yData), yData, xData))
    ValidationError.append(CalculateError(CalculateTheta(xData, yData), vs_y, vs_x))
print(ValidationError)
print(TrainingError)
plt.plot([None, None] + TrainingError, marker='o', linestyle='-')
plt.plot([None, None] + ValidationError, marker='o')
plt.ylabel('Error')
plt.xlabel('No. of Rows')
plt.show()

temp = []
for i in range(2, 7):
    for j in range(0,12):
        #print(x[j,1])
        temp.append(numpy.math.pow(x[j,1], i))
    x = numpy.column_stack((x,(numpy.matrix(temp)).getT()))
    temp = []

TrainingError2 = []
ValidationError2 = []

for i in range(0, 11):
    xData = x[0:i+2, :]
    yData = y[:,0:i+2]
    TrainingError2.append(CalculateError(CalculateTheta(xData, yData), yData, xData))
    ValidationError2.append(CalculateError(CalculateTheta(xData, yData), vs_y, vs_x))
print(ValidationError2)
print(TrainingError2)

plt.plot([None, None] + TrainingError2, marker='o')
plt.plot([None, None] + ValidationError2, marker='o')
plt.ylabel('Error')
plt.xlabel('No. of Rows')
plt.show()
