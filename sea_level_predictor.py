import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    plt.clf()

    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"],
        label="CSIRO Adjusted Sea Level",
        s=20,
    )

    # Create first line of best fit
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    extended_years = pd.Series(range(df["Year"].min(), 2050 + 1))
    plt.plot(
        extended_years,
        result.slope * extended_years + result.intercept,
        label="Line of Best Fit",
        color="magenta",
    )

    # Create second line of best fit
    recent_df = df[df["Year"] >= 2000]
    recent_result = linregress(
        recent_df["Year"], recent_df["CSIRO Adjusted Sea Level"]
    )
    recent_extended_years = pd.Series(range(recent_df["Year"].min(), 2050 + 1))
    plt.plot(
        recent_extended_years,
        recent_result.slope * recent_extended_years + recent_result.intercept,
        label="Recent Line of Best Fit",
        color="orange",
    )

    # Add labels and title
    plt.legend(numpoints=1)
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
