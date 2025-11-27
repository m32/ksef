#!/bin/bash
WariantFormularza=$(grep WariantFormularza $1 | sed -E 's/.*>([0-9]+)<.*/\1/g')
if [ ! -f styl-fa${WariantFormularza}.xsd ]; then
    echo "Brak pliku XSD dla wersji dokumentu = ${WariantFormularza}"
else
    ./xmlvalid.py --xml $1 --xsd=schemat-fa${WariantFormularza}.xsd --validate
fi
