class Aircraft:
    def __init__(self, callsign, type, capacity):
        self.callsign = callsign
        self.type = type
        self.capacity = int(capacity)


def PrintAircraft(aircraft):
    print("Callsign: ", aircraft.callsign)
    print("Type: ", aircraft.type)
    print("Capacity: ", aircraft.capacity)


def PrintAircrafts(aircrafts):
    for aircraft in aircrafts:
        PrintAircraft(aircraft)


def AddAircraft(aircrafts, aircraft):
    aircrafts.append(aircraft)


def RemoveAircraft(aircrafts, callsign):
    for aircraft in aircrafts:
        if aircraft.callsign == callsign:
            aircrafts.remove(aircraft)
            return 0
    return -1


def LoadAircrafts(filename):
    aircrafts = []
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 3:
                    try:
                        callsign = parts[0]
                        type_ac = parts[1]
                        capacity = int(parts[2])
                        aircrafts.append(Aircraft(callsign, type_ac, capacity))
                    except ValueError:
                        # Ignora la línea de encabezado (CALLSIGN AC-TYPE SEATS)
                        pass
    except FileNotFoundError:
        return []
    return aircrafts


def SaveAircrafts(aircrafts, filename):
    with open(filename, "w") as file:
        for aircraft in aircrafts:
            file.write(f"{aircraft.callsign} {aircraft.type} {aircraft.capacity}\n")


# test section
if __name__ == "__main__":
    aircraft1 = Aircraft("AAAA", "A220-100", 135)
    aircraft2 = Aircraft("BBBB", "A230-100", 200)
    aircrafts = [aircraft1, aircraft2]

    print("Initial aircrafts:")
    PrintAircrafts(aircrafts)

    SaveAircrafts(aircrafts, "Aircrafts.txt")
    print("\nAircrafts saved to file.")

    loaded_aircrafts = LoadAircrafts("Aircrafts.txt")
    print("\nLoaded aircrafts:")
    PrintAircrafts(loaded_aircrafts)

    aircraft3 = Aircraft("CCCC", "A320-200", 180)
    AddAircraft(loaded_aircrafts, aircraft3)

    result = RemoveAircraft(loaded_aircrafts, "BBBB")
    print("\nRemove result:", result)