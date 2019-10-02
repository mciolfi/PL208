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

# Threshould function to enable the neuron
def func(net, actFunc):
    if actFunc == 'Sig':
        fnet = 1 / (1 + exp(-(net)))
    elif actFunc == 'Tan':
        fnet = tanh(net)
    return(fnet)

# Function to enable the neuron
def dFunc(net, actFunc):
    if actFunc == 'Sig':
        fnet = net * (1 - net)
    elif actFunc == 'Tan':
        fnet = 1 - (tanh(net)) ** 2
    return(fnet)

# Function to record inputs by layer
def newLayer():
    for i in range(1,3):   
        inpt.append(neu[i].output)

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
def backPropagation(neu, nLayer, ANNLayout, inpt, outpt, weights, learningRate):
    feedForward(neu, nLayer, ANNLayout, inpt, weights)
    #print(len(nNeu), nNeu[2].output)
    feedBackward(neu, nLayer, ANNLayout, inpt, outpt, weights, learningRate)

# Function Feed-Forward
def feedForward(neu, nLayer, ANNLayout, inpt, weights):
    for layer in range(nLayer + 1):
        for countNeu in range(len(ANNLayout[layer])):
            neu.append([])
            neu[len(neu) - 1] = neuron(layer, countNeu, inpt[layer], weights[len(neu) - 1], 'Sig')
            print(len(neu) - 1, layer, countNeu, neu[len(neu) - 1].output)
        #if layer < nLayer:
            #print (len(nNeu) - 1, len(ANNLayout[layer]))
        inpt.append([neu[i].output for i in range(len(neu) - len(ANNLayout[layer]) , len(neu))])
    print(inpt)

# Function Feed-Backward
def feedBackward(neu, nLayer, ANNLayout, inpt, outpt, weights, learningRate):
    dWeights = [[weights[i][j] for j in range(len(weights[i]))] for i in range(len(weights))]
    e = (outpt - neu[len(neu) - 1].output) * dFunc(net(neu[len(neu) - 1].input, neu[len(neu) - 1].weight), 'Sig')
    e2 = (outpt - neu[len(neu) - 1].output) * dFunc(net(neu[len(neu) - 1].input, neu[len(neu) - 1].weight), 'Sig')
    print(weights)
    for countNeu in range(len(ANNLayout[len(neu) - 2]) + 1):
        delta = learningRate * e * neu[countNeu].output
        print (float(delta))
        weights[len(neu) - 1][countNeu] -= float(delta)
    print(weights)
    #print (delta, e, outpt, - nNeu[len(nNeu) - 1].output, net(nNeu[len(nNeu) - 1].input, nNeu[len(nNeu) - 1].weight),  dFunc(net(nNeu[len(nNeu) - 1].input, nNeu[len(nNeu) - 1].weight), 'Sig'))
    #net(inpt, weight)
    #print(e, nNeu[len(nNeu) - 1].output, len(nNeu) - 1)
    #for layer in range(nLayer, -1 , -1):
        #for neu in range(len(ANNLayout[layer]) - 1, -1, -1):
            #print(layer, neu)
            #dWeights[layer][neu] = 1   
    #print(dWeights)

# Input data
nInpt, nOutput, nLayer, neu, inputs = 2, 1, 1, [], []
ANNLayout = [[1, 2], [3]]
inpt = [[2, 1]]
outpt = [2]
weights = [[0.5, 0.4], [-0.1, 0.3], [1, 0.01]]
archtetureType = 'MLP'
learningRate = 0.4


# Main program
# exploreNNA()
# generateWeights()
backPropagation(neu, nLayer, ANNLayout, inpt, outpt, weights, learningRate)
#feedBackward(nNeu, nLayer, ANNLayout, inpt, outpt, weights)

# Function set properties for each Neuron 
#a = NNAv(nInpt, nOutput, nLayer)

    