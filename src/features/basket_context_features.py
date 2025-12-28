"""
Contextual constraints.
"""

import pandas as pd


def compute_context_features(pbp: pd.DataFrame) -> pd.DataFrame:
    score_diff = pbp["score_diff"].mean()
    home = int(pbp["home"].iloc[0])

    return pd.DataFrame(
        {
            "score_diff": [score_diff],
            "home": [home],
        }
    )
