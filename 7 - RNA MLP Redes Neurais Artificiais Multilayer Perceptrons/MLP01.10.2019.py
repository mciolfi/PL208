# New DSNN MLP test
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

        
# Function to define the Neural network type
def archtype(archtetureType, neu, inpt, weights):
    inputs = []
    if archtetureType == 'RNN':
        if len(inpt) > 0:
            [inputs.append(inpt[n]) for n in range(len(inpt)-1)]
        inputs2 = []
        [inputs2.append(inpt[len(inpt) - 1][n]) for n in range(len(inpt[len(inpt) - 1]))]
        [inputs2.append(0) for n in range(len(weights[len(neu)])-len(inpt[len(inpt) - 1]))]
        inputs.append(inputs2)
    else:
        inputs = inpt
    print('input', inputs)
    return inputs
        
# Function to multiply inputs and weights
def net(inpt, weight):
    print('mult', inpt, weight)
    return dot(array(weight).T, inpt)

# Function to enable the neuron
def func(net, actFunc):
    if actFunc == 'Sig':
        fnet = 1 / (1 + exp(-(net)))
    elif actFunc == 'Step':
         if net < 0:
            fnet = 0
        else:
            fnet = 1
    elif actFunc == 'Tan':
        fnet = tanh(net)
        # 2 / (1 + exp(-(2 * net)))
    elif actFunc == 'ReLu':
        if net < 0:
            fnet = 0
        else:
            fnet = net
    return fnet

# Derivation Function to enable the neuron
def dFunc(net, actFunc):
    if actFunc == 'Sig':
        fnet = net * (1 - net)
    elif actFunc == 'Tan':
        fnet = 1 - (tanh(net)) ** 2
    elif actFunc == 'Tan':
        fnet = 1 - (tanh(net)) ** 2  
    return fnet

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
def backPropagation(archtetureType, neu, nLayer, ANNLayout, nInputs, inpt, outpt, weights, learningRate):
    feedForward(archtetureType, neu, nLayer, ANNLayout, nInputs, inpt, weights)
    #print(len(nNeu), nNeu[2].output)
    feedBackward(archtetureType, neu, nLayer, ANNLayout, inpt, outpt, weights, learningRate)

# Function Feed-Forward
def feedForward(archtetureType, neu, nLayer, ANNLayout, nInputs, inpt, weights):
     for layer in range(nLayer + 1):
        print('teste1', inpt)
        inputs = archtype(archtetureType, neu, inpt, weights)
        for countNeu in range(len(ANNLayout[layer])):
            if archtetureType == 'RNN':
                if countNeu > 0:
                    inputs[layer][nInputs + len(neu) - 1] = neu[len(neu) - 1].output
            neu.append([])
            print('data', layer, countNeu, len(neu) - 1, inputs, weights[len(neu) - 1])
            neu[len(neu) - 1] = neuron(layer, countNeu, inputs[layer], weights[len(neu) - 1], 'Sig')
            print('Neuron', len(neu) - 1, '=', neu[len(neu) - 1].output)
        inputs.append([neu[i].output for i in range(len(neu) - len(ANNLayout[layer]) , len(neu))])
        inpt = inputs
        print('input', inputs)

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
nInput, nOutput, nLayer, neu, inputs = 2, 1, 2, [], []
ANNLayout = [[1, 2, 3], [4, 5, 6], [7]]
inpt = [[2, 1]]
outpt = [0]
# Define the ANN achteture type
archtetureType = 'RNN'
# MLP = Each neuron receives inputs from previous layer and give output to the next layer
# weights = [[0.5, 0.4], [-0.1, 0.3], [1, 0.01], [0.5, 0.4], [-0.1, 0.3]]
# RNN = Each neuron receives inputs from previous layer and other neurons from same layer and give output to the next layer
weights = [[0.5, 0.4, 0.3, 0.4], [-0.1, 0.3, 0.2, -0.3], [1, 0.01, 0.1, 1], [0.5, 0.4, 0.3, 0.5, 0.1], [-0.1, 0.3, 0.2, 0.7], [-0.1, 0.3, 0.2, -0.3], [1, 0.01, 0.1, 1]]
learningRate = 0.4


# Main program
# inputs = archtype(archtetureType, inpt, inputs, weights)
# exploreNNA()
# generateWeights()
# backPropagation(archtetureType, neu, nLayer, ANNLayout, inpt, outpt, weights, learningRate)
feedForward(archtetureType, neu, nLayer, ANNLayout, nInput, inpt, weights)
#feedBackward(nNeu, nLayer, ANNLayout, inpt, outpt, weights)

# Function set properties for each Neuron 
#a = NNAv(nInpt, nOutput, nLayer)
