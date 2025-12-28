"""
Sensitivity of attribution to window size.
"""

import pandas as pd


def window_sensitivity(
    attribution_fn,
    pbp,
    player_id,
    player_team,
    windows: list[int],
):
    rows = []

    for w in windows:
        res = attribution_fn(
            pbp.tail(w),
            player_id=player_id,
            player_team=player_team,
        )
        dom = res["domain_contributions"]
        dom["window"] = w
        rows.append(dom)

    return pd.concat(rows, axis=0)
