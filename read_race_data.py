import numpy as np
import pandas as pd
from pathlib import Path

root = Path(__file__).resolve().parent
qualifying = pd.read_csv(root / "race data" / "qualifying.csv")
constructor_standings = pd.read_csv(root / "race data" / "constructor_standings.csv")

root = Path(__file__).resolve().parent
constructor_lap_times = pd.read_csv(root / "race data" / "lap_times.csv")

conlap = constructor_lap_times[["StandingsId", "position"]].rename(columns={"position": "constructor_position"})
qualpos = qualifying[["StandingsId", "position"]].rename(columns={"position": "qualifying_position"})
conpos = constructor_standings[["StandingsId", "position"]].rename(columns={"position": "constructor_position"})

combined = pd.merge(qualpos, conpos, on="StandingsId")
combined["position_delta"] = abs(combined["qualifying_position"].astype(int) - combined["constructor_position"].astype(int))
print(combined)

combined.to_csv(root / "race data" / "combined_output.csv", index=False)

