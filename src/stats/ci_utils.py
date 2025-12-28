"""
Confidence interval utilities.
"""

import pandas as pd
import numpy as np


def domain_confidence_intervals(
    boot_df: pd.DataFrame,
    alpha: float = 0.05,
):
    return (
        boot_df
        .groupby("domain")["mean_contribution"]
        .agg(
            mean="mean",
            lower=lambda x: np.quantile(x, alpha / 2),
            upper=lambda x: np.quantile(x, 1 - alpha / 2),
        )
        .reset_index()
    )
