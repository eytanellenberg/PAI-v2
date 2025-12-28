"""
Run a minimal end-to-end attribution on prepared basket features.

Expected inputs (not included in repo):
- X: features DataFrame (n_samples, n_features)
- y: outcome Series (n_samples,)

This script shows how SHAP values are computed and aggregated into domains.
"""

import pandas as pd

from src.attribution.shapley_basket import compute_shap_values, aggregate_by_domain
from src.attribution.domain_maps import BASKET_DOMAIN_MAP


def run(model, X: pd.DataFrame) -> pd.DataFrame:
    shap_vals = compute_shap_values(model, X)
    domains = aggregate_by_domain(shap_vals, list(X.columns), BASKET_DOMAIN_MAP)
    return domains
