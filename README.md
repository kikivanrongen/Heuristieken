# RailNL
The purpose of this case is to optimize the lining of the intercity trains.
We searches for the best algorithm to optimize the score function. The score function includes the fraction of driven critical lines, the number of routes and the total time of the routes.

## Getting Started

### Prerequisites
This codebase is completely written in Pyhton3.6.3. Requirements.txt contains all neseccary packages to succesfully run the code. These requirements are easy to install via:

pip install -r requirements.text

### Structure
We have got the three folders: data, pythoncode and results. The file data contains the data about the stations and connections of NZ Holland and the Netherlands. The file pythoncode contains four folders: algorithms, classes, functions and visualisation. In the folder algorithms we have the algorithms dijksta, greedy, hillclimber and random_solution. In the folder classes we have a folder named classes which contains three classes: Stations, Train, Trains. The folder functions contains a file random_trajectory with a function that contains a function that runs a random trajectory. The folder visualisation has two files: histogram and visual. The file histogram plots a histogram of scores. The file visual contains two functions, visual_solution and visual. These functions visualize the best solution and the possible trajectories. The folder results contains the results of all the random trains and algorithms.

### Testing
Run the following command to find out how the programm works:
python main.py --help


## Authors
* Kiki van Rongen
* Eleanoor Polder
* Zooey Bossert

## Acknowledgments
* Quinten our tech assistant
* Daan van den Berg
* StackOverflow
* Minor programming at the UvA
