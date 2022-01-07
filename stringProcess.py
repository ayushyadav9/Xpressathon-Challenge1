from fuzzywuzzy import fuzz, process
import json


pincodes = json.load(open('pincode.json'))

locality = set()
cities = set()
states = set()
hashedLocal = {}
hashedCities = {}

for pin in pincodes['results']:

    #States
    states.add(pin['StateName'])
    
    #Districts
    stateKey = pin['StateName'].replace(" ", "")
    
    if stateKey in hashedCities.keys():
        hashedCities[stateKey].append(pin['District'])
    else:
        hashedCities[stateKey] = []
        hashedCities[stateKey].append(pin['District'])
    
    #Locality
    distKey = pin['District'].replace(" ", "")

    if distKey in hashedLocal.keys():
        hashedLocal[distKey].append(pin['OfficeName'])
        hashedLocal[distKey].append(pin['RegionName'])
    else:
        hashedLocal[distKey] = []
        hashedLocal[distKey].append(pin['OfficeName'])
        hashedLocal[distKey].append(pin['RegionName'])
    
    
    # hashedCities[pin['StateName'].replace(" ", "")].append(pin["District"])
    # hashedLocal[pin['District'].replace(" ", "")].append(pin["OfficeName"])
    # hashedCities.update(pin['StateName'].replace(" ", ""), pin["District"])
    # hashedLocal.update(pin['District'].replace(" ", ""), pin["OfficeName"])

    # locality.add(pin['OfficeName'])
    cities.add(pin['District'])

# locality = list(locality)
cities = list(cities)
states = list(states)

  



