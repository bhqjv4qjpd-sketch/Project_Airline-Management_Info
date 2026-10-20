class Airline:
    def __init__(self, name, fleet, operations):
        self.name = name
        self.fleet = fleet
        self.operations = operations

def PrintAirline(airline):
    print("Name: ", airline.name)
    print("Fleet: ")
    for aircraft in airline.fleet:
        PrintAircraft(aircraft)
    print("Operations: ")
    for flight in airline.operations:
        PrintFlight(flight)

# test section
if __name__ == "__main__":
    from aircraft import *
    from flight import *

    # Test PrintAirline
    aircrafts = []
    aircrafts.append(Aircraft("AAAA", "A220-100", 135))
    aircrafts.append(Aircraft("BBBB", "A230-100", 200))

    flights = []
    flights.append(Flight("A11", "LEBL", "EGLL", "12:30", "14:30", 120))
    flights.append(Flight("A12", "EGLL", "LEBL", "16:30", "18:30", 150))

    airline = Airline("Vueling", aircrafts, flights)
    PrintAirline(airline)