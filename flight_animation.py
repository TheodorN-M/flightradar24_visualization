import flight_plot as fp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon
import numpy as np


path = "data/SK909_34c4767d.csv"

# Get the flight info
test_flight = fp.FlightInfo(path)
buffer = 5

# Set plot limits
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
dir_text = ax.text(0.01, 0.90, '', transform=ax.transAxes, ha='left', va='top', fontsize=9)

# Plane size will depend on flight path
plane_size = 0.5 
# Initial position for plane triangle 
triangle = np.array([[0, 0], [-plane_size, -plane_size * 2], [plane_size, -plane_size * 2]])

# Make and add plane
plane = Polygon(triangle, closed=True, fc='red')
ax.add_patch(plane)

# Initialize plot
def init():
    fp.plot_flight_path_and_coasts(ax, path, False)
    return ln, alt_text, plane, alt_text, dir_text

# Frame update
def update(frame):
    lat, long, alt, direction = frame
    angle = np.radians(direction)
    x_data.append(long)
    y_data.append(lat)
    rotated_triangle = np.dot(triangle, [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    plane.set_xy(rotated_triangle + [long, lat])

    ln.set_data(x_data, y_data)
    alt_text.set_text(f"Altitude: {alt} ft")
    dir_text.set_text(f"Direction: {direction}°")

    return ln, plane, alt_text, dir_text


positions = fp.handle_data(fp.load_flight(path))
ani = FuncAnimation(fig, update, frames=positions, init_func=init, blit=True, interval=100)

plt.show()



