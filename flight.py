class Flight:
    def __init__(self,ID,DepartureAirport,ArrivalAirport,DepartureTime,ArrivalTime,Passangers):
        self.ID = ID
        self.DepartureAirport = DepartureAirport
        self.ArrivalAirport = ArrivalAirport
        self.DepartureTime = DepartureTime
        self.ArrivalTime = ArrivalTime
        self.Passangers = Passangers

def PrintFlight (flight):
    print("ID: ", flight.ID)
    print("DepartureAirport: ", flight.DepartureAirport)
    print("ArrivalAirport: ", flight.ArrivalAirport)
    print("DepartureTime: ", flight.DepartureTime)
    print("ArrivalTime: ", flight.ArrivalTime)
    print("Passangers: ", flight.Passangers)

def TimeToMinutes (time):
# Converts and returns time hh:mm to minutes counted from 00:00
    try:
        parts = time.split(":")
        hours = int(parts[0])
        minutes = int(parts[1])
        return hours * 60 + minutes
    except ValueError:
         return -1

def FlightDuration (flight):
# Returns the duration of the flight in minutes
    departure = TimeToMinutes(flight.DepartureTime)
    arrival = TimeToMinutes(flight.ArrivalTime)
    duration = arrival - departure
    if duration < 0:
        duration += 24 * 60
    return duration

# test section
if __name__ == "__main__":
    flight = Flight("A11", "LEBL", "EGLL", "12:30", "14:30", 135)
    PrintFlight(flight)
    print(FlightDuration(flight))
