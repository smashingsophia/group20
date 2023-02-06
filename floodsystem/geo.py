# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key #noqa
from haversine import haversine

def stations_by_distance(stations, p):

    station_distance= []

    for station in stations:
        coord= station.coord
        distance= haversine(p, coord)
        
        station_distance.append((station, distance))
        
    station_distance = sorted_by_key(station_distance, 1)
            
    return station_distance




def stations_within_radius(stations, centre, r):
    stations_in_radius = []

    for station in stations:
        coord = station.coord
        distance = haversine(centre, coord)
        
        if distance <= r:
            stations_in_radius.append(station)     
            
        else:
            continue           
            
    return stations_in_radius



def rivers_with_station(stations):
    river_names = set()
       
    for station in stations:
        river_names.add(station.river)

    
    set(river_names)
    
    return river_names
        
        
def stations_by_river(stations):
    rivers_dictionary = {}

    for station in stations:
        if station.river not in rivers_dictionary:
            rivers_dictionary[station.river]= [station.name]
            
        else:
            rivers_dictionary[station.river].append(station.name)

    return rivers_dictionary
    
    
def rivers_by_station_number(stations,N):
    map = {}
    for river in stations:
        if river.river in map:
            map[river.river] += 1
        else:
            map[river.river] = 1 #for non-existing keys it just creates one
    riverlist = [(river, number) for river, number in map.items()]
    riverlist.sort(key=lambda x: x[1], reverse=True)
    nlist = riverlist[:N]
    i = N
    flag = True
    while i<len(riverlist) and flag == True:
        if riverlist[i] == riverlist[N-1]:
            nlist.append(riverlist[i])
        else:
            flag = False
            
    return nlist
    


    
        
    