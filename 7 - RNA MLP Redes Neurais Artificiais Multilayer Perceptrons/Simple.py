# Programa princial

# Define o numero de entradas
nInput, nTotal = 4, 4

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

