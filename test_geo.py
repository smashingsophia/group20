from floodsystem.station import MonitoringStation
from floodsystem.geo import rivers_with_station, stations_by_distance, stations_by_river, stations_within_radius, rivers_by_station_number

def test_stations_by_distance():
    Test_station_list= []
    
    for i in range(50):
        s_id = "test-s-id"
        m_id = "test-m-id"
        label = "some station"
        coord = (i, 4.0)
        trange = (-2.3, 3.4445)
        river = "River X"
        town = "My Town"
        s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
        
        Test_station_list.append(s)
        
    
    x= stations_by_distance(Test_station_list, (0,0))

    assert type(x) == list
    
    
test_stations_by_distance()




def test_stations_within_radius():
    Test_station_list= []
    
    for i in range(50):
        s_id = "test-s-id"
        m_id = "test-m-id"
        label = "some station"
        coord = (i, 4.0)
        trange = (-2.3, 3.4445)
        river = "River X"
        town = "My Town"
        s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
        
        Test_station_list.append(s)
        
    x = stations_within_radius(Test_station_list, (0,0), 15)
    
    assert type(x) == list

test_stations_within_radius()


def test_rivers_with_station():
    Test_station_list= []
    
    for i in range(50):
        s_id = "test-s-id"
        m_id = "test-m-id"
        label = "some station"
        coord = (i, 4.0)
        trange = (-2.3, 3.4445)
        river = "River X"
        town = "My Town"
        s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
        
        Test_station_list.append(s)
        
    x= rivers_with_station(Test_station_list)
    
    assert type(x) == set
    
    

def test_stations_by_river():
    Test_station_list= []
    
    for i in range(50):
        s_id = "test-s-id"
        m_id = "test-m-id"
        label = "some station"
        coord = (i, 4.0)
        trange = (-2.3, 3.4445)
        river = "River X"
        town = "My Town"
        s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
        
        Test_station_list.append(s)
        
    x = stations_by_river(Test_station_list)
    
    assert type(x) == dict
    
def test_rivers_by_station_number():
    Test_station_list= []
    
    for i in range(50):
        s_id = "test-s-id"
        m_id = "test-m-id"
        label = "some station"
        coord = (i, 4.0)
        trange = (-2.3, 3.4445)
        river = "River X"
        town = "My Town"
        s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
        
        Test_station_list.append(s)
        
    x = rivers_by_station_number(Test_station_list,1)
    
    assert type(x) == list
    
test_rivers_by_station_number()
