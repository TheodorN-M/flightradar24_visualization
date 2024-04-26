import flight_plot as fp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

path = "data/BGO-AMS-ATH.csv"
# path = "data/KL1953_34c792d0.csv"
# Get the flight info

test_flight = fp.FlightInfo(path)

# Find coordinates for flight plot
left = min(test_flight.min_pos[1], test_flight.max_pos[1]) - 5
right = max(test_flight.min_pos[1], test_flight.max_pos[1]) + 5
top = max(test_flight.max_pos[0], test_flight.min_pos[0]) + 5
bottom = min(test_flight.max_pos[0], test_flight.min_pos[0]) - 5

# Initialize the plot
fig, ax = plt.subplots(figsize=((right-left) // 4, (top-bottom) // 4))


ax.set_xlim(left, right) 
ax.set_ylim(bottom, top) 

# ax.set_xlim(-5, 45) 
# ax.set_ylim(20, 70) 

x_data, y_data = [], []
ln, = ax.plot([], [], 'b-', animated=True)  

def init():
    fp.plot_flight_path_and_coasts(ax, path, False)
    return ln,

def update(frame):
    lat, long = frame
    x_data.append(long)
    y_data.append(lat)
    ln.set_data(x_data, y_data)
    return ln,

positions = fp.handle_data(fp.load_flight(path))
ani = FuncAnimation(fig, update, frames=positions, init_func=init, blit=True, interval=100)

plt.show()
