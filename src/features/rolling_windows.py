"""
Rolling window utilities for longitudinal athlete analysis.
"""

import pandas as pd


def rolling_aggregate(
    df: pd.DataFrame,
    time_col: str,
    value_cols: list[str],
    window: int,
    min_periods: int = 1,
):
    """
    Compute rolling means over a specified window.

    Parameters
    ----------
    df : DataFrame sorted by time_col
    time_col : column used for ordering (e.g. game_date)
    value_cols : features to aggregate
    window : rolling window size
    """
    out = df.sort_values(time_col).copy()
    for c in value_cols:
        out[f"{c}_roll{window}"] = (
            out[c].rolling(window=window, min_periods=min_periods).mean()
        )
    return out
