import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(8,5))
plt.title("Função linear")

x=np.linspace(-10,10,10000)
y=5+x*2

plt.plot(x,y)
plt.show()