import pandas as pd
from sklearn.model_selection import train_test_split

# Load and shuffle dataset
df = pd.read_csv("dataset.csv")
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Add a composite stratification column
df_shuffled["Strata"] = (
    df_shuffled["Gender"].astype(str) + "_" +
    df_shuffled["Program"].astype(str) + "_" +
    df_shuffled["Nationality"].astype(str)
)

# Define sampling sizes
sizes = {
    "dataset_small.csv": 50,
    "dataset_medium.csv": 100,
    "dataset_large.csv": 200
}

# Stratified sampling by 'Strata'
for filename, size in sizes.items():
    sampled_df, _ = train_test_split(
        df_shuffled,
        train_size=size,
        stratify=df_shuffled["Strata"],
        random_state=42
    )
    sampled_df.drop(columns=["Strata"]).to_csv(filename, index=False)