"""
Helpers to load & clean NBA wingspan datasets.
"""
import pandas as pd

def height_to_inches(height: str) -> float:
    parts = height.replace('"','').split("'")
    feet = int(parts[0])
    inches = float(parts[1]) if len(parts)>1 else 0.0
    return feet*12 + inches

def wingspan_to_inches(wingspan: str) -> float:
    parts = wingspan.replace('"','').split("'")
    feet = int(parts[0])
    inches = float(parts[1]) if len(parts)>1 else 0.0
    return feet*12 + inches

def load_and_clean(path: str) -> pd.DataFrame:
    """
    Read CSV at `path`, convert Height/ Wingspan to inches, return DataFrame.
    """
    df = pd.read_csv(path)
    df['Height']   = df['Height'].apply(height_to_inches)
    df['Wingspan'] = df['Wingspan'].apply(wingspan_to_inches)
    return df
