from pathlib import Path
import pandas as pd

from src.models.basket_model import fit_basket_model
from src.attribution.shapley_basket import compute_shap_values, aggregate_by_domain
from src.attribution.domain_maps import BASKET_DOMAIN_MAP
from src.stats.bootstrap_shap import bootstrap_domain_attribution
from src.stats.ci_utils import domain_confidence_intervals
from src.features.build_basket_dataset import build_dataset_per_game


def _prep_pbp(pbp: pd.DataFrame) -> pd.DataFrame:
    # normalize column names we rely on
    pbp = pbp.copy()
    if "player_code" in pbp.columns and "player_id" not in pbp.columns:
        pbp["player_id"] = pbp["player_code"]
    # fill context if missing
    if "score_diff" not in pbp.columns:
        pbp["score_diff"] = 0
    if "home" not in pbp.columns:
        pbp["home"] = 0
    if "points" not in pbp.columns:
        pbp["points"] = 0
    return pbp


def run_for_player(pbp: pd.DataFrame, player_code: str, team: str, outdir: str, n_boot: int = 200):
    pbp = _prep_pbp(pbp)

    X, y = build_dataset_per_game(pbp, player_code=player_code, team=team)
    if len(X) < 8:
        raise ValueError(f"Not enough games for player {player_code}. Need ~8+ games, got {len(X)}.")

    model = fit_basket_model(X, y)

    # SHAP per game (feature-level) + domain aggregation
    shap_vals = compute_shap_values(model, X)
    dom = aggregate_by_domain(shap_vals, list(X.columns), BASKET_DOMAIN_MAP)

    # Bootstrap uncertainty at domain-level
    boot = bootstrap_domain_attribution(model, X, BASKET_DOMAIN_MAP, n_boot=n_boot)
    ci = domain_confidence_intervals(boot)

    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)

    X.to_csv(out / f"{player_code}_X.csv", index=False)
    y.to_csv(out / f"{player_code}_y.csv", index=False)
    dom.to_csv(out / f"{player_code}_domain_contributions.csv", index=False)
    boot.to_csv(out / f"{player_code}_domain_bootstrap.csv", index=False)
    ci.to_csv(out / f"{player_code}_domain_ci.csv", index=False)

    return {"domains": dom, "ci": ci}


def run_WD(pbp_csv_path: str, team_W: str, team_D: str, outdir: str = "outputs/tables/basket", n_boot: int = 200):
    pbp = pd.read_csv(pbp_csv_path)

    pbp_W = pbp[pbp["player_code"] == "W"].copy()
    pbp_D = pbp[pbp["player_code"] == "D"].copy()

    resW = run_for_player(pbp_W, "W", team_W, outdir, n_boot=n_boot)
    resD = run_for_player(pbp_D, "D", team_D, outdir, n_boot=n_boot)

    # Merge for comparison figure/table
    comp = pd.concat(
        [
            resW["ci"].assign(player="W"),
            resD["ci"].assign(player="D"),
        ],
        axis=0
    )
    Path(outdir).mkdir(parents=True, exist_ok=True)
    comp.to_csv(Path(outdir) / "WD_domain_ci_comparison.csv", index=False)
    return comp
