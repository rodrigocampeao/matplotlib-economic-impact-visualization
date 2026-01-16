import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Countries analyzed
countries = [
    "India",
    "Saudi Arabia",
    "Morocco",
    "Iraq",
    "Brazil",
    "Pakistan",
    "Bangladesh",
    "Syria (ISIS-controlled areas)",
    "Turkey"
]

# Downtime duration in days
days = [
    70.54, 45, 182, 2.75, 5, 3.83, 25, 348, 2.75
]

# Total economic impact (USD)
cost = [
    968080702, 465280632, 320456034, 209578705,
    116038230, 69769394, 69178309, 47945886, 35142917
]

# Figure size for editorial-style layout
plt.figure(figsize=(9, 5))

# Emphasize mid-range values with larger markers
sizes = [120 if c < 1e8 else 80 for c in cost]

plt.scatter(days, cost, s=sizes, alpha=0.8)

for i, country in enumerate(countries):
    plt.annotate(
        country,
        (days[i], cost[i]),
        xytext=(6, 6),
        textcoords="offset points"
    )

# Log scale to handle wide value ranges
plt.yscale("log")

# Custom Y-axis ticks (values expressed in millions)
y_ticks = [3e7, 5e7, 7e7, 1e8, 2e8, 5e8, 9e8]
plt.yticks(y_ticks)

# Format Y-axis labels in millions (M)
plt.gca().yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda x, _: f"{x/1e6:.0f}")
)

# Grid for better readability
plt.grid(axis="y", which="major", linestyle="--", linewidth=0.6, alpha=0.6)
plt.grid(axis="x", which="major", linestyle="--", linewidth=0.6, alpha=0.6)

plt.xlabel("Downtime duration (days)")
plt.ylabel("Economic impact (USD)")
plt.title("Downtime duration vs economic impact\n", loc="left")

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["left"].set_color("#D3D3D3")
plt.gca().spines["bottom"].set_color("#D3D3D3")

plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))
plt.xlim(left=1, right=190)
plt.ylim(bottom=3e7, top=max(cost) * 1.15)

plt.text(
    0, -0.35,
    "Economic impact does not scale linearly with downtime duration.\n"
    "In most cases, cost vs time reflects the accumulation of multiple incidents,\n"
    "rather than a single isolated event.",
    transform=plt.gca().transAxes,
    ha="left",
    fontsize=10
)

plt.tight_layout()
plt.savefig("downtime_scatter.png", dpi=300, bbox_inches="tight")
plt.show()