from calculator import load_emission_factors, calc_emissions_per_person_km, calc_yearly_savings
from visualize import bar_chart_emissions, bar_chart_yearly_savings, pie_chart_comparison

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

# generate charts
print("Generating charts...")
bar_chart_emissions(df)
bar_chart_yearly_savings(yearly)
pie_chart_comparison(df)
print("\nDone! Check the plots/ folder.")
