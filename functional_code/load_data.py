import pandas as pd

def load_team_avg_runs(cubs_file, sox_file):
    cubs_df = pd.read_csv(cubs_file)
    sox_df = pd.read_csv(sox_file)

    cubs_avg = cubs_df['R'].sum() / cubs_df['G'].sum()
    sox_avg = sox_df['R'].sum() / sox_df['G'].sum()

    return {
        "Cubs": {"team_name": "Cubs", "avg_runs": cubs_avg},
        "White Sox": {"team_name": "White Sox", "avg_runs": sox_avg}
    }

def load_schedule(cubs_schedule_file, sox_schedule_file):
    abbrev_to_name = {
        "CHC": "Cubs",
        "CHW": "White Sox"
    }

    cubs_df = pd.read_csv(cubs_schedule_file)
    sox_df = pd.read_csv(sox_schedule_file)

    cubs_games = [
        ("Cubs", abbrev_to_name.get(row["Opp"], row["Opp"]))
        for _, row in cubs_df.iterrows()
        if row["Opp"] in abbrev_to_name and abbrev_to_name[row["Opp"]] == "White Sox"
    ]

    sox_games = [
        ("White Sox", abbrev_to_name.get(row["Opp"], row["Opp"]))
        for _, row in sox_df.iterrows()
        if row["Opp"] in abbrev_to_name and abbrev_to_name[row["Opp"]] == "Cubs"
    ]

    schedule = cubs_games + sox_games
    return schedule
