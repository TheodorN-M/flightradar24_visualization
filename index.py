import csv
import matplotlib.pyplot as plt
import json

def load_fligt(path: str) -> list[list[str]]:
    with open(path, "rt", encoding="utf-8") as csv_file:
        flight_data = list(csv.reader(csv_file, delimiter=","))

    return flight_data[1:]

def handle_data(flight_data: list[list[str]]):
    callsign = flight_data[0][2]
    lats = []
    longs = []
    for row in flight_data:
        pos = row[3].split(",")

        lats.append(pos[0])
        longs.append(pos[1])
    
def read_file(filnavn):
    with open(filnavn, 'r', encoding='utf-8') as filobjekt:
        return filobjekt.read()

def load_coastlines():
    string = read_file("data/ne_110m_coastline.json")
    d = json.loads(string)
    islands = d['features']
    cords = []
    for island in islands:
        island_cords = island['geometry']['coordinates']
        cords.append(island_cords)
    return cords

def plot_coastlines(lines):
    for line in lines:
        xs = []
        ys = []
        for cord in line:
            xs.append(cord[0])
            ys.append(cord[1])
        plt.plot(xs,ys, color='grey')

load_fligt("data/KL1341_34bda3c5.csv")
plt.figure(figsize=(12,8))
plot_coastlines(load_coastlines())
plt.show()