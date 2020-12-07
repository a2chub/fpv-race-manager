

import os
import csv
import json

DATA_PATH = '../data/data_csv/'
DATA_lap_file = 'Latest-Result.csv'
DATA_result_file = 'data.json'

LAP_DATA = os.path.join(DATA_PATH, DATA_lap_file)
RESULT_DATA = os.path.join(DATA_PATH, DATA_result_file)


with open(LAP_DATA, newline='') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  ret = {}
  for row in spamreader:
    _tmp = ', '.join(row).split(',')
    _pilot = {_tmp[0]: _tmp[1:] }
    ret.update(_pilot)
  #print( json.dumps( ret ))

with open(DATA_result_file) as total_json:
    result_data = total_json.readlines()
    x = "".join(result_data)
    y = json.loads( x )
    print( y )


