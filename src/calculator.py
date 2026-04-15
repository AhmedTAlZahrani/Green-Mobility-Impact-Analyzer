import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "emission_factors.csv"


def load_emission_factors():
    df = pd.read_csv(DATA_FILE)
    return df


def calc_emissions_per_person_km(df):
    # for shared modes, divide total CO2 by average passengers
    df = df.copy()
    df["co2_per_person_km"] = df["co2_grams_per_km"] / df["passengers_avg"]
    return df


def calc_yearly_savings(df, daily_km=20, work_days=250):
    # compare each mode against ICE car for a year of commuting
    df = calc_emissions_per_person_km(df)
    ice_row = df[df["mode"] == "ICE Car"]
    if ice_row.empty:
        print("Warning: no ICE Car row found")
        return df

    ice_co2 = ice_row["co2_per_person_km"].values[0]
    df = df.copy()
    df["yearly_co2_kg"] = (df["co2_per_person_km"] * daily_km * work_days) / 1000
    df["yearly_savings_kg"] = ((ice_co2 - df["co2_per_person_km"]) * daily_km * work_days) / 1000
    return df
