import random

class Agent:
    def __init__(self):
        self.state = random.uniform(0, 1)

    def __repr__(self):
        return f"State({self.state})\n"

#agent lists
agent_list = [Agent() for _ in range(100)]

agent_state_snapshot = [float for _ in range(100)]

#rate of convergence per tick t for agents
convergence_rate = 2
#placeholder for current average of all states
current_agent_average = 0.0
# calculate aggregate average
def calculate_agent_average():
    #placeholder for sum of all states
    agent_average = 0.0
    #placeholder for average of all states
    agent_sum_total = 0.0

    for i in range(len(agent_list)):
        agent_sum_total += agent_list[i].state
    agent_average = agent_sum_total/len(agent_list)
    return agent_average

# begin time stepping
for x in range(10):
    #recalculate average
    current_agent_average = calculate_agent_average()
    for y in range(len(agent_list)):
        #record moved agent state slightly towards average if not on average
        if(current_agent_average - agent_list[y].state < 0):
            agent_state_snapshot[y] = (agent_list[y].state - (agent_list[y].state - current_agent_average)/convergence_rate)
        elif(current_agent_average - agent_list[y].state > 0):
            agent_state_snapshot[y] = (agent_list[y].state + (current_agent_average - agent_list[y].state)/convergence_rate)

    #update snapshotted values at time t
    for z in range(len(agent_list)):
        agent_list[z].state = agent_state_snapshot[z]

print(agent_list)