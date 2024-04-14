import csv
import matplotlib.pyplot as plt
import json


def load_flight(path: str) -> list[list[str]]:
    with open(path, "rt", encoding="utf-8") as csv_file:
        flight_data = list(csv.reader(csv_file, delimiter=","))

    return flight_data[1:]


def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def handle_data(flight_data: list[list[str]]):
    positions = []
    for row in flight_data:
        pos = row[3].split(",")
        latitude = float(pos[0])
        longitude = float(pos[1])
        positions.append((latitude, longitude))
    return positions


#def get_plane_speed():

def load_coastlines():
    string = read_file("data/ne_110m_coastline.json")
    d = json.loads(string)
    islands = d['features']
    cords = []
    for island in islands:
        island_cords = island['geometry']['coordinates']
        cords.append(island_cords)
    return cords


def plot_coastlines(ax, lines):
    for line in lines:
        xs = []
        ys = []
        for coord in line:
            xs.append(coord[0])
            ys.append(coord[1])
        ax.plot(xs, ys, color='grey')



def plot_flight_path_and_coasts(ax, path, show):
    data = load_flight(path)
    poss = handle_data(data)  # Assuming this function now just returns positions without plotting
    plot_coastlines(ax, load_coastlines())
    if show:
        plt.show()
    return poss

