// 'Pdf build/main.pdf'
#import "./lib.typ" as lib
#let lang = "de"
#show: lib.praktikum.with(
  experimentNo: "XXX",
  experimentName: "experiment name",
  initVersuchAm: "2024-MM-DD",
  authors: (
    (name: "Laurin Hagemann", email: "laurin.hagemann@udo.edu"),
    (name: "Clara Sondermann", email: "clara.sondermann@udo.edu"),
  ),
  lang: lang,
)

= #lib.goal.at(lang)
= #lib.theory.at(lang)
#include "section/theory.typ"
// = Task
// = Preparation
// = Experimental Setup and Experimental Procedure
= #lib.expsetup.at(lang)
= #lib.expprocedure.at(lang)
= #lib.measurements.at(lang)
= #lib.analysis.at(lang)
= #lib.discussion.at(lang)
