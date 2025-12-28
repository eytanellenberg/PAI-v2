"""
Download NBA play-by-play data using nba_api (public).
"""

from nba_api.stats.endpoints import playbyplayv2
from nba_api.library.http import NBAStatsHTTP
import pandas as pd
import time

# Force browser-like headers (critical for cloud)
NBAStatsHTTP.DEFAULT_HEADERS = {
    "Host": "stats.nba.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "x-nba-stats-token": "true",
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "x-nba-stats-origin": "stats",
    "Referer": "https://www.nba.com/",
    "Accept-Language": "en-US,en;q=0.9",
}


def download_game_pbp(game_id):
    pbp = playbyplayv2.PlayByPlayV2(
        game_id=game_id,
        timeout=60  # increase timeout
    )
    df = pbp.get_data_frames()[0]
    return df


def download_games(game_ids, sleep=2.0):
    frames = []
    for gid in game_ids:
        print(f"Downloading {gid}")
        df = download_game_pbp(gid)
        df["game_id"] = gid
        frames.append(df)
        time.sleep(sleep)  # slow down requests
    return pd.concat(frames, axis=0)
