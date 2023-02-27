import datetime
import numpy as np
import matplotlib
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list,update_water_levels
stations = build_station_list()[:30]
severe = []
high = []
moderate = []
low = []
for station in stations:
    dt = 2
    dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
    dates = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(dates, levels, 4)
    poly = np.poly1d(p_coeff)
    dp = np.polyder(poly, 1)
    if levels[-1] > station.typical_range[1] and dp(-1) > 0:
        severe.append(station.town)
    elif levels[-1] > station.typical_range[1]:
        high.append(station.town)
    elif levels[-1] < station.typical_range[0]:
        low.append(station.town)
    else:
        moderate.append(station.town)
print('severe:',severe, 'high:',high, 'moderate:',moderate, 'low:',low)
    
    
        
        

    