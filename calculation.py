import numpy as NP

p = NP.matrix("0.538 0.500 0.385; 0.154 0.250 0.077; 0.308 0.250 0.538")
x_0 = NP.matrix("0.3; 0.7; 0.0")

k = 5
for i in range(1, k):
    x_k = (p ** i) * x_0
    print("x_" + str(i) + " = " + str(x_k))
