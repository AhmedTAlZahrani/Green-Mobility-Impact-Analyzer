import matplotlib.pyplot as plt
from pathlib import Path

PLOTS_DIR = Path(__file__).resolve().parents[1] / "plots"
PLOTS_DIR.mkdir(parents=True, exist_ok=True)


def bar_chart_emissions(df):
    # bar chart of CO2 per person-km for each mode
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ["#e74c3c" if v > 50 else "#2ecc71" for v in df["co2_per_person_km"]]
    ax.bar(df["mode"], df["co2_per_person_km"], color=colors)
    ax.set_title("CO2 Emissions per Person-km")
    ax.set_ylabel("grams CO2")
    ax.set_xlabel("")
    plt.xticks(rotation=30)
    plt.tight_layout()
    outpath = PLOTS_DIR / "emissions_per_person_km.png"
    fig.savefig(outpath, dpi=150)
    plt.close(fig)
    print(f"Saved: {outpath}")
    return outpath


def bar_chart_yearly_savings(df):
    # how many kg CO2 saved vs driving a gasoline car
    savings = df[df["mode"] != "ICE Car"].copy()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(savings["mode"], savings["yearly_savings_kg"], color="#3498db")
    ax.set_title("Yearly CO2 Savings vs ICE Car (20km daily commute)")
    ax.set_xlabel("kg CO2 saved per year")
    plt.tight_layout()
    outpath = PLOTS_DIR / "yearly_savings.png"
    fig.savefig(outpath, dpi=150)
    plt.close(fig)
    print(f"Saved: {outpath}")
    return outpath


def pie_chart_comparison(df):
    # pie chart showing share of emissions
    fig, ax = plt.subplots(figsize=(7, 7))
    non_zero = df[df["co2_per_person_km"] > 0]
    ax.pie(non_zero["co2_per_person_km"], labels=non_zero["mode"], autopct="%1.0f%%")
    ax.set_title("Emission Share by Transport Mode")
    plt.tight_layout()
    outpath = PLOTS_DIR / "emission_share_pie.png"
    fig.savefig(outpath, dpi=150)
    plt.close(fig)
    print(f"Saved: {outpath}")
    return outpath
