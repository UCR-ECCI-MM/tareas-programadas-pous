from itertools import permutations
import time
from deliveryman_problem import calculate_total_distance

def brute_force(distance_matrix, priority_nodes=[], nodes_to_remove=[]):
    start_time = time.time()
    number_of_points = len(distance_matrix)
    nodes = set(range(number_of_points)) - set(nodes_to_remove)

    if not nodes:
        return None, float('inf')

    remaining_nodes = nodes - set(priority_nodes) - {0}
    all_permutations = permutations(remaining_nodes)
    min_distance = float('inf')
    best_route = None

    for perm in all_permutations:
        route = [0] + list(priority_nodes) + list(perm)
        current_distance = calculate_total_distance(route, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route
    end_time = time.time()
    duration_ms = (end_time - start_time) * 1000
    return best_route, min_distance, duration_ms
