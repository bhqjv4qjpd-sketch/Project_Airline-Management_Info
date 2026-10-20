class Airline:
   def __init__(self, name, fleet, operations):
       self.name = name
       self.fleet = fleet
       self.operations = operations

def PrintAirline (airline):
    print("Name: ", airline.name)
    print("Fleet: ", airline.fleet)
    print("Operations: ", airline.operations)
