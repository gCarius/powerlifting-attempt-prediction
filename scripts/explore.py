import pandas as pd
import numpy as np
from pathlib import Path

df = pd.read_csv(
    "data/raw/openipf-2026-10-17/openipf-2026-10-17-c7782562.csv", low_memory=False
)
df["Year"] = pd.to_datetime(df["Date"]).dt.year

# Output step
output = Path("result/tables")
output.mkdir(parents=True, exist_ok=True)


def save_counts(df, col, out_dir, top=None):
    counts = df[col].value_counts(dropna=False)
    if top is not None:
        counts = counts.head(top)
    counts.reset_index().to_csv(out_dir / f"{col.lower()}_counts.csv", index=False)


settings = {
    "Event": None,
    "Place": None,
    "Sex": None,
    "Equipment": None,
    "ParentFederation": None,
    "Federation": 15,
    "Tested": None,
    "Division": 20,
    "Year": None,
}

for col, top in settings.items():
    save_counts(df, col, output, top)


numerical_cat = ["Squat1Kg", "Squat2Kg", "Squat3Kg", "BodyweightKg", "Age"]

rows = []
for col in numerical_cat:
    s = df[col]
    rows.append(
        {
            "column": col,
            "n_missing": s.isna().sum(),
            "pct_missing": round(s.isna().mean() * 100, 2),
            "n_negative": (s < 0).sum(),
            "n_zero": (s == 0).sum(),
            "n_positive": (s > 0).sum(),
            "min_abs": s.abs().min(),
            "median_abs": s.abs().median(),
            "mean_abs": round(s.abs().mean(), 2),
            "max_abs": s.abs().max(),
        }
    )

numeric_table = pd.DataFrame(rows)
numeric_table.to_csv(output / "numeric_summary.csv", index=False)


missing = (df.isna().mean() * 100).round(2).sort_values(ascending=False)
missing.rename_axis("column").reset_index(name="pct_missing").to_csv(
    output / "missing_values.csv", index=False
)

pd.crosstab(df["Event"], df["Squat3Kg"].isna()).to_csv(output / "event_vs_missing_squat3.csv")
pd.crosstab(df["Year"], df["Squat3Kg"].isna()).to_csv(output / "year_vs_missing_squat3.csv")