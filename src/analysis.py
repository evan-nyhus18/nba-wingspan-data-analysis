"""
Exploratory analysis: merge RAPTOR & DFG data, visualize correlations.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_processing import load_and_clean

def merge_raptor(wingspan_df: pd.DataFrame, raptor_csv: str) -> pd.DataFrame:
    r = pd.read_csv(raptor_csv)
    r = r[r['mp'] > 400]
    return pd.merge(r, wingspan_df, how='inner', left_on='player_name', right_on='Name')

def plot_scatter(df: pd.DataFrame, x: str, y: str, title: str):
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df, x=x, y=y)
    plt.title(title); plt.xlabel(x); plt.ylabel(y)
    plt.show()

def compute_correlation(df: pd.DataFrame, cols: list):
    corr = df[cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix"); plt.show()
    return corr

if __name__ == "__main__":
    # Example workflow
    center_df  = load_and_clean("data/Center_wingspan.csv")
    merged_df  = merge_raptor(center_df, "data/modern_RAPTOR_by_player.csv")
    plot_scatter(merged_df, 'Wingspan', 'raptor_total', 'Center Wingspan vs. RAPTOR')
    compute_correlation(merged_df, ['Height','Wingspan','raptor_total'])
