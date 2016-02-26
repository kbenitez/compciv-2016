import requests
import json

def read_mapzen_credentials():
    creds_filename = "creds_mapzen.txt"
    keytxt = open(creds_filename).read().strip() # e.g. "search-blahblah"
    return keytxt

def fetch_mapzen_response(location):
    """
    "location" is a string that will be passed onto Mapzen API for geocoding

    returns a text string containing JSON-formatted data from Mapzen
    """
    MAPZEN_BEG =  'https://search.mapzen.com/v1/search'
    keytxt = read_mapzen_credentials()
    mapzenparams = {'api_key': keytxt,  'text': location}
    resp = requests.get(MAPZEN_BEG, params = mapzenparams)
    return resp.text

def parse_mapzen_response(txt):
    """
    "txt" is a string containing JSON-formatted text from Mapzen's API

    returns a dictionary containing the useful key/values from the most
    relevant result.
    """
    geoDict = {}
    receivedJSONDict = json.loads(txt)
    if receivedJSONDict['features']:
        geoDict['status'] = "OK"
        geoDict['label'] = receivedJSONDict['features'][0]['properties']['label']
        geoDict['confidence'] = receivedJSONDict['features'][0]['properties']['confidence']
        geoDict['latitude'] = receivedJSONDict['features'][0]['geometry']['coordinates'][1]
        geoDict['longitude'] = receivedJSONDict['features'][0]['geometry']['coordinates'][0]
    else:
    	geoDict['status'] = None
    return geoDict


def geocode(location):
    """
    Using Mapzen Search API to attempt to geocode a location string 

    What it expects:
    ----------------
    It expects a "location" string, representing some kind of human-readable,
     existing geographical location, e.g. "Cornwall, NY"

    It also expects the variable `CREDS_FILE` to point to an existing file
    that contains a valid Mapzen Search key for the particular student.

    What it does:
    -------------
    It opens and reads the file at CREDS_FILE to get the API key.

    It calls the Mapzen Search API via a HTTP request, using the API key, 
    and the user-provided "location" string as the "text" parameter.

    It deserializes the Mapzen Search response into a dictionary, using
    the JSON library.

    It then creates a dictionary.

    What it returns:
    ----------------
    A dictionary containing these key-value pairs:

    - query_text: the "location" string provided by the user
    - label: The string label that Mapzen provides of the found location
    - confidence: A float representing the confidence level that Mapzen has in its result
    - latitude: a float representing the latitude coordinate
    - longitude: a float representing the longitude coordinate
    - status: "OK", a string that indicates a result was found; Else, None

    """
    GeoDict = parse_mapzen_response(fetch_mapzen_response(location))
    GeoDict['query_text'] = location
    return GeoDict
