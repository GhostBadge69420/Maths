import matplotlib.pyplot as plt

from random_walk import RandomWalk

plt.style.use("classic")


def plot_random_walk(num_points=50_000):
    """Generate and plot a random walk."""
    rw = RandomWalk(num_points)
    rw.fill_walk()

    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors="none",
        s=1,
    )

    # Emphasize the first and last points.
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()


def main():
    """Keep making new walks, as long as the program is active."""
    while True:
        plot_random_walk()

        keep_running = input("Make another walk? (y/n): ")
        if keep_running.lower() == "n":
            break


if __name__ == "__main__":
    main()
