"""
Reconstruct possessions from play-by-play data.

Expected columns (typical public PBP):
- game_id
- period
- clock
- team
- event_type
- points
"""

import pandas as pd


END_POSSESSION_EVENTS = {
    "shot_made",
    "shot_missed",
    "turnover",
    "end_period",
    "foul_ft",
}


def build_possessions(pbp: pd.DataFrame) -> pd.DataFrame:
    pbp = pbp.sort_values(
        ["game_id", "period", "clock"], ascending=[True, True, False]
    ).reset_index(drop=True)

    pbp["end_possession"] = pbp["event_type"].isin(END_POSSESSION_EVENTS)
    pbp["possession_id"] = pbp["end_possession"].cumsum()

    possessions = (
        pbp.groupby("possession_id")
        .agg(
            game_id=("game_id", "first"),
            team=("team", "first"),
            period=("period", "first"),
            points=("points", "sum"),
        )
        .reset_index()
    )

    return possessions
