import matplotlib.pyplot as plt
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


# Function to calculate signal strength 
def get_signal_strength(distance):
  # Simulate weaker signal with larger distance from transmitter
  strength = 10 / distance
  return strength

# Define antenna position
antenna_x = 0
antenna_y = 0

# Define transmitter position
transmitter_x = 5
transmitter_y = 0

# Calculate distance between antenna and transmitter
distance = abs(antenna_x - transmitter_x)

# Get signal strength based on distance
signal_strength = get_signal_strength(distance)

# Plot antenna and transmitter locations
plt.plot(antenna_x, antenna_y, marker='o', label='receiving antenna')
plt.plot(transmitter_x, transmitter_y, marker='o', label='transmitting antenna')
# Plot a circle around the antenna representing signal strength
circle = plt.Circle((transmitter_x, transmitter_y), signal_strength, alpha=0.4, label='Signal Strength')
plt.gca().add_patch(circle)

# Add labels and title
plt.xlabel('X-position')
plt.ylabel('Y-position')
plt.axis('equal')
plt.title(f'Signal Strength (Strength: {signal_strength:.2f})')
plt.legend()

plt.show()