import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_win_distributions(csv_path, output_dir="results/"):
    """
    Read the Monte Carlo results CSV and plot win distributions for each team.
    Saves a histogram plot as PNG in the results directory.
    """
    # Read the results
    df = pd.read_csv(csv_path)

    # Set up the plot
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x="Wins", hue="Team", kde=False, bins=30, multiple="dodge")

    plt.title("Monte Carlo Simulation: Win Distribution per Team")
    plt.xlabel("Number of Wins per Season")
    plt.ylabel("Frequency (across simulations)")
    plt.legend(title="Team")
    plt.grid(True)

    # Save the plot
    os.makedirs(output_dir, exist_ok=True)
    plot_path = os.path.join(output_dir, "win_distribution.png")
    plt.savefig(plot_path)
    plt.close()

    print(f"✅ Plot saved to {plot_path}")

if __name__ == "__main__":
    plot_win_distributions("results/monte_carlo_results.csv")
