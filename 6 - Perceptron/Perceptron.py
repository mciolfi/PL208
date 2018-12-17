# Threshold function: Binary result
def linear (inputs,weights):
    output = dot(inputs,weights)    #Multiply the inputs with weights
    for cont in range(len(output)):
        if output[cont][0] > 0.5: output[cont][0] = 1   # Establishes the value of 0.5 as a limit for binary
        else: output[cont][0] = 0
    return (output)

# Perceptron with 2 inputs (2 Neuron) and 1 output (1 Neuron)
def perceptron (inputs, training_set_outputs, txlearning):
    random.seed(1)
    weights = random.random((len(inputs[0]), 1))        # Define the initial weight as random
    weightsold = [[0]] * len(inputs[0])                 # Define matrix to save old weight value
    iteration = 0
    while iteration < 100 and max(abs(weightsold-weights))[0] > 0.01:      # Learning iteraction until 500 or when the weights stop to change
        iteration += 1
        output = linear(inputs,weights)                                         # Output = linear thresold
        #for i in range (len(weights)): weightsold [i][0] = weights[i][0]
        weightsold [0][0] = weights [0][0]
        weightsold [1][0] = weights [1][0]
        weights += txlearning * dot(inputs.T,(training_set_outputs.T - output)) # Weights update
        print (max(abs(weightsold-weights))[0],weightsold,weights)
    print('#Iteration =',iteration)
    print('Weights =',weights.T)
    print('Expected value =',training_set_outputs)
    final_test = linear(inputs,weights).T == training_set_outputs
    if min(final_test[0]): print ('Final value =',linear(inputs,weights).T,'Learned!')
    else: print ('Final value =',linear(inputs,weights).T,'NOT Learned!')
    print ('\n')

from numpy import exp, array, random, dot
# 2 entradas X1 e X2
inputs = array([[0, 0], [0, 1], [1, 0], [1, 1]])
txlearning = 0.01
#And
print ('AND Test')
training_set_outputs = array([[0, 0, 0, 1]])
perceptron (inputs, training_set_outputs, txlearning)
#OR
print ('OR Test')
training_set_outputs = array([[0, 1, 1, 1]])
perceptron (inputs, training_set_outputs, txlearning)
#XOR
print ('XOR Test')
training_set_outputs = array([[0, 1, 1, 0]])
perceptron (inputs, training_set_outputs, txlearning)
