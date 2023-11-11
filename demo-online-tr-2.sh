#!/bin/bash
./demo-online.py \
--server=ksef-demo \
--user=tr \
--query=2 \
--query-type=incremental \
--date-from=2023-11-03T07:00:00 \
--date-to=2023-11-03T09:0:00 \
$* \
fv-tr-*.xml
