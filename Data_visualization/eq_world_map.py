import json
from pathlib import Path

from plotly import offline
from plotly.graph_objects import Layout

BASE_DIR = Path(__file__).resolve().parent


def load_earthquake_data(filename):
    """Load earthquake data from a USGS JSON file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


def extract_earthquake_points(all_eq_data):
    """Extract magnitudes, locations, and hover text for plotting."""
    mags, lons, lats, hover_texts = [], [], [], []
    for eq_dict in all_eq_data["features"]:
        mag = eq_dict["properties"]["mag"]
        lon = eq_dict["geometry"]["coordinates"][0]
        lat = eq_dict["geometry"]["coordinates"][1]
        title = eq_dict["properties"]["title"]
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        hover_texts.append(title)
    return mags, lons, lats, hover_texts


def make_map(mags, lons, lats, hover_texts, output_file):
    """Save a global earthquake map as an HTML file."""
    data = [{
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_texts,
        "marker": {
            "size": [5 * mag for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }]
    fig = {"data": data, "layout": Layout(title="Global Earthquakes")}
    offline.plot(fig, filename=str(output_file), auto_open=False)


def main():
    """Create the global earthquake visualization."""
    filename = BASE_DIR / "data" / "eq_data_30_day_m1.json"
    all_eq_data = load_earthquake_data(filename)
    mags, lons, lats, hover_texts = extract_earthquake_points(all_eq_data)

    output_file = BASE_DIR / "global_earthquakes.html"
    make_map(mags, lons, lats, hover_texts, output_file)

    readable_file = BASE_DIR / "data" / "readable_eq_data.json"
    with open(readable_file, "w", encoding="utf-8") as f:
        json.dump(all_eq_data, f, indent=4)

    print(f"Saved {len(mags)} earthquakes to {output_file}")


if __name__ == "__main__":
    main()
