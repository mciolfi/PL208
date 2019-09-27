# New MLP test
# Import libraries to open csv file and matrix operators
import csv
from numpy import exp, array, random, dot

# Define Neuron as class with name, inputs, weights and type
class neuron:
    def __init__(self, layer, neuNumber, inpt, weight, actFunc):
        self.layer = layer
        self.neuNumber = neuNumber
        self.input = inpt
        self.weight = weight
        self.actFunc = actFunc
        self.output = func(net(inpt, weight), actFunc)


# Function to multiply inputs and weights
def net(inpt, weight):
    return dot(array(weight).T, inpt)

# Function to enable the neuron
def func(net, actFunc):
    if actFunc == 'Sig':
        fnet = 1 / (1 + exp(-(net)))
    elif actFunc == 'Tan':
        fnet = tanh(net)
    return(fnet)

# Function to enable the neuron
def dfunc(net, actFunc):
    if actFunc == 'Sig':
        fnet = fnet * (1 - net)
    elif actFunc == 'Tan':
        fnet = 1 - (tanh(net)) ** 2
    return(fnet)

# Function to record inputs by layer
def newLayer():
    for i in range(1,3):   
        inpt.append(nNeu[i].output)

def NNAV(nInpt, nOutput, nLayer):
    for i in range(nLayer):
        for j in range(2):
            print('N', i, j)

# Explore more layers and Neurons
# def exploreNNA():

# Randomize weights by synapses
# def generateWeights(nInput, nOutput):

# Function update the weights
# def updateWeights()
# error = t - o
# deltaW = n * (error)

# Function back propagation
#def backPropagation()

# Function Feed-Foward
#def feedForward()

# Function Feed-Backward
#def feedBackward()

# Input data
nInpt, nOutput, nLayer, nNeu, inputs = 2, 1, 2, [[]], []
ANNLayout = [[1, 2], [3, 4], [5]]
inpt = [[2, 1]]
outpt = [0]
weights = [[0.5, 0.4], [-0.1, 0.3], [1, 0.01], [1, 1], [1, 1]]
archtetureType = 'MLP'
learningRate = 0.4


# Main program
# exploreNNA()
# generateWeights()
# backPropagation()

# Function set properties for each Neuron 
#a = NNAv(nInpt, nOutput, nLayer)
for layer in range(nLayer + 1):
    for neu in range(len(ANNLayout[layer])):
        nNeu.append([])
        nNeu[len(nNeu) - 2] = neuron(layer, neu, inpt[layer], weights[len(nNeu) - 2], 'Sig')
        print(len(nNeu) - 2, layer, neu, nNeu[len(nNeu) - 2].output)
    if layer < nLayer:
        inpt.append([nNeu[i].output for i in range(len(ANNLayout[0]))])
    print(inpt)
