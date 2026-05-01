from plotly import colors


def main():
    """Print the available Plotly color scales."""
    for key in colors.PLOTLY_SCALES:
        print(key)


if __name__ == "__main__":
    main()
