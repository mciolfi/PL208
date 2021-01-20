# Importe bibliotecas
import random
import numpy as np

# Programa princial

# Define o numero de entradas
nTotal = nInput = 8

# Escolha as entradas aleatoreamente
Input = [1, 2, 3, 4, 5, 6, 7, 8]

# Define a quantidade de layers (camadas escondidas)
nLayer = 3

# Define tipo e quantidade de saidas
out = ['triste', 'feliz']
nOutput = len(out)

# Define o tipo de matriz
typ = ['decrescent', 'square', 'crescent', 'free']
if nOutput > nInput:
    typ = 'crescent'
elif nOutput < nInput:
    typ = 'decrescent'
print(typ)

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
M[0] = Input
print('M =')
[print(i) for i in M]

# Define os pesos iniciais
weights = []
weights.append([[random.random() * 2 - 1 for j in range(i)] for i in nNeuron])
weights = weights[0]
# print([[(j) for j in range(i)] for i in nNeuron]) # Contador
print('pesos = ', weights, '\nM =', M)
#print(np.random.random((2, 2)))
print (Input)
for i in nNeuron:
    #M[i + 1][1] = np.dot(Input[i], weights[0])
    print('lei', i)
print('res=', M)
s = 0
for t in range(8):
    s = + weights[0][t]
print ('sol = ', s)