from pathlib import Path

from plotly import offline
from plotly.graph_objects import Bar, Layout

from die import Die

BASE_DIR = Path(__file__).resolve().parent


def roll_dice(die_1, die_2, roll_count=50_000):
    """Return frequencies for the sums from rolling two dice."""
    max_result = die_1.num_sides + die_2.num_sides
    results = [die_1.roll() + die_2.roll() for _ in range(roll_count)]
    return [results.count(value) for value in range(2, max_result + 1)]


def make_chart(die_1, die_2, frequencies, output_file):
    """Create an HTML bar chart for dice-roll frequencies."""
    x_values = list(range(2, die_1.num_sides + die_2.num_sides + 1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {"title": "Result", "dtick": 1}
    y_axis_config = {"title": "Frequency of Result"}
    layout = Layout(
        title=f"Results of rolling a D{die_1.num_sides} and a D{die_2.num_sides}",
        xaxis=x_axis_config,
        yaxis=y_axis_config,
    )
    offline.plot(
        {"data": data, "layout": layout},
        filename=str(output_file),
        auto_open=False,
    )


def main():
    """Roll a D6 and D10, then save the visualization."""
    die_1 = Die()
    die_2 = Die(10)
    frequencies = roll_dice(die_1, die_2)
    output_file = BASE_DIR / "d6_d10.html"
    make_chart(die_1, die_2, frequencies, output_file)
    print(f"Saved dice visualization to {output_file}")


if __name__ == "__main__":
    main()
