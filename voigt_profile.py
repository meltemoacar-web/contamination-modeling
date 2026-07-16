import numpy as np
from scipy.special import wofz
import matplotlib.pyplot as plt
import calculations
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

#This snippet of code is from htt' ps://scipython.com/books/book2/chapter-8-scipy/examples/the-voigt-profile/
#I used this code for the voigt profile modeling. It models the "perfect spectral line" and I will later in this program be adding 'noise' (in the correct context: telluric lines or contamination.
#------------------------------------------------------------------------

def find_max(x,y):

    y_max = y.max()

    ymax_indices = []

    for index, i in enumerate(y):

        if abs(i - y_max) <= 0.0001:
            ymax_indices.append(index)

    x_max=[]
    for i in  ymax_indices:
        x_max.append(x[i])


    return x_max[0],y_max

#####################################################

def find_half(x,y,y_max):

    '''
    Given x, y, x_max,y_max returns the half values of max
    These are to calculate the full width half maximum, when you run the program it will give you some points. Thats what this is. This is only calculating the points on the voigt profile graph though.

    '''

    y_max_half = y_max/2

    half_indices = []

   for index, yy in enumerate(y):
       print(f" delta:{abs(yy - y_max_half)}")
       if abs(yy - y_max_half) <= 0.008:
           half_indices.append(index)

    x_max_half=[]
    for i in  half_indices:
        x_max_half.append(x[i])
       
    print(f"x_max_half:{x_max_half}")

    return x_max_half, y_max_half

#####################################################

figure, axes = plt.subplots(2,2)
alpha, gamma = 0.1, 0.1


#calculating the x,y of voight function

x = np.linspace(-1, 1, 1000)
y = V(x,alpha,gamma)

#------------------------------------------------------------------------------

#Change this to alter noise 

peak_location = -0.8 + 1.6/1000 * 300       #center of the spike 
peak_height1 = 0.4                          #max height of spike
peak_height2=0.8                               
peak_width = 0.05                            #changes width

y_noise1 = peak_height1 * np.exp(-0.5 * ((x - peak_location) / peak_width) ** 2)
peak_location = -0.8+1.6/1000 * 650
y_noise2 = peak_height2 * np.exp(-0.5 * ((x - peak_location) / peak_width) ** 2)


#For subplots 
axes[0,0].plot(x,y, color="green")
axes[0,0].set_title("Voigt")

axes[0,1].plot(y_noise1, color="pink")
axes[0,1].set_title("Noise 1")

axes[1,0].plot(y_noise2, color="purple")
axes[1,0].set_title("Noise 2")

axes[1,1].plot(x,y + y_noise1 + y_noise2, color="blue")
axes[1,1].set_title("Added")



y_final = y + y_noise1 + y_noise2

x_final_max, y_final_max = find_max(x,y_final)

x_final_max_half, y_final_max_half = find_half(x,y_final,y_final_max)

x_h = (x_final_max_half[1] - x_final_max_half[0])/2 + x_final_max_half[0]



axes[1,1].axvline(x_final_max)

for i in x_final_max_half:

    axes[1,1].axvline(i)

axes[1,1].axvline(x_h,color='red')


plt.xlim(-1,1)
plt.show()
































#Useless but useful stuff 


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
