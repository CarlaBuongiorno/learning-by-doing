import requests
import subprocess


def main():
    url = 'http://api.citybik.es/v2/networks' # process
    r = requests.get(url) # input/output -> can't test
    nl = get_nl_network(r.json()) # process
    netherlands_url = get_nl_url(nl, url) # process
    r = requests.get(netherlands_url) # input/output
    latitude, longitude = get_station_coordinates(r.json())
    station = construct_map_url(latitude, longitude) # process
    subprocess.run(['firefox', station]) # output


def get_nl_network(obj):
    for network in obj['networks']:
        if network['location']['country'] == 'NL':
            nl = network
    return nl


def get_nl_url(nl, url):
    return f'{url}/{nl["id"]}'


def get_station_coordinates(obj):
    for station in obj['network']['stations']:
        if station['name'] == 'Atlas':
            lat = station['latitude']
            long = station['longitude']
    return lat, long


def construct_map_url(lat, long):
    # process (creating an f string) ->
    # can test you're creating the correct data to give to it
    return f'https://www.google.com/maps/@{lat},{long},13z' 


if __name__ == '__main__':
    main()
