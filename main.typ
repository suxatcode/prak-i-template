// 'Pdf build/main.pdf'
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

= Goal
= Theory
#include "section/theory.typ"
// = Task
// = Preparation
// = Experimental Setup and Experimental Procedure
= Experimental Setup
= Experimental Procedure
= Measurements
= Analysis
= Discussion
