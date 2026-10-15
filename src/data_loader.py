
import pandas as pd
from pathlib import Path

def load_data(path: Path, target: str) -> pd.DataFrame:
    """Load the gallstone dataset and check that it has the expected shape.

    Parameters
    ----------
    path : Path
        Location of the CSV file.
    target : str
        Name of the target column; must be present and binary (0/1).

    Returns
    -------
    pd.DataFrame
        The raw dataset with numeric columns.
    """
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found at {path.resolve()}")

    df = pd.read_csv(path)

    if target not in df.columns:
        raise KeyError(f"Target column '{target}' is missing from the data")
    if not set(df[target].unique()) <= {0, 1}:
        raise ValueError(f"Target column '{target}' must only contain 0 and 1")

    return df