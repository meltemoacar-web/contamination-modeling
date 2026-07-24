import numpy as np
from scipy.special import voigt_profile
import matplotlib.pyplot as plt
import calculations as cal

#--------------------------------------------------------------------------

def noise(x,peak_location,peak_height,peak_width):
    
    return peak_height * np.exp(-0.5 * ((x - peak_location) / peak_width) ** 2)


#For subplots
figure, axes = plt.subplots(1,2)

#for ax in axes.flat:
    #ax.set_ylim(0, 0.5)
    #ax.set_xlim(300,400)

    
#parameters for the voigt 
sigma = 0.5
gamma = 0.3


# values to calculate voigt function
x = np.linspace(-20, 20, 1000)


# noise

y_noise = noise(x,-1,0.1,0.1)
y_noise1 = noise(x,1,0.05,0.2)
y_noise2 = noise(x,3,0.1,0.2)

axes[1].plot(x,y_noise, color="pink")
axes[1].plot(x,y_noise1, color="pink")
axes[1].plot(x,y_noise2, color="pink")
axes[1].set_title("Noise")

# for shifting 
centers = []

shift_values = np.arange(-np.pi,np.pi*3,0.2)
shift_values = np.sin(shift_values)

center_wavelength = 374.55

shift_values = shift_values + center_wavelength

x = x + center_wavelength

for shift in shift_values:
    
    y = voigt_profile( x - shift, sigma, gamma)
 
    y_final = y +y_noise +y_noise1 +y_noise2

    x_final_max, y_final_max = cal.find_max(x,y_final)
    
    x_final_max_half_min, x_final_max_half_max,x_final_max_half,y_final_max_half = cal.find_half(x,y_final,y_final_max)
    
 
    axes[0].plot(x,y_final, color='green')
    axes[0].set_title("Voigt")
    #axes[0].axvline(x_final_max,color=color)
    #axes[0].axvline(x_final_max_half_min,ls='dashed',color=color)
    #axes[0].axvline(x_final_max_half_max,ls='dashed',color=color)
    axes[0].axvline(x_final_max_half,ls='dotted',color='red')

   
    centers.append(x_final_max_half)
    
#-----------------------------------------------------------------------------
with open("output.txt", "w") as file:
    file.write(f"t,value\n")
    for index,item in enumerate(centers):
        file.write(f"{index},{item}\n")
#------------------------------------------------------------------------------

plt.show()





