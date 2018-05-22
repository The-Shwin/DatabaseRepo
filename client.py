from influxdb import DataFrameClient
import argparse
import datetime
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as pdr



def parse_args():
    parser = argparse.ArgumentParser(
        description='Argument parser for influxdb')
    parser.add_argument('--host', type=str, required=False, default='localhost', help='hostname')
    parser.add_argument('--port', type=int, required=False, default=8086, help='port')
    return parser.parse_args()


def main(host='localhost', port=8086):
    user = 'root'
    password = 'root'
    dbname = 'Stock Data'
    protocol = 'line'
    client = DataFrameClient(host, port, user, password, dbname)
    print('passed DataFrameClient creation')
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime(2016, 1, 1)
    df = pdr.DataReader('F', 'iex', start, end)
    df.index = pd.DatetimeIndex(pd.to_datetime(list(df.index)))
    print(type(df.index))
    print('Trying to create database')
    client.create_database(dbname)
    client.write_points(df, 'Stock', protocol=protocol)
    client.query("select * from stock")
    client.drop_database(dbname)
    print('Finished')

if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port)
