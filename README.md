![Snap! Logo](./images/snap-logo.png)

# The Snap<em>!</em> Reference Manual
## [Read at docs.snap.berkeley.edu][website] ([Original PDF][original_pdf])

[![GitHub Pages](https://img.shields.io/badge/website-GitHub%20Pages-blue.svg)](https://docs.snap.berkeley.edu/)

[website]: https://docs.snap.berkeley.edu
[pdf]: https://docs.snap.berkeley.edu/snap-manual.pdf
[original_pdf]: ./SnapManual.pdf

The reference manual for the [Snap<em>!</em> programming language][snap]. ([GitHub][snap_gh])

[snap]: https://snap.berkeley.edu
[snap_gh]: https://github.com/jmoenig/snap/

> [!NOTE]
> The web manual is a "translation" of the original PDF, which was last largely updated for
> Snap<em>!</em> 8. We're first working on the making the web version readable, then we'll
> update the content to match recent Snap<em>!</em> releases.

## Citing Snap! and the Snap! Manual

To cite the _manual_ specifically:

DOI: https://doi.org/10.5281/zenodo.16892852

```
Harvey, B., & Mönig, J. (2022). Snap! Reference Manual. Zenodo. https://doi.org/10.5281/zenodo.16892852
```

```bibtex
@book{harvey_2022_16892853,
  author       = {Harvey, Brian and
                  Mönig, Jens},
  title        = {Snap! Reference Manual},
  publisher    = {Zenodo},
  year         = 2022,
  month        = aug,
  doi          = {10.5281/zenodo.16892852},
  url          = {https://doi.org/10.5281/zenodo.16892852},
}
```
To cite Snap<em>!</em> in general, please use the following citation:

DOI: https://doi.org/10.5281/zenodo.15460068

```
Mönig, J., & Harvey, B. (2025). Snap! (latest). Zenodo. https://doi.org/10.5281/zenodo.15460068
```

```bibtex
@software{monig_2025_15460069,
  author       = {Mönig, Jens and
                  Harvey, Brian},
  title        = {Snap!},
  month        = may,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {latest},
  doi          = {10.5281/zenodo.15460068},
  url          = {https://doi.org/10.5281/zenodo.15460068},
}
```

These DOI's always point to the latest version of the manual and Snap! software, respectively. You can visit Zenodo to cite a specific version if you need to.

## Authors
Brian Harvey, Jens Mönig, Michael Ball, Jadge Hügle, Victoria Phelps, Mary Fries

## Quarto
This version of the Snap! manual is built using [Quarto][quarto].

[quarto]: https://quarto.org/docs/

### Brief installation guide

You need:
* Quarto
* Pandoc
* LaTeX

macOS:
```shell
brew install quarto
brew install pandoc
brew install mactex-no-gui
```

It is also recommended to install the [Quarto VSCode extension][quarto_vscode].

[quarto_vscode]: https://marketplace.visualstudio.com/items?itemName=quarto.quarto

### Building the book

**While writing content:**

```shell
quarto preview
```

This will automatically build the web version and display it in the browser.
Your webpage will automatically refresh as you save changes to files.

**To compile the PDF and final version:**

```shell
quarto render [--to pdf | --to html]
```

## Writing Style

Please read [`STYLEGUIDE.md`](./STYLEGUIDE.md)

## VSCode and Editing

* Use the GitHub Codespace link to edit the book in the browser.
https://quarto.org/docs/visual-editor/vscode/


## Document Conversion
If you are making large updates to the md structure, it may be worth working on the script to convert the Word document to markdown.
The script assumes you have `pandoc` installed and available in your path.

```
cd _support/conversion
ruby convert-word-doc.rb
```

This conversion script dumps content into `conversion/chapters/` and then copies it into the `content/` folder. These have been moved to the top of the repo so the URLs in the compiled site are nicer.

## Published Book

The website is hosted on GitHub pages, compiled by the `quarto.yml` workflow.

## License

AGPL, CC-BY-NC-SA
