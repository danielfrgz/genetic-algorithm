import os
import pandas as pd
import numpy as np
import itertools
import io
import contextlib
import import_ipynb
import enhanced_genetic_algorithm as ega
import utils.fitness_functions as ff

RUNS = 10

P_r_VALUES = [5, 10, 15, 20]
DATASETS = ["data/dataset_small.csv", "data/dataset_medium.csv", "data/dataset_large.csv"]

combinations = list(itertools.product(P_r_VALUES, DATASETS))

for P_r, dataset_path in combinations:
    dataset_name = os.path.splitext(os.path.basename(dataset_path))[0]
    print(f'\nDataset: {dataset_name} | P_r: {P_r}')
    
    ega.PARENT_RESET_THRESHOLD = P_r
    ega.DATASET = pd.read_csv(dataset_path)
    ega.BASE_DIR = f"output/parameter_setting/ega/{dataset_name}/p_r_{P_r}"
    
    scores = []
    for _ in range(RUNS):
        with contextlib.redirect_stdout(io.StringIO()):
            df_ega, best_ega = ega.execute()
            score = ff.evaluate_all_teams(best_ega)
            scores.append(score)
    
    mean_score = np.mean(scores)
    std_score = np.std(scores)
    print(f'Average Score over {RUNS} runs: {mean_score:.4f} ± {std_score:.4f}')