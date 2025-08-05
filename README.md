# The Snap*!* Reference Manual
> by Brian Harvey, Jens Mönig

![Snap! Logo](./images/snap-logo.png)

## [Read the Manual][webiste] ([PDF - coming soon][pdf]) (Original PDF)[orginal_pdf]

[![GitHub Pages](https://img.shields.io/badge/website-GitHub%20Pages-blue.svg)](https://snap-cloud.github.io/manual/)


[webiste]: https://snap-cloud.github.io/manual/
[pdf]: https://snap-cloud.github.io/manual/snap-manual.pdf
[orginal_pdf]: ./SnapManual.pdf

The reference manual for the [Snap<em>!</em> programming language][sbe]. ([GitHub][snap_gh])

[sbe]: https://snap.berkeley.edu
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

* The `content/` folder contains the markdown files, organized by chapter.
    * Images sho
* The `blockly/` folder contains 1 markdown file per block, organized by palette.
  * `blocks/images/` one image per block.

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
