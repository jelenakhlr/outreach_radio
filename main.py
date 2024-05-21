import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import matplotlib as mpl
# fancy plots
from matplotlib import rc
from cycler import cycler
import cmasher as cmr
rc('font', **{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('font', size = 11.0)
n = 3 # Number of colors
new_colors = [plt.get_cmap('cmr.bubblegum')(1. * i/n) for i in range(n)]
mpl.rcParams['axes.prop_cycle'] = cycler('color', new_colors)
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Define positions for multiple receiving antennas
antenna_positions = [(0, 0), (5, 0), (2, 5)]
transmitter_x = 10
transmitter_y = 10
fig, ax = plt.subplots()

# Function to calculate signal strength based on distance (replace with your logic)
def get_signal_strength(distance):
  if distance == 0:
    # Handle zero distance (e.g., return a high value)
    return 100
  else:
    strength = 10 / distance
    return strength

# Function to handle user clicks
def on_click(event):
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


# Plot antenna locations
for antenna_pos in antenna_positions:
  plt.plot(antenna_pos[0], antenna_pos[1], marker='o', color='blue', label='Antenna')
  distance = min(abs(pos[0] - antenna_pos[0]) for pos in antenna_positions)  # Find min distance to another antenna (replace with actual transmitter logic)
  signal_strength = get_signal_strength(distance)
  circle = plt.Circle(antenna_pos, signal_strength, color='green', alpha=0.4, label='Signal Strength')
  plt.gca().add_patch(circle)


# Call `on_click` when user clicks anywhere on the plot
cid = fig.canvas.mpl_connect('button_press_event', on_click)

# Add labels and title
plt.xlabel('X-position')
plt.ylabel('Y-position')
plt.title('Radio Signal Strength (Click to Guess Transmitter Location)')

plt.show()
