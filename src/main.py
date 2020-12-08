
import os
import csv
import json

DATA_PATH = '../data/data_csv/'
DATA_PATH = '../data/'
DATA_lap_file = 'heat.csv'
DATA_result_file = 'data.json'

LAP_DATA = os.path.join(DATA_PATH, DATA_lap_file)
RESULT_DATA = os.path.join(DATA_PATH, DATA_result_file)

LAST_DATA = None
CUR_CSV_RESULT = {}


def loadCSV(_LAP_DATA=LAP_DATA):
    global CUR_CSV_RESULT
    with open(_LAP_DATA, newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
      ret = {}
      for row in spamreader:
        _tmp = ', '.join(row).split(',')
        _pilot = {_tmp[0]: _tmp[1:] }
        ret.update(_pilot)
    CUR_CSV_RESULT = ret


def loadLASTJSON():
    global LAST_DATA
    with open(DATA_result_file) as total_json:
        result_data = total_json.readlines()
        x = "".join(result_data)
        LAST_DATA = json.loads( x )


def parseCsvData(rawArr):
    global CUR_CSV_RESULT, LAST_DATA
    _template = {
          "heats":[{},{},{},{},{},{},{},{},{},{},{}]
          }

    for pilotID in CUR_CSV_RESULT.keys():
      _tmp = rawArr[pilotID]

      if pilotID in LAST_DATA['pilots']:
          _tgt_data = LAST_DATA['pilots'][pilotID]
      else:
          _tgt_data = _template

      _h_id_idx = int(_tmp[6]) -1
      _tgt_data['heats'][_h_id_idx]['heat'] = int(_tmp[6])
      _tgt_data['heats'][_h_id_idx]['laps'] = [float(i) for i in _tmp[0:4]]
      _tgt_data['heats'][_h_id_idx]['total'] = float(_tmp[4])
      _tgt_data['heats'][_h_id_idx]['unixtime'] = int(_tmp[5])

      LAST_DATA["pilots"][pilotID] = _tgt_data
    return LAST_DATA


def writeCurData():
    global CUR_CSV_RESULT, LAST_DATA
    with open(DATA_result_file, 'w') as write_json:
        new_result = json.dumps(parseCsvData(CUR_CSV_RESULT), indent=2)
        write_json.write( new_result )


def main()
    pass

if __name__ == "__main__":
    loadCSV()
    loadLASTJSON()
    writeCurData()




