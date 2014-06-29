Fractionauts
=================
Fractionauts is a fraction and astronaut based puzzle/quiz game centered around 4th grade students interested in learning how to perform basic arithmetic with fractions.

Running
-------
To run, make sure you have all of the application's dependencies installed on your machine. 
run `sudo apt-get install python-pygame` using a debian based distro.

To run the game run `python Main.py`


Installing onto the OLPC
------------------------
To install the latest stable release of Fractionauts onto OLPC, go to [Fractionauts' Activity Page](http://activities.sugarlabs.org/en-US/sugar/addon/4746/).

To compile and install our application on the OLPC we used [Sugar Activity Quick Start](https://github.com/FOSSRIT/SAQS-sugar-activity-quick-start-). 
To create a .xo file, run `./setup.py dist_xo` inside the *Sugar OS's Terminal Activity*. The .xo file can be found in `/dist`.

Once we created the .xo file we copied it onto a flash drive and plugged it into the OLPC

Open the .xo file on the OLPC to install and launch the game. If you have a previous version of the game installed on your OLPC, delete the .Activity file and relaunch the new .xo file to overwrite it.


Resources
---------
To reduce package size, the art assets are archived at [this repo](https://github.com/lcb931023/fractionauts_resource).


Contributing
------------
A list of open issues can be found in our issue section of our github. Any problems found can be logged there and we will work with you to help solve them.

For making modifications and fixing bugs feel free to fork our repository and submit pull requests.
