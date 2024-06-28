# ------------------------------------------------------------
# Copyright [2024] <Maria Fernanda Andres, Fabian Calvo & Andres Quesada Gonzalez>
# ------------------------------------------------------------

from deliveryman_problem import calculate_total_distance

def nearest_neighbor_heuristic(distance_matrix, priority_nodes=[], nodes_to_remove=[]):
    num_nodes = len(distance_matrix)
    nodes = set(range(num_nodes)) - set(nodes_to_remove) - {0}
    
    if not nodes:
        return None, float('inf')
    
    visited = [0] + priority_nodes
    for node in priority_nodes:
        nodes.discard(node)
    
    current_node = priority_nodes[-1] if priority_nodes else 0
    
    while nodes:
        nearest_neighbor = None
        min_distance = float('inf')
        
        for neighbor in nodes:
            if distance_matrix[current_node][neighbor] < min_distance:
                min_distance = distance_matrix[current_node][neighbor]
                nearest_neighbor = neighbor
        
        if nearest_neighbor is not None:
            visited.append(nearest_neighbor)
            nodes.discard(nearest_neighbor)
            current_node = nearest_neighbor

    # Return to the starting node (factory)
    visited.append(0)
    total_distance = calculate_total_distance(visited, distance_matrix)
    
    return visited, total_distance
