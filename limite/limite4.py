import numpy as np
import matplotlib.pyplot as plt


fig=plt.figure(figsize=(8,5))
plt.title("Função constante")


x=np.linspace(-10,10,1000)
y=(x+1)/(2*x+1)

plt.plot(x,y)
plt.show()