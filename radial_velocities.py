import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Listen, you might've seen the radial_velocites calculations txt file. And just completely ignore that, because the calculations will be done HERE, along with the graphing of the data from the calculations. This is because I had big issues with the whole scaling of everything, and while the other graph "output_graph.py" looks fine, the data that we get from there is what we are using to calcualte the radial velocity shift, but to get accurate data I need to completely rescale the data values, since the difference between each value as it is being shifted along, is insanely large. So yes, I had to scale it way down so that when we are looking at the radial velocity shift graph, you don't see it being graphed on a DIABOLICALLY large scale. Where it realistically wouldn't ever even be possible to have a radial velocity shift that large. Anyway, that's just a quick rant of what went wrong previously so you know why the calculations had to be re-done in it's own file. But to sum it up: Ignore this file "radial_velocities.txt" !!!!

#ALSO, since my model is supposed to be interactive and more hands-on. Everytime you want to alter the 'noise' (telluric contamination) in the Voigt_profile.py file, you need to run that file command, so that the data in the "out_put.txt" file can update, and then you'll be able to run this file and do the calculations and graph. Which I probably mentioned before but this is just a reminder. 

#--------------------------------------------------------------------------------------------------
#Reading the file with the center points shifting over time
df = pd.read_csv("output.txt")
df["difference"] = df['value'].diff() #Calculating the difference between those center points
print(df) #This was just so that if anything goes wrong, CHECK the difference in values. Anyway, these differences are way too big so that's why below I modified them to be more realisitc. 


#Below is where the radial velocity shift equation comes into play. Defining variables and then doing the calculations. 
c = 299792458  #m/s
lambda_rest = 374.55 #nm 
df['velocity'] = c * (df['difference'] / lambda_rest)

#HERE IS WHERE THE FIXING AND RE-SCALING IS DONE. This is what turns the data from being crazy to actually realistic. 
target_amplitude = 100  # m/s 
current_amplitude = df['velocity'].abs().max()
scale_factor = target_amplitude / current_amplitude
df['velocity_scaled'] = df['velocity'] * scale_factor

#Now we plot. 
plt.figure(figsize=(10, 5))
plt.plot(df['t'], df['velocity_scaled'], marker='o')
plt.ylabel('Radial Velocity (m/s)')
plt.xlabel('Time (t)')
plt.title('Radial Velocity shift')
plt.grid(True, alpha=0.3)
plt.show()








