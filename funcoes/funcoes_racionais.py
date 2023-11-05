import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(8,5))
plt.title("Função racional Potencial de Leonard- sones")

x=np.linspace(0.1,0.5,10000)
y= ( 5e-15)*((1/x)**12 - (9.6/x)**6)

plt.plot(x,y)
plt.show()