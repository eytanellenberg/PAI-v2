"""
Temporal stability of domain attributions.
"""

import pandas as pd


def rolling_domain_means(
    domain_df: pd.DataFrame,
    time_col: str,
    window: int = 5,
):
    out = domain_df.sort_values(time_col).copy()
    out["rolling_mean"] = (
        out
        .groupby("domain")["mean_contribution"]
        .rolling(window, min_periods=2)
        .mean()
        .reset_index(level=0, drop=True)
    )
    return out
