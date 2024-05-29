# GRAND Radio Signal Detection - Masterclass Code

This repository contains Python code for a two-part masterclass on radio signal detection inspired by the GRAND experiment.

authors:\
Laetitia Megel, @Laetitia227\
Jelena Köhler, @jelenakhlr

## Learning Objectives:

Part 1: Understand how an array of antennas can be used to locate a radio transmitter.\
Part 2: Explore the concept of signal strength and how it varies with distance using few antennas.

## Code Structure:

```masterclass_part1.py```: Simulates radio signal detection using a GP300 antenna layout.\
```masterclass_part2.py```: Simulates radio signal detection using three individual antennas.

## Running the Code:

### Prerequisites:

Python 3.x\
NumPy library (```pip install numpy```)
Matplotlib library (```pip install matplotlib```)
Pandas library (```pip install pandas```)

### Execution:

Navigate to the directory containing the code files.\
Open a terminal window in the directory.\
Run each part of the code using the following commands:

    python masterclass_part1.py
    python masterclass_part2.py


## Explanation:

Each script provides a commented code example demonstrating the concepts mentioned in the learning objectives.

### Part 1 - GP300 Antenna Layout:

This part simulates the detection of a radio transmitter using a grid of antennas similar to the GRAND experiment's GP300 layout. The code calculates the signal strength at each antenna based on its distance from the transmitter and visualizes the results. Click on the position where you expect the transmitter to be located.

### Part 2 - Three Individual Antennas:

This part simulates the signal strength received by three individual antennas placed at different distances from the transmitter. The results are visualized to illustrate how signal strength weakens with increasing distance. Click on the position where you expect the transmitter to be located.

## Further Exploration:

Modify the code to change the number and positions of the antennas.\
The transmitter is placed randomly for each run. Experiment with different transmitter locations by running the script multiple times.\
Explore more advanced signal processing techniques used in real-world radio detection experiments.

## Disclaimer:

This code is for educational purposes only and simplifies the complexities of real-world radio detection systems.
