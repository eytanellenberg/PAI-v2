"""
Execution / efficiency features.
"""

import pandas as pd


def compute_efficiency_features(pbp: pd.DataFrame, player_id: str) -> pd.DataFrame:
    df = pbp[pbp["player_id"] == player_id]

    fgm = (df["event_type"] == "shot_made").sum()
    fga = (df["event_type"].isin(["shot_made", "shot_missed"])).sum()
    tov = (df["event_type"] == "turnover").sum()

    fg_pct = fgm / max(fga, 1)
    tov_rate = tov / max(fga + tov, 1)

    return pd.DataFrame(
        {
            "fg_pct": [fg_pct],
            "tov_rate": [tov_rate],
        }
    )
