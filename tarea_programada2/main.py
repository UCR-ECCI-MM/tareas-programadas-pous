from deliveryman_problem import generate_coordinates, plot_route, solve_deliveryman_problem
from brute_force_dp import brute_force
from nearest_neighbor_dp import nearest_neighbor_heuristic
from simulated_annealing_dp import simulated_annealing_metaheuristic

if __name__ == '__main__':
    distance_matrix = [
            [ 19,  35,  19,  95,  89,  13,  96,  10,  38,  44,  67,  82,  51,  73,  28,  40,  62,  15,  80,  91],
            [  5,  91,  95,  12,  93,  43,  81,  62,  15,  50,  34,  78,  22,  65,  89,  37,  54,  38,  47,  21],
            [ 19,  25,  63,  98,  20,  82,  97,  43,  22,  19,  74,  31,  86,  50,  10,  60,  70,  80,  90, 100],
            [ 25,  81,  91,  37,  54,  38,  47,  21,  56,  43,  15,  68,  93,  25,  47,   2,   5,  92,  48,  74],
            [ 62,  89,  32,  13,  32,  14,  25,  45,  54,  73,  58,  39,  27,  90,  45,  26,  56,  94,  25,  47],
            [ 48,  99,  49,  63,  95,  68,  45,  20,  95,   7,  15,  25,  35,  45,  55,  65,  75,  85,  95, 105],
            [100,  44,  30,  79,  22,  22,  81,  82,  30,   8,  40,  60,  80, 100, 120, 140, 160, 180, 200, 220],
            [ 45,  26,  56,  94,  25,  47,   2,   5,  92,  48,  15,  25,  35,  45,  55,  65,  75,  85,  95, 105],
            [ 95,  66,  77,  91,  85,  28,  39,  97,  76,  40,  70,  80,  90, 110, 130, 150, 170, 190, 210, 230],
            [ 57,  57,  54,  91,  17,  51,  56,  77,  21,  20,  33,  48,  95,  40,  63,  89,  37,  54,  38,  47],
            [ 30,  20,  10,  50,  60,  70,  80,  90, 100, 110,  39,  58,  76,  54,  33,  42,  55,  76,  48,  91],
            [ 40,  60,  80, 100, 120, 140, 160, 180, 200, 220,  63,  48,  95,  40,  33,  57,  66,  34,  50,  21],
            [ 15,  25,  35,  45,  55,  65,  75,  85,  95, 105, 115,  84,  97,  32,  74,  88,  66,  27,  19,  59],
            [ 75,  65,  55,  45,  35,  25,  15,   5,  95, 105,  54,  89,  67,  39,  41,  78,  43,  65,  28,  47],
            [ 90,  78,  63,  57,  33,  25,  19,  56,  94,  25,  31,  59,  88,  73,  12,  44,  66,  88,  50,  42],
            [ 49,  67,  90,  79,  44,  33,  25,  75,  32,  45,  57,  33,  56,  69,  71,  43,  95,  60,  32,  15],
            [ 95,  25,  43,  45,  20,  50,  66,  87,  96,  48,  99,  74,  28,  43,  62,  41,  77,  33,  55,  28],
            [ 50,  77,  39,  90,  66,  44,  34,  52,  16,  87,  92,  48,  37,  29,  55,  45,  66,  72,  36,  81],
            [ 30,  45,  62,  74,  83,  92,  25,  54,  47,  65,  48,  29,  81,  62,  53,  44,  35,  26,  17,  19],
            [ 57,  28,  39,  91,  65,  48,  70,  82,  14,  36,  57,  91,  12,  45,  61,  78,  84,  37,  20,  50]
        ]
                
    priority_nodes = [5, 2]
    nodes_to_remove = [3]

    coordinates = generate_coordinates(len(distance_matrix))
    
    # Solve using brute force
    method = 'bf'
    best_route, min_distance, time = solve_deliveryman_problem(method, distance_matrix, priority_nodes, nodes_to_remove, brute_force_fn=brute_force)
    if best_route:
        print(f"Brute Force - Best route: {best_route}")
        print(f"Minimum distance: {min_distance}")
        print(f"Execution time: {time:.2f} milliseconds")
        plot_route(best_route, distance_matrix, coordinates)
    else:
        print("No valid route found for Brute Force.")

    # Solve using nearest neighbor heuristic
    method = 'nn'
    best_route, min_distance, time = solve_deliveryman_problem(method, distance_matrix, priority_nodes, nodes_to_remove, nearest_neighbor_fn=nearest_neighbor_heuristic)
    if best_route:
        print(f"Nearest Neighbor - Best route: {best_route}")
        print(f"Minimum distance: {min_distance}")
        print(f"Execution time: {time:.2f} milliseconds")
        plot_route(best_route, distance_matrix, coordinates)
    else:
        print("No valid route found for Nearest Neighbor.")

    # Solve using simulated annealing
    method = 'sa'
    best_route, min_distance, time = solve_deliveryman_problem(method, distance_matrix, priority_nodes, nodes_to_remove, simulated_annealing_fn=simulated_annealing_metaheuristic)
    if best_route:
        print(f"Simulated Annealing - Best route: {best_route}")
        print(f"Minimum distance: {min_distance}")
        print(f"Execution time: {time:.2f} milliseconds")
        plot_route(best_route, distance_matrix, coordinates)
    else:
        print("No valid route found for Nearest Neighbor.")
