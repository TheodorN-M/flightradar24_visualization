import csv
import matplotlib.pyplot as plt

def load_fligt(path: str) -> list[list[str]]:
    with open(path, "rt", encoding="utf-8") as csv_file:
        flight_data = list(csv.reader(csv_file, delimiter=","))

    return flight_data[1:]

def handle_data(flight_data: list[list[str]]):
    callsign = flight_data[0][2]
    for row in flight_data[1:]:
        pos = row[3].split(",")
        lat = pos[0]
        long = pos[1]



load_fligt("data/KL1341_34bda3c5.csv")