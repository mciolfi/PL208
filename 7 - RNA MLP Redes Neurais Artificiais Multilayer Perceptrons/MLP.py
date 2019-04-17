import numpy as np

Ninput = 4
Noutput = 3
Nlayer = 2
net = []
Nstart = round((Ninput + Noutput) / 2, 0)
print (Nstart)

# Neural Network generation
for layer in range(Nlayer):
    for neu in range(Ninput):
        net.append (1)
print (net)