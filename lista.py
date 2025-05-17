import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



x = np.linspace(0, 10, 100)

y = np.sin(x)

plt.title('Função seno')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend(['sin(x)'])
plt.plot(x, y)
plt.show()

