import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#This graph just graphs the radial velocity shift calculations done in the "voigt_profile.py" file.
#---------------------------------------------------------------------------
df = pd.read_csv("radial_velocities.txt")

plt.plot(df.Time,df.RVS, marker='o')

plt.title('Radial Velocities over time')
plt.xlabel('Time')
plt.ylabel('Radial Velocity')
plt.grid(True)

plt.show()
print(df)

