#!/bin/bash
grep tags -A1 ./open-api.json | grep -v tags | sed 's/^[ \t]*//; s/,$// ; s/\-\-//;' |sort|uniq