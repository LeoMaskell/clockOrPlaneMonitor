import requests
from geopy.distance import geodesic


# NOTE: all mesurements are metric


planes = requests.get("https://opensky-network.org/api/states/all").json() # get planes

# example coords
Mumbai = (19.0760, 72.8777)
Pune = (18.5204, 73.8567)
Liverpool = (53.3349, -2.8496) # JLA


def parse_planes(plane):
    dictPlane = dict(callsign = plane[1].strip(), latt = plane[6], long = plane[5], alt = plane[7], time = plane[3], velocity = plane[9]) # NOTE: uses barometric alt not geometric alt - uses pressure
    return dictPlane

def geo_dist(pointA, pointB):
    return geodesic(pointA, pointB).km

def postcodeToLattLong(postCode):
    try:
        lookup = requests.get(f"https://api.postcodes.io/postcodes/{postCode}").json()["result"]
        coords = (lookup["latitude"], lookup["longitude"])
        return coords
    except:
        return LookupError
        exit
    

def in_radius(planes, coords, radius): # TODO: make the coords the w3w_addr
    # NOTE: coords is a tuple
    # NOTE: radius is in km
    planeLs = [] # list of planes (in dict form)

    for plane in planes:
        plane = parse_planes(plane)
        if geo_dist((plane["latt"], plane["long"]), coords) < radius:
            planeLs.append(plane)
    return planeLs


print(f"coords: {postcodeToLattLong('l24 1yd')}") # JLA airport for an example
print(in_radius(planes["states"], Liverpool, 5))


"""
print(planes.keys())
print(f"example data: {planes["states"][0]}")


print(parse_planes(planes["states"][0]))
"""