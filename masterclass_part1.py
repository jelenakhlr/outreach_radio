import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib import rc

rc("text", usetex=False)
rc("font", size=11.0)

fig, ax = plt.subplots()

# Function to handle user clicks
def on_click(event):
    transmitter_x, transmitter_y = transmitter[0], transmitter[1]
    clicked_x = event.xdata
    clicked_y = event.ydata
    print(clicked_x)
    distance_to_transmitter = abs(clicked_x - transmitter_x) + abs(
        clicked_y - transmitter_y
    )
    threshold = (
        50.0  # Adjust this value based on your plot scale and desired sensitivity
    )

    if distance_to_transmitter <= threshold:
        ax.scatter(
            transmitter_x, transmitter_y, marker="x", color="r", label="transmitter"
        )
        text = "Correct! You found the transmitter location."
        props = dict(boxstyle="round", facecolor="white")
        ax.text(
            1.1, 0.99, text, transform=ax.transAxes, verticalalignment="top", bbox=props
        )
        plt.legend()

    else:
        text = f"You clicked at: ({clicked_x:.2f}, {clicked_y:.2f})\n Try again! The transmitter might be closer to one of the stronger signal areas."
        props = dict(boxstyle="round", facecolor="white")
        ax.text(
            1.1, 0.99, text, transform=ax.transAxes, verticalalignment="top", bbox=props
        )

    fig.canvas.draw_idle()  # Trigger redrawing
    fig.canvas.flush_events()  # Process events for a smooth update
    return True


def distance(transmitter, gp300):
    antennas = pd.DataFrame(
        columns=[
            "position_x",
            "position_y",
            "distance_to_transmitter",
            "signal_strength",
        ]
    )
    antenna_position_x = gp300[:, 2]
    antenna_position_y = gp300[:, 3]
    N = len(antenna_position_x) - 1
    for station in range(N):
        position_x = antenna_position_x[station] * 10 ** -4
        position_y = antenna_position_y[station] * 10 ** -4
        position_xy = np.array([position_x, position_y])
        distance = np.sqrt(
            (transmitter[0] - position_x) ** 2 + (transmitter[1] - position_y) ** 2
        )
        signal_strength = 1 / distance
        antennas = antennas.append(
            {
                "position_x": position_x,
                "position_y": position_y,
                "distance_to_transmitter": distance,
                "signal_strength": signal_strength,
            },
            ignore_index=True,
        )
    return antennas


gp300 = np.genfromtxt("gp300.list")

transmitter = np.array([np.random.randint(0,80), np.random.randint(0,80)])
receivers_df = distance(transmitter, gp300)


plt.scatter(
    receivers_df["position_x"],
    receivers_df["position_y"],
    c=receivers_df["signal_strength"],
    cmap="gist_ncar",
    marker="o",
    s=20,
    label="gp300",
)

# Add colorbar
cbar = plt.colorbar()
cbar.set_label("signal strength")


# Call `on_click` when user clicks anywhere on the plot
cid = fig.canvas.mpl_connect("button_press_event", on_click)

plt.title("Radio Signal Strength (Click to Guess Transmitter Location)")
plt.axis("equal")
plt.xlabel("Position X")
plt.ylabel("Position Y")
plt.legend()
plt.show()
