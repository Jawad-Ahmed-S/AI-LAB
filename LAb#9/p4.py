import numpy as np


states = ["Sunny", "Cloudy","Rainy"]
transition_matrix = np.array([
    [0.6, 0.3, 0.1],  
    [0.3, 0.4, 0.3],  
    [0.1, 0.5, 0.4]   
])


def simulate_markov_process(initial_state, num_steps):
    current_state = initial_state
    state_sequence = [current_state]

    for _ in range(num_steps -1):
        
        state_idx = states.index(current_state)
        next_state = np.random.choice(states , p= transition_matrix[state_idx])

        state_sequence.append(next_state)
        current_state = next_state

    return state_sequence


initial_state = "Sunny"
num_steps = 10
state_sequence = simulate_markov_process(initial_state, num_steps)
print(f"State sequence for {num_steps} steps starting from {initial_state}:")
print(" -> ".join(state_sequence))

trials = 10000
atleast3 =0

for _ in range(trials):
    seq = simulate_markov_process("Sunny",10)
    if seq.count("Rainy") >= 3:
        atleast3 +=1
 

print(f"P(Rainy>=3): {atleast3/trials}")
