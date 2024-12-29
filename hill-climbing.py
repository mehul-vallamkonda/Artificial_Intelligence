import random

def hill_climbing(problem):
    # Initialize with a random state
    current_state = random.choice(list(problem.keys()))
    current_cost = problem[current_state]['cost']  # Access the cost of the current state

    while True:
        # Get neighbors of the current state
        neighbors = problem[current_state]['neighbors']

        if not neighbors:  # No neighbors to explore
            return current_state, current_cost

        # Find the best neighbor
        best_neighbor = None
        best_neighbor_cost = current_cost  # Default to current cost for comparison

        for neighbor, cost in neighbors:
            if cost < best_neighbor_cost:  # Check for improvement
                best_neighbor_cost = cost
                best_neighbor = neighbor

        if best_neighbor is None or best_neighbor_cost >= current_cost:
            return current_state, current_cost  # Local optimum or no better neighbor found

        # Move to the best neighbor
        current_state = best_neighbor
        current_cost = best_neighbor_cost


# Example usage: Problem definition
# State: (x, y)
# Neighbors: [{'neighbors': [(neighbor_state1, cost1), (neighbor_state2, cost2)], 'cost': current_state_cost}]
problem_definition = {
    (0, 0): {'neighbors': [((0, 1), 5), ((1, 0), 3)], 'cost': 10},
    (0, 1): {'neighbors': [((1, 1), 2), ((0, 0), 5)], 'cost': 8},
    (1, 0): {'neighbors': [((1, 1), 1), ((0, 0), 3)], 'cost': 6},
    (1, 1): {'neighbors': [((1, 0), 1), ((0, 1), 2)], 'cost': 4}
}

# Run the Hill Climbing algorithm
best_state, best_cost = hill_climbing(problem_definition)

if best_state is not None:
    print("Best state found:", best_state)
    print("Cost:", best_cost)
else:
    print("No solution found.")
