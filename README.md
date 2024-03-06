# Lottery Scheduling Algorithm

## Functionality
This Python script implements a basic lottery scheduling algorithm. 
There scheduler that randomly selects a process to run based on the number of lottery tickets assigned to each process. 
Processes with more tickets have a higher chance of being selected, but the selection remains random.

The script will print the winner of the lottery (the next process to run based on the algorithm)
You can modify the script to add/remove processes and change the amount of tickets they have.

There are 2 classes in the script:
1. Process: Represents a process with a unique identifier (pid) and a number of lottery tickets assigned to it.
2. Scheduler: Manages the lottery scheduling algorithm. It allows adding processes, allocating lottery tickets, and selecting the next process to run randomly.

## Instructions for Execution
1. Ensure you have Python installed on your system or a compiler that can execute Python or use an Online-IDE that can compile Python.

2. Download the 'cs540assignment2.py' file to your device.

3. Open a terminal/command prompt and navigate to the directory where the script is saved and excute by using 'python cs540assignment2.py'

4. Or on your own compiler/online compiler, open the file and execute.
