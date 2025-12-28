"""
Compare domain-level attribution between two athletes.
"""

import pandas as pd


def compare_domain_contributions(
    contrib_W: pd.DataFrame,
    contrib_D: pd.DataFrame,
):
    df_W = contrib_W.copy()
    df_W["player"] = "W"

    df_D = contrib_D.copy()
    df_D["player"] = "D"

    out = pd.concat([df_W, df_D], axis=0)
    return out
