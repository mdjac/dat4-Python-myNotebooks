import json
import requests
import folium
import urllib


def get_geojson(url): 
    """
    return the response body as json
    GeoJSON is an open standard format designed for representing simple geographical features, along with their non-spatial attributes
    """
    response = requests.get(url)
    geo_json = response.json()
    return geo_json


def get_city_location(city='Copenhagen'):
    """Get the location coordinates from OpenStreetMaps"""
    url_nomatim_api = 'https://nominatim.openstreetmap.org/search'
    r = requests.get(url_nomatim_api, params={'format': 'json', 'city': city})
    results = r.json()  # Potentially many matches
    print('results: ',results)
    location = results[0]
    lat, lon = float(location['lat']), float(location['lon'])
    return lat, lon


cph_lat, cph_lon = get_city_location()
url_environ = 'http://wfs-kbhkort.kk.dk/k101/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=k101:f_udsatte_byomraader&outputFormat=application%2Fjson&SRSNAME=EPSG:4326'
geo_json = get_geojson(url_environ) # contains attribute: geometri: type: multipolygon
print('\n\nGeoJSON open standard format:\n',geo_json)

map_osm = folium.Map(location=(cph_lat, cph_lon), zoom_start=10) # show the map
folium.GeoJson(geo_json, name='geojson').add_to(map_osm) # add 
map_osm.save('./osm2.html')
map_osm