
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
          "heats-laps":    [[],[],[],[],[],[],[],[],[],[],[]],
          "heats-total":   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
          "heats-unixtime":[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
          }
  for pilotID in ret.keys():
      _tmp = rawArr[pilotID]

      if pilotID in LAST_DATA:
          _tgt_data = LAST_DATA[pilotID]
      else:
          _tgt_data = _template

      _tgt_h_id = int(_tmp[6])
      _tgt_data['heats-laps'][_tgt_h_id] = _tmp[0:4]
      _tgt_data['heats-total'][_tgt_h_id] = _tmp[4]
      _tgt_data['heats-unixtime'][_tgt_h_id] = _tmp[5]


      LAST_DATA["pilots"][pilotID] = _tgt_data
  return LAST_DATA

if __name__ == "__main__":

  parseCsvData(ret)


