import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import matplotlib as mpl
# fancy plots
from matplotlib import rc
rc('font', **{'family':'serif','serif':['Palatino']})
rc('text', usetex=False)
rc('font', size = 11.0)
from matplotlib.widgets import Button


# Function to handle user clicks
def on_click(event):
    transmitter_x, transmitter_y = transmitter[0], transmitter[1]
    clicked_x = event.xdata
    clicked_y = event.ydata
    distance_to_transmitter = abs(clicked_x - transmitter_x) + abs(clicked_y - transmitter_y)
    # Define a threshold distance to consider a close guess (adjust as needed)
    threshold = 5.0  # Adjust this value based on your plot scale and desired sensitivity

    if distance_to_transmitter <= threshold:
        print(f"Correct! You found the transmitter location.")
    else:
        print(f"You clicked at: ({clicked_x:.2f}, {clicked_y:.2f})")
        print(f"Try again! The transmitter might be closer to one of the stronger signal areas.")
    return 

def distance(transmitter, gp300):
    receivers = pd.DataFrame(columns=['position_x', 'position_y', 'distance_to_transmitter', 'signal_strength'])
    antenna_position_x = gp300[:,2]
    antenna_position_y = gp300[:,3]
    N = len(antenna_position_x) - 1
    for station in range(N):
        position_x = antenna_position_x[station]*10**-4
        position_y = antenna_position_y[station]*10**-4
        position_xy = np.array([position_x, position_y])
        distance   = np.linalg.norm(np.array([position_xy, transmitter]))
        signal_strength = 1/distance
        receivers = receivers.append({
            'position_x' : position_x, 
            'position_y' : position_y, 
            'distance_to_transmitter' : distance, 
            'signal_strength' : signal_strength
            }, ignore_index=True)
    return receivers

gp300 = np.genfromtxt("gp300.list")

transmitter = np.array([random.random()*100, random.random()*100])
receivers_df = distance(transmitter, gp300)



fig, ax = plt.subplots()
plt.scatter(receivers_df['position_x'], receivers_df['position_y'], c=receivers_df['distance_to_transmitter'],
            cmap="plasma", marker='o', s=20, norm=mpl.colors.LogNorm())
# Add colorbar
cbar = plt.colorbar()
cbar.set_label("signal strength")

# Call `on_click` when user clicks anywhere on the plot
cid = fig.canvas.mpl_connect('button_press_event', on_click)

plt.title('Radio Signal Strength (Click to Guess Transmitter Location)')
plt.axis('equal')
plt.xlabel('Position X')
plt.ylabel('Position Y')
plt.show()
