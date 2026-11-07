import matplotlib.pyplot as plt
from aircraft import Aircraft, PrintAircraft, LoadAircrafts, SaveAircrafts
from flight import Flight, PrintFlight, LoadFlights, SaveFlights, TimeToMinutes


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


def LoadAirline(name, fleet_filename, operations_filename):
    fleet = LoadAircrafts(fleet_filename)
    operations = LoadFlights(operations_filename)
    return Airline(name, fleet, operations)


def SaveAirline(airline, fleet_filename, operations_filename):
    SaveAircrafts(airline.fleet, fleet_filename)
    SaveFlights(airline.operations, operations_filename)


def PlotFlights(airline):
    hours = list(range(24))
    flights_per_hour = [0] * 24

    for flight in airline.operations:
        departure = TimeToMinutes(flight.departure_time)
        arrival = TimeToMinutes(flight.arrival_time)

        if arrival <= departure:
            arrival += 24 * 60

        for hour in hours:
            start = hour * 60
            end = start + 60

            if departure < end and arrival > start:
                flights_per_hour[hour] += 1

    plt.bar(hours, flights_per_hour, color='skyblue', edgecolor='black')
    plt.xlabel("Hour of the day")
    plt.ylabel("Number of flights in the air")
    plt.title(f"Flights in the Air per Hour - {airline.name}")
    plt.xticks(hours, [f"{hour:02d}:00" for hour in hours], rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


# test section
if __name__ == "__main__":
    # Test Carga e Impresión completa de la aerolínea desde archivos
    airline = LoadAirline("Vueling", "Aircrafts.txt", "operations.txt")
    PrintAirline(airline)

    # Test Gráfica de vuelos en el aire
    PlotFlights(airline)