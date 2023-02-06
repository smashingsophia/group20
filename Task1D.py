from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run_f1():
    stations = build_station_list()
    x = rivers_with_station(stations) 
    
    length = len(x)
    sorted_stations = sorted(x)
    
    first_10 = sorted_stations[:10]
    
    print(f"{length} stations\n")
    print(f"first 10- {first_10}\n")
    
run_f1()



def run_f2():
    stations = build_station_list()
    
    y = stations_by_river(stations)
    
    
    
    river_aire = sorted(y["River Aire"])
    river_cam = sorted(y["River Cam"])
    river_thames = sorted(y["River Thames"])
    
    print(f"River Aire:\n{river_aire}\n")
    print(f"River Cam:\n{river_cam}\n")
    print(f"River Thames:\n{river_thames}\n")
    

run_f2()
    


