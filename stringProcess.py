import csv

locality = set()
cities = set()
states = set()
hashedLocal = {}
hashedCities = {}

with open("pincode.csv", 'r') as file:
    csvreader = csv.DictReader(file)
    for pin in csvreader:
        #States
        states.add(pin['StateName'])
        
        #Districts
        stateKey = pin['StateName'].replace(" ", "")
        
        if stateKey in hashedCities.keys():
            hashedCities[stateKey].add(pin['District'])
        else:
            hashedCities[stateKey] = set()
            hashedCities[stateKey].add(pin['District'])
        
        #Locality
        distKey = pin['District'].replace(" ", "")

        if distKey in hashedLocal.keys():
            hashedLocal[distKey].add(pin['OfficeName'])
            hashedLocal[distKey].add(pin['RegionName'])
        else:
            hashedLocal[distKey] = set()
            hashedLocal[distKey].add(pin['OfficeName'])
            hashedLocal[distKey].add(pin['RegionName'])
        
        cities.add(pin['District'])

file.close()
cities = list(cities)
states = list(states)

  



