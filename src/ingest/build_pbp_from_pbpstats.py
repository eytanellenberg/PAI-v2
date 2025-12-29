import os
import pandas as pd

from pbpstats.client import Client
from pbpstats.resources.settings import (
    NBASettings,
    DATA_NBA_ENDPOINT
)

# --- pbpstats settings (REQUIRED) ---
settings = NBASettings(
    data_provider=DATA_NBA_ENDPOINT
)

client = Client(settings)

# --- single test game ---
GAME_ID = "0022300061"

game = client.Game(game_id=GAME_ID)

rows = []

for event in game.play_by_play:
    rows.append({
        "game_id": GAME_ID,
        "period": event.period,
        "clock": event.clock,
        "event_type": event.event_type,
        "points": event.points if event.points else 0,
        "player_id": event.player_id if event.player_id else "other",
        "score_diff": event.score_margin,
        "home": 1 if event.team_id == game.home_team_id else 0
    })

df = pd.DataFrame(rows)

os.makedirs("data/raw/basket", exist_ok=True)
df.to_csv("data/raw/basket/pbp.csv", index=False)

print("Saved data/raw/basket/pbp.csv")
print(df.head())
