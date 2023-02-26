from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    list = []
    
    for station in stations:
        level = MonitoringStation.relative_water_level(station)
        
        if level == None:
            pass
        elif level <= tol:
            pass
        else:
            x = (station.name, level)
            list.append(x)
            
    sorted_list = sorted_by_key(list, 1, True)
            
    return sorted_list


def stations_highest_rel_level(stations, N):
    list = []
    
    for station in stations:
        level = MonitoringStation.relative_water_level(station)
        
        if level == None:
            pass
        else:
            x = (station.name, level)
            list.append(x)
        
    sorted_list = sorted_by_key(list, 1, True)
    N_highest = sorted_list[:N]
    
    return N_highest

