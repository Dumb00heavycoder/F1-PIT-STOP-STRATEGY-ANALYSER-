     ####combinatorial optimizer####

#For the 0.1 version we will consider the lap time of each tyre to be specific 
#We will only use 3 tyres in 2 pit strategy 

#Soft= 10 laps
#Medium = 20 laps
#Hard = 30 laps 

from itertools import product 
import numpy as np

total_laps = input("Enter the number of laps:- ")
pit_stop_time_loss = 25  #seconds
tyre_lap_time = {'soft': 80, 'medium' : 85, 'hard' : 92} #seconds

def generate_stint_combinations(laps, max_stints=3):
    from itertools import combinations_with_replacement, permutations

    results = []
    for stint_count in range(1, max_stints+1):
        for combo in product(range(1, laps), repeat=stint_count):
            if sum(combo) == laps:
                results.append(combo)
    return results
