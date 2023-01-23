#!/usr/bin/python
import astropy.units as u
import astropy.constants as c
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy as unp
import scipy
import uncertainties as un
from pprint import pp
import itertools

print("rolling...")


from lib import *


tex = {
    "TODOREMOVETHIS": un.ufloat(1, 0.1),
}
data = [[1, 2], [2, 3]]
tex_tables.append(
    {
        "tex": "TODOREMOVETHIS",
        "name": r"Messreihe $X_i$",
        "label": "tab:messreihei",
        "rowdescription": [r"$X_i$", r"$\alpha{}_i$"],
        "content": data,
    }
)

# fig, ax = plt.subplots(1, 2, figsize=(9, 5))
# out = scipy.optimize.curve_fit(absorptionsgesetz, d, N)
# ax[0].plot(fit_x, fit, color="cyan", label="fit N, with N_0=%.00f, μ=%.02f" % (N_0, mu))
# ax[0].scatter(d, N, marker="x", label="data points")
# ax[0].errorbar(X, Y, xerr=Xerr, yerr=Yerr, linestyle="None")
# ax[0].set_xlabel("d [cm]")
# ax[0].set_ylabel("N [1/60s]")
# ax[0].legend()
# plt.savefig("plot.pdf")
# plt.show()


def exampleplot():
    x = np.linspace(0, 10, 1000)
    y = x ** np.sin(x)
    plt.subplot(1, 2, 1)
    plt.plot(x, y, label="Kurve")
    plt.xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")
    plt.ylabel(r"$y \mathbin{/} \unit{\micro\joule}$")
    plt.legend(loc="best")
    plt.subplot(1, 2, 2)
    plt.plot(x, y, label="Kurve")
    plt.xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")
    plt.ylabel(r"$y \mathbin{/} \unit{\micro\joule}$")
    plt.legend(loc="best")
    # in matplotlibrc leider (noch) nicht möglich
    fuckinglayout(plt)
    plt.savefig("plot.pdf")


if __name__ == "__main__":
    exampleplot()
    maketables()
    makeconstants(tex)

print("done!")
