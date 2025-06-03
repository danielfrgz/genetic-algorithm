# GA Implementations for Solving the TFP

This repository contains Genetic Algorithm implementations for solving the **Team Formation Problem (TFP)**. 

Developed as part of the thesis project:  
_"A Comparison of Optimization Techniques for Solving the Team Formation Problem"_  
by **Daniel Frutos Rodriguez**.

## Authors and Acknowledgement

Frutos-Rodriguez D., Barrios-Fleitas Y., and Lalla E. 2025. _A Comparison of Optimization Techniques for Solving the Team Formation Problem._ In _Proceedings Placeholder_. ACM, New York, NY, USA, 6 pages. [https://doi.org/10.1145/nnnnnnn.nnnnnnn](https://doi.org/10.1145/nnnnnnn.nnnnnnn)

> Last updated: **03/06/2025**

## Usage

1. Open `standard_genetic_algorithm.ipynb`
2. Adjust constants at the top (e.g., `NUMBER_OF_GENERATIONS`, `EFFICIENCY_GOAL`)
3. Ensure `SYNTHETIC_DATASET` and `DATA` point to a valid CSV in the `data/` folder
4. Run the notebook

Performance logs and arrangement outputs are saved under the `output/` directory, organized by timestamp.

`standard_genetic_algorithm.ipynb` includes algorithm implementation. File uses exhaustive solver, restriction checker and fitness functions from utils package and a team assignment class from the model package. Raw data can be found in data package.

## Project status

**In development**

### Next steps:
- Explore different crossover functions and benchmark performance
- Test on larger real datasets
- Extend fitness function with soft constraints or weights per criterion
