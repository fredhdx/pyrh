# type: ignore

import csv
import shelve

from pyrh import Robinhood
from datetime import datetime

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--username', required=True)
parser.add_argument('--password', required=True)
args = vars(parser.parse_args())

# !!!!!! change the username and passs, be careful when paste the code to public
rh = Robinhood(username=args["username"], password=args["password"])
rh.login()

# trade history
keys, orders = rh.trade_history()
with open(f"tade_history_{datetime.today().strftime('%Y-%m-%d')}.csv", "w") as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(orders)
# position data
positions, raw = rh.positions()
keys = ['symbol', 'quantity', 'price', 'created', 'updated']
with open(f"position_{datetime.today().strftime('%Y-%m-%d')}.csv", "w") as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(positions)
