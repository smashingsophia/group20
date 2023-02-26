from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    
    x = stations_level_over_threshold(stations, tol)
    
    print(x)
    
    
    
run()