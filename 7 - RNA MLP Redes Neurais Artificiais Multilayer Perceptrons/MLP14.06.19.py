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

import csv                                                              # Module to read csv file type
from numpy import exp, array, random, dot                               # Load functions


# Open dataset as csv file using the file name, columns number and type of delimiter between the datas
def arq(name, ndata, types):
    listt = []                                                          # Define listt as matrix
    with open(name, newline='') as csvfile:                             # csv module will detect new lines
        if types == ' ':  text = csv.reader(csvfile, delimiter=' ')     # classify by space
        if types == ',':  text = csv.reader(csvfile, delimiter=',')     # classify by comma
        if types == '\t': text = csv.reader(csvfile, delimiter='\t')    # classify by tab
        for line in text:
            for t in range(len(line) - ndata): line.remove('')          # Removes zeros inside data
            listt.append(line)                                          # Define listt as the data inside file
    return (listt)                                                      # Returns with the data inside file

# Weights Matrix generation using the inputs number and the RNA layout
def random_weights(Ninp, RNAlay):
    weights = []                                                        # Define weights as matrix
    ncols = [Ninp] * (len(RNAlay))                                      # Matrix w. synapse number for 1st layer
    for i in range(1, len(RNAlay)):
        ncols[i] = len(RNAlay[i - 1])                                   # Synapse number definition for next layers
    for i in ncols:
        for j in range(i):
            weights.append([(2 *random.random()-1)] * i)                # Random weights
    return weights,ncols                                                # Returns with Weights and synapse per layer

# Multiply input and weights
def net(inputs, weights):
    return dot(inputs, weights)                                         # Returns matrix multiplication results

# Threshold function: Sigmoid
def fnet(net):
    fnet = 1 / (1 + exp(-(net)))                                        # Sigmoid function considering the inputs
    return fnet                                                         # Returns Sigmoid results

# Prepare the inputs and training outputs matrix using file name, columns number and tab type
def dataconv(file, cols, tab):
    # Define inputs and training_set_outputs as matrix
    inputs = []
    training_set_outputs = []
    listt = array(arq(file, cols, tab))                                     # Define listt as the data inside the file
    # Check all file lines and assign one neuron for each classification:
    # Iris-setosa = [1,0,0] ,Iris-versicolor = [0,1,0], ,Iris-virginica = [0,0,1]
    for count in range(len(listt)):
        inputs.append([float(listt[count][i]) for i in range(cols - 1)])    # Add inputs at matrix
        if listt[count][cols-1] == 'Iris-setosa':                           # Last column = Setosa
            training_set_outputs.append([1,0,0])
        if listt[count][cols-1] == 'Iris-versicolor':                       # Last column = Versicolor
            training_set_outputs.append([0,1,0])
        if listt[count][cols-1] == 'Iris-virginica':                        # Last column = Virginica
            training_set_outputs.append([0,0,1])
    inputs = array(inputs)                                                  # Define inputs as matrix to transpose after
    training_set_outputs = array(training_set_outputs)                      # Define outputs as matrix to transpose aft.
    return (inputs, training_set_outputs)                                   # Returns inputs and training ser outputs


# Main programm
inputs, training_set_outputs = dataconv('iris.data1.txt', 5, ',')           # Gets the inputs and training outputs
learningrate = 0.4                                                          # Define learning rate

# Define the RNA layout
Ninp = 4
Nout = 3
RNAlay = [[1,2,3,4],[5,6,7,8],[9,10,11]]
Nstart = int(round((Ninp + Nout) / 2 , 0))

# Defining random weights by synapse connection numbers
random.seed(1)
weights,ncols = array(random_weights(Ninp, RNAlay))                         # Gets Weights and synapse connections

# Create a looping process to calcule feed-forward
for iteration in range(10000):
    # Define and clear the matrices
    netf = []                                                               # Define results of net function matrix
    dweights = []                                                           # Delta weights results of backpropagation
    inputslay = []                                                          # Define inputs in each layer matrix
    e = []                                                                  # Define error matrix for each layer

    # Define and clear inputs of each layer
    last = 0                                                                # Value step definition
    inputslay.append(inputs[0])                                             # Define inputs matrix

    # Calculing the neurons output for each layer
    for layer in range(len(RNAlay)):
        weightsl = []                                                       # Define weights of each layer
        [weightsl.append(weights[i + last]) for i in range(ncols[layer])]   # Get the weights of each layer
        last += len(RNAlay[layer])                                          # Get step to next weights calculation
        netf.append(net(inputslay[layer], array(weightsl).T))               # Append on netf the net results
        inputslay.append(fnet(netf[layer]))                                 # Append on matrix the neurons output
    inputslay.append(training_set_outputs[0])
    print('a',inputslay,'b')

    # Calculating the error for each layer
    delta = output - inputslay[len(RNAlay)]
    for layer in range(len(RNAlay), 0, -1):
        e[layer - 1] = delta * inputslay[layer] * (1 - inputslay[layer])
        delta = e[layer - 1] * weights[layer]

    # Show iteration number and the result of last neuron
    # print(iteration,inputslay[len(inputslay) - 1])

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