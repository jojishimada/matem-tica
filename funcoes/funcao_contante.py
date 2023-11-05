import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(8,5))
plt.title("Função constante")

x=np.linspace(-10,10,10000)
y=20*np.ones(x.shape)

plt.plot(x,y)
plt.show()