# PythonImageTranslation
Captures a hand drawn image using a Jetson TX1s build in camera and inputs it into a liquid simulation.

##Installation

###Connect board to internet
Log in to the Jetson board with the default password of `ubuntu`
Click on the wifi symbol in the top right hand corner
Put in your wifi credentials


###Put the required files on your board

Open up your terminal by either clicking on the terminal icon or using the keyboard shortcut `CTRL+ALT+T`

run `sudo apt-get install git`

Be sure you are in home dir `cd ~`

run `git clone https://lavine4@lc.llnl.gov/bitbucket/scm/pit/pythonimagetranslation.git image`

#Setting up

run `cd ~/image'
run `sudo ./setup.sh`

##Usage

Be sure you are in image dir `cd ~/image`
Then run `./go.sh`

press any key to dismiss the image, and press space or r to continue or retake the image.

###Clustering

cluster.py is an example of cluster definition file
Cluster definition requires passwordless ssh to be set up between all nodes and that all required software is on each node
