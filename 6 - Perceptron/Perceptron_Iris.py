__author__ = 'Márcio Ciolfi'
__copyright__ = 'Copyright 2018, ML'
__license__ = 'Ciolfi'
__version__ = '1.0'
__maintainer__ = 'Márcio Ciolfi'
__email__ = 'ciolfi@gmail.com'
__course__ = 'PL208'
__username__ = 'mciolfi'
__description__ = 'Perceptron linear using Iris dataset'
__status__ = 'Production'


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


# Threshold function: Binary result
def linear(inputs, weights):
    output = dot(inputs, weights)  # Multiply the inputs with weights
    for cont in range(len(output)):
        if output[cont][0] > 0.5:
            output[cont][0] = 1  # Establishes the value of 0.5 as a limit for binary
        else:
            output[cont][0] = 0
    return (output)


# Perceptron with 4 inputs (4 Neuron) and 1 output (1 Neuron)
def perceptron(inputs, training_set_outputs, txlearning):
    weights = random.random((len(inputs[0]), 1))  # Define the initial weight as random
    weightsold = [[0] for a in range(len(inputs[0]))]  # Define matrix to save old weights value
    iteration = 0  # Define variable iteration
    while iteration < 10000 and max(abs(weightsold - weights))[
        0] > 0.001:  # Learning iteraction until 100 or when the weights stop to change
        iteration += 1  # Count iteration number
        output = linear(inputs, weights)  # Output = linear thresold
        for i in range(len(weights)): weightsold[i][0] = weights[i][0]  # Save old weights
        weights += txlearning * dot(inputs.T, (training_set_outputs - output))  # Weights update
    print('#Iteration =', iteration)
    print('Weights =', weights.T)
    print('Expected value =', training_set_outputs.T)
    final_test = linear(inputs, weights).T == training_set_outputs.T  # Check if the inputs plus weights = outputs
    if min(final_test[0]):
        print('Final value =', linear(inputs, weights).T, 'Learned!\n')  # If all results are true then has been learned
    else:
        print('Final value =', linear(inputs, weights).T, 'NOT Learned!\n')


# Classificator between Iris-setosa and Iris-versicolor
def classificator(inputs,training_set_outputs,typef):
    # Check number of sample match with flower type
    count = 0
    for i in range(len(training_set_outputs)):
        if training_set_outputs[i][0] == typef:
            count = count + 1
    data = [[0] * count for i in range(4)]
    # Define the data matriz with only cases matched
    count = 0
    for i in range(len(training_set_outputs)):
        if training_set_outputs[i][0] == typef:
            for j in range(4):
                data[j][count] = inputs[i][j]
            count = count + 1
    # Print max and min results of each type of flower
    print ('Sepal length from',min(data[0]),'to',max(data[0]),'cm')
    print ('Sepal width from',min(data[1]),'to',max(data[1]),'cm')
    print ('Petal length from',min(data[2]),'to',max(data[2]),'cm')
    print ('Petal width from',min(data[3]),'to',max(data[3]),'cm')
    return (data)
    #if max(sl)<max(pl) && min(sl)


# Plot results
def plot (x1, y1, x2, y2, cat1, x3, y3, x4, y4, cat2):
    import matplotlib.pyplot as plt
    #plot above results of Sepal differencies
    plt.subplot(211)
    plt.title('Dataset Iris Setosa vs. Versicolor')
    plt.plot(x1, y1, 'go', label = cat1 + ' - Sepal')
    plt.plot(x3, y3, 'r^', label = cat2 + ' - Sepal')
    plt.grid(True)
    plt.ylabel('width')
    plt.legend()
    # plot above results of Petal differencies
    plt.subplot(212)
    plt.plot(x2, y2, 'go', label = cat1 + ' - Petal')
    plt.plot(x4, y4, 'r^', label = cat2 + ' - Petal')
    plt.grid(True)
    plt.xlabel('lenght')
    plt.ylabel('width')
    plt.legend()
    plt.show()


# Main program
from numpy import exp, array, random, dot

listt = array(arq('iris.data.txt', 5, ','))  # Define listt as the data inside the file
inputs = []
training_set_outputs = []
for cont in range(len(listt)):
    # Define one value for each classification: Iris-setosa = 0,Iris-versicolor = 1
    if listt[cont][4] == 'Iris-setosa':
        inputs.append([float(listt[cont][i]) for i in range(4)])
        training_set_outputs.append([0])
    if listt[cont][4] == 'Iris-versicolor':
        inputs.append([float(listt[cont][i]) for i in range(4)])
        training_set_outputs.append([1])
    # if listt[cont][4] == 'Iris-virginica':  don't include on list
inputs = array(inputs)  # Define inputs as matrix to transpose after
training_set_outputs = array(training_set_outputs)  # Define outputs as matrix to transpose after
print('Iris')
txlearning = 0.01  # Define learning rate
perceptron(inputs, training_set_outputs, txlearning)  # Run perceptron
# Show differencies between Iris setosa and versicolor
print('Iris-setosa')
data0 = classificator(inputs,training_set_outputs,0)
print('Iris-versicolor')
data1 = classificator(inputs,training_set_outputs,1)
# Plot results
plot (data0[0], data0[1], data0[2], data0[3], 'Iris-setosa',data1[0], data1[1], data1[2], data1[3], 'Iris-versicolor')
