import pandas as pd
import pytest

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from calculator import (
    load_emission_factors,
    calc_emissions_per_person_km,
    calc_yearly_savings,
)


def test_load_emission_factors_returns_modes():
    df = load_emission_factors()
    assert len(df) > 0
    assert {"mode", "co2_grams_per_km", "passengers_avg"}.issubset(df.columns)


def test_per_person_km_matches_formula():
    df = pd.DataFrame({
        "mode": ["Car", "Bus"],
        "co2_grams_per_km": [180.0, 90.0],
        "passengers_avg": [1.5, 30.0],
    })
    out = calc_emissions_per_person_km(df)
    assert out.loc[0, "co2_per_person_km"] == pytest.approx(120.0)
    assert out.loc[1, "co2_per_person_km"] == pytest.approx(3.0)


def test_yearly_savings_is_zero_for_ice_car():
    df = load_emission_factors()
    yearly = calc_yearly_savings(df)
    ice = yearly[yearly["mode"] == "ICE Car"].iloc[0]
    assert ice["yearly_savings_kg"] == pytest.approx(0.0)


def test_bike_saves_all_ice_emissions():
    df = load_emission_factors()
    yearly = calc_yearly_savings(df)
    bike = yearly[yearly["mode"] == "Bike"].iloc[0]
    ice = yearly[yearly["mode"] == "ICE Car"].iloc[0]
    assert bike["yearly_savings_kg"] == pytest.approx(ice["yearly_co2_kg"])
