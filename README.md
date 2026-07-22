# contamination-modeling
This is a model of the effect of telluric contamination on solar emission lines. Rather than using real solar data from our sun, it uses a Voigt profile to mathematically model the shape of a spectral line. By simulating telluric contamination on this profile, the model will also calculate radial velocity shift as the emission line moves. 

# Cloning the repository 
To get this program and all the needed files, run this command:
```
git clone git@github.com:meltemoacar-web/contamination-modeling.git
cd contamination-modeling
```
# Setup
You will need to use a virtual environment. To set this up follow these steps:
First you must have the repository cloned, then you need to navigate into the directory 
```
cd contamination-modeling
```
Then you can create the virtual environment. Do it with this:
```
python3 -m venv .venv
```
After creating the vitural environment, activate it:
```
source .venv/bin/activate
```
# Installing the packages 
You will need to install these following packages on python to successfully run the program
* numpy
* scipy
* matplotlib
* pandas

Use this to install each package (You must be in the vitural environment you created, so that we can install all these packages at once):
```
pip install requests numpy scipy matplotlib pandas 
```
# Running the model (WIP) 
This will just be a simple breakdown of how each file relates to eachother, since when the project is finished, to see finished results you will only have to run the file that contains the final graphs. However, right now each step will be explained. 
```
voigt_profile.py
```
This command will run and pull up a graph showing the added telluric lines I made, and this file utilizes the "calculations.py" file as an import to do the FWHM calculations, which finds the center point of the voigt profile with added telluric lines as it shifts. The data generated from this file gets put into the "output.txt" file. You can skip running the voigt_profile.py command at all, since it just shows you the work behind getting the results. 
```
output_graph.py
```
Running this command will give you a graphed verison of the generated data points (Though currently it has issues that are soon to be fixed) This graph represents how the center line of Voigt profile with telluric lines is shifting continuously.
