import flight_plot as fp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


path = "data/HV5685_34c4fcbc.csv"
# Get the flight info

test_flight = fp.FlightInfo(path)
buffer = 5

# Find coordinates for flight plot
left   = test_flight.min_long
right  = test_flight.max_long
top    = test_flight.max_lat
bottom = test_flight.min_lat

# Initialize the plot
fig, ax = plt.subplots(figsize=((right-left) // 4, (top-bottom) // 4))

ax.set_xlim(left - buffer, right + buffer) 
ax.set_ylim(bottom - buffer, top + buffer) 


x_data, y_data = [], []
ln, = ax.plot([], [], 'b-', animated=True)  

alt_text = ax.text(0.01, 0.95, '', transform=ax.transAxes, ha='left', va='top', fontsize=9)

def init():
    fp.plot_flight_path_and_coasts(ax, path, False)
    return ln, alt_text

def update(frame):
    lat, long, alt = frame
    x_data.append(long)
    y_data.append(lat)
    ln.set_data(x_data, y_data)
    alt_text.set_text(f"Altitude: {alt} ft")
    return ln, alt_text

positions = fp.handle_data(fp.load_flight(path))
ani = FuncAnimation(fig, update, frames=positions, init_func=init, blit=True, interval=100)

plt.show()
