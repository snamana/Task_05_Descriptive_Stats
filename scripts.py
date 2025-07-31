import os

# Re-create the folder structure after code execution environment reset
base_path = "/mnt/data/Task_05_Descriptive_Stats/scripts"
os.makedirs(base_path, exist_ok=True)

# Define the script contents
scripts = {
    "basic_stats.py": """
# Calculate total games played from a mock dataset
games = ["W", "L", "W", "W", "L", "W", "L", "W", "W", "W", "L", "W", "L", "W", "L", "W", "W", "L", "W", "L", "W", "W", "W", "L", "W", "L", "W", "W", "W", "W", "L", "W"]
print("Total Games Played:", len(games))
print("Wins:", games.count("W"))
print("Losses:", games.count("L"))
""",

    "improvement_check.py": """
# Manually verify most improved player
players = {
    "Player A": {"first_5_avg": 8.2, "last_5_avg": 9.0},
    "Player B": {"first_5_avg": 4.4, "last_5_avg": 12.8},
    "Player C": {"first_5_avg": 11.0, "last_5_avg": 13.2},
}

print("PPG Improvement Over Season:")
for name, stats in players.items():
    diff = stats["last_5_avg"] - stats["first_5_avg"]
    print(f"{name}: +{diff:.1f} PPG")
""",

    "margin_of_victory.py": """
# Calculate average scoring margin
game_scores = [
    {"SU": 75, "OPP": 70},
    {"SU": 68, "OPP": 72},
    {"SU": 81, "OPP": 65},
    {"SU": 59, "OPP": 78},
    {"SU": 84, "OPP": 80},
]

total_margin = 0
for game in game_scores:
    margin = game["SU"] - game["OPP"]
    total_margin += margin

average_margin = total_margin / len(game_scores)
print("Average Scoring Margin:", round(average_margin, 2))
""",

    "offense_vs_defense.py": """
# Compare points in wins vs. losses
games = [
    {"result": "W", "SU": 80, "OPP": 65},
    {"result": "W", "SU": 78, "OPP": 70},
    {"result": "L", "SU": 62, "OPP": 81},
    {"result": "L", "SU": 68, "OPP": 75},
    {"result": "W", "SU": 83, "OPP": 66},
]

win_points = [g["SU"] for g in games if g["result"] == "W"]
loss_points = [g["SU"] for g in games if g["result"] == "L"]
loss_opponent_pts = [g["OPP"] for g in games if g["result"] == "L"]

print("Avg Points Scored in Wins:", sum(win_points) / len(win_points))
print("Avg Points Scored in Losses:", sum(loss_points) / len(loss_points))
print("Avg Opponent Points in Losses:", sum(loss_opponent_pts) / len(loss_opponent_pts))
"""
}

# Save scripts to files
for filename, content in scripts.items():
    with open(os.path.join(base_path, filename), "w") as f:
        f.write(content.strip())

import shutil
shutil.make_archive("/mnt/data/LLM_Evaluation_Scripts", 'zip', base_path)

"/mnt/data/LLM_Evaluation_Scripts.zip"
