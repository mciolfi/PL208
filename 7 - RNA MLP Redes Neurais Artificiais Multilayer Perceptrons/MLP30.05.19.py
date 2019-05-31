__author__ = 'Márcio Ciolfi'
__copyright__ = 'Copyright 2019, ML'
__license__ = 'Ciolfi'
__version__ = '1.0'
__maintainer__ = 'Márcio Ciolfi'
__email__ = 'ciolfi@gmail.com'
__course__ = 'PL208'
__username__ = 'mciolfi'
__description__ = 'MLPerceptron using Iris dataset'
__status__ = 'Development'

import numpy as np
from numpy import exp, array, random, dot


# Class definition of a generic neuron
class Neuron(object):
    def __init__(self, weights, fnet):
        self.weights = weights          # Weights array
        self.fnet = fnet                # Define type of function that represent the neuron function


# Open dataset
def arq(name, ndata, types):
    import csv

    listt = []  # Define listt as matrix
    with open(name, newline='') as csvfile:  # csv module will detect new lines
        if types == ' ':  text = csv.reader(csvfile, delimiter=' ')  # classify by space
        if types == ',':  text = csv.reader(csvfile, delimiter=',')  # classify by comma
        if types == '\t': text = csv.reader(csvfile, delimiter='\t') # classify by tab
        for line in text:
            for t in range(len(line) - ndata): line.remove('')  # Removes zeros inside data
            listt.append(line)  # Define listt as the data inside file
    return (listt)

# Matrix generation
def matrix_gen (n_lines, n_columns):
    return [[((j+1)+i*n_columns) for j in range(n_columns)] for i in range(n_lines)]


# Multiply input and weights
def net(inputs, weights):
    return (dot(inputs, weights))

# Threshold function: Sigmoid
def fnet(net):
    fnet = 1 / (1 + exp(-(net)))        # Sigmoid function considering the inputs
    return (fnet)

# Perceptron with 4 inputs (4 Neuron) and 1 output (1 Neuron)
def perceptron(inputs, training_set_outputs, learningrate):
    weights = random.random((len(inputs[0]), 1))                        # Define the initial weight as random
    weightsold = [[0] for a in range(len(inputs[0]))]                   # Define matrix to save old weights value
    iteration = 0                                                       # Define variable iteration
    # Learning iteraction until 10000 or when the weights stops to change
    while iteration < 10000 and \
            max(abs(weightsold - weights))[0] > 0.001:
        iteration += 1                                                  # Count iteration number
        output = fnet(net(inputs, weights))                             # Output = sigmoid thresold
        #print (output)
        for i in range(len(weights)): weightsold[i][0] = weights[i][0]  # Save old weights
        print (training_set_outputs, output)
        weights += learningrate * dot(inputs.T, (training_set_outputs - output))  # Weights update
    print('#Iteration =', iteration)
    print('Weights =', weights.T)
    print('Expected value =', training_set_outputs.T)
    final_test = fnet(net(inputs, weights)).T == training_set_outputs.T # Check if the inputs plus weights = outputs
    if min(final_test[0]):
        print('Final value =', fnet(net(inputs, weights)).T, 'Learned!\n')  # If all results are true then has been learned
    else:
        print('Final value =', fnet(net(inputs, weights)).T, 'NOT Learned!\n')

# Prepare the inputs and training outputs matrix
def dataconv(file, cols, tab):
    listt = array(arq(file, cols, tab))                                 # Define listt as the data inside the file
    inputs = []
    training_set_outputs = []
    for cont in range(len(listt)):
        # Define one neuron for each classification: Iris-setosa = [1,0,0] ,Iris-versicolor = [0,1,0], ,Iris-virginica = [0,0,1]
        if listt[cont][cols-1] == 'Iris-setosa':
            inputs.append([float(listt[cont][i]) for i in range(cols-1)])
            training_set_outputs.append([1,0,0])
        if listt[cont][cols-1] == 'Iris-versicolor':
            inputs.append([float(listt[cont][i]) for i in range(cols-1)])
            training_set_outputs.append([0,1,0])
        if listt[cont][cols-1] == 'Iris-virginica':
            inputs.append([float(listt[cont][i]) for i in range(cols-1)])
            training_set_outputs.append([0,0,1])
    inputs = array(inputs)                                                  # Define inputs as matrix to transpose after
    training_set_outputs = array(training_set_outputs)                      # Define outputs as matrix to transpose after
    return (inputs, training_set_outputs)

# Main programm
inputs, training_set_outputs = dataconv('iris.data.txt', 5, ',')
#print('Iris')
learningrate = 0.4  # Define learning rate
#perceptron(inputs, training_set_outputs, learningrate)  # Run perceptron

Ninp = 4
Neu1a = 4
Nout = 3
RNAlay = [[1,2,3,4],[5,6,7,8],[9,10,11]]

Nstart = int(round((Ninp + Nout) / 2 , 0))
#Nneurons = matrix_gen (Nlay,Nstart)
#print (Nneurons)

# Defining random weights by synapt connection numbers
random.seed(1)
weights = 2 * random.random((len(RNAlay), len(inputs[0]))) - 1
#print(weights,'test')


for iteration in range(10000):

    # Define and clear the matrices
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
        #print(last, weights[0 + last], len(RNAlay[layer]))
        [weightsl.append(weights[i + last]) for i in range(len(RNAlay[layer])-2)]
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
    # dweights.append([learningrate * e[0][0] * inputslay[0][0], learningrate * e[0][0] * inputslay[0][1]])
    # dweights.append(learningrate * e[0][1] * inputslay[0][0], learningrate * e[0][1] * inputslay[0][1])
    # dweights.append(learningrate * e[1][0] * inputslay[1][0], learningrate * e[1][0] * inputslay[1][1])

    # Add to weight the delta weights resulted by the error on backpropagation
    weights = [[weights[i][j] + dweights[i][j] for j in range(len(weights[0]))] for i in range(len(weights))]