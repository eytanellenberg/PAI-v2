"""
Download NBA play-by-play data using nba_api (public).
"""

from nba_api.stats.endpoints import playbyplayv2
import pandas as pd
import time


def download_game_pbp(game_id: str) -> pd.DataFrame:
    pbp = playbyplayv2.PlayByPlayV2(game_id=game_id)
    df = pbp.get_data_frames()[0]
    return df


def download_games(game_ids, sleep: float = 0.6) -> pd.DataFrame:
    frames = []
    for gid in game_ids:
        print(f"Downloading {gid}")
        df = download_game_pbp(gid)
        df["game_id"] = gid
        frames.append(df)
        time.sleep(sleep)  # polite rate limit
    return pd.concat(frames, axis=0)
