class Aircraft:
   def __init__(self, callsign, type, capacity):
       self.callsign = callsign
       self.type = type
       self.capacity = capacity

def PrintAircraft (aircraft):
    print("Callsign: ", aircraft.callsign)
    print("Type: ", aircraft.type)
    print("Capacity: ", aircraft.capacity)

# test section
aircraft = Aircraft("AAAA","A220-100",135)
PrintAircraft(aircraft)
