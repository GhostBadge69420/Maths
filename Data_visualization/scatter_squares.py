import matplotlib.pyplot as plt


def plot_square_scatter(limit=1000):
    """Plot square numbers as a color-mapped scatter chart."""
    x_values = range(1, limit + 1)
    y_values = [x**2 for x in x_values]

    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)
    ax.tick_params(axis="both", which="major", labelsize=14)
    ax.axis([0, limit + 100, 0, (limit + 50) ** 2])

    plt.show()


if __name__ == "__main__":
    plot_square_scatter()
