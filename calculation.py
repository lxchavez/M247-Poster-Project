import numpy as NP

p = NP.matrix("0.538 0.5 0.385; 0.154 0.25 0.077; 0.308 0.25 0.539")
x_0 = NP.matrix("0.5; 0.5; 0")

k = 5
x_k = (p ** k) * x_0
print(x_k)
