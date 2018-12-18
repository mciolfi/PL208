# Open dataset
def arq(name,ndata,types):
    import csv
    listt = []                                                      # Define listt as matrix
    with open(name, newline='') as csvfile:                         # csv module will detect new lines
        if types == ' ':  text = csv.reader(csvfile, delimiter=' ') # classify by space
        if types == ',':  text = csv.reader(csvfile, delimiter=',') # classify by comma
        if types == '\t': text = csv.reader(csvfile, delimiter='\t')# classify by tab
        for line in text:
            for t in range(len(line)-ndata): line.remove('')        # Removes zeros inside data        
            listt.append(line)                                      # Define listt as the data inside file
    return (listt)

# Threshold function: Binary result
def linear (inputs,weights):
    output = dot(inputs,weights)                        # Multiply the inputs with weights
    for cont in range(len(output)):
        if output[cont][0] < -0.5:   output[cont][0] = -1 # Establishes the value of 0.5 as a limit for binary
        if output[cont][0] > 0.5:   output[cont][0] = 1
        if output[cont][0] >= -0.5 and output[cont][0] <= 0.5:   output[cont][0] = 0
        #else:                       output[cont][0] = 0
    return (output)

# Perceptron with 4 inputs (4 Neuron) and 1 output (1 Neuron)
def perceptron (inputs, training_set_outputs, txlearning):
    weights = random.random((len(inputs[0]), 1))        # Define the initial weight as random
    weightsold = [[0] for a in range(len(inputs[0]))]   # Define matrix to save old weights value
    iteration = 0                                       # Define variable iteration
    while iteration < 10000 and max(abs(weightsold-weights))[0] > 0.001:  # Learning iteraction until 100 or when the weights stop to change
        iteration += 1                                  # Count iteration number
        output = linear(inputs,weights)                 # Output = linear thresold
        for i in range (len(weights)): weightsold [i][0] = weights[i][0]        # Save old weights
        weights += txlearning * dot(inputs.T,(training_set_outputs.T - output)) # Weights update
    print('#Iteration =',iteration)
    print('Weights =',weights.T)
    print('Expected value =',training_set_outputs)
    final_test = linear(inputs,weights).T == training_set_outputs   # Check if the inputs plus weights = outputs
    if min(final_test[0]):  print ('Final value =',linear(inputs,weights).T,'Learned!\n')     # If all results are true then has been learned
    else:                   print ('Final value =',linear(inputs,weights).T,'NOT Learned!\n')

# Main program
from numpy import exp, array, random, dot
listt = array(arq('iris.data.txt',5,','))  # Define listt as the data inside the file
inputs = []
training_set_outputs = []
for cont in range(len(listt)):
    inputs.append([float(listt[cont][i]) for i in range(4)])
    # Define one value for each classification: Iris-setosa = 0,Iris-versicolor = 1, Iris-virginica = 2
    if listt[cont][4] == 'Iris-setosa':     typef = -1
    if listt[cont][4] == 'Iris-versicolor': typef = 0
    if listt[cont][4] == 'Iris-virginica':  typef = 1
    training_set_outputs.append(typef)
inputs = array(inputs)                                  # Define inputs as matrix to transpose after
training_set_outputs = array([training_set_outputs])    # Define outputs as matrix to transpose after
print ('Iris')
txlearning = 0.01
perceptron (inputs, training_set_outputs, txlearning)
