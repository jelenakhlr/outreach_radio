# GRAND Radio Signal Detection - Masterclass Code

This repository contains Python code for a masterclass on radio signal detection inspired by the GRAND experiment.

authors:\
Laetitia Megel, @Laetitia227\
Jelena Köhler, @jelenakhlr

## Learning Objectives:

Part 0: Explore the concept of signal strength and how it varies with distance using few antennas.\
Part 1: Understand how the GP300 array of antennas can be used to locate a radio transmitter.\
Part 2: Observe radio signals emitted from air showers on the GP300 array.

## Code Structure:

```masterclass_part0.py```: Simulates radio signal detection using three individual antennas.\
```masterclass_part1.py```: Simulates radio signal detection using a GP300 antenna layout.\
```masterclass_part2.py```: Visualizes radio signals emitted from cosmic ray air showers for both time and signal strength distributions.

## Running the Code:

### Prerequisites:

Python 3.x\
NumPy library (```pip install numpy```)\
Matplotlib library (```pip install matplotlib```)\
Pandas library (```pip install pandas```)

### Execution:

Navigate to the directory containing the code files.\
Open a terminal window in the directory.\
Run each part of the code using the following commands:

    python masterclass_part0.py

    python masterclass_part1.py
    
    python masterclass_part2.py


## Explanation:

Each script provides a commented code example demonstrating the concepts mentioned in the learning objectives.

### Part 0 - Three Individual Antennas:

This part simulates the signal strength received by three individual antennas placed at different distances from the transmitter. The results are visualized to illustrate how signal strength weakens with increasing distance. Click on the position where you expect the transmitter to be located.


### Part 1 - GP300 Antenna Layout:

This part simulates the detection of a radio transmitter using a grid of antennas similar to the GRAND experiment's GP300 layout. The code calculates the signal strength at each antenna based on its distance from the transmitter and visualizes the results. Click on the position where you expect the transmitter to be located.

### Part 2 - GP300 Air Showers:

This part visualizes a simulated cosmic ray event detected by the GP300 array. You can choose to display either the signal strength ("ADCfluence") distribution or the time distribution of the event.

## Further Exploration:

Modify the code to change the number and positions of the antennas.\
The transmitter is placed randomly for each run. Experiment with different transmitter locations by running the script multiple times.\
Explore more advanced signal processing techniques used in real-world radio detection experiments.

## Disclaimer:

This code is for educational purposes only and simplifies the complexities of real-world radio detection systems.
