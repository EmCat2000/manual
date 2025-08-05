![Snap! Logo](./images/snap-logo.png)

# The [Snap<em>!</em>][snap] Reference Manual
## [Read at https://docs.snap.berkeley.edu][webiste] (Original PDF)[orginal_pdf]

[![GitHub Pages](https://img.shields.io/badge/website-GitHub%20Pages-blue.svg)](https://docs.snap.berkeley.edu/)

([PDF - coming soon][pdf])
[webiste]: https://docs.snap.berkeley.edu
[pdf]: https://docs.snap.berkeley.edu/snap-manual.pdf
[orginal_pdf]: ./SnapManual.pdf

The reference manual for the [Snap<em>!</em> programming language][snap]. ([GitHub][snap_gh])

[snap]: https://snap.berkeley.edu
[snap_gh]: https://github.com/jmoenig/snap/

## Authors
Brian Harvey, Jens Mönig, Michael Ball, Jadge Hügle, Victoria Phelps

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
quarto render
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
cd conversion
ruby convert-word-doc.rb
```

This conversion script dumps content into `conversion/chapters/` and then copies it into the `content/` folder.

## Published Book

The website is hosted on GitHub pages, compiled by the `quarto.yml` workflow.

## Credits

## License

AGPL, CC-BY-NC-SA
