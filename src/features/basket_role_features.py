"""
Role / opportunity features for basketball.
"""

import pandas as pd


def compute_role_features(pbp: pd.DataFrame, player_id: str) -> pd.DataFrame:
    df = pbp[pbp["player_id"] == player_id]

    poss_on = df["possession_id"].nunique()
    fga = (df["event_type"].isin(["shot_made", "shot_missed"])).sum()
    tov = (df["event_type"] == "turnover").sum()
    fta = (df["event_type"] == "foul_ft").sum()

    usage_proxy = (fga + tov + 0.44 * fta) / max(poss_on, 1)

    return pd.DataFrame(
        {
            "poss_on": [poss_on],
            "fga": [fga],
            "tov": [tov],
            "fta": [fta],
            "usage_proxy": [usage_proxy],
            "shot_share": [fga / max(poss_on, 1)],
        }
    )
