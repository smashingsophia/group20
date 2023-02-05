# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from distutils.command import install
from .utils import sorted_by_key  # noqa



def stations_by_distance(stations, p):

    station_distance= []

    for station in stations:
        coord= station.coord
        distance= haversine(p, coord)
        
        station_distance += (station, distance)
        
    return station_distance

