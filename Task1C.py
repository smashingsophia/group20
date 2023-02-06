from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10
    
    x= stations_within_radius(stations, centre, r)
    y= []
    for i in x:
        y.append(i.name)
        
    sorted_list= y.sort()
    
    print(sorted_list)
    
    
run()