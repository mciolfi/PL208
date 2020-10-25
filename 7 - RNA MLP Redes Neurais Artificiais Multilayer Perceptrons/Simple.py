import random
import numpy as np

# Programa princial

# Define o numero de entradas
nInput = 6
nTotal = nInput

# Define a quantidade de layers
nLayer = 2

# Define a quantidade de saidas
out = ['triste', 'feliz']
nOutput = len(out)

# Define o tipo de matriz
typ = ['decrescent', 'square', 'crescent']

# Define a quantidade de neuronios nas camadas ocultas
nNeuron = [nInput]
if nInput >= ((nInput + nOutput) / (nLayer + 2)) * nLayer:
    nLay = (nInput + nOutput) / (nLayer + 2)
    print('ok')
else:
    nLay = 0
    print('Nok')

for lay in range(nLayer):
    nTotal = int(nTotal - nLay)
    nNeuron.append(nTotal)
nNeuron.append(nOutput)
print('nNeuron', nNeuron)

# Cria a matriz de zeros
M = [[0] * nNeuron[i] for i in range(len(nNeuron))]
print('M =')
[print(i) for i in M]

# Define os pesos iniciais
weights = []
[[weights.append(j) for j in range(i)] for i in nNeuron]
M = [[0] * 5 for i in range(2)]
print(weights, M)
print(np.random.random((2, 2)))