from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance, stations_within_radius

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