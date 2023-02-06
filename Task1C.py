from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key #noqa

def run():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10
    
    x= stations_within_radius(stations, centre, r)
    y= []
    
    for i in x:
        y.append(i.name)
        
    sorted_list= sorted(y)
    
    print(f"Sations within {r}km\n")
    print(sorted_list)
    
    
run()