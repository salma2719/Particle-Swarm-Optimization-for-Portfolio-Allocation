import numpy as np

def calculate_fitness(x, mean_returns, cov_matrix, environmental_scores, social_scores, governance_scores, R, E, S, G):
    portfolio_mean_return = np.sum(mean_returns * x)
    portfolio_covariance = np.sum(np.outer(x, x) * cov_matrix)
    environmental_constraint = np.sum(environmental_scores * x)
    social_constraint = np.sum(social_scores * x)
    governance_constraint = np.sum(governance_scores * x)
    
    constraint_penalty = max(0, R - portfolio_mean_return) + \
                         max(0, E - environmental_constraint) + \
                         max(0, S - social_constraint) + \
                         max(0, G - governance_constraint)
    
    return portfolio_covariance + constraint_penalty

def get_input_scores(N):
    environmental_scores = np.array([float(input(f"Enter environmental score for asset {i + 1}: ")) for i in range(N)])
    social_scores = np.array([float(input(f"Enter social score for asset {i + 1}: ")) for i in range(N)])
    governance_scores = np.array([float(input(f"Enter governance score for asset {i + 1}: ")) for i in range(N)])
    return environmental_scores, social_scores, governance_scores

def main():
    # Get user input for parameters
    N = int(input("Enter the number of assets (N): "))
    num_particles = int(input("Enter the number of particles: "))
    max_iterations = int(input("Enter the maximum number of iterations: "))
    w = float(input("Enter the inertia weight (w): "))
    c1 = float(input("Enter the cognitive component weight (c1): "))
    c2 = float(input("Enter the social component weight (c2): "))
    R = float(input("Enter the desired mean return (R): "))
    E = float(input("Enter the desired environmental score (E): "))
    S = float(input("Enter the desired social score (S): "))
    G = float(input("Enter the desired governance score (G): "))

    # Get user input for mean returns, covariance matrix, and scores
    mean_returns = np.array([float(input(f"Enter mean return for asset {i + 1}: ")) for i in range(N)])
    cov_matrix = np.array([[float(input(f"Enter covariance between assets {i + 1} and {j + 1}: ")) for j in range(N)] for i in range(N)])
    
    environmental_scores, social_scores, governance_scores = get_input_scores(N)

    # particles and velocities are initialized
    particles = np.random.rand(num_particles, N)
    velocities = np.random.rand(num_particles, N)

    # global best position and value are initialized
    global_best_position = particles[0].copy()
    global_best_value = calculate_fitness(global_best_position, mean_returns, cov_matrix, environmental_scores, social_scores, governance_scores, R, E, S, G)

    for iteration in range(max_iterations):
        # Evaluate fitness of each particle
        fitness_values = np.zeros(num_particles)
        for i in range(num_particles):
            x = particles[i]
            fitness_values[i] = calculate_fitness(x, mean_returns, cov_matrix, environmental_scores, social_scores, governance_scores, R, E, S, G)
            
            # constraint checking
            if (
                np.sum(x * mean_returns) <= R
                or np.sum(x) != 1
                or np.sum(environmental_scores * x) <= E
                or np.sum(social_scores * x) <= S
                or np.sum(governance_scores * x) <= G
                or np.any(x < 0) or np.any(x > 1)):
                fitness_values[i] = np.inf
        
        # global best position and value are updated
        best_particle_idx = np.argmin(fitness_values)
        if fitness_values[best_particle_idx] < global_best_value:
            global_best_value = fitness_values[best_particle_idx]
            global_best_position = particles[best_particle_idx].copy()

        # particle velocities and positions are updated
        for i in range(num_particles):
            r1 = np.random.rand(N)
            r2 = np.random.rand(N)
            cognitive_velocity = c1 * r1 * (global_best_position - particles[i])
            social_velocity = c2 * r2 * (particles[best_particle_idx] - particles[i])
            velocities[i] = w * velocities[i] + cognitive_velocity + social_velocity
            particles[i] += velocities[i]

        for i in range(num_particles):
            particles[i] = particles[i] / np.sum(particles[i])

    # the particle with the minimum fitness value is found
    optimal_particle_idx = np.argmin(fitness_values)
    optimal_weights = particles[optimal_particle_idx]
    portfolio_return_ = np.dot(optimal_weights, mean_returns)
    # Print results
    print("Optimal Portfolio Allocation:")
    print(optimal_weights)

if __name__ == "__main__":
    main()
