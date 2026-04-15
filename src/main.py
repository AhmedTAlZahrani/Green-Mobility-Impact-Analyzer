from pathlib import Path

from calculator import load_emission_factors, calc_emissions_per_person_km, calc_yearly_savings
from visualize import bar_chart_emissions, bar_chart_yearly_savings, pie_chart_comparison

RESULTS_DIR = Path(__file__).resolve().parents[1] / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def write_summary_md(yearly, path):
    lines = [
        "# Green Mobility Impact Analyzer — Results",
        "",
        "Per-person CO2 and yearly savings for a 20 km daily commute (250 working days).",
        "Shared-mode numbers assume average occupancy: 30 passengers for bus, 150 for metro.",
        "",
        "| Mode | CO2 per person-km (g) | Yearly CO2 (kg) | Savings vs ICE Car (kg/year) |",
        "|------|-----------------------|-----------------|------------------------------|",
    ]
    for _, r in yearly.iterrows():
        lines.append(
            f"| {r['mode']} | {r['co2_per_person_km']:.1f} | "
            f"{r['yearly_co2_kg']:.0f} | {r['yearly_savings_kg']:.0f} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


print("=== Green Mobility Impact Analyzer ===\n")

# load data
df = load_emission_factors()
print(f"Loaded {len(df)} transport modes from emission_factors.csv")
print()

# calculate per-person emissions
df = calc_emissions_per_person_km(df)
print("CO2 per person-km:")
for _, row in df.iterrows():
    print(f"  {row['mode']:15s} -> {row['co2_per_person_km']:.1f} g/km")
print()

# calculate yearly impact for a 20km daily commute
yearly = calc_yearly_savings(df)
print("Yearly CO2 for 20km daily commute:")
for _, row in yearly.iterrows():
    print(f"  {row['mode']:15s} -> {row['yearly_co2_kg']:.0f} kg/year  (saves {row['yearly_savings_kg']:.0f} kg vs car)")
print()

# save the computed table as CSV + a human-readable markdown summary
csv_out = RESULTS_DIR / "summary.csv"
md_out = RESULTS_DIR / "summary.md"
yearly.to_csv(csv_out, index=False)
write_summary_md(yearly, md_out)
print(f"Saved: {csv_out}")
print(f"Saved: {md_out}")
print()

# generate charts
print("Generating charts...")
bar_chart_emissions(df)
bar_chart_yearly_savings(yearly)
pie_chart_comparison(df)
print("\nDone! Check the plots/ and results/ folders.")
