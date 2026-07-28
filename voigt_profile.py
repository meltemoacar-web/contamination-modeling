import numpy as np
from scipy.special import voigt_profile
import matplotlib.pyplot as plt
import calculations as cal

#--------------------------------------------------------------------------
#Since this is an interactive program, you will see that this file contains the code that is the 'backbone' of everything. In this code you are able to alter the 'noise' lines, which represent telluric contamination.
#Just look at the function to see how you can alter the noise, such as it's location and amplitude(height) But you must run this code in order to get the final graphs.
#Running this code will spit out a bunch of data, which the file "output_graph.py" will take this data and then graph it, after you run the command in a terminal. That graph just shows you the center point of the voigt profile, with or without contamination over time. (You must change the code if you want more contamination or less, or none at all!)
#There are 3 important files that you just follow in a path: First is this file "voigt_profile.py" where you can alter the noise, but to see the visible changes and results from chaninging the noise, you will need to run this file and THEN run the "output_graph.py" file after, because the data will calculated and put into another file where running the next file "output_graph.py", will just pull up a graph of it.
#After that, from changing the noise, you will also be able to see how the calculations of the radial velocity shift will change. To see that graph and visually compare, after running both the previous files, you will run the "radial_velocities.py" file. Which will calculate and graph the radial velocity shift from the current data that you ran and calculated previously.
#To sum it up: 1. Change noise as you please--> run "python3 voigt_profile.py" in terminal 2. Run "python3 output_graph.py" to see center points over time. 3. run "radial_velocities.py" to see the radial velocity shift. 
#---------------------------------------------------------------------------
def noise(x,peak_location,peak_height,peak_width):
    
    return peak_height * np.exp(-0.5 * ((x - peak_location) / peak_width) ** 2)
#Above shows how the function is defined

# for subplots
figure, axes = plt.subplots(1,2)
    
# parameters for the voigt 
sigma = 0.5
gamma = 0.3

# values to calculate voigt function
x = np.linspace(-20, 20, 1000)


# noise -- this is where you can interact and alter the noise as you please
y_noise = noise(x,-1.5,0.1,0.1)
y_noise1 = noise(x,2,0.05,0.2)
y_noise2 = noise(x,3,0.08,0.2)
#-------------------------------------------------------------------------
axes[1].plot(x,y_noise, color="pink")
axes[1].plot(x,y_noise1, color="pink")
axes[1].plot(x,y_noise2, color="pink")
axes[1].set_title("Noise")

# for shifting 
centers = []
center_wavelength = 374.55
speedoflight = 299792458

shift_values = np.arange(-np.pi,np.pi*3,0.2)
shift_values = np.sin(shift_values)

shift_values = shift_values + center_wavelength

x = x + center_wavelength

#radial_velocities =[]

for shift in shift_values:
    
    y = voigt_profile( x - shift, sigma, gamma)
 
    y_final = y +y_noise +y_noise1 +y_noise2

    x_final_max, y_final_max = cal.find_max(x,y_final)
    
    x_final_max_half_min, x_final_max_half_max,x_final_max_half,y_final_max_half = cal.find_half(x,y_final,y_final_max)
   
    #radial_velocity =  -((speedoflight * (shift - center_wavelength) )/  center_wavelength)
    
    #radial_velocities.append(radial_velocity)
    
    axes[0].plot(x,y_final, color='green')
    axes[0].set_title("Voigt")
    axes[0].axvline(x_final_max_half,ls='dotted',color='red')

   
    centers.append(x_final_max_half)
    
#-----------------------------------------------------------------------------
#This where the data is spit out, to get the most up-to-date output graph of the data, you MUST run this file in a terminal. 
with open("output.txt", "w") as file:
    file.write(f"t,value\n")
    for index,item in enumerate(centers):
        file.write(f"{index},{item}\n")
#------------------------------------------------------------------------------

#with open("radial_velocities.txt", "w") as file:
    #file.write(f"Time,RVS\n")
    #for index,item in enumerate(radial_velocities):
        #file.write(f"{index},{item}\n")
#------------------------------------------------------------------------------


plt.show() #you dont really need to look at this graph since its a whole bunch of chaos, this file is just doing the calculations and spitting it out into another file 





