from flight_plot import plot_flight_path_and_coasts, handle_data, load_flight
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize the plot
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 10)  # Adjust these limits based on the longitude range
ax.set_ylim(50, 60)  # Adjust these limits based on the latitude range

x_data, y_data = [], []
ln, = ax.plot([], [], 'ro', animated=True)  # Ensure this is plotting to ax

def init():
    plot_flight_path_and_coasts(ax, "data/KL1341_34bda3c5.csv", False)
    return ln,

def update(frame):
    lat, long = frame
    x_data.append(long)
    y_data.append(lat)
    ln.set_data(x_data, y_data)
    return ln,

positions = handle_data(load_flight("data/KL1341_34bda3c5.csv"))
ani = FuncAnimation(fig, update, frames=positions, init_func=init, blit=True, interval=100)

plt.show()
