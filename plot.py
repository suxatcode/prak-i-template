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
tables = []
data = [
    [un.ufloat(1.1, 0.1), un.ufloat(2.2, 0.2)],
    [un.ufloat(1.123456e-10, 1e-11), un.ufloat(1.1, 0.1)],
]
tex_tables = []
tex_tables.append(
    {
        "tex": "TODOREMOVETHIS",
        "name": r"Messreihe $X_i$",
        "rowdescription": [r"$X_i$", r"$\alpha{}_i$"],
        "content": data,
    }
)
tables.append(
    {
        "tex": "sample",
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
# plt.savefig("build/plot.svg")
# plt.show()


def exampleplot():
    x = np.linspace(0, 10, 1000)
    y = x ** np.sin(x)
    plt.subplot(1, 2, 1)
    plt.plot(x, y, label="Kurve")
    plt.xlabel(r"$\alpha / \Omega$")
    plt.ylabel(r"$y / \text{mJ}$")
    plt.legend(loc="best")
    plt.subplot(1, 2, 2)
    plt.plot(x, y, label="Kurve")
    plt.xlabel(r"$\alpha / \Omega$")
    plt.ylabel(r"$y / \text{mJ}$")
    plt.legend(loc="best")
    plotdefaults(plt)
    plt.savefig("build/plot.svg")


if __name__ == "__main__":
    exampleplot()
    maketables(tex_tables)
    make_typst_tables(tables)
    makeconstants(tex)

print("done!")
