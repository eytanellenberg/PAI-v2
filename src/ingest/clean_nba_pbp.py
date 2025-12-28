"""
Minimal cleaning to adapt NBA PBP to PAI pipeline.
"""

import pandas as pd


EVENT_MAP = {
    "Made Shot": "shot_made",
    "Missed Shot": "shot_missed",
    "Turnover": "turnover",
    "Free Throw": "foul_ft",
    "End Period": "end_period",
}


def clean_pbp(df: pd.DataFrame, player_map: dict) -> pd.DataFrame:
    out = pd.DataFrame()
    out["game_id"] = df["game_id"]
    out["period"] = df["PERIOD"]
    out["clock"] = df["PCTIMESTRING"]
    out["event_type"] = df["EVENTMSGTYPE"].map({
        1: "shot_made",
        2: "shot_missed",
        5: "turnover",
        3: "foul_ft",
        13: "end_period",
    }).fillna("other")

    out["points"] = df["SCORE"].str.extract(r"(\d+)$").fillna(0).astype(int)

    out["player_id"] = df["PLAYER1_NAME"].map(player_map).fillna("other")
    out["score_diff"] = 0  # optionnel
    out["home"] = 1        # optionnel

    return out
