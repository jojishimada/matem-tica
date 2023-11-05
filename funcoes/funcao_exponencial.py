import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(8,5))
plt.title("Função exponencial")

x=np.linspace(-10,10,10000)
y=np.exp(x)

plt.plot(x,y)
plt.show()