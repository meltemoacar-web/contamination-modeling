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
# Running this interactive model
This model is pretty flexible, and is more on the interactive side if you choose it to be. There is only one file where you can edit the 'noise', representing the telluric contamination. In the file, check the comments to see how this is done if you would like to alter the location of the telluric lines, or the strength of them. Once done, if you chose to alter the telluric contamination, you will need to run the following command:
```
python3 voigt_profile.py
```
After you run this command, ignore the graph if it shows. Since what running this file does is it creates the data and spits it out into another file. This data is the center point of the Voigt profile shifting across the axis, with the telluric conatmination being stationary. Now you can move onto running the following command and seeing what the center points over time look like graphed. To continue, run this command:
```
python3 output_graph.py
```
Now you are able to visually see how the telluric contamination is affecting the Voigt profile, it should be pretty obvious where. Now, after the center points have been graphed, we are able to calculate the radial velocity shift. The next file will be taking that data from the previous graph and calculating the radial velocity shift, which is then graphed. In order to have to calculations done and to see this graph, run this last command: 
```
python3 radial_velocities.py
```
Now you will have seen the visual representation of how telluric contamination impacts spectral lines. Based on location and intensity. You can mess around with with the telluric contamination to have some fun. Enjoy. 