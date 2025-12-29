import pandas as pd

def clean_static_pbp(path):
    df = pd.read_csv(path)

    out = pd.DataFrame({
        "game_id": df["game_id"],
        "period": df["period"],
        "clock": df["clock"],
        "secs_game": df["secs_game"],
        "event_type": df["msg_type"],
        "action_type": df["act_type"],

        # attribution joueur
        "player": df["player1_name"],
        "shot_pts": df["shot_pts"].fillna(0),

        # contexte score
        "score_diff": df["margin_before"].fillna(0),
        "garbage_time": df["garbage_time"],

        # possession
        "possession": df["possession"],
        "poss_home": df["poss_home"],
        "poss_away": df["poss_away"],

        # contexte collectif
        "lineup_home": df["lineup_home"],
        "lineup_away": df["lineup_away"],
        "secs_played": df["secs_played"]
    })

    return out
