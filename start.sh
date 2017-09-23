#!/bin/ash

while true; do python pihole2influx.py; sleep $DAEMON_SLEEP_TIME; done

