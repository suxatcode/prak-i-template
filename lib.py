import numpy as np
import uncertainties as un
from uncertainties import unumpy as unp
from pprint import pp
import itertools


def fuckinglayout(plt):
    plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)


def plotdefaults(plt, ax=None):
    if ax is not None:
        ax.legend()
    plt.grid(True)
    fuckinglayout(plt)


TEX_CONSTANTS = r"""% autogenerated by plot.py - do not edit
{}
"""


__min_exponent = -2
__reduce_by = 3


def new_command_tex_float(key, value, precision=None):
    key = key[0].upper() + key[1:]
    if type(value) == str:
        return r"\newcommand{{\py{}}}{{{}}}".format(key, value)
    appendix = ""
    reduce = 0
    while unp.log10(np.abs(value)) < __min_exponent:
        reduce -= __reduce_by
        appendix = r"\cdot 10^{%d}" % reduce
        value *= 10**__reduce_by
    try:
        if precision is None:
            err = "{:f}".format(value).split("+/-")
            number = "{}".format(value.n)
        else:
            err = "{:.{prec}f}".format(value, prec=precision).split("+/-")
            number = "{:.{prec}f}".format(value.n, prec=precision)
        number = number.rstrip("0")
        number = number.rstrip(".")
        return (
            r"\newcommand{{\py{}}}{{{}{}}}".format(key, number, appendix)
            + "\n"
            + r"\newcommand{{\py{}Un}}{{({} \pm{{}} {}){}}}".format(
                key, err[0], err[1], appendix
            )
        )
    except AttributeError:
        # there is no uncertainty attached
        return r"\newcommand{{\py{}}}{{{}{}}}".format(key, value, appendix)


def format_tex_float(value, precision=None, always_parenthesis=False):
    if value is None:
        return ""
    try:
        # print("XXX", value, precision)
        if type(precision) is float and type(value) is float:
            exp = np.round(unp.log10(value).item())
            precision = int(abs(unp.log10(precision * 10**exp).item()))
        appendix = ""
        prefix = ""
        if always_parenthesis:
            appendix = ")"
            prefix = "("
        reduce = 0
        try:
            while value and unp.log10(np.abs(value)) < __min_exponent:
                reduce -= __reduce_by
                appendix = r") \cdot 10^{%d}" % reduce
                prefix = r"("
                value *= 10**__reduce_by
        except (ValueError, np.core._exceptions.UFuncTypeError) as e:
            print("XXX", e)
            pass  # unp.log10(un.ufloat(0, N)) throws
        if precision is None:
            err = "{:f}".format(value).split("+/-")
        else:
            err = "{:.{prec}f}".format(value, prec=precision).split("+/-")
        return r"${}{} \pm{{}} {}{}$".format(prefix, err[0], err[1], appendix)
    except (IndexError, ValueError):
        if precision is None:
            f = "{}".format(value)
        else:
            f = "{:.{prec}f}".format(value, prec=precision)
        return prefix + f.rstrip("0").rstrip(".") + appendix


def makeconstants(tex, precision=None):
    with open("constants.tex", "w") as fd:
        __makeconstants(tex, fd, precision)


def __makeconstants(tex, fd, precision):
    pp(tex)
    cs = []
    for key, value in tex.items():
        cs.append(new_command_tex_float(key, value, precision))
    fmt = "\n".join(cs)
    fd.write(TEX_CONSTANTS.format(fmt))


TABLE_TEMPLATE = """\
% usage: \\makeTable{tex}{{<ref>}}
\\newcommand{{\\makeTable{tex}}}[1]{{
\\tableAny{{{name}}}{{{layout}}}{{#1}}{{
{content}
}}
}}
"""


# each entry must be a dict with following keys
#    {
#        "tex": "MacroName", # -tex-> \pyMacroName{}
#        "name": r"Messreihe $T_1$ mit $p_1 < 1\Unit{bar}$",
#        "rowdescription": [r"$T_1 [\degC]$", r"$p_1 [\Unit{mbar}]$"],
#        "content": [ ... ]
#        "precision": 2,  # optional integer precision, or float percentual precision, or arrow of those
#        "multicolumn": 2,  # optional integer for multicolumn
#    }
def maketables(tex_tables):
    tables = _maketables(tex_tables)
    with open("data-tables.tex", "w") as fd:
        fd.write("% autogenerated by plot.py - do not edit\n" + "\n".join(tables))


def _maketables(tex_tables):
    tables = []

    def to_str(entry_or_row):
        try:
            N_entries = len(entry_or_row)
        except TypeError:
            N_entries = 1  # None type entry
        precisions = table["precision"] if "precision" in table else [None] * N_entries
        try:
            return [
                format_tex_float(entry, precision=precisions[row])
                for row, entry in enumerate(entry_or_row)
            ]
        except TypeError:
            return [format_tex_float(entry_or_row, precision=precisions[0])]

    def grouped(iterable, n):
        "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
        return itertools.zip_longest(*[iter(iterable)] * n)

    for table in tex_tables:

        tabcopy = dict(table)
        multicol = 1
        if tabcopy.get("multicolumn"):
            multicol = tabcopy["multicolumn"]
        try:
            length = len(table["content"][0])
        except (TypeError, IndexError):
            length = 1
        tabcopy["layout"] = "|" + "|".join(["r"] * length) + "|"
        tabcopy["layout"] = (tabcopy["layout"] * multicol).replace("||", "|")
        tabcopy["content"] = (
            r"\headerAny{{{}}}".format("&".join(table["rowdescription"] * multicol))
            + "\n"
        )
        tabcopy["content"] += "\n".join(
            [
                r"\entryAny{"
                + "&".join("&".join(to_str(entry)) for entry in entries)
                + r"}"
                for entries in grouped(table["content"], multicol)
            ]
        )
        tables.append(TABLE_TEMPLATE.format(**tabcopy))
    return tables


def mean(ar):
    "calculate the mean of an un.ufloat array"
    return un.ufloat(np.mean(ar).n, np.std([i.n for i in ar]))
