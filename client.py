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
    parser.add_argument('--port', type=int, required=False, default=8088, help='port')
    return parser.parse_args()


def main(host='localhost', port=8088):
    user = 'root'
    password = 'root'
    dbname = 'Stock Data'
    protocol = 'json'
    client = DataFrameClient(host, port, user, password, dbname)
    print('passed DataFrameClient creation')
    df = pdr.DataReader('F', 'robinhood')
    print('Trying to create database')
    client.create_database(dbname)
    #client.write_points(df, 'Stock', protocol=protocol)
    #client.query("select * from stock")
    #client.drop_database(dbname)


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port)
