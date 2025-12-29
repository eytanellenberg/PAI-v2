import os
import pandas as pd

from pbpstats.client import Client
from pbpstats.resources.settings import NBASettings

# REQUIRED: settings object
settings = NBASettings()
client = Client(settings)

# One test game (NBA 2023-24)
GAME_ID = "0022300061"

game = client.Game(game_id=GAME_ID)

rows = []
for event in game.play_by_play:
    rows.append({
        "game_id": GAME_ID,
        "period": event.period,
        "clock": event.clock,
        "event_type": event.event_type,
        "points": event.points or 0,
        "player_id": event.player_id or "other",
        "score_diff": event.score_margin,
        "home": int(event.team_id == game.home_team_id)
    })

df = pd.DataFrame(rows)

os.makedirs("data/raw/basket", exist_ok=True)
df.to_csv("data/raw/basket/pbp.csv", index=False)

print("✅ Saved data/raw/basket/pbp.csv")
print(df.head())
