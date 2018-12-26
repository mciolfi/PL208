# Threshold function: Binary result
def linear (inputs,weights):
    output = dot(inputs,weights)    #Multiply the inputs with weights
    for cont in range(len(output)):
        if output[cont][0] > 0.5:   output[cont][0] = 1   # Establishes the value of 0.5 as a limit for binary
        else:                       output[cont][0] = 0
    return (output)


# Perceptron with 2 inputs (2 Neuron) and 1 output (1 Neuron)
def perceptron (inputs, training_set_outputs, txlearning):
    weights = random.random((len(inputs[0]), 1))        # Define the initial weight as random
    weightsold = [[0] for a in range(len(inputs[0]))]   # Define matrix to save old weights value
    iteration = 0                                       # Define variable iteration
    while iteration < 100 and max(abs(weightsold-weights))[0] > 0.001:  # Learning iteraction until 100 or when the weights stop to change
        iteration += 1                                  # Count iteration number
        output = linear(inputs,weights)                 # Output = linear thresold
        for i in range (len(weights)): weightsold [i][0] = weights[i][0]        # Save old weights
        weights += txlearning * dot(inputs.T,(training_set_outputs - output)) # Weights update
    print('#Iteration =',iteration)
    print('Weights =',weights.T)
    print('Expected value =',training_set_outputs.T)
    final_test = linear(inputs,weights).T == training_set_outputs.T   # Check if the inputs plus weights = outputs
    if min(final_test[0]):  print ('Final value =',linear(inputs,weights).T,'Learned!\n')     # If all results are true then has been learned
    else:                   print ('Final value =',linear(inputs,weights).T,'NOT Learned!\n')

# Main program
from numpy import exp, array, random, dot
# 2 entradas X1 e X2
inputs = array([[0, 0], [0, 1], [1, 0], [1, 1]])
txlearning = 0.01
#And
print ('AND Test')
training_set_outputs = array([[0, 0, 0, 1]]).T
perceptron (inputs, training_set_outputs, txlearning)
#OR
print ('OR Test')
training_set_outputs = array([[0, 1, 1, 1]]).T
perceptron (inputs, training_set_outputs, txlearning)
#XOR
print ('XOR Test')
training_set_outputs = array([[0, 1, 1, 0]]).T
perceptron (inputs, training_set_outputs, txlearning)
