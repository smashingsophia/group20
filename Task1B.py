from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    p= (52.2053, 0.1218)

    x= stations_by_distance(stations, p)
    y= []
    for i in x:
        y.append((i[0].name, i[0].town, i[1]))
        
    first_ten = y[:10]
    last_ten = y[-10:]

    print("First ten stations:\n")
    print(first_ten, "\n")
    print("Last ten stations:\n")
    print(last_ten)
    

run()