import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(8,5))
plt.title("Função seno")

x=np.linspace(-1,1,10000)
y=np.tan(x)

plt.plot(x,y)
plt.show()