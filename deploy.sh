#!/bin/sh
#Change these variables to your own corresponding directories.
CGIDIR=/Library/WebServer/CGI-Executables

#Copy all the files
cp -r DataModel ${CGIDIR}
cp -r Session ${CGIDIR}
cp -r conf ${CGIDIR}
cp -r images ${CGIDIR}
cp -r *.py ${CGIDIR}

#Add executable permission to python scripts.
find ${CGIDIR} -name "*.py" | xargs chmod a+x


