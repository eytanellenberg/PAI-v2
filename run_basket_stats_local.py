from src.reports.run_basket_stats import run_WD

# path local (non push)
PBPCSV = "data/raw/basket/pbp.csv"

# Remplace par les équipes correspondant à W et D dans ton fichier
TEAM_W = "TEAM_W"
TEAM_D = "TEAM_D"

comp = run_WD(PBPCSV, TEAM_W, TEAM_D, outdir="outputs/tables/basket", n_boot=200)
print(comp)
