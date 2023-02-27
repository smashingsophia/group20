
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list,update_water_levels

def run():
    stations = build_station_list()
    #print(stations)
    update_water_levels(stations)
    names = stations_highest_rel_level(stations, 5)
    
    #print(names)
    for i in range(5):
         # Station name to find
        station_name = names[i][0]
        #print(station_name)

    # Find station
        station_current = None
        for station in stations:
            if station.name == station_name:
                station_current = station
                break
        #print(station_current)

    # Check that station could be found. Return if not found.
        if not station_current:
            print("Station {} could not be found".format(station_name))
            return


    # Fetch data over past 10 days
        dt = 10
        dates, levels = fetch_measure_levels(
            station_current.measure_id, dt=datetime.timedelta(days=dt))

    # Print level history
        
        plot_water_levels(station_current, dates, levels)
    
    
    
    

run()