flights = {"JFK": ["LAX", "DFW"], "LAX" : ["JFK"], "DFW" : ["JFK", "ATL"], "ATL" : ["DFW"]}

print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])