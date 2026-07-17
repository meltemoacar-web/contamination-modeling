import numpy as np
#from scipy.special import wofz
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
figure, axes = plt.subplots(2,2)

for ax in axes.flat:
    ax.set_ylim(0, 0.5)
    ax.set_xlim(-10,10)

#calculating the x,y of voigt 

sigma = 1.0
gamma = 0.2

x = np.linspace(-10, 10, 1000)

y_noise = noise(x,-1,0.1,0.1)

axes[0,1].plot(x,y_noise, color="pink")
axes[0,1].set_title("Noise")


colors = ['blue', 'green', 'yellow', 'red','pink']

centers = []

for shift in range(0,3,1):

    color =colors[shift]
    
    y = voigt_profile(x - shift, sigma, gamma)

    y_final = y +y_noise

    x_final_max, y_final_max = cal.find_max(x,y_final)
    
    x_final_max_half, y_final_max_half = cal.find_half(x,y_final,y_final_max)
    
    axes[0,0].plot(x,y, color="green")
    axes[0,0].set_title("Voigt")

    axes[1,0].plot(x,y_final, color=color)
    axes[1,0].set_title("Voigt")
    
    axes[1,0].axvline(x_final_max,color=color)
    
    for xx in x_final_max_half:
        axes[1,0].axvline(xx,ls='dashed',color=color)
    
    x_h = (x_final_max_half[1] - x_final_max_half[0])/2 + x_final_max_half[0]
    print(f"-------{x_h}")
    axes[1,0].axvline(x_h,ls='dotted',color=color)
    centers.append(x_h)
    
with open("output.txt", "w") as file:
    for item in centers:
        file.write(f"{item}\n")

#------------------------------------------------------------------------------

plt.show()

#other stuff not needed right now 

axes[0,0].plot(x,y, color="green")
axes[0,0].set_title("Voigt")

axes[0,1].plot(y_noise1, color="pink")
axes[0,1].set_title("Noise 1")

axes[1,0].plot(y_noise2, color="purple")
axes[1,0].set_title("Noise 2")

axes[1,1].plot(x,y + y_noise1 + y_noise2, color="blue")
axes[1,1].set_title("Added")

plt.show()

#-------------------------------------------------------------------------------

y_final = y + y_noise1 + y_noise2

x_final_max, y_final_max = cal.find_max(x,y_final)

x_final_max_half, y_final_max_half = cal.find_half(x,y_final,y_final_max)

print(x_final_max_half)

x_h = (x_final_max_half[1] - x_final_max_half[0])/2 + x_final_max_half[0]

axes[1,1].axvline(x_h,color='red')



#Stuff below not being used right now. Useless. 

#axes[1,1].axvline(x_final_max)

#for i in x_final_max_half:

    #axes[1,1].axvline(i)

#plt.xlim(-1,1)
#plt.show()

#These are for the full width half maximum lines that appear on the graph, so if you dont wanna see that just comment these commands out.
#for i in x_max_half:             #Shows the vertical lines going through our selected "width" points 
#    axes[0,0].axvline(i)
    
#axes[0,0].axhline(y_max)         #Shows the horizontal lines going through the same points, but is a horizontal point going through the maximum point. (This is just visual representation for later) 
#axes[0,0].axhline(y_max_half)


#plotting stuff, you dont need this unless you want to see all 4 graphs at once
#plt.plot(x, y_noise1, label="Noise 1")
#plt.plot(x, y_noise2, label="Noise 2")
#plt.plot(x, y, label="Voigt")                     
#plt.plot(x, y + y_noise1 + y_noise2, label="Added") #added verison
