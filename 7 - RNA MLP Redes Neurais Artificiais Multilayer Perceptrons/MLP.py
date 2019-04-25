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

def Ninput(inputs, weights):
    output = 1 / (1 + exp(-(dot(inputs, weights))))
    print ('saida',output)
    return (output)

# Main programm
#training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
Ninp = 3
Neu1a = 2
Nlay = 2
Nout = 3
#weights =[]
Nstart = int(round((Ninp + Nout) / 2 , 0))
Nneurons = matrix_gen (Nlay,Nstart)
print (Nneurons)

# Applying the inputs and the desired outputs
inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T
random.seed(1)

# Defining randomic weights by synapt connection numbers
#weights = 2 * random.random(((len(inputs[0]), 2)) - 1)
weights = 2 * random.random((len(inputs[0]), Neu1a)) - 1
print (weights)
Ninput(inputs, weights)

    #Ninput(inputs, weights[i])

#for iteration in range(10000):
#    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
#    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
#print (1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights)))))


fnet = 0
f_ativ = lambda x: 1.0 / (1 + np.power(np.e, -x))


