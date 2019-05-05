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
    # Sigmoid function considering the inputs
    fnet = 1 / (1 + exp(-(net)))
    return (fnet)

# Main programm
#training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
Ninp = 2
Neu1a = 2
Nout = 1
weights =[]     # Define weights as matrix of synaptic weights for all the neurons
netf = []       # Define netf as matrix for the results of net funciotn
dweights = []   # Define dweights as matrix for delta weights results of backpropagation
inputslay = []  # Define inputslay as matrix for inputs in each layer
e = [[],[],[]]          # Define e as matrix of error for each layer
RNAlay = [[1,2],[3]]
txlearning = 0.4


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
weights = ([[0.5, 0.4], [-0.1, 0.3], [1, 0.01]])

# Define and clear inputs of each layer
last = 0
inputslay.append(inputs)

# Calculing the neurons output for each layer
for layer in range(len(RNAlay)):

    # Get the weights of each layer
    weightsl = []
    [weightsl.append(weights[i+last]) for i in range(len(RNAlay[layer]))]
    last = len(RNAlay[layer])                                               # Get the length to sum on next weights calculation

    netf.append (net(inputslay[layer], array(weightsl).T))                  # Append on netf the net results
    inputslay.append(fnet(netf[layer]))                                     # Append on matrix the neurons output

print (netf, inputslay)

# Calculating the error for each layer
delta = output - inputslay[len(RNAlay)]

for layer in range (len(RNAlay), 0, -1):
    #e[layer] = delta * fnet(netf[layer - 1]) * 1- fnet(netf[layer - 1])
    e[layer] = delta * inputslay[layer] * (1 - inputslay[layer])
    print(layer, delta, inputslay[layer], e[layer], weights[layer])
    delta = e[layer] * weights [layer]

#, fnet(netf[layer]) , (1 - fnet(netf[layer])))
print ('e',e)

#e = (output - inputsl) * fnet(out) * (1 - fnet(out))
#dweights.append(txlearning * e * function[0])
#print (dweights)
#e1 = e * weights[2] * function[0] * (1- function[0])
#print (e1)
#dweights.append(txlearning * e1 * inputs)
#print (txlearning, e1 , inputs)
#weights = txlearning * e * function

#print (e)

#for iteration in range(10000):
#    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
#    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
#print (1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights)))))


#fnet = 0
#f_ativ = lambda x: 1.0 / (1 + np.power(np.e, -x))


