"""
Export results for figures and tables.
"""

from pathlib import Path
import pandas as pd


def export_domain_results(df: pd.DataFrame, outdir: str, name: str):
    Path(outdir).mkdir(parents=True, exist_ok=True)
    df.to_csv(Path(outdir) / f"{name}.csv", index=False)
