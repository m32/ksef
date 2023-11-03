#!/bin/bash
./demo-online.py \
--server=ksef-demo \
--user=m32 \
--query=2 \
--query-type=incremental \
--date-from=2023-10-20T09:00:00Z \
--date-to=2023-10-20T09:15:00Z \
$*
