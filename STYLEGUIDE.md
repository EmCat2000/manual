# Snap_!_ Manual Style Guide

* Write UI elements inside quoted code blocks. e.g. `"\\`Open\\`"`
* Monospaced text should use the CSS class `.mono` e.g. `[text here]{.mono}`
* Do not put spaces around index entries. `text\index{text},`
* To write Snap! as stylized text write: `[Snap]{.snap}`

## Editing Section References

* Replace original text with a markdown link (e.g. `[text](url)`) with the section name but no page number
* Links should be formatted like the URL, e.g. `../chapter-name`

## Images

Some images do not need custom CSS classes, but images used as inline examples and those expeorted from Retina displays should have CSS classes applied.

* We have two classes: `.image-2x`, and `.image-inline`
* The `-2x` class should be used for most retina-sized images.
* The `-inline` class should be used when you want to place an example within the rest of a paragraph.

Write markdown like this:
```md
![alt text](filename.png){.image-2x}
![alt text](filename.png){.image-inline}
![alt text](filename.png){.image-2x .image-inline}
```

### Making new CSS classes

Add all CSS to the file `snap-manual.scss`. All "image" related CSS should be prefixed with `image-`
* If you need to make a generic generic class, call it something like what it used for
* If you need to make classes for a specific chapter include that, e.g. `image-ch3-...`
* Otherwise you can use `{style="..."}` to manually set the style of a single image

## Callouts
https://quarto.org/docs/authoring/callouts.html

You may want to replace images on text with a callout block.

```md
::: {.callout-tip}
## Tip with Title

This is an example of a callout with a title.
:::
```
