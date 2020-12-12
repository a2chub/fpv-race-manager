#!/usr/bin/env python
# coding:utf-8

import os
import sys
import csv
import json
from copy import deepcopy

DATA_lap_file = 'Latest-Result.csv'      # QR app$B$N=PNO%G!<%?(B
DATA_result_file = 'data.json'  # $BCf4V%G!<%?%U%!%$%k(B
DATA_GS_CSV_file = 'data.csv'   # GSheet$B$NFI$_9~$_%U%#%"%k(B

DATA_PATH = '../data/data_csv/' # GoogleDrive$B$N%j%s%/(BPath

# $B3F<o(BPath$BJQ49(B
DATA_gss_file = os.path.join(DATA_PATH, DATA_GS_CSV_file)
LAP_DATA = os.path.join(DATA_PATH, DATA_lap_file)
RESULT_DATA = os.path.join(DATA_PATH, DATA_result_file)

LAST_DATA = None
CUR_CSV_RESULT = {}


def loadCSV(_LAP_DATA=LAP_DATA):
    global CUR_CSV_RESULT
    print( LAP_DATA )
    with open(_LAP_DATA, newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
      ret = {}
      for row in spamreader:
        _tmp = ', '.join(row).split(',')
        _pilot = {_tmp[0]: _tmp[1:] }
        ret.update(_pilot)
    CUR_CSV_RESULT = ret
    return CUR_CSV_RESULT


def loadLASTJSON():
    global LAST_DATA
    with open(DATA_result_file) as total_json:
        result_data = total_json.readlines()
        x = "".join(result_data)
        LAST_DATA = json.loads( x )
    return LAST_DATA


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

      _h_id_idx = int(_tmp[5]) -1
      _tgt_data['heats'][_h_id_idx]['heat'] = int(_tmp[5])
      _tgt_data['heats'][_h_id_idx]['laps'] = [float(i) for i in _tmp[0:3]]
      _tgt_data['heats'][_h_id_idx]['total'] = float(_tmp[3])
      _tgt_data['heats'][_h_id_idx]['unixtime'] = int(_tmp[4])
      print( _tgt_data )

      LAST_DATA["pilots"][pilotID] = deepcopy(_tgt_data)
    return LAST_DATA


def writeCurData():
    global CUR_CSV_RESULT, LAST_DATA
    print( LAST_DATA )
    with open(DATA_result_file, 'w') as write_json:
        new_result = json.dumps(parseCsvData(CUR_CSV_RESULT), indent=2)
        write_json.write( new_result )


def writeForGoogleSS_csv():
    global CUR_CSV_RESULT, LAST_DATA
    with open(DATA_result_file, 'w') as write_json:
        new_result = json.dumps(parseCsvData(CUR_CSV_RESULT), indent=2)
        write_json.write( new_result )


def cnvtJson2Csv():
    global LAST_DATA
    all_pilot = list(LAST_DATA["pilots"].keys())
    print( all_pilot )
    _time_all = []
    for _pilot in all_pilot:
        one_pilot = LAST_DATA['pilots'][_pilot]
        print( _pilot )
        #print( one_pilot )
        #print( one_pilot['heats'] )
        _total_times = []
        _complete_heat_cnt = 0
        _total_times.append( _complete_heat_cnt )
        for tt in one_pilot['heats'][:4]:
            if "total" in tt:
                _complete_heat_cnt += 1
                _total_times.append( tt['total'] )
            else:
                _total_times.append( -1 )
        _total_times[0] = _complete_heat_cnt
        _total_times.insert(0, _pilot)
        _time_all.append( _total_times )
    with open(DATA_gss_file, 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(_time_all)


def main():
    writeCurData()

if __name__ == "__main__":
    now_csv = loadCSV()
    print("now csv")
    print ( now_csv )

    loadLASTJSON()
    print(" Last Data")
    print( LAST_DATA )

    # QRapp$B$+$i$N(BCSV$B$rCf4V%U%)!<%^%C%H$K%3%s%P!<%H(B
    main()

    # $BCf4V%U%)!<%^%C%H$r(BGSheet$B$GFI$_9~$_2DG=$J(Bcsv$B$K%3%s%P!<%H(B
    cnvtJson2Csv()


