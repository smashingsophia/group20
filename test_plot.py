from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels,plot_water_level_with_fit
import numpy as np
stations = build_station_list()
station = stations[0]

x = np.linspace(0, 2, 10)
y = [0.1, 0.09, 0.23, 0.34, 0.78, 0.74, 0.43, 0.31, 0.01, -0.05]

plot_water_levels(station, x, y)
plot_water_level_with_fit(station, x, y, 4)