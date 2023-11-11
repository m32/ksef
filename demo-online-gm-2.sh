#!/bin/bash
./demo-online.py \
--server=ksef-demo \
--user=gm \
--query=2 \
--query-type=incremental \
--date-from=2023-09-29T10:30:00 \
--date-to=2023-09-29T10:45:00 \
$* \
fv-gm-*.xml
