# Green Mobility Impact Analyzer

Compare CO2 emissions across different transport modes (car, bus, metro, bike, etc.) and see how much carbon you can save by switching your daily commute.

Uses emission factor data to calculate per-person CO2 and generates simple charts.

## How to Run

```bash
pip install -r requirements.txt
cd src
python main.py
```

Charts are saved to the `plots/` folder.

## What It Does

- Loads emission factors from `src/data/emission_factors.csv`
- Calculates CO2 per person-km for each transport mode
- Estimates yearly savings vs driving a gasoline car
- Generates bar charts and a pie chart comparing modes

## Project Structure

```
src/
  main.py          - main script
  calculator.py    - emission calculation functions
  visualize.py     - chart generation
  data/            - emission factors CSV
plots/             - generated charts (gitignored)
```
