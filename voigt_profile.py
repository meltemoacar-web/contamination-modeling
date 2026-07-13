import numpy as np
from scipy.special import wofz
import matplotlib.pyplot as plt

#--------------------------------------------------------------------------
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

figure, axes = plt.subplots(2,2)
alpha, gamma = 0.1, 0.1
x = np.linspace(-0.8, 0.8, 1000)
y = V(x,alpha,gamma)

#This snippet of code is from htt' ps://scipython.com/books/book2/chapter-8-scipy/examples/the-voigt-profile/
#I used this code for the voigt profile modeling. It models the "perfect spectral line" and I will later in this program be adding 'noise' (in the correct context: telluric lines or contamination.
#-------------------------------------------------------------------------

#These are to calculate the full width half maximum, when you run the program it will give you some points. Thats what this is. This is only calculating the points on the voigt profile graph though.
y_max = y.max()
y_max_half = y_max/2
print(y_max_half)

half_indices = []

for index, i in enumerate(y):

    if abs(i - y_max_half) <= 0.005:
        half_indices.append(index)

x_max_half=[]
for i in  half_indices:
    x_max_half.append(x[i])
print(x_max_half)


#Change this to alter noise 
peak_location = -0.8 + 1.6/1000 * 300        #center of the spike 
peak_height1 = 0.5                           #max height of spike
peak_height2=1                               
peak_width = 0.05                            #changes width

y_noise1 = peak_height1 * np.exp(-0.5 * ((x - peak_location) / peak_width) ** 2)
peak_location = -0.8+1.6/1000 * 600
y_noise2 = peak_height2 * np.exp(-0.5 * ((x - peak_location) / peak_width) ** 2)


#plotting stuff, you dont need this unless you want to see all 4 graphs at once
#plt.plot(x, y_noise1, label="Noise 1")
#plt.plot(x, y_noise2, label="Noise 2")
#plt.plot(x, y, label="Voigt")                     
#plt.plot(x, y + y_noise1 + y_noise2, label="Added") #added verison

#For subplots 
axes[0,0].plot(x,y, color="green")
axes[0,0].set_title("Voigt")

axes[0,1].plot(y_noise1, color="pink")
axes[0,1].set_title("Noise 1")

axes[1,0].plot(y_noise2, color="purple")
axes[1,0].set_title("Noise 2")

axes[1,1].plot(x,y + y_noise1 + y_noise2, color="blue")
axes[1,1].set_title("Added")


for i in x_max_half:
    axes[0,0].axvline(i)

#These are for the full width half maximum lines that appear on the graph, so if you dont wanna see that just comment these commands out. 
axes[0,0].axhline(y_max)
axes[0,0].axhline(y_max_half)

#plt.title("Voigt with contamination/test", color="purple")
plt.xlim(-0.8, 0.8)
#plt.legend()
plt.show()
