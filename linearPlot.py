import matplotlib.pyplot as plt
from uncertainty import *
from chiSquared import *
from linearFit import *


def linearPlot(x_val, x_err, y_val, y_err, title, x_label, y_label):

    # Determine Values and Uncertainty for Slope and Intercept
    [m, m_err, b, b_err] = fit(x_val, y_val)

    # Print slope and intercept uncertainties
    print("slope:")
    print(m)
    print("")
    print("slope uncertainty:")
    print(m_err)
    print("")
    print("y-intercept:")
    print(b)
    print("")
    print("y-intercept uncertainty:")
    print(b_err)
    print("")

    # Initialize list to represent linear fit
    yline = []
    for i in range(0, len(y_val)):
        yline = yline + [m * (x_val[i]) + b]

    # Find Reduced Chi Squared Value
    c = chi(yline, y_val, y_err)
    v = len(x_val) - 2
    print("Reduced chi-squared for Plot 1:")
    print(c / v)
    print("")

    # Plot Figure
    plt.figure(1)
    plt.scatter(x_val, y_val)
    plt.plot(x_val, yline)
    plt.errorbar(x_val, y_val, xerr=x_err, yerr=y_err, linestyle="None")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Plot Residual
    residual = []

    for i in range(0, len(y_val)):
        residual = residual + [y_val[i] - yline[i]]

    plt.figure(2)
    plt.scatter(x_val, residual)
    plt.plot(x_val, [0] * len(x_val), "k")
    plt.title(title + " (Residual Plot)")
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.show
