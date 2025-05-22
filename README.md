# 🧢 Monte Carlo Baseball Simulation

This project simulates the outcomes of baseball games between the **Chicago Cubs** and **Chicago White Sox** using Monte Carlo methods, based on real player performance data and the official 2025 schedule.

It is designed for transparent, reproducible, and AI-assisted development as part of a data science coursework project.

---

##  Project Objective

- Simulate 1000 seasons of Cubs vs. White Sox matchups.
- Estimate win distributions based on historical team performance.
- Visualize the range of possible outcomes using histograms.

---

##  Repository Structure

Root/
├── functional_code/
│ ├── load_data.py # Load team stats and real schedule
│ ├── simulate_game.py # Simulate a single game
│ ├── simulate_season.py # Simulate full season
│ ├── run_monte_carlo.py # Run Monte Carlo simulation and save results
│ └── plot_results.py # Visualize win distributions
├── prepared_data/ # Cleaned input data files
├── documentation_and_project_management_artifacts/ # Project documentation (Functional Specs, WBS, etc.)
├── results/
│ ├── monte_carlo_results.csv # Simulation outputs
│ └── win_distribution.png # Result visualization
└── README.md

---

##  How It Works

1. **load_data.py**:
   - Loads batting team totals to calculate average runs per game.
   - Extracts games between Cubs and White Sox from 2025 schedule files.

2. **simulate_game.py**:
   - Simulates one game using normal distribution centered at each team's average runs.

3. **simulate_season.py**:
   - Simulates an entire season based on the filtered schedule.

4. **run_monte_carlo.py**:
   - Repeats the season simulation 1000 times.
   - Saves the win count for each team per simulation to a CSV.

5. **plot_results.py**:
   - Plots a histogram of win distributions for both teams.

---

##  How to Run

> Make sure you have `pandas`, `matplotlib`, and `seaborn` installed:
```bash
pip install pandas matplotlib seaborn
```
---

## Sample Output

- After running, you'll find:

- results/monte_carlo_results.csv: Raw simulation data

- results/win_distribution.png: Histogram of wins across simulations

## AI Collaboration
This project was developed in collaboration with ChatGPT to:

Generate some functional simulation code

Improve reproducibility and code quality

