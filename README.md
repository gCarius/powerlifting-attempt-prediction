# powerlifting-attempt-prediction
Predicting attempt successfulness in squats (CMPUT 466/566 course project, Fall 2026).

**Task:** given a lifter's information and their squat attempts 1 and 2 plus the declared 3rd attempt weight, predict whether the 3rd squat attempt is made (binary classification). Squat only. Lifters are split into train/validation/test by lifter, never by row.

## Data
- Source: OpenIPF dataset from the OpenPowerlifting project, https://www.openpowerlifting.org (data: https://gitlab.com/openpowerlifting/opl-data).
- File: `openipf-2026-10-17-c7782562.csv`, snapshot dated 2026-10-17 (IPF and affiliated federations).
- License: public domain (see `data/raw/openipf-2026-10-17/LICENSE.txt`).
- Attribution: This project uses data from the OpenPowerlifting project, https://www.openpowerlifting.org. You may download a copy of the data at https://gitlab.com/openpowerlifting/opl-data.
- The raw CSV is not committed (about 330 MB). To reproduce, download the OpenIPF file from openpowerlifting.org and unzip it into `data/raw/openipf-2026-10-17/`.

## Setup
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Folder structure
```
data/raw/        raw CSV (not committed)
data/processed/  filtered squat table, saved splits, counts tables
src/             data, features, split, models, tuning, evaluation code
scripts/         numbered scripts that run the experiments
result/         tuning tables, final tables, figures
report/          final report
```

## Reproducing the results
To be filled in once the scripts exist (run order, random seeds, expected outputs).
