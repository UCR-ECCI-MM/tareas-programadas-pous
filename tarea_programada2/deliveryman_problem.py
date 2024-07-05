import matplotlib.pyplot as plt
import numpy as np

def calculate_total_distance(permutation, distance_matrix):
    total_distance = 0
    number_of_points = len(permutation)

    for i in range(number_of_points - 1):
        total_distance += distance_matrix[permutation[i]][permutation[i + 1]]
    
    # Back to starting point (Factory)
    total_distance += distance_matrix[permutation[-1]][permutation[0]]
    
    return total_distance

def generate_coordinates(num_points, radius=1):
    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    coordinates = [(radius * np.cos(angle), radius * np.sin(angle)) for angle in angles]
    return coordinates

def plot_route(route, distance_matrix, coordinates):
    plt.figure(figsize=(10, 8))
    
    x = [coordinates[i][0] for i in route] + [coordinates[route[0]][0]]
    y = [coordinates[i][1] for i in route] + [coordinates[route[0]][1]]
    
    plt.plot(x, y, marker='o')
    
    for i, point in enumerate(route + [route[0]]):  # Including the return to the start
        plt.text(x[i], y[i], f'P{point}', fontsize=12, ha='right')
        if i < len(route):  # To avoid out of range error for distance_matrix access
            next_point = (i + 1) % len(route)
            distance = distance_matrix[route[i]][route[next_point]]
            mid_x = (x[i] + x[next_point]) / 2
            mid_y = (y[i] + y[next_point]) / 2
            plt.text(mid_x, mid_y, str(distance), fontsize=10, ha='center', color='blue')
    
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Route')
    plt.grid(True)
    plt.show()

def solve_deliveryman_problem(method, distance_matrix, priority_nodes=[], nodes_to_remove=[], brute_force_fn=None, nearest_neighbor_fn=None, simulated_annealing_fn=None):
    if method == 'bf':
        return brute_force_fn(distance_matrix, priority_nodes, nodes_to_remove)
    elif method == 'nn':
        return nearest_neighbor_fn(distance_matrix, priority_nodes, nodes_to_remove)
    elif method == 'sa':
        return simulated_annealing_fn(distance_matrix, priority_nodes, nodes_to_remove)
    else:
        raise ValueError("Invalid method. Use 'bf' for brute force, 'nn' for nearest neighbor heuristic or 'sa' for simulated annealing metaheuristic")
