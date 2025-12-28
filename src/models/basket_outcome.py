"""
Context-adjusted performance outcome.
"""

import pandas as pd


def compute_outcome(possessions: pd.DataFrame, player_team: str) -> float:
    team_poss = possessions[possessions["team"] == player_team]
    return team_poss["points"].mean()
