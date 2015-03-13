#!/bin/sh
#Change these variables to your own corresponding directories.
cgidir=/Library/WebServer/CGI-Executables


#mysql.conf is the configuration file.
sudo cp mysql.conf $cgidir

sudo cp *.jpeg $cgidir

sudo cp *.py $cgidir
#Add permission for executing.
cd $cgidir
sudo chmod a+x *.py
