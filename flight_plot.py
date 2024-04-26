import csv
import matplotlib.pyplot as plt
import json

class FlightInfo:
    def __init__(self, path: str):
        all_data = load_flight(path)
        self.flight_info = make_map(all_data)
        self.timestamp = 0
        self.position = 0, 0
        self.speed = 0
        self.altitude = 0
        self.direction = 0

        poses = handle_data(all_data)
        self.max_lat = -100
        self.max_long = -100
        self.min_lat = 100
        self.min_long = 100
    

        for lat, long in poses:
            self.max_long = max(self.max_long, long)
            self.max_lat = max(self.max_lat, lat)

            self.min_long = min(self.min_long, long)
            self.min_lat = min(self.min_lat, lat)

    def update_info(self, timestamp: int):
        self.position, self.altitude, self.speed, self.direction = self.flight_info[timestamp]

    def print_info(self):
        print(f"Position: {self.position}")
        print(f"Speed: {self.speed}")
        print(f"Altitude: {self.altitude}")
        print(f"Direction: {self.direction}")



def load_flight(path: str) -> list[list[str]]:
    with open(path, "rt", encoding="utf-8") as csv_file:
        flight_data = list(csv.reader(csv_file, delimiter=","))

    return flight_data[1:]

def make_map(info: list[list[str]]):
    dic = {}
    for row in info:
        pos = row[3].split(",")
        latitude = float(pos[0])
        longitude = float(pos[1])
        dic[int(row[0])] = ((latitude, longitude), row[4], row[5], row[6])
    return dic


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


