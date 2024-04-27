import flight_plot as fp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

path = "data/KL1953_34c792d0.csv"

# Initialize the plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Get the flight info and plot limits
test_flight = fp.FlightInfo(path)
buffer = 5
ln, = ax.plot([], [], [])

ax.set_xlim3d([test_flight.min_long - buffer, test_flight.max_long + buffer])
ax.set_xlabel('Longitude')

ax.set_ylim3d([test_flight.min_lat - buffer, test_flight.max_lat + buffer])
ax.set_ylabel('Latitude')

ax.set_zlim3d([0, 100000])
ax.set_zlabel('Altitude')

# Plot coastlines
fp.plot_coastlines(ax, fp.load_coastlines())

coord_alt_text = ax.text2D(0.05, 0.95, "", transform=ax.transAxes)

x_data, y_data, z_data = [], [], []

# Initialize plot
def init():
    ln.set_data([], [])
    ln.set_3d_properties([])
    coord_alt_text.set_text('')
    return ln, coord_alt_text

# Frame update
def update(frame):
    lat, long, alt, direction = frame

    x_data.append(long)
    y_data.append(lat)
    z_data.append(alt)
    
    ln.set_data(x_data, y_data)
    ln.set_3d_properties(z_data)
    coord_alt_text.set_text(f'Latitude: {lat:.3f}\nLongitude: {long:.3f}\nAltitude: {alt:.2f} ft')


    return ln, coord_alt_text

positions = fp.handle_data(fp.load_flight(path))  
ani = FuncAnimation(fig, update, frames=positions, interval=100, blit= False)

plt.show()


