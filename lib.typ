#let praktikum(
  experimentNo: "experiment number",
  experimentName: "experiment name",
  initVersuchAm: "experiment date",
  authors: ((name: "example author", email: "me@example.com")),
  paper-size: "us-letter",
  body,
) = {
  let title = [V#experimentNo: #experimentName]
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

  // display experiment dates
  align(center, grid(
    columns: 2 * (1fr,),
    gutter: 12pt,
    text(16pt, [Experiment: #initVersuchAm]),
    text(16pt, [Submission: #datetime.today().display()]),
  ))

  // display TU Dortmund things
  v(220pt, weak: true)
  align(center, text(16pt, [TU Dortmund -- Fakultät Physik]))

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

  bibliography("literature.bib", title: "References")
}
#let TODO(body) = {
  text(stroke: red, [TODO: #body])
}
