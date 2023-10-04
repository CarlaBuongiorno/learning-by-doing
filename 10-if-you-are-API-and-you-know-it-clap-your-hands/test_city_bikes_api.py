from city_bikes_api import (get_nl_network, get_nl_url, 
                            get_station_coordinates, construct_map_url)

def test_get_nl_network():
    obj = {'networks': [
        {'location': {'country': 'IE'}},
        {'location': {'country': 'NL'}}
        ]}
    expected_object = {'location': {'country': 'NL'}}
    nl = get_nl_network(obj)
    assert nl == expected_object

def test_get_nl_url():
    url = 'http://city.bikes.com'
    obj = {'location': {'country': 'NL'}, 'id': 'cykl'}
    nl_url = get_nl_url(obj, url)
    assert nl_url == f'http://city.bikes.com/cykl'

def test_get_station_coordinates():
    obj = {'network': {'id': 'cykl', 'location': {'country': 'NL'}, 'stations': [
            {'latitude': 51.9865, 'longitude': 5.66634, 'name': 'Atlas'},
            {'latitude': 51.97017, 'longitude': 5.66765, 'name': 'Cantil'}
            ]}}
    expected_coordinates = 51.9865, 5.66634
    lat, long = get_station_coordinates(obj)
    assert lat, long == expected_coordinates

def test_construct_map_url():
    lat = 51.9865
    long = 5.66634
    url = construct_map_url(lat, long)
    assert url == f'https://www.google.com/maps/@51.9865,5.66634,13z'