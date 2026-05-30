import requests

planes = requests.get("https://opensky-network.org/api/states/all").json()

print(planes.keys())
print(f"example data: {planes["states"][0]}")

def parse_planes(plane):
    dictPlane = dict(callsign = plane[1].strip(), latt = plane[6], long = plane[5], alt = plane[7], time = plane[3], velocity = plane[9]) # NOTE: uses barometric alt not geometric alt - uses pressure
    return dictPlane

print(parse_planes(planes["states"][0]))