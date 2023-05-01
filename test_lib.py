import uncertainties as un
import pytest
import io
from lib import new_command_tex_float, __makeconstants, format_tex_float


@pytest.mark.parametrize(
    "constants, expected",
    [
        [
            {"A": 1},
            r"""% autogenerated by plot.py - do not edit
\newcommand{\pyA}{1}
""",
        ],
        [
            {"ok": un.ufloat(1, 0.1)},
            r"""% autogenerated by plot.py - do not edit
\newcommand{\pyOk}{1}
\newcommand{\pyOkUn}{(1.00 \pm{} 0.10)}
""",
        ],
    ],
)
def test___makeconstants(constants, expected):
    fd = io.StringIO()
    __makeconstants(constants, fd)
    assert fd.getvalue() == expected


@pytest.mark.parametrize(
    "key, value, expected",
    [
        [
            "A",
            un.ufloat(1, 0.1),
            r"""\newcommand{\pyA}{1}
\newcommand{\pyAUn}{(1.00 \pm{} 0.10)}""",
        ],
        [
            "A",
            un.ufloat(0.0001, 0.00001),
            r"""\newcommand{\pyA}{0.1\cdot 10^{-3}}
\newcommand{\pyAUn}{(0.100 \pm{} 0.010)\cdot 10^{-3}}""",
        ],
        [
            "A",
            un.ufloat(0.001, 0.0001),
            r"""\newcommand{\pyA}{1\cdot 10^{-3}}
\newcommand{\pyAUn}{(1.00 \pm{} 0.10)\cdot 10^{-3}}""",
        ],
        [
            "A",
            0.0001,
            r"""\newcommand{\pyA}{0.1\cdot 10^{-3}}""",
        ],
        [
            "A",
            un.ufloat(-0.1, 0.01),
            r"""\newcommand{\pyA}{-0.1}
\newcommand{\pyAUn}{(-0.100 \pm{} 0.010)}""",
        ],
        [
            "A",
            "lol",
            r"""\newcommand{\pyA}{lol}""",
        ],
        [
            "A",
            0.000001,
            r"""\newcommand{\pyA}{1.0\cdot 10^{-6}}""",
        ],
    ],
)
def test_new_command_tex_float(key, value, expected):
    assert new_command_tex_float(key, value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        [un.ufloat(0.0001, 0.00001), r"(0.100 \pm{} 0.010) \cdot 10^{-3}"],
        [1.000, r"1.0"],
        [r"abc", r"abc"],
    ],
)
def test_format_tex_float(value, expected):
    assert format_tex_float(value) == expected
