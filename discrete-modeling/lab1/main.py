import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import norm
from math import sqrt


def main():
    a = float(input("Enter start point a: "))
    b = float(input("Enter end point b: "))
    mu = float(input("Enter mu for normal distribution: "))
    sigma = float(input("Enter sigma for normal distribution: "))

    delta = b - a

    x_uniform = np.arange(a - delta / 2, b + delta / 2, 0.001)
    x_normal = np.arange(a, b, 0.001)

    y_uniform_cdf = [uniform_distribution_cdf(a, b, value) for value in x_uniform]
    y_uniform_pdf = [uniform_distribution_pdf(a, b, value) for value in x_uniform]

    y_normal_cdf = normal_distribution_cdf(x_normal, mu, sigma)
    y_normal_pdf = normal_distribution_pdf(x_normal, mu, sigma)

    draw_plots(x_uniform, y_uniform_cdf, y_uniform_pdf)
    draw_plots(x_normal, y_normal_cdf, y_normal_pdf)


def draw_plots(x, y_cdf, y_pdf):
    fig, axs = plt.subplots(2, figsize=(6,7))

    axs[0].plot(x, y_cdf)
    axs[1].plot(x, y_pdf)

    axs[0].set_xlabel('$x$')
    axs[0].set_ylabel('$F(x)$')

    axs[1].set_xlabel('$x$')
    axs[1].set_ylabel('$f(x)$')

    axs[0].grid(True)
    axs[1].grid(True)

    plt.show()


def uniform_distribution_cdf(a, b, x):
    return (x - a) / (b - a) if (a <= x < b) else 0 if x < a else 1

def uniform_distribution_pdf(a, b, x):
    return 1 / (b - a) if (a <= x <= b) else 0

def normal_distribution_cdf(x, mu, sigma):
    return norm.cdf(x, mu, sqrt(sigma))

def normal_distribution_pdf(x, mu, sigma):
    return norm.pdf(x, mu, sqrt(sigma))


if __name__ == '__main__':
    main()