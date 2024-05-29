import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import matplotlib as mpl
from matplotlib import rc
# fancy plots
rc('text', usetex=False)
rc('font', size = 11.0)
from matplotlib.widgets import Button

fig, ax = plt.subplots()

# Function to handle user clicks
def on_click(event):
    transmitter_x, transmitter_y = transmitter[0], transmitter[1]
    clicked_x = event.xdata
    clicked_y = event.ydata
    distance_to_transmitter = abs(clicked_x - transmitter_x) + abs(clicked_y - transmitter_y)
    threshold = 50.0  # Adjust this value based on your plot scale and desired sensitivity
    
    if distance_to_transmitter <= threshold:
        ax.plot(transmitter_x, transmitter_y, marker="x", color='r', label="transmitter")
        text="Correct! You found the transmitter location."
        props = dict (boxstyle = 'round' , facecolor = "white")
        ax.text(1.1, 0.99, text , transform = ax.transAxes,
        verticalalignment = 'top' , bbox = props)
        plt.show()
        
    else:
        ax.plot(transmitter_x, transmitter_y, marker="x", color='r', label="transmitter")
        text=f"You clicked at: ({clicked_x:.2f}, {clicked_y:.2f})\n Try again! The transmitter might be closer to one of the stronger signal areas."
        props = dict (boxstyle = 'round' , facecolor = "white")
        ax.text(1.1, 0.99, text , transform = ax.transAxes,
        verticalalignment = 'top' , bbox = props)
    return 

def signal_strength(antenna_position_x, antenna_position_y):
    distance   = np.sqrt((transmitter[0]-antenna_position_x)**2 + (transmitter[1]-antenna_position_y)**2)
    signal_strength = 1/distance
    return signal_strength

AntennaPosition1 = np.array([5,15])
AntennaPosition2 = np.array([15,30])
AntennaPosition3 = np.array([15,5]) 
print(AntennaPosition1, AntennaPosition2, AntennaPosition3)

antennas = pd.DataFrame({
    'position_x': np.array([AntennaPosition1[0], AntennaPosition2[0], AntennaPosition3[0]]),
    'position_y': np.array([AntennaPosition1[1], AntennaPosition2[1], AntennaPosition3[1]])
})

transmitter = np.array([np.random.randint(0,35), np.random.randint(0,35)])
receivers_df = pd.DataFrame({
    'position_x': antennas['position_x'],
    'position_y': antennas['position_y'],
    'signal_strength': np.array([signal_strength(AntennaPosition1[0], AntennaPosition1[1]), signal_strength(AntennaPosition2[0], AntennaPosition2[1]), signal_strength(AntennaPosition3[0], AntennaPosition3[1])])
})


                     
plt.scatter(receivers_df['position_x'], receivers_df['position_y'], c=receivers_df['signal_strength'],
            cmap="plasma", marker='o', edgecolors= "black", s=20, label="antennas")
 

# Add colorbar
cbar = plt.colorbar()
cbar.set_label("signal strength")


# Call `on_click` when user clicks anywhere on the plot
cid = fig.canvas.mpl_connect('button_press_event', on_click)

plt.title('Radio Signal Strength (Click to Guess Transmitter Location)')
plt.axis('equal')
plt.xlim(0,37)
plt.ylim(0,37)
plt.xlabel('Position X') 
plt.ylabel('Position Y')
plt.legend()
plt.show()

