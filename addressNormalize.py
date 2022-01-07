from rapidfuzz.process import extractOne
from stringProcess import hashedLocal,hashedCities, states, cities
import googlemaps, re

gmaps = googlemaps.Client(key='GOOGLE_API_KEY')

def localityFinder(city, address):
    local = ""
    ratio = 0
    for add in address:
        tup = extractOne(add,hashedLocal[city])
        if(tup[1]>=ratio):
            ratio = tup[1]
            local = tup[0]
            addLocal = add
    return local


def cityFinder(state, address):
    city = ""
    if(state != None):
        state = state.replace(" ", "")

    ratio = 0
    for add in address:
        tup = None
        tup = extractOne(add,hashedCities[state])
        if(tup[1]>=ratio):
            ratio = tup[1]
            city = tup[0]
            addCity = add
        
    if(ratio > 80):
        address.remove(addCity)
        return city
    return None


def stateFinder(address):
    state = None
    ratio = 0
    for add in address:
        tup = extractOne(add,states)
        if(tup[1]>=ratio):
            ratio = tup[1]
            state = tup[0]
            addState = add
    if(ratio > 90):
        address.remove(addState)
        return state
    return None

def googleAPI(address):
    adda = ' '.join(address)
    geocode_result = gmaps.geocode(adda)
    return geocode_result
    
def localityParser(geocode):
    locality = None
    for component in geocode['address_components']:
        if 'sublocality_level_2' in component['types']:
            locality = component['long_name']
            break
    
    if(locality == None):
        for component in geocode['address_components']:
            if 'sublocality_level_1' in component['types']:
                locality = component['long_name']
                break

    if(locality == None):
        for component in geocode['address_components']:
            if 'administrative_area_level_2' in component['types']:
                locality = component['long_name']
                break

    if(locality == None):
        for component in geocode['address_components']:
            if 'administrative_area_level_1' in component['types']:
                locality = component['long_name']
                break
    
    if(locality == None):
        for component in geocode['address_components']:
            if 'neighborhood' in component['types']:
                locality = component['long_name']
                break
    if(locality == None):
        for component in geocode['address_components']:
            if 'locality' in component['types']:
                locality = component['long_name']
                break
    return locality

def addNormalizer(address):
    geocode = googleAPI(address)[0]
    state = stateFinder(address)
    locality = localityParser(geocode)

    if(state == None):
        for component in geocode['address_components']:
            if 'administrative_area_level_1' in component['types']:
                state = extractOne(component['long_name'], states)[0]
                break
            
    city = cityFinder(state, address)

    if(city == None):
        for component in geocode['address_components']:
            if 'locality' in component['types']:
                city = extractOne(component['long_name'], cities)[0]
                break
            
        if(city == None):
            for component in geocode['address_components']:
                if 'administrative_area_level_2' in component['types']:
                    city = extractOne(component['long_name'], cities)[0]
                    break
            
    pincode = None
    
    for component in geocode['address_components']:
        if 'postal_code' in component['types']:
            pincode = component['long_name']
    if pincode == None:
        pincode = re.sub("[^0-9]", "", address[-1])

    coordinates = str(geocode['geometry']['location']['lat']) + "," + str(geocode['geometry']['location']['lng'])

    address = address[:-1]
    length = len(address)
    add1 = ' '.join(address[:length//2+1])
    add2 = ' '.join(address[length//2+1: ])
    add1 = add1.title()
    add2 = add2.title()

    finalAddress = {
        "addressline1":add1,
        "addressline2":add2,
        "locality":locality,
        "city":city,
        "state":state,
        "pincode":pincode,
        "geocodes":coordinates
    }
    return finalAddress
