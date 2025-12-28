"""
End-to-end test: download -> clean -> save NBA PBP
"""

from src.ingest.download_nba_pbp import download_games
from src.ingest.clean_nba_pbp import clean_pbp
import pandas as pd


# Exemple minimal (à ajuster)
GAME_IDS = [
    "0022300061",  # exemple
    "0022300062",
]

PLAYER_MAP = {
    "Victor Wembanyama": "W",
    "Luka Doncic": "D",
}


def main():
    pbp_raw = download_games(GAME_IDS)
    pbp_clean = clean_pbp(pbp_raw, player_map=PLAYER_MAP)

    pbp_clean.to_csv("data/raw/basket/pbp.csv", index=False)

    print("Saved pbp.csv")
    print(pbp_clean.head())
    print(pbp_clean["event_type"].value_counts())


if __name__ == "__main__":
    main()
