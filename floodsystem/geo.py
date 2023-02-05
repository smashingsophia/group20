# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


from haversine import haversine

def stations_by_distance(stations, p):

    station_distance= []

    for station in stations:
        coord= station.coord
        distance= haversine(p, coord)
        
        station_distance.append((station, distance))
        
    station_distance = sorted_by_key(station_distance, 1)
            
    return station_distance


