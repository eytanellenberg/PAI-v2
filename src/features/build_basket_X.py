import pandas as pd

from src.features.basket_role_features import compute_role_features
from src.features.basket_efficiency_features import compute_efficiency_features
from src.features.basket_context_features import compute_context_features


def build_basket_features(pbp: pd.DataFrame, player_id: str) -> pd.DataFrame:
    role = compute_role_features(pbp, player_id)
    eff = compute_efficiency_features(pbp, player_id)
    ctx = compute_context_features(pbp)

    X = pd.concat([role, eff, ctx], axis=1)
    return X
