import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent


def load_temperature_data(filename):
    """Load dates, highs, and lows from a weather CSV file."""
    dates, highs, lows = [], [], []
    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            try:
                high = int(row[4])
                low = int(row[5])
            except ValueError:
                print(f"Missing data for {current_date:%Y-%m-%d}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    return dates, highs, lows


def plot_temperatures(dates, highs, lows):
    """Plot high and low temperatures."""
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c="red", alpha=0.5)
    ax.plot(dates, lows, c="blue", alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
    ax.set_title(title, fontsize=20)
    ax.set_xlabel("", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis="both", which="major", labelsize=16)

    plt.show()


def main():
    """Load and plot Death Valley temperature data."""
    filename = BASE_DIR / "data" / "death_valley_2018_simple.csv"
    dates, highs, lows = load_temperature_data(filename)
    print(f"Loaded {len(dates)} daily records.")
    print(f"High range: {min(highs)}F to {max(highs)}F")
    print(f"Low range: {min(lows)}F to {max(lows)}F")
    plot_temperatures(dates, highs, lows)


if __name__ == "__main__":
    main()
