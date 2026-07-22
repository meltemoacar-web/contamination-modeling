import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("output.txt")

plt.plot(df['0'],df['0.0'], marker='o')

plt.title('Center points over time')
plt.xlabel('Time')
plt.ylabel('Center point')
plt.grid(True)

plt.show()
print(df)

#Graph looks weird cause I gotta go back and fix some stuff in the voigt profile file, the range is being messy...
