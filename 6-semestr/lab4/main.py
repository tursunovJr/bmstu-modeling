import matplotlib.pyplot as plt
import numpy as np
from lab4 import work, l, h, t

res, ti = work()
length = len(res)
print(length)
te = list(np.arange(0, ti + t, t))
x = list(np.arange(0, l + h, h))
for i in range(0, len(x), 100):
    graph = [y[i] for y in res]
    plt.plot(te, graph)
plt.xlabel("t")
plt.ylabel("T")
plt.show()
for i in range(0, length, 5):
    plt.plot(x, res[i])
plt.plot(x, res[-1])
plt.xlabel("x")
plt.ylabel("T")
plt.show()