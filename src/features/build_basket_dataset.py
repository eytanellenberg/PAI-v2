import pandas as pd

from src.ingest.build_possessions import build_possessions
from src.features.build_basket_X import build_basket_features
from src.models.basket_outcome import compute_outcome


def build_dataset_per_game(pbp: pd.DataFrame, player_code: str, team: str) -> tuple[pd.DataFrame, pd.Series]:
    """
    Build a supervised dataset where each row is one game for one player_code.

    X: features computed from that game's events for that player
    y: outcome computed at team possession level for that game
    """
    games = sorted(pbp["game_id"].unique())
    rows = []
    ys = []

    for gid in games:
        g = pbp[pbp["game_id"] == gid].copy()

        # possession reconstruction for outcome
        poss = build_possessions(g)
        y = compute_outcome(poss, player_team=team)

        # player-specific features
        Xg = build_basket_features(g, player_id=player_code)
        Xg["game_id"] = gid
        rows.append(Xg)
        ys.append(y)

    X = pd.concat(rows, axis=0).reset_index(drop=True)
    y = pd.Series(ys, name="outcome")
    return X.drop(columns=["game_id"]), y
