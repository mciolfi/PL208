# New DSNN MLP test
# Import libraries to open csv file and matrix operators
import csv
from numpy import exp, array, random, dot

# Define Neuron as class with name, inputs, weights and type
class neuron:
    def __init__(self, layer, neuNumber, INPUTS, WEIGHTS, actFunc):
        self.layer = layer
        self.neuNumber = neuNumber
        self.INPUTS = INPUTS
        self.WEIGHTS = WEIGHTS
        self.actFunc = actFunc
        self.output = func(net(INPUTS, WEIGHTS), actFunc)


# Function to multiply inputs and weights
def net(INPUTS, WEIGHTS):
    return dot(array(WEIGHTS).T, INPUTS)

# Function to enable the neuron
def func(net, actFunc):
    print (net)
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

# Function to define the Neural network type
def archtype(archtetureType, NEU, INPT, WIEGHTS):
    INPUTS = []
    if archtetureType == 'RNN':
        if len(INPT) > 0:
            [INPUTS.append(INPT[n]) for n in range(len(INPT)-1)]
        INPUTS2 = []
        [INPUTS2.append(INPT[len(INPT) - 1][n]) for n in range(len(INPT[len(INPT) - 1]))]
        [INPUTS2.append(0) for n in range(len(WIGHTS[len(NEU)])-len(INPT[len(INPT) - 1]))]
        INPUTS.append(INPUTS2)
    else:
        [INPUTS.append(INPT[0][n]) for n in range(len(INPT[len(INPT) - 1]))]
    print('Output Archtype', INPUTS)
    return INPUTS

# Derivation Function to enable the neuron
def dFunc(net, actFunc):
    if actFunc == 'Sig':
        fnet = net * (1 - net)
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
def feedForward(archtetureType, NEU, nLayer, ANNLAYOUT, nInputs, INPUTS, WEIGHTS):
    for layer in range(nLayer + 1):
        for countNeu in range(len(ANNLAYOUT[layer])):
            if archtetureType == 'RNN':
                if countNeu > 0:
                    INPUTS[layer][nInputs + len(NEU) - 1] = NEU[len(NEU) - 1].output
            NEU.append([])
            print('data', layer, countNeu, len(NEU) - 1, INPUTS, WEIGHTS[len(NEU) - 1])
            NEU[len(NEU) - 1] = neuron(layer, countNeu, INPUTS, WEIGHTS[len(NEU) - 1], 'Sig')
            print('Neuron', len(NEU) - 1, '=', NEU[len(NEU) - 1].output)
        print ('add', INPUTS)
        INPUTS.append([NEU[i].output for i in range(len(NEU) - len(ANNLAYOUT[layer]) , len(NEU))])
        #INPT = INPUTS
        print('input', INPUTS)

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
nInput, nOutput, nLayer, NEU, INPUTS = 2, 1, 2, [], []
ANNLAYOUT = [[1, 2, 3], [4, 5, 6], [7]]
INPT = [[2, 1]]
OUTPT = [0]
# Define the ANN achteture type
archtetureType = 'MLP'
# MLP = Each neuron receives inputs from previous layer and give output to the next layer
WEIGHTS = [[0.5, 0.4], [-0.1, 0.3], [1, 0.01], [0.5, 0.4], [-0.1, 0.3], [0.5, 0.3], [0.4, 0.2]]
# RNN = Each neuron receives inputs from previous layer and other neurons from same layer and give output to the next layer
# weights = [[0.5, 0.4, 0.3, 0.4], [-0.1, 0.3, 0.2, -0.3], [1, 0.01, 0.1, 1], [0.5, 0.4, 0.3, 0.5, 0.1], [-0.1, 0.3, 0.2, 0.7], [-0.1, 0.3, 0.2, -0.3], [1, 0.01, 0.1, 1]]
INPUTS = archtype(archtetureType, NEU, INPT, WEIGHTS)
learningRate = 0.4


# Main program
# inputs = archtype(archtetureType, inpt, inputs, weights)
# exploreNNA()
# generateWeights()
# backPropagation(archtetureType, neu, nLayer, ANNLayout, inpt, outpt, weights, learningRate)
feedForward(archtetureType, NEU, nLayer, ANNLAYOUT, nInput, INPUTS, WEIGHTS)
#feedBackward(nNeu, nLayer, ANNLayout, inpt, outpt, weights)

# Function set properties for each Neuron 
#a = NNAv(nInpt, nOutput, nLayer)
