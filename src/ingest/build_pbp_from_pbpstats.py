from pbpstats.client import Client
import pandas as pd

# IMPORTANT : utiliser data.nba.com (moins bloqué)
client = Client(season="2023-24", league="NBA", data_provider="data_nba")

# Un match test (remplace plus tard)
GAME_ID = "0022300061"

game = client.Game(game_id=GAME_ID)

rows = []

for event in game.play_by_play:
    rows.append({
        "game_id": GAME_ID,
        "period": event.period,
        "clock": event.clock,
        "event_type": event.event_type,
        "points": event.points,
        "player_id": event.player_id if event.player_id else "other",
        "score_diff": event.score_margin,
        "home": 1 if event.team_id == game.home_team_id else 0
    })

df = pd.DataFrame(rows)

df.to_csv("data/raw/basket/pbp.csv", index=False)
print("Saved pbp.csv")
