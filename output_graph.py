import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#This code just simply reads the file where the data was spit out into and then graphs it. It is a good visual representation of the center points over time, you can see how it changes as noise location, height, differ. 
df = pd.read_csv("output.txt")

plt.plot(df.t,df.value, marker='o')

plt.title('Center points over time')
plt.xlabel('Time')
plt.ylabel('Center point')
plt.axhline(y=374.5, color='red', linestyle='dashed')
plt.grid(True)

plt.show()
print(df)

