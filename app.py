import sys
sys.path.insert(0, "src")

from calculator import load_emission_factors, calc_emissions_per_person_km, calc_yearly_savings
from visualize import bar_chart_emissions, bar_chart_yearly_savings, pie_chart_comparison

# simple script that generates all charts at once
# can be extended to a Streamlit dashboard later

print("Loading data...")
df = load_emission_factors()
df = calc_emissions_per_person_km(df)
yearly = calc_yearly_savings(df)

print("Generating all charts...")
bar_chart_emissions(df)
bar_chart_yearly_savings(yearly)
pie_chart_comparison(df)

print("All charts saved to plots/ folder.")
