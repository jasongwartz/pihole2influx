FROM arm32v6/python:alpine3.6

RUN pip install influxdb
COPY pihole2influx.py /
COPY start.sh /

ENV DAEMON_SLEEP_TIME=60
CMD ["/start.sh"]


