

import os
import csv
import json

DATA_PATH = '../data/data_csv/'
DATA_lap_file = 'Latest-Result.csv'
DATA_result_file = 'result_A.csv'

LAP_DATA = os.path.join(DATA_PATH, DATA_lap_file)
RESULT_DATA = os.path.join(DATA_PATH, DATA_result_file)


with open(LAP_DATA, newline='') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  ret = {}
  for row in spamreader:
    _tmp = ', '.join(row).split(',')
    _pilot = {_tmp[0]: _tmp[1:] }
    ret.update(_pilot)
  print( json.dumps( ret ))

with open(RESULT_DATA, newline='') as total_csv:
  total_result = csv.reader(total_csv, delimiter=' ', quotechar='|')


pilot = "A1":{
        "name": "A1",
        "heat1":{
            "lap":[-1,-1,-1,-1],
            "total":-1,
            "unixtime":99999999
            }
        }






