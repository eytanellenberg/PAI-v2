"""
Basic loader for public soccer event data.

This script only handles data loading and filtering.
No modeling, attribution, or performance logic is included.
"""

import json
import pandas as pd
from pathlib import Path


def load_event_file(path):
    """Load a single event JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.json_normalize(data)


def filter_by_player(events, player_name):
    """Filter events for a given player."""
    if "player.name" not in events.columns:
        return events.iloc[0:0]
    return events[events["player.name"] == player_name].copy()
