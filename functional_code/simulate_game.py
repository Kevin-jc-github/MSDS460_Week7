import random

def simulate_game(team1_stats, team2_stats):
    """
    Simulate a single game based on average runs using normal distribution.
    """
    team1_score = random.gauss(mu=team1_stats["avg_runs"], sigma=1.5)
    team2_score = random.gauss(mu=team2_stats["avg_runs"], sigma=1.5)

    if team1_score > team2_score:
        return team1_stats["team_name"]
    elif team2_score > team1_score:
        return team2_stats["team_name"]
    else:
        return random.choice([team1_stats["team_name"], team2_stats["team_name"]])
