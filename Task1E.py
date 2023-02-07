from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    stations = build_station_list()
    N = 9
    
    N_stations = rivers_by_station_number(stations, N)
    
    print(N_stations)


run()

