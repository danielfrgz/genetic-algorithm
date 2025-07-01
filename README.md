# Metaheuristic Algorithm Implementations for Solving the TFP

This repository contains **metaheuristic algorithm implementations** for solving the **Team Formation Problem (TFP)**. 

Developed as part of the Bachelor Thesis project: _"Balancing diversity and preferences: Mono-objective versus Multi-objective Approaches to the Educational Team Formation Problem"_ by **Daniel Frutos Rodriguez**.

## Authors and Acknowledgement

Frutos-Rodriguez D., Barrios-Fleitas Y., and Lalla E. 2025. _Balancing diversity and preferences: Mono-objective versus Multi-objective Approaches to the Educational Team Formation Problem_. ACM, New York, NY, USA, 17 pages. [https://doi.org/10.1145/nnnnnnn.nnnnnnn](https://doi.org/10.1145/nnnnnnn.nnnnnnn)

> Last updated: **01/07/2025**

## Files

```
📂 data
├── 📄 **`2022_23_arrangement.csv`**: Original arrangement (2022/23 Data & Information course).
├── 📄 **`corrected_2022_23_arrangement.csv`**: Arrangement corrected for restriction violations.
├── 📄 **`corrected_dataset.xlsx`**: Source data with annotations on data cleaning.
├── 📄 **`data_shuffler.py`**: Util that creates subset datasets while maintaining demographic distributions.
├── 📄 **`dataset_small.csv`**: Reduced dataset, 50 students.
├── 📄 **`dataset_medium.csv`**: Reduced dataset, 100 students.
├── 📄 **`dataset_large.csv`**: Reduced dataset, 200 students.
├── 📄 **`dataset.csv`**: Cleaned dataset with 278 students.
├── 📄 **`reduced_dataset_1.csv`**: Reduced dataset with 15 students for optimum benchmarking.
├── 📄 **`reduced_dataset_2.csv`**: Reduced dataset with 15 students for optimum benchmarking.
└── 📄 **`reduced_dataset_3.csv`**: Reduced dataset with 15 students for optimum benchmarking.

📂 figures: Folder for figure output.

📂 models
└── 📄 **`team_assignment.py`**: Team Assignment class for global algorithm use.

📂 output
├── 📄 **`optimal_arrangement_reduced_dataset_1.txt`**: Optimal solution for `reduced_dataset_1`.
├── 📄 **`optimal_arrangement_reduced_dataset_2.txt`**: Optimal solution for `reduced_dataset_2`.
└── 📄 **`optimal_arrangement_reduced_dataset_3.txt`**: Optimal solution for `reduced_dataset_3`.

📂 utils
├── 📄 **`fitness_functions.py`**: Provides method to compute fitness functions for one or all teams in an arrangement.
├── 📄 **`monoobjective_exhaustive_solver.py`**: Exhaustive solver for optimal solution (to be used with `reduced_dataset_{n}`, n = [1, 2, 3]).
└── 📄 **`restriction_checker.py`**: Util to check that an input team arrangement meets all restrictions.

📄 **`enhanced_genetic_algorithm.ipynb`**: Enhanced Genetic Algorithm Implementation.
📄 **`non_dominated_sorting_genetic_algorithm_2.ipynb`**: Non-dominated Sorting Genetic Algorithm II Implementation.
📄 **`particle_swarm_optimization.ipynb`**: Particle Swarm Optimization Implementation.
📄 **`standard_genetic_algorithm.ipynb`**: Standard Genetic Algorithm Implementation (Deprecated).
📄 **`random_baseline_algorithm.py`**: Random Baseline Algorithm Implementation.

📄 **`evaluate_assignment.ipynb`**: Evaluates an assignment following the format of `{corrected}_2022_23_arrangement.csv`

📄 **`ega_parameter_tester.ipynb`**: Parameter setting runs for `enhanced_genetic_algorithm.ipynb`.
📄 **`ega_parameter_setting_statistics.ipynb`**: Parameter setting statistics for `enhanced_genetic_algorithm.ipynb`.
📄 **`pso_parameter_tester.ipynb`**: Parameter setting runs for `particle_swarm_optimization.ipynb`.
📄 **`pso_parameter_setting_statistics.ipynb`**: Parameter setting statistics for `particle_swarm_optimization.ipynb`.

📄 **`mono_vs_optimal.ipynb`**: Mono-objective algorithm vs. optimum experiment.
📄 **`mono_vs_random.ipynb`**: Mono-objective algorithm vs. random baseline experiment.
📄 **`mono_vs_self_selected.ipynb`**: Mono-objective algorithm vs. self-selected arrangement experiment.
📄 **`multi_vs_self_selected.ipynb`**: Multi-objective-algorithm vs. self-selected arrangement experiment.
📄 **`mono_multi_comparison.ipynb`**: Mono-objective algorithm vs. multi-objective algorithm experiment.

📄 **README.md**: This file.
```

# Usage

## Viewing

Open any figure in `figures/` directory, or `efficiency_time_complexity_statistics.ipynb` to view statistics.
All files are commented for inspection, adaptation or expansion. `.ipynb` files include markdown labeling/descriptions.

## Experiments

1. Open any experiment file.
2. Adjust constants at the top (e.g., `NUMBER_OF_GENERATIONS`, `EFFICIENCY_GOAL`) if desired.
3. Ensure `DATASET` and `DATA` point to a valid CSV in the `data/` folder.
4. Run the notebook.
5. Find output logs in `output/` folder, or visualizations in `figures/` folder.

Performance logs and arrangement outputs are saved under the `output/` directory, categorized by test and organized by timestamp. Figures are saved in `figures/` directory.

## Project status

**Complete**

### Extensions:
- Explore different evolutionary functions or parameter values and benchmark performance.
- Extend fitness function with soft constraints, different weights per criterion, new criterion, etc.
- Attempt time/computational optimizations to existing code.
- Benchmark against newly developed algorithms with shared data baseline.