# New MLP test
# Import library to open csv file and matrix operators
import csv
from numpy import exp, array, random, dot

# Define Neuron as class with name, inputs and weights
class neuron:
    def __init__(self, name, inpt, weight, tp):
        self.name = name
        self.input = inpt
        self.weight = weight
        self.type = tp
        self.output = func(net(inpt, weight))


# Function to multipli inputs and weights
def net(inpt, weight):
    output = dot(weight, inpt)
    return (output)

def func(fnet):
    f = 1 / (1 + exp(-(fnet)))
    return(f)
    #else: #tp == tan:
        #f = tanhip (net(inpt, weight))
#    return (f)

# def weightstart(nInput, nOutput):


# Main program
nInpt, nOutput, nLayer, nL, nNeu, inputs = 2, 1, 1, [2], [[]], []
inpt = [2, 1]
outpt = [2]
weights = [[0.5, 0.4], [-0.1, 0.3], [1, 0.01]]

for neu in range(1,3):
    nNeu.append([])
    nNeu[neu] = neuron(neu, inpt, weights[neu-1], 0)
    print (nNeu[neu].output)
for i in range(1,3):
    inputs.append(nNeu[i].output)
nNeu.append([])
nNeu[3] = neuron('3', inputs, weights[2], 0)
print(nNeu[3].output)
#nNeu[2] = neuron('2', inpt, weights[1], 0)

#print (n[1].weight)
#print (net(inpt, weights))