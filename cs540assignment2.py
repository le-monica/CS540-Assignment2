import random 

class Process:
    def __init__(self, pid, tickets):
        self.pid = pid  # unique identifier for the process
        self.tickets = tickets  # number of lottery tickets assigned to the process

class Scheduler:
    def __init__(self):
        self.processes = []  # list to hold the processes

    def add_process(self, process):
        self.processes.append(process)  # function to add process to list

    def allocate_tickets(self):
        total_tickets = sum(process.tickets for process in self.processes)  # calculate total number of tickets
        allocated_tickets = 0  # initialize the allocated_tickets counter
        
        for process in self.processes:
            allocated_tickets += process.tickets / total_tickets  # allocate probability for each process
            process.allocated_tickets = allocated_tickets  # assign probability

    def select_winner(self):
        rand = random.random()  # generate random number
        for process in self.processes: # iterate through process list
            if rand <= process.allocated_tickets:  # compare random with allocated tickets
                return process  # return the winning process

if __name__ == "__main__":
    scheduler = Scheduler()  # initialize scheduler

    # create processes with pid and random amt of tickets
    scheduler.add_process(Process(1, 5))  
    scheduler.add_process(Process(2, 10))  
    scheduler.add_process(Process(3, 3))  

    # allocate tickets
    scheduler.allocate_tickets() 

    # select winner
    winner = scheduler.select_winner()
    print(f"Process {winner.pid} wins the lottery") 
