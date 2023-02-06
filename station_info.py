from distutils.command.build import build
from floodsystem.stationdata import build_station_list

x = build_station_list()

for i in x:
    print(f"{i}\n")