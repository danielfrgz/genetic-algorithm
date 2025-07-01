import os
import contextlib
import pandas as pd
import utils.fitness_functions as ff
import import_ipynb
import particle_swarm_optimization as pso

def execute(dataset=pso.DATASET, generations=100, population_size=10):
    scores = []
    best_score = 0

    for gen in range(generations + 1):
        gen_scores = []
        for _ in range(population_size):
            arrangement = pso.create_random_teams(dataset)
            if arrangement:
                with open(os.devnull, 'w') as fnull:
                    with contextlib.redirect_stdout(fnull):
                        score = ff.evaluate_all_teams(arrangement)
                        gen_scores.append(score)
        if gen_scores:
            best_score = max(best_score, max(gen_scores))
        scores.append(best_score)

    df = pd.DataFrame({
        "score": scores,
        "iteration": list(range(generations + 1))
    }).set_index("iteration")

    return df

