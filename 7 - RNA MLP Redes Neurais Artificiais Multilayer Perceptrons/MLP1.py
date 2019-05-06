import numpy as np
from numpy import exp, array, random, dot


# Class definition of a generic neuron
class Neuron(object):
    def __init__(self, weights, fnet):
        self.weights = weights          # Weights array
        self.fnet = fnet                # Define type of function that represent the neuron function


def matrix_gen (n_lines, n_columns):
    return [[((j+1)+i*n_columns) for j in range(n_columns)] for i in range(n_lines)]

# Threshold function: Binary result
def linear(inputs, weights):
    output = dot(inputs, weights)  # Multiply the inputs with weights
    for cont in range(len(output)):
        if output[cont][0] > 0.5:
            output[cont][0] = 1  # Establishes the value of 0.5 as a limit for binary
        else:
            output[cont][0] = 0
    return (output)

# Multiply input and weights
def net (inputs, weights):
    return (dot(inputs, weights))

# Threshold function: Sigmoid
def fnet(net):
    fnet = 1 / (1 + exp(-(net)))        # Sigmoid function considering the inputs
    return (fnet)

# Main programm
#training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
Ninp = 2
Neu1a = 2
Nout = 1
RNAlay = [[1,2],[3]]
learningrate = 0.4


Nstart = int(round((Ninp + Nout) / 2 , 0))
#Nneurons = matrix_gen (Nlay,Nstart)
#print (Nneurons)

# Applying the inputs and the desired outputs
# inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
inputs = array([2,1])
#training_set_outputs = array([[0, 1, 1, 0]]).T
output = array([2]).T
random.seed(1)

# Defining random weights by synapt connection numbers
# weights = 2 * random.random(((len(inputs[0]), 2)) - 1)
# weights = 2 * random.random((len(inputs[0]), Neu1a)) - 1
# weights = []  # Define weights as matrix of synaptic weights for all the neurons
weights = ([[0.5, 0.4], [-0.1, 0.3], [1, 0.01]])

for iteration in range(100):

    # Define and clear the matrix
    netf = []       # Define results of net function matrix
    dweights = []   # Define delta weights matrix results of backpropagation
    inputslay = []  # Define inputs in each layer matrix
    e = [[], []]    # Define error matrix for each layer

    # Define and clear inputs of each layer
    last = 0
    inputslay.append(inputs)

    # Calculing the neurons output for each layer
    for layer in range(len(RNAlay)):
        weightsl = []                                           # Get the weights of each layer
        [weightsl.append(weights[i + last]) for i in range(len(RNAlay[layer]))]
        last = len(RNAlay[layer])                               # Get the length to sum on next weights calculation
        netf.append(net(inputslay[layer], array(weightsl).T))   # Append on netf the net results
        inputslay.append(fnet(netf[layer]))                     # Append on matrix the neurons output

    # Calculating the error for each layer
    delta = output - inputslay[len(RNAlay)]
    for layer in range(len(RNAlay), 0, -1):
        e[layer - 1] = delta * inputslay[layer] * (1 - inputslay[layer])
        delta = e[layer - 1] * weights[layer]

    # Show iteration number and the result of last neuron
    print(iteration,inputslay[len(inputslay) - 1])

    del (inputslay[len(inputslay) - 1])     # Delete the last result of inputs matrix
    dweights = []                           # Define and clean delta weights matrix
    count = 0                               # Define a count as zero
    for i in range(len(weights) - 1):
        for j in range(len(weights[0])):
            # Count iteration and add on delta weights matrix until the count number be the length of layers
            count += 1
            dweights.append([learningrate * e[i][j] * inputslay[i][0], learningrate * e[i][j] * inputslay[i][1]])
            if count == len(RNAlay) + 1:
                break
    # dweights.append([txlearning * e[0][0] * inputslay[0][0], txlearning * e[0][0] * inputslay[0][1]])
    # dweights.append(txlearning * e[0][1] * inputslay[0][0], txlearning * e[0][1] * inputslay[0][1])
    # dweights.append(txlearning * e[1][0] * inputslay[1][0], txlearning * e[1][0] * inputslay[1][1])
    
    # Add to weight the delta weights resulted by the error on backpropagation
    weights = [[weights[i][j] + dweights[i][j] for j in range(len(weights[0]))] for i in range(len(weights))]