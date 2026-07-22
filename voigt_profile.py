import numpy as np
from scipy.special import voigt_profile
import matplotlib.pyplot as plt
import calculations as cal
#-------------------------------------------------------------------------
def V(x, alpha, gamma):
    """
    Return the Voigt line shape at x with Lorentzian component HWHM gamma
    and Gaussian component HWHM alpha.

    """
    sigma = alpha / np.sqrt(2 * np.log(2))

    return (
        np.real(wofz((x + 1j * gamma) / sigma / np.sqrt(2)))
        / sigma
        / np.sqrt(2 * np.pi)
    )

#This snippet of code is from htt'ps://scipython.com/books/book2/chapter-8-scipy/examples/the-voigt-profile/
#I used this code for the voigt profile modeling. It models the "perfect spectral line" and I will later in this program be adding 'noise' (in the correct context: telluric lines or contamination.
#--------------------------------------------------------------------------

def noise(x,peak_location,peak_height,peak_width):
    
    return peak_height * np.exp(-0.5 * ((x - peak_location) / peak_width) ** 2)


#For subplots
figure, axes = plt.subplots(1,2)

for ax in axes.flat:
    ax.set_ylim(0, 0.5)
    ax.set_xlim(-10,10)

    
#calculating the x,y of voigt 
sigma = 1.0
gamma = 0.2

x = np.linspace(-10, 10, 1000)

y_noise = noise(x,-6,0.1,0.1)
y_noise1 = noise(x,4,0.05,0.5)


axes[1].plot(x,y_noise, color="pink")
axes[1].plot(x,y_noise1, color="pink")
axes[1].set_title("Noise")


colors = ['blue', 'green', 'yellow', 'red','pink','magenta','purple','gray','black']

centers = []

for shift in range(0,1000,1):
    
    y = voigt_profile(x - shift, sigma, gamma)

    y_final = y +y_noise +y_noise1

    x_final_max, y_final_max = cal.find_max(x,y_final)
    
    x_final_max_half_min, x_final_max_half_max,x_final_max_half,y_final_max_half = cal.find_half(x,y_final,y_final_max)
    
 
    #axes[0].plot(x,y_final, color=color)
    #axes[0].set_title("Voigt")
    #axes[0].axvline(x_final_max,color=color)
    #axes[0].axvline(x_final_max_half_min,ls='dashed',color=color)
    #axes[0].axvline(x_final_max_half_max,ls='dashed',color=color)
    #axes[0].axvline(x_final_max_half,ls='dotted',color=color)

   
    centers.append(x_final_max_half)
    
#-----------------------------------------------------------------------------
with open("output.txt", "w") as file:
    for index,item in enumerate(centers):
        file.write(f"{index},{item}\n")
#------------------------------------------------------------------------------

plt.show()

#-------------------------------------------------------------------------------

y_final = y + y_noise1 + y_noise2

x_final_max, y_final_max = cal.find_max(x,y_final)

x_final_max_half, y_final_max_half = cal.find_half(x,y_final,y_final_max)

print(x_final_max_half)

x_h = (x_final_max_half[1] - x_final_max_half[0])/2 + x_final_max_half[0]

axes[1,1].axvline(x_h,color='red')



