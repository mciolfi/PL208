# New MLP test
# Import libraries to open csv file and matrix operators
import csv
from numpy import exp, array, random, dot

# Define Neuron as class with name, inputs, weights and type
class neuron:
    def __init__(self, name, inpt, weight, tp):
        self.name = name
        self.input = inpt
        self.weight = weight
        self.type = tp
        self.output = func(net(inpt, weight))


# Function to multiply inputs and weights
def net(inpt, weight):
    output = dot(array(weight).T, inpt)
    return (output)

# Fucntion to enable the neuron
def func(fnet):
    f = 1 / (1 + exp(-(fnet)))
    return(f)
    #else: #tp == tan:
        #f = tanhip (net(inpt, weight))
#    return (f)

# Function to record inputs by layer
def newLayer():
    for i in range(1,3):   
        inpt.append(nNeu[i].output)

def NNAV(nInpt, nOutput, nLayer):
    for i in range(nLayer):
        for j in range(2):
            print('N', i, j)


# def weightstart(nInput, nOutput):


# Main program
nInpt, nOutput, nLayer, nNeu, inputs = 2, 1, 1, [[]], []
h = [[1, 2], [3]]
inpt = [[2, 1]]
outpt = [0]
weights = [[0.5, 0.4], [-0.1, 0.3], [1, 0.01]]
#a = NNAv(nInpt, nOutput, nLayer)
for layer in range(nLayer + 1):
    for neu in range(1, len(h[layer]) + 1):
        nNeu.append([])
        nNeu[neu] = neuron(layer + neu, inpt[layer], weights[layer + neu - 1], 0)
        print(layer + neu, nNeu[layer + neu].output)
    inpt.append([nNeu[1].output, nNeu[2].output])
    print (layer,inpt)

for neu in range(1,3):
    inpt.append(nNeu[neu].output)
print(inpt)
newLayer()
nNeu.append([])
nNeu[3] = neuron('3', inputs, weights[2], 0)
print(nNeu[3].output)
#nNeu[2] = neuron('2', inpt, weights[1], 0)

#print (n[1].weight)
#print (net(inpt, weights))