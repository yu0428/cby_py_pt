#!/bin/sh
#Change these variables to your own corresponding directories.
CGIDIR=/Library/WebServer/CGI-Executables

#Copy all the files

cp -r . ${CGIDIR}

#Add executable permission to python scripts.
find ${CGIDIR} -name "*.py" | xargs chmod a+x


