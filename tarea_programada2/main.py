from deliveryman_problem import generate_coordinates, plot_route, solve_deliveryman_problem
from brute_force_dp import brute_force
from nearest_neighbor_dp import nearest_neighbor_heuristic
from simulated_annealing_dp import simulated_annealing_metaheuristic

if __name__ == '__main__':
    distance_matrix = [
       [ 19,  35,  19,  95,  89,  13,  96,  10,  38,  44],
       [  5,  91,  95,  12,  93,  43,  81,  62,  15,  50],
       [ 19,  25,  63,  98,  20,  82,  97,  43,  22,  19],
       [ 25,  81,  91,  37,  54,  38,  47,  21,  56,  43],
       [ 62,  89,  32,  13,  32,  14,  25,  45,  54,  73],
       [ 48,  99,  49,  63,  95,  68,  45,  20,  95,   7],
       [100,  44,  30,  79,  22,  22,  81,  82,  30,   8],
       [ 45,  26,  56,  94,  25,  47,   2,   5,  92,  48],
       [ 95,  66,  77,  91,  85,  28,  39,  97,  76,  40],
       [ 57,  57,  54,  91,  17,  51,  56,  77,  21,  20]
    ]
    
    priority_nodes = [5, 2]
    nodes_to_remove = [3]

    coordinates = generate_coordinates(len(distance_matrix))
    
    # Solve using brute force
    method = 'bf'
    best_route, min_distance = solve_deliveryman_problem(method, distance_matrix, priority_nodes, nodes_to_remove, brute_force_fn=brute_force)
    if best_route:
        print(f"Brute Force - Best route: {best_route}")
        print(f"Minimum distance: {min_distance}")
        plot_route(best_route, distance_matrix, coordinates)
    else:
        print("No valid route found for Brute Force.")

    # Solve using nearest neighbor heuristic
    method = 'nn'
    best_route, min_distance = solve_deliveryman_problem(method, distance_matrix, priority_nodes, nodes_to_remove, nearest_neighbor_fn=nearest_neighbor_heuristic)
    if best_route:
        print(f"Nearest Neighbor - Best route: {best_route}")
        print(f"Minimum distance: {min_distance}")
        plot_route(best_route, distance_matrix, coordinates)
    else:
        print("No valid route found for Nearest Neighbor.")

    # Solve using simulated annealing
    method = 'sa'
    best_route, min_distance = solve_deliveryman_problem(method, distance_matrix, priority_nodes, nodes_to_remove, simulated_annealing_fn=simulated_annealing_metaheuristic)
    if best_route:
        print(f"Nearest Neighbor - Best route: {best_route}")
        print(f"Minimum distance: {min_distance}")
        plot_route(best_route, distance_matrix, coordinates)
    else:
        print("No valid route found for Nearest Neighbor.")
