"""
Bootstrap uncertainty estimation for domain-level SHAP attributions.
"""

import numpy as np
import pandas as pd
from sklearn.utils import resample

from src.attribution.shapley_basket import compute_shap_values, aggregate_by_domain


def bootstrap_domain_attribution(
    model,
    X: pd.DataFrame,
    domain_map: dict,
    n_boot: int = 200,
    random_state: int = 42,
):
    rng = np.random.RandomState(random_state)
    results = []

    for b in range(n_boot):
        Xb = resample(X, random_state=rng.randint(1e6))
        shap_vals = compute_shap_values(model, Xb)
        dom = aggregate_by_domain(
            shap_vals, list(X.columns), domain_map
        )
        dom["boot"] = b
        results.append(dom)

    out = pd.concat(results, axis=0)
    return out
