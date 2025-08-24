import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import ScalarFormatter
import matplotlib as mpl
from matplotlib.widgets import RadioButtons

# Set up Matplotlib styles
rc("font", **{"family": "serif"})
rc("font", size=12)

gp300 = np.genfromtxt("gp300.list", delimiter=" ")
gp300_x = gp300[:, 2] * 10**-2  # convert from cm to m
gp300_y = gp300[:, 3] * 10**-2  # convert from cm to m

def plot_event(event, event_number):
    """
    Plots the data for a single event and allows interactive clicks on dots.

    Args:
        event (pd.DataFrame): The DataFrame containing event data.
        event_number (int): The event ID to plot.
    """
    title = f"Event {event_number}"
    
    # Filter the data for the selected event
    event_mask = (event["eventID"] == event_number) 
    event_df = event[event_mask].copy()
    energy = event_df["energy"].unique()[0]
    theta = np.around(event_df["Zenith"].unique()[0],2)
    phi = np.around(event_df["Azimuth"].unique()[0],2)
    stations = event_df["stationID"].unique()
    print(f"Event {event_number}, Energy: {energy / 1e9:.2e} GeV, {len(stations)} stations with signal")

    # Add a variable to store the current type
    type_options = ["ADCfluence", "time"]
    type = [type_options[0]]  # Use a mutable object for closure
    cmap = "RdPu" if type[0] == "ADCfluence" else "Blues"
        
    # Create the figure with a GridSpec layout
    fig = plt.figure(figsize=(14, 14))
    gs = GridSpec(5, 4, figure=fig)  # 4 columns: last for radio buttons
    main_ax = fig.add_subplot(gs[:2, :3])  # Main plot spans top two rows, first 3 columns

    # Add radio buttons for type selection
    radio_ax = fig.add_axes([0.82, 0.7, 0.12, 0.12])
    radio = RadioButtons(radio_ax, type_options)
    radio_ax.set_title("type", fontsize=12)

    if type[0] == "ADCfluence":
        norm = mpl.colors.LogNorm(vmin=max(event_df["ADCfluence"].min(), 1e-2), vmax=event_df["ADCfluence"].max())
        cmap = "RdPu"
        cbar_label = "signal strength"
    elif type[0] == "time":
        norm = plt.Normalize(vmin=event_df["time"].min(), vmax=event_df["time"].max())
        cmap = "Blues"
        cbar_label = "time in ns"


    main_ax.scatter(gp300_x, gp300_y, color="grey", s=20, alpha=0.5)
    sc = main_ax.scatter(event_df['positionX'], event_df['positionY'], c=event_df[f"{type[0]}"],
                         marker='o', s=50, norm=norm, cmap=cmap)
    main_ax.set_xlabel('x position in m')
    main_ax.set_ylabel('y position in m')
    main_ax.set_title(f'{title} - Event {event_number}\nE={energy:.2e} eV, ' + rf'$\theta$={theta}, $\varphi$={phi}')

    # Add a colorbar
    cbar = fig.colorbar(sc, ax=main_ax, orientation='vertical')
    cbar.set_label(cbar_label)

    def update_type(label):
        type[0] = label
        if type[0] == "ADCfluence":
            current_cmap = "RdPu"
            # Avoid log(0) by setting a small positive vmin
            vmin = max(event_df["ADCfluence"].min(), 1e-2)
            norm = mpl.colors.LogNorm(vmin=vmin, vmax=event_df["ADCfluence"].max())
            cbar_label = "signal strength"
        elif type[0] == "time":
            current_cmap = "Blues"
            norm = plt.Normalize(vmin=event_df["time"].min(), vmax=event_df["time"].max())
            cbar_label = "time in ns"

        sc.set_array(event_df[f"{type[0]}"])
        sc.set_norm(norm)
        sc.set_cmap(current_cmap)
        cbar.set_label(cbar_label)
        cbar.update_normal(sc)
        fig.canvas.draw_idle()

    radio.on_clicked(update_type)
    plt.show()


if __name__ == "__main__":
    # Load the data
    file = pd.read_csv("/Users/jelenapetereit/work/GRAND_DB/database.csv")
    events = sorted(file["eventID"].unique())
    # Select an event to display
    print("Available events:", events)
    event_number = int(input("Enter the event ID to display: "))
    
    # Plot the selected event
    plot_event(file, event_number)
