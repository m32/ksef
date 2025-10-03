#!/bin/bash
shopt -s globstar

gen() {
rm -rf ksefproject
openapi-python-client \
generate \
--config ksef.yaml \
--path openapi.json \
2>x-openapi-python-client-log-2
}

for a in ksef/api/**/__init__.py; do
    rm $a
    touch $a
done
