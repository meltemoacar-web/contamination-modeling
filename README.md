# contamination-modeling
This is a model of the effect of telluric contamination on solar emission lines. Rather than using real solar data from our sun, it uses a Voigt profile to mathematically model the shape of a spectral line. By simulating telluric contamination on this profile, the model will also calculate radial velocity shift as the emission line moves. 

# Prequisities
You will need to install these following packages on python to successfully run the program
* numpy
* scipy
* matplotlib
Use this example to install each package:
```
sudo apt install numpy
```
# Cloning the repository 
To get this program and all the needed files, run this command:
```
git clone git@github.com:meltemoacar-web/contamination-modeling.git
cd contamination-modeling
```
# Running the model
To access and view this model, run the following command:
```
python3 voigt_profile.py
```
This will allow you to see the current graphs. 
(Also note that this is far from finished so you'll only be able to access the basic graphs of the model so far. Working currently on the rest of the code to do calculations and other graphs...)
