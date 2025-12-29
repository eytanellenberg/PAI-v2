import os
from src.ingest.clean_nba_pbp_static import clean_static_pbp

df = clean_static_pbp("data/raw/basket/pbp_raw.csv")

os.makedirs("data/raw/basket", exist_ok=True)
df.to_csv("data/raw/basket/pbp.csv", index=False)

print("✅ pbp.csv ready")
print(df.head())
