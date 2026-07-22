'''Task 4: Sports Data Analysis with Pandas
• Tech Stack: Python, pandas, matplotlib
• Description: Analyze a historical CSV dataset of Indian Premier League (IPL) matches. Write a script to
calculate team win rates, specifically filtering the data to visualize the historical performance and toss-decision
outcomes for franchises like the Kolkata Knight Riders'''


import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset

df = pd.read_csv("matches.csv")

print("First 5 Rows:")
print(df.head())

# 1. Team Win Rates

# Total matches played by each team
team_matches = pd.concat([df['team1'], df['team2']]).value_counts()

# Total wins
team_wins = df['winner'].value_counts()

# Create DataFrame
win_rate_df = pd.DataFrame({
    "Matches Played": team_matches,
    "Matches Won": team_wins
}).fillna(0)

win_rate_df["Matches Won"] = win_rate_df["Matches Won"].astype(int)

# Calculate Win Rate
win_rate_df["Win Rate (%)"] = (
    win_rate_df["Matches Won"] /
    win_rate_df["Matches Played"] * 100
).round(2)

# Sort by Win Rate
sorted_df = win_rate_df.sort_values(
    by="Win Rate (%)",
    ascending=False
)

print("\nTeam Win Rates")
print(sorted_df)

# ----------------------------------
# 2. Kolkata Knight Riders Analysis
# ----------------------------------

kkr_matches = df[
    (df['team1'] == 'Kolkata Knight Riders') |
    (df['team2'] == 'Kolkata Knight Riders')
]

kkr_total = len(kkr_matches)

kkr_wins = len(
    kkr_matches[kkr_matches['winner'] == 'Kolkata Knight Riders']
)

kkr_losses = kkr_total - kkr_wins

print("\nKKR Performance")
print("Matches Played:", kkr_total)
print("Wins:", kkr_wins)
print("Losses:", kkr_losses)
print("Win %:", round(kkr_wins / kkr_total * 100, 2))

# ----------------------------------
# 3. Toss Decision Analysis for KKR
# ----------------------------------

kkr_toss = kkr_matches[
    kkr_matches['toss_winner'] == 'Kolkata Knight Riders'
].copy()

toss_choice = kkr_toss['toss_decision'].value_counts()

print("\nKKR Toss Decisions")
print(toss_choice)

# ----------------------------------
# 4. KKR Winning After Winning Toss
# ----------------------------------

kkr_toss["Won Match"] = (
    kkr_toss["winner"] == "Kolkata Knight Riders"
)

toss_result = (
    kkr_toss.groupby("toss_decision")["Won Match"]
    .mean() * 100
).round(2)

print("\nWin % after Winning Toss")
print(toss_result)

# Visualization 1
# Team Win Rate

plt.figure(figsize=(12,6))

ax = sorted_df["Win Rate (%)"].plot(
    kind="bar",
    color="skyblue"
)

plt.title("IPL Team Win Rate")
plt.ylabel("Win Rate (%)")
plt.xlabel("Teams")
plt.xticks(rotation=75)

# Add value labels
for p in ax.patches:
    ax.annotate(
        f"{p.get_height():.1f}%",
        (p.get_x() + p.get_width()/2, p.get_height()),
        ha="center",
        va="bottom",
        fontsize=8
    )

plt.tight_layout()
plt.show()




# Visualization 2
# KKR Historical Performance by Season

if "season" in df.columns:
    kkr_season_wins = (
        kkr_matches[
            kkr_matches["winner"] == "Kolkata Knight Riders"
        ]
        .groupby("season")
        .size()
    )

    plt.figure(figsize=(8,5))

    kkr_season_wins.plot(
        marker="o",
        linewidth=2
    )

    plt.title("KKR Wins by Season")
    plt.xlabel("Season")
    plt.ylabel("Number of Wins")
    plt.grid(True)

    plt.tight_layout()
    plt.show()
else:
    print("\n'Season' column not found. Skipping historical performance chart.")