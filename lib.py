import numpy as np
import uncertainties as un
from uncertainties import unumpy as unp
from pprint import pp


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


def new_command_tex_float(key, value):
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
        err = "{:f}".format(value).split("+/-")
        number = "{:f}".format(value.n)
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
        # there is not uncertainty attached
        return r"\newcommand{{\py{}}}{{{}{}}}".format(key, value, appendix)


def format_tex_float(value, always_parenthesis=False):
    if value is None:
        return ""
    try:
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
        except (ValueError, np.core._exceptions.UFuncTypeError):
            pass  # unp.log10(un.ufloat(0, N)) throws
        err = "{:f}".format(value).split("+/-")
        return r"${}{} \pm{{}} {}{}$".format(prefix, err[0], err[1], appendix)
    except (IndexError, ValueError):
        return str(value)


def makeconstants(tex):
    with open("constants.tex", "w") as fd:
        __makeconstants(tex, fd)


def __makeconstants(tex, fd):
    pp(tex)
    cs = []
    for key, value in tex.items():
        cs.append(new_command_tex_float(key, value))
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
#    }
tex_tables = []


def maketables():
    tables = []
    for table in tex_tables:

        def entry_to_str(entry):
            try:
                return [format_tex_float(i) for i in entry]
            except TypeError:
                return [format_tex_float(entry)]

        tabcopy = dict(table)
        try:
            length = len(table["content"][0])
        except (TypeError, IndexError):
            length = 1
        tabcopy["layout"] = "|" + "|".join(["r"] * length) + "|"
        tabcopy["content"] = (
            r"\headerAny{{{}}}".format("&".join(table["rowdescription"])) + "\n"
        )
        tabcopy["content"] += "\n".join(
            [
                r"\entryAny{" + ("&").join(entry_to_str(entry)) + r"}"
                for entry in table["content"]
            ]
        )
        tables.append(TABLE_TEMPLATE.format(**tabcopy))
    with open("data-tables.tex", "w") as fd:
        fd.write("% autogenerated by plot.py - do not edit\n" + "\n".join(tables))


def mean(ar):
    "calculate the mean of an un.ufloat array"
    return un.ufloat(np.mean(ar).n, np.std([i.n for i in ar]))
