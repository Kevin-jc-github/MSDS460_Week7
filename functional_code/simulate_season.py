from simulate_game import simulate_game

def simulate_season(teams_stats, schedule):
    """
    Simulate a full season of games using a real schedule.
    """
    win_counter = {team: 0 for team in teams_stats}

    for team1, team2 in schedule:
        if team1 in teams_stats and team2 in teams_stats:
            winner = simulate_game(teams_stats[team1], teams_stats[team2])
            win_counter[winner] += 1

    return win_counter
