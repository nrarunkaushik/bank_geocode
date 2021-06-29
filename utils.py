"""Support functions"""

import requests
import urllib.parse
import re

def find_coord(obs):
    """Function to find latitude and longitude of a data point using
    its address, branch name, center, district and state information.
    If one of more match is found, then the coordinates are checked if
    they are inside India's bounding box.
    If nothing matches, it will return NaN in string format
    
    Input:
    
        obs: pd.Series object
            Datapoint of one branch with info on address, branch name,
            center, district and state
        
    Output
    
        (index,lat,long) : tuple object
            Index od observation, latitude and longitude identified

    """

    address = obs['Address']
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    if len(response) != 0:
        for res in response:
            if float(res['lon']) > 68.11 and float(res['lon']) < 97.4:
                if float(res['lat']) > 6.46 and float(res['lat']) < 35.52:
                    return obs.name,res['lat'],res['lon']
            
    address = obs.Bank + ', '+ obs.Branch + ', ' + obs.Center
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json&type=bank'
    response = requests.get(url).json()
    if len(response) != 0:
        for res in response:
            if float(res['lon']) > 68.11 and float(res['lon']) < 97.4:
                if float(res['lat']) > 6.46 and float(res['lat']) < 35.52:
                    return obs.name,res['lat'],res['lon']
            
    address = obs.Bank + ', '+ obs.Branch + ', ' + obs.Center
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    if len(response) != 0:
        for res in response:
            if float(res['lon']) > 68.11 and float(res['lon']) < 97.4:
                if float(res['lat']) > 6.46 and float(res['lat']) < 35.52:
                    return obs.name,res['lat'],res['lon']
            
    address = obs.Bank + ', '+ obs.Branch + ', ' + obs.District
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json&type=bank'
    response = requests.get(url).json()
    if len(response) != 0:
        for res in response:
            if float(res['lon']) > 68.11 and float(res['lon']) < 97.4:
                if float(res['lat']) > 6.46 and float(res['lat']) < 35.52:
                    return obs.name,res['lat'],res['lon']
            
    address = obs.Bank + ', '+ obs.Branch + ', ' + obs.District
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    if len(response) != 0:
        for res in response:
            if float(res['lon']) > 68.11 and float(res['lon']) < 97.4:
                if float(res['lat']) > 6.46 and float(res['lat']) < 35.52:
                    return obs.name,res['lat'],res['lon']
            
    address = obs.Branch + ', ' + obs.Center + ', ' + obs.District + ', ' + obs.State
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    if len(response) != 0:
        for res in response:
            if float(res['lon']) > 68.11 and float(res['lon']) < 97.4:
                if float(res['lat']) > 6.46 and float(res['lat']) < 35.52:
                    return obs.name,res['lat'],res['lon']
            
    address = obs.Center + ', ' + obs.District + ', ' + obs.State
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    if len(response) != 0:
        for res in response:
            if float(res['lon']) > 68.11 and float(res['lon']) < 97.4:
                if float(res['lat']) > 6.46 and float(res['lat']) < 35.52:
                    return obs.name,res['lat'],res['lon']
            
    address = obs.District + ', ' + obs.State
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    if len(response) != 0:
        for res in response:
            if float(res['lon']) > 68.11 and float(res['lon']) < 97.4:
                if float(res['lat']) > 6.46 and float(res['lat']) < 35.52:
                    return obs.name,res['lat'],res['lon']
            
    return obs.name,'nan','nan'

def trim(x):
    """To remove postal office organizational naming in place name"""

    y = re.split(r' S.O', x)[0]
    y = re.split(r' H.O', y)[0]
    y = re.split(r' P.O', y)[0]
    y = re.split(r' G.P.O', y)[0]
    return y
