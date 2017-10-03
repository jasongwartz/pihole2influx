from influxdb import InfluxDBClient
import requests
import os
import datetime


INFLUX_HOST = os.environ['INFLUX_HOST'] if 'INFLUX_HOST' in os.environ else 'localhost'
INFLUX_PORT = os.environ['INFLUX_PORT'] if 'INFLUX_PORT' in os.environ else 8086
INFLUX_DATABASE = os.environ['INFLUX_DATABASE'] if 'INFLUX_DATABASE' in os.environ else 'pihole'
PIHOLE_API = os.environ['PIHOLE_API'] if 'PIHOLE_API' in os.environ else 'http://localhost/admin/api.php'

def get_pihole_stats():
    data =  requests.get(PIHOLE_API).json()
    data['ads_percentage_today'] = float(data['ads_percentage_today']) # Will be refused by influxdb if it's an integer
    return data

def write_to_influx(stats_dict):
    client = InfluxDBClient(INFLUX_HOST, INFLUX_PORT, '', '', INFLUX_DATABASE)
    client.create_database('pihole')
    client.write_points([
        {
            'measurement': 'pihole',
            'fields': stats_dict,
        }
    ])
    print("{} Wrote pihole data to influxdb.".format(str(datetime.datetime.now())))

def main():
    stats = get_pihole_stats()
    write_to_influx(stats)

if __name__ == "__main__":
    main()
