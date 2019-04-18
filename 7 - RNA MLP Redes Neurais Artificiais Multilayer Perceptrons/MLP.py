import numpy as np

# Class definition of a generic neuron
class Neuron(object):
    def __init__(self, weights, fnet):
        self.weights = weights          # Weights array
        self.fnet = fnet                # Define type of function that represent the neuron function
        
def matrix_gen (n_lines, n_columns):
    return [[((j+1)+i*n_columns) for j in range(n_columns)] for i in range(n_lines)]

# Main programm
Ninp = 4
Nlay = 3
Nout = 3
Nstart = int(round((Ninp + Nout) / 2 , 0))
Nneurons = matrix_gen (Nlay,Nstart)
print (Nneurons)
