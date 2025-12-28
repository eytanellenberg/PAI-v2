"""
Shapley attribution helpers (basketball).

This module computes SHAP values for a fitted predictive model and aggregates
feature-level contributions into higher-level domains (role/opportunity, efficiency,
context, etc.) for coach-friendly reporting.

Note: the "engine" advantage is NOT here. It lives in feature engineering and
how domains are defined/validated.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

try:
    import shap
except ImportError as e:
    raise ImportError("Missing dependency 'shap'. Install via requirements.txt") from e


def compute_shap_values(model, X: pd.DataFrame) -> np.ndarray:
    """
    Compute SHAP values for a fitted model on dataset X.

    - Uses TreeExplainer when available (fast for tree models).
    - Falls back to a model-agnostic explainer if needed.

    Returns
    -------
    shap_values : np.ndarray
        Shape (n_samples, n_features)
    """
    # Fast path: tree-based models
    try:
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X)
        # Some models return a list for multi-output; we handle the common single-output case
        if isinstance(shap_values, list):
            shap_values = shap_values[0]
        return np.asarray(shap_values)
    except Exception:
        # Generic fallback (slower): use independent masker
        masker = shap.maskers.Independent(X)
        explainer = shap.Explainer(model, masker)
        shap_values = explainer(X)
        return np.asarray(shap_values.values)


def aggregate_by_domain(
    shap_values: np.ndarray,
    feature_names: list[str],
    domain_map: dict[str, list[str]],
) -> pd.DataFrame:
    """
    Aggregate feature-level SHAP contributions into domains.

    Parameters
    ----------
    shap_values: np.ndarray
        (n_samples, n_features)
    feature_names: list[str]
        Names aligned with columns in X.
    domain_map: dict
        Example:
        {
          "Opportunity/Role": ["usage_proxy", "shot_share", "minutes"],
          "Efficiency": ["ts_proxy", "tov_rate"],
          "Context": ["score_diff", "home_away"]
        }

    Returns
    -------
    pd.DataFrame with columns:
        domain, mean_contribution, mean_abs_contribution
    """
    X_idx = {f: i for i, f in enumerate(feature_names)}

    rows = []
    for domain, feats in domain_map.items():
        idx = [X_idx[f] for f in feats if f in X_idx]
        if not idx:
            continue
        dom_vals = shap_values[:, idx].sum(axis=1)
        rows.append(
            {
                "domain": domain,
                "mean_contribution": float(np.mean(dom_vals)),
                "mean_abs_contribution": float(np.mean(np.abs(dom_vals))),
            }
        )

    out = pd.DataFrame(rows).sort_values("mean_abs_contribution", ascending=False)
    return out
