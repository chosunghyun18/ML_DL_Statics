import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





array= [55,48,50,49,54,58,95,20,50,57,47,49,58,48,49,47
        ,49,59,47,53,50,49,49,46,55,53,48,47,52,48,49,47,
        58,57,47,53,56,51,46,52,47,53,46,49,56,48,49,47,58,55]


a1 = pd.DataFrame(array)


plt.figure(figsize=(5,6))

plt.boxplot(a1)
#make a ticks
plt.yticks(np.arange(0,101,3))

plt.grid()
plt.show()
