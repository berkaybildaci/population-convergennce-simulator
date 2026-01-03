import random
import csv

class Agent:
    def __init__(self):
        self.state = random.uniform(0, 1)

    def __repr__(self):
        return f"State({self.state})\n"

#agent lists
agent_list = [Agent() for _ in range(100)]
agent_state_snapshot = [float for _ in range(100)]

global_divided_agent_matrix = []
global_divided_agent_matrix_snapshot = []


#rate of convergence per tick t for agents
convergence_rate = 2
#placeholder for current average of all states
current_agent_average = 0.0
#current average of grouped states
current_group_agent_average = []

#split agents into equal groups
def split_agents(num_groups, group_size):
    #instantiate matrix with correct number of rows/cols
    temp_divided_agent_matrix = [[Agent() for _ in range(group_size)] for _ in range(num_groups)]

    #assign agents to slots within matrix
    t_ticker = 0
    for x in range(num_groups):
        for y in range(group_size):
            temp_divided_agent_matrix[x][y] = agent_list[t_ticker]
            t_ticker+=1

    return temp_divided_agent_matrix
    

# calculate global aggregate average
def calculate_global_agent_average():
    #placeholder for sum of all states
    agent_average = 0.0
    #placeholder for average of all states
    agent_sum_total = 0.0

    for i in range(len(agent_list)):
        agent_sum_total += agent_list[i].state
    agent_average = agent_sum_total/len(agent_list)
    return agent_average

def calculate_group_agent_average():

    #placeholder for sum of one group states
    temp_agent_average = 0.0
    #placeholder for average of one group states
    temp_agent_sum_total = 0.0
    #placeholder for all averages in a list
    temp_agent_all_averages = [0.0 for _ in range(len(global_divided_agent_matrix))]

    for x in range(len(global_divided_agent_matrix)):
        temp_agent_average = 0.0
        temp_agent_sum_total = 0.0
        for y in range(len(global_divided_agent_matrix[x])):
            temp_agent_sum_total += global_divided_agent_matrix[x][y].state
        temp_agent_average = temp_agent_sum_total/len(global_divided_agent_matrix[x])
        temp_agent_all_averages[x] = temp_agent_average
    
    return temp_agent_all_averages


global_divided_agent_matrix = split_agents(10, 10)
global_divided_agent_matrix_snapshot = [
    [0.0 for _ in range(len(global_divided_agent_matrix[0]))]
    for _ in range(len(global_divided_agent_matrix))]
# begin time stepping
for x in range(10):
    #recalculate average
    current_group_agent_average = calculate_group_agent_average()
    print(current_group_agent_average)
    for a in range(len(global_divided_agent_matrix)):
        for b in range(len(global_divided_agent_matrix[a])):
            #record moved agent state slightly towards average if not on average
            if(current_group_agent_average[a] - global_divided_agent_matrix[a][b].state < 0):
                global_divided_agent_matrix_snapshot[a][b] = (global_divided_agent_matrix[a][b].state - (global_divided_agent_matrix[a][b].state - current_group_agent_average[a])/convergence_rate)
            elif(current_group_agent_average[a] - global_divided_agent_matrix[a][b].state > 0):
                global_divided_agent_matrix_snapshot[a][b] = (global_divided_agent_matrix[a][b].state + (current_group_agent_average[a] - global_divided_agent_matrix[a][b].state)/convergence_rate)
    
    for c in range(len(global_divided_agent_matrix)):
        for d in range(len(global_divided_agent_matrix[c])):
            global_divided_agent_matrix[c][d].state = global_divided_agent_matrix_snapshot[c][d]

#print(global_divided_agent_matrix)

#with open ('output_agent_matrix.csv', 'w', newline='') as csv_file:
#    writer = csv.writer(csv_file)
#    writer.writerows(global_divided_agent_matrix)
