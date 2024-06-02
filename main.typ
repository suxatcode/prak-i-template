// 'Pdf main.pdf'
#import "./lib.typ": praktikum
#show: praktikum.with(
  experimentNo: "XXX",
  experimentName: "experiment name",
  initVersuchAm: "2024-MM-DD",
  authors: (
    (name: "Laurin Hagemann", email: "laurin.hagemann@udo.edu"),
    (name: "Clara Sondermann", email: "clara.sondermann@udo.edu"),
  ),
)

= Theory
#include "section/theory.typ"
