import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(8,5))
plt.title("Função Polinomial")

x=np.linspace(-10,10,10000)
y=x**3 + 10*x**2+ 5*x

plt.plot(x,y)
plt.show()