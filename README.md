# Particle Swarm Optimization for the ESG-constrained mean-variance problem
This Python script implements a Particle Swarm Optimization (PSO) algorithm for portfolio optimization. PSO is a heuristic optimization technique inspired by the social behavior of birds and fish. The script aims to find the optimal asset allocation for a portfolio based on user-defined constraints, such as desired mean return, environmental score, social score, and governance score.

PSO operates on the concept of modeling a group of potential solutions, called particles, each particle in the swarm embodies a potential portfolio allocation. The position of a particle represents a specific combination of asset weights that define the composition of an investment portfolio. These allocations represent the distribution of resources across each asset composing the portfolio.

The best possible solution is determined by a fitness function responsible for assessing the solution's quality. The fitness function acts as the critical evaluator of each particle's portfolio allocation. The fitness function quantifies how well a particular portfolio aligns with the desired objectives, which include minimizing portfolio risk while adhering to ESG constraints.

# Features
Particle Swarm Optimization algorithm for portfolio optimization. User input for customizing parameters, mean returns, covariance matrix, and scores.
