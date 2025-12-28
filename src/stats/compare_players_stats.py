"""
Statistical comparison of domain attributions between players.
"""

import pandas as pd
from scipy.stats import mannwhitneyu


def compare_players_domains(
    df_W: pd.DataFrame,
    df_D: pd.DataFrame,
):
    rows = []

    for domain in set(df_W["domain"]) & set(df_D["domain"]):
        x = df_W.loc[df_W["domain"] == domain, "mean_contribution"]
        y = df_D.loc[df_D["domain"] == domain, "mean_contribution"]

        stat, p = mannwhitneyu(x, y, alternative="two-sided")

        rows.append(
            {
                "domain": domain,
                "median_W": x.median(),
                "median_D": y.median(),
                "p_value": p,
            }
        )

    return pd.DataFrame(rows)
