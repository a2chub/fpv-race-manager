

LapCnt = 4
HEATLIST = ["A","B","C","D"]
Pilot= ["1","2","3"]

pilots = []

def getLapArr(lap_cnt=LapCnt):
    return ["-1" for i in range(lap_cnt)]

def getResultInitData(lap_cnt=LapCnt):
    Result = getLapArr(lap_cnt)
    ret = ""
    for i in HEATLIST:
        _heat = []
        for ii in Pilot:
            _heat.append(i+ii)
        pilots.append( _heat )


    for i in pilots:
        for ii in i:
            ret +=  "%s,%s"%(ii,",".join(Result))
            ret += "\n"
    return ret

def makePilotsData(pilot_list, lap_cnt=LapCnt):
    ret = {}
    _heats = {}
    for h in HEATLIST:
        _heats.update({"heat%s"%h:{
            "lap":getLapArr(lap_cnt),
            "total":-1,
            "unixtime":99999999
            }
            })
    for i in pilot_list:
        _key = "%s"%i
        x = { _key: { "name": i } }
        x[_key].update(_heats)
        ret.update(x)
    return ret


if __name__ == "__main__":
    print( getResultInitData() )
    print( makePilotsData( Pilot ) )

