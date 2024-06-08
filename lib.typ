#let praktikum(
  experimentNo: "experiment number",
  experimentName: "experiment name",
  initVersuchAm: "experiment date",
  authors: ((name: "example author", email: "me@example.com")),
  paper-size: "us-letter",
  lang: "en",
  body,
) = {
  // LaTeX style
  set text(font: "New Computer Modern")
  show raw: set text(font: "New Computer Modern Mono")
  set page(margin: 1.25in)
  set par(leading: 0.55em, first-line-indent: 1.8em, justify: true)
  show par: set block(spacing: 0.55em)
  show heading: set block(above: 1.4em, below: 1em)
  // set document language
  set text(lang: lang)
  // make links blue
  show link: set text(fill: rgb(0, 0, 255))
  // underline links
  show link: underline
  // surround refs with a blue box
  show ref: box.with(stroke: blue, inset: (bottom: 2pt))

  let title = [V#experimentNo: #experimentName]
  // set pdf meta-info
  set document(title: title, author: authors.map(author => author.name))

  // display title
  align(center, text(16pt, experimentNo))
  v(100pt, weak: true)
  align(center, text(24pt, title))
  //v(8.35mm, weak: true)
  v(50pt, weak: true)

  // display authors
  grid(
    columns: 2 * (1fr,),
    gutter: 14pt,
    ..authors.map(author => align(center, {
      text(14pt, author.name)
      [\ #text(14pt, link("mailto:" + author.email))]
    }))
  )
  v(50pt, weak: true)
  let experiment = (
    de: "Experiment am",
    en: "Experiment",
  )
  let submission = (
    en: "Submission",
    de: "Abgabe am",
  )

  // display experiment dates
  align(center, grid(
    columns: 2 * (1fr,),
    gutter: 12pt,
    text(16pt, [#experiment.at(lang): #initVersuchAm]),
    text(16pt, [#submission.at(lang): #datetime.today().display()]),
  ))

  // display TU Dortmund things
  v(220pt, weak: true)
  let fakphys = (
    en: "Faculty of Physics",
    de: "Fakultät Physik",
  )
  align(center, text(16pt, [TU Dortmund -- #fakphys.at(lang)]))

  // display outline
  let appendix(body) = {
    set heading(numbering: "A", supplement: [Appendix])
    body
  }
  set heading(numbering: "1.")
  pagebreak(weak:true)
  outline()
  pagebreak(weak:true)

  // Start two column mode and configure paragraph properties.
  //show: columns.with(2, gutter: 12pt)
  set par(justify: true, first-line-indent: 1em)
  show par: set block(spacing: 0.65em)

  // body and references
  body

  pagebreak(weak:true)

  let references = (
    en: "References",
    de: "Referenzen",
  )
  bibliography("literature.bib", title: references.at(lang))
}
#let TODO(body) = {
  text(stroke: red, [TODO: #body])
}
#let goal = (
  de: "Zielsetzung",
  en: "Goal",
)
#let theory = (
  de: "Theorie",
  en: "Theory",
)
#let expsetup = (
  de: "Versuchsaufbau",
  en: "Experimental Setup",
)
#let expprocedure = (
  de: "Versuchsdurchfuehrung",
  en: "Experimental Procedure",
)
#let measurements = (
  de: "Messwerte",
  en: "Measurements",
)
#let analysis = (
  de: "Auswertung",
  en: "Analysis",
)
#let discussion = (
  de: "Diskussion",
  en: "Discussion",
)
