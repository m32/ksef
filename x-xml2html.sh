#!/bin/bash
WariantFormularza=$(grep WariantFormularza $1 | sed -E 's/.*>([0-9]+)<.*/\1/g')
if [ ! -f styl-fa${WariantFormularza}.xsl ]; then
    echo "Brak pliku XSL dla wersji dokumentu = ${WariantFormularza}"
else
    ./xmlvalid.py --xml $1 --xsl=styl-fa${WariantFormularza}.xsl --html=$1.html
fi
