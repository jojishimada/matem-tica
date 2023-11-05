import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(8,5))
plt.title("Função sigmoide")

x=np.linspace(-10,10,10000)
y=1/(1+np.exp(-x))

plt.plot(x,y)
plt.show()