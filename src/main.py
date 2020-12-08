
import os
import csv
import json

DATA_PATH = '../data/data_csv/'
DATA_lap_file = 'Latest-Result.csv'
DATA_result_file = 'data.json'

LAP_DATA = os.path.join(DATA_PATH, DATA_lap_file)
RESULT_DATA = os.path.join(DATA_PATH, DATA_result_file)

LAST_DATA = None

with open(LAP_DATA, newline='') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  ret = {}
  for row in spamreader:
    _tmp = ', '.join(row).split(',')
    _pilot = {_tmp[0]: _tmp[1:] }
    ret.update(_pilot)

with open(DATA_result_file) as total_json:
    result_data = total_json.readlines()
    x = "".join(result_data)
    LAST_DATA = json.loads( x )

def parseCsvData(rawArr):
  _template = {
          "name":"",
          "total":-1,
          "laps":[-1,-1,-1,-1],
          "heat":-1,
          'unixtime':-1
          }
  for pilotID in ret.keys():
      _tmp = rawArr[pilotID]
      _template["name"] = pilotID
      _template['total'] = _tmp[4]
      _template['laps'] = _tmp[0:4]
      _template['heat'] = _tmp[6]
      _template['unixtime'] = _tmp[5]
      print(_template )


if __name__ == "__main__":

  parseCsvData(ret)
