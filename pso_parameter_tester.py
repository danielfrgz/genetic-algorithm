import os
import pandas as pd
import numpy as np
import itertools
import io
import contextlib
import import_ipynb
import particle_swarm_optimization as pso
import utils.fitness_functions as ff

RUNS = 10

W_VALUES = [0.25, 0.5, 0.75]
C1_VALUES = [0.25, 0.5, 0.75]
C2_VALUES = [0.25, 0.5, 0.75]
DATASETS = ["data/dataset_small.csv", "data/dataset_medium.csv", "data/dataset_large.csv"]

combinations = list(itertools.product(W_VALUES, C1_VALUES, C2_VALUES, DATASETS))

for W, C1, C2, dataset_path in combinations:
    dataset_name = os.path.splitext(os.path.basename(dataset_path))[0]
    print(f'\nDataset: {dataset_name} | W: {W}, C1: {C1}, C2: {C2}')
    
    pso.W = W
    pso.C1 = C1
    pso.C2 = C2
    pso.DATASET = pd.read_csv(dataset_path)
    pso.BASE_DIR = f"output/parameter_setting/pso/{dataset_name}/w{W}_c1{C1}_c2{C2}"
    
    scores = []
    for _ in range(RUNS):
        with contextlib.redirect_stdout(io.StringIO()):
            df_pso, best_pso = pso.execute()
            score = ff.evaluate_all_teams(best_pso)
            scores.append(score)
    
    mean_score = np.mean(scores)
    std_score = np.std(scores)
    print(f'Average Score over {RUNS} runs: {mean_score:.4f} ± {std_score:.4f}')