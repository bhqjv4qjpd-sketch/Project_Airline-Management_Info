class Flight:
    def __init__(self, id, departure_airport, arrival_airport, departure_time, arrival_time, passengers):
        self.id = id
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.passengers = int(passengers)


def PrintFlight(flight):
    print("ID: ", flight.id)
    print("Departure Airport: ", flight.departure_airport)
    print("Arrival Airport: ", flight.arrival_airport)
    print("Departure Time: ", flight.departure_time)
    print("Arrival Time: ", flight.arrival_time)
    print("Passengers: ", flight.passengers)


def PrintFlights(flights):
    for flight in flights:
        PrintFlight(flight)


def AddFlight(flights, flight):
    flights.append(flight)


def RemoveFlight(flights, flight_id):
    for flight in flights:
        if flight.id == flight_id:
            flights.remove(flight)
            return 0
    return -1


def TimeToMinutes(time):
    try:
        parts = time.strip().split(":")
        hours = int(parts[0])
        minutes = int(parts[1])
        return hours * 60 + minutes
    except (ValueError, IndexError):
        return -1


def FlightDuration(flight):
    departure = TimeToMinutes(flight.departure_time)
    arrival = TimeToMinutes(flight.arrival_time)
    duration = arrival - departure
    if duration < 0:
        duration += 24 * 60
    return duration


def LoadFlights(filename):
    flights = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split()
                # Formato en operaciones.txt: ID TIMD TIMA DEPT ARRV PASS
                if len(parts) == 6:
                    try:
                        flight_id = parts[0]
                        dep_time = parts[1]
                        arr_time = parts[2]
                        dep_apt = parts[3]
                        arr_apt = parts[4]
                        passengers = int(parts[5])
                        flights.append(Flight(flight_id, dep_apt, arr_apt, dep_time, arr_time, passengers))
                    except ValueError:
                        # Ignora la línea de cabecera
                        pass
    except FileNotFoundError:
        return []
    return flights


def SaveFlights(flights, filename):
    with open(filename, "w") as file:
        for flight in flights:
            file.write(f"{flight.id} {flight.departure_time} {flight.arrival_time} {flight.departure_airport} {flight.arrival_airport} {flight.passengers}\n")


# test section
if __name__ == "__main__":
    flight = Flight("A11", "LEBL", "EGLL", "12:30", "14:30", 135)
    PrintFlight(flight)
    print("Duration:", FlightDuration(flight))