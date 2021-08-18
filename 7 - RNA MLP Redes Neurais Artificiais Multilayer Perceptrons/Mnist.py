import mnist_loader
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

import network
#net = network.Network([784, 30, 10])
net = network.Network([9, 30, 59])

net.SGD(training_data, 30, 59, 0.001, test_data=test_data)