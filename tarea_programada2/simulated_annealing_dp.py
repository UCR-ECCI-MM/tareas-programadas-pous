import random
import math
import time
from deliveryman_problem import calculate_total_distance

def simulated_annealing_metaheuristic(distance_matrix, priority_nodes, nodes_to_remove, initial_temperature=1000.0, cooling_rate=0.01, stopping_temperature=1e-5, max_iterations=1000):
    start_time = time.time()
    num_nodes = len(distance_matrix)
    all_nodes = list(range(num_nodes))
    
    priority_nodes = [node for node in priority_nodes if node not in nodes_to_remove]
    
    current_order = [0] + [node for node in all_nodes if node not in priority_nodes and node not in nodes_to_remove and node != 0]
    current_distance = calculate_total_distance(current_order, distance_matrix)
    nodes = [node for node in all_nodes if node not in priority_nodes and node not in nodes_to_remove and node != 0]

    temperature = initial_temperature
    iteration = 0
    while temperature > stopping_temperature and iteration < max_iterations:
        new_order = current_order[:]

        random.shuffle(nodes)
        new_order = [0] + priority_nodes + nodes

        new_distance = calculate_total_distance(new_order, distance_matrix)
        
        delta_distance = new_distance - current_distance
        acceptance_probability = math.exp(-delta_distance / temperature)
        
        if random.random() < acceptance_probability:
            current_order = new_order
            current_distance = new_distance

        temperature *= 1 - cooling_rate
        iteration += 1

    best_order = current_order
    best_distance = current_distance
    end_time = time.time()
    duration_ms = (end_time - start_time) * 1000
    return best_order, best_distance, duration_ms
