"""
End-to-end basket pipeline for a given athlete and time window.
"""

import pandas as pd

from src.ingest.build_possessions import build_possessions
from src.features.build_basket_X import build_basket_features
from src.models.basket_outcome import compute_outcome
from src.models.basket_model import fit_basket_model
from src.attribution.shapley_basket import compute_shap_values, aggregate_by_domain
from src.attribution.domain_maps import BASKET_DOMAIN_MAP


def run_basket_pipeline(
    pbp: pd.DataFrame,
    player_id: str,
    player_team: str,
):
    possessions = build_possessions(pbp)
    X = build_basket_features(pbp, player_id)
    y = pd.Series([compute_outcome(possessions, player_team)])

    model = fit_basket_model(X, y)
    shap_vals = compute_shap_values(model, X)
    domain_contrib = aggregate_by_domain(
        shap_vals, list(X.columns), BASKET_DOMAIN_MAP
    )

    return {
        "features": X,
        "outcome": float(y.iloc[0]),
        "domain_contributions": domain_contrib,
    }
