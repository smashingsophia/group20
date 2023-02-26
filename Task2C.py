from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    stations = build_station_list()
    update_water_levels(stations)
    N = 10
    
    x = stations_highest_rel_level(stations, N)
    
    print(x)
    
    
run()