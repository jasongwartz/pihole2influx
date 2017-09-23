# pihole2influx
A script which will read Pihole statistics and write them to InfluxDB.

Run using:
```
docker run --name=pihole2influx \
  -e ENVIRONMENT_VARIABLE=value \       # see below for options
  jasongwartz/pihole2influx:arm32v6
```

The default image `jasongwartz/pihole2influx:arm32v6` is built for ARM devices (will work on all Raspberry Pi models).

Configuration:
The following parameters can be customised using environment variables:
- `INFLUX_HOST` - default is `localhost`
- `INFLUX_PORT` - default is `8086`
- `INFLUX_DATABASE` - default is `pihole`
- `PIHOLE_API` - default is `http://localhost/admin/api.php`
