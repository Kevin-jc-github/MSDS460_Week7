import random
import csv
from load_data import load_team_avg_runs, load_schedule
from simulate_season import simulate_season

# Load team stats and schedule
teams_stats = load_team_avg_runs(
    "prepared_data/cubs_standard_batting_team_totals_clean.csv",
    "prepared_data/whitesox_standard_batting_team_totals_clean.csv"
)

schedule = load_schedule(
    "prepared_data/2025_Cubs_schedule.csv",
    "prepared_data/2025_CWS_schedule.csv"
)

def run_simulations(num_simulations=1000):
    total_results = {team: [] for team in teams_stats}

    for _ in range(num_simulations):
        wins = simulate_season(teams_stats, schedule)
        for team in wins:
            total_results[team].append(wins[team])
    return total_results

def save_results(results, filename="results/monte_carlo_results.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Team", "Wins"])
        for team, win_list in results.items():
            for wins in win_list:
                writer.writerow([team, wins])

if __name__ == "__main__":
    random.seed(42)
    results = run_simulations(num_simulations=1000)
    save_results(results)
    print("✅ Simulation complete. Results saved to results/monte_carlo_results.csv.")

