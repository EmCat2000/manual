---
toc: true
---

# Blocks, Scripts, and Sprites {#sec-ch01}

This chapter describes the [Snap]{.snap} features inherited from Scratch; experienced Scratch users can skip to @sec-sprites-parallelism.

[Snap]{.snap} is a programming language—a notation in which you can tell a
computer what you want it to do. Unlike most programming languages,
though, [Snap]{.snap} is a *visual* language; instead of writing a program
using the keyboard, the [Snap]{.snap} programmer uses the same drag-and-drop
interface familiar to computer users.

Start [Snap]{.snap}. You should see the following
arrangement of regions in the window:

![An annotated screenshot of blank Snap! editor](../12-user-interface-elements/assets/snap-ide-annotated.png)

(The proportions of these areas may be different, depending on the size and shape of your browser window.)

A [Snap]{.snap} program consists of one or more *scripts,* each of which is made of *blocks.* Here’s a typical script
 :

![image6.png](assets/image6.png){#fig-draw-square}

```
(
    (receiveGo) 
    (down) 
    (repeat 4 (
        (move 100) 
        (right 90)
    ))
)
```

The five blocks that make up this script have three different
colors, corresponding to three of the eight *palettes* in which blocks
can be found. The palette area at the left edge of the
window shows one palette at a time, chosen with the eight buttons just
above the palette area. In this script, the gold blocks are from the
Control palette; the green block is from the Pen palette; and the blue
blocks are from the Motion palette. A script is assembled by dragging
blocks from a palette into the *scripting area*
in the middle part of the window. Blocks snap together (hence the name
[Snap]{.snap} for the language) when you drag a block so that its indentation
is near the tab of the one above it:

::: {#fig-snapping-blocks .evenly-spaced-images layout-ncol=2}

![image7.png](assets/image7.png)

![image8.png](assets/image8.png)
:::

```
(
    (receiveGo) 
    (down)
)
```
The white horizontal line is a signal that if you let go of the green
block it will snap into the tab of the gold one.

## Hat Blocks and Command Blocks

At the top of the script is a *hat* block, which indicates when the
script should be carried out. Hat block names typically start with the
word “when”; in the square-drawing example in @fig-draw-square, the script should
be run when the green flag near the right end of the
[Snap]{.snap} tool bar tool bar is
part of the [Snap]{.snap} window, not the same as the browser’s or operating
system’s menu bar.) A script isn’t required to have a hat block
, but if not, then the script will be run only if the
user clicks on the script itself. A script can’t have more than one hat
block, and the hat block can be used only at the top of the script; its
distinctive shape is meant to remind you of
that.[^1]

<!-- TODO: Different CSS for an inline hat block? -->
[^1]: One of the hat blocks, the generic
“when anything” block ![generic when hat block](assets/image10.png){.image-inline #fig-generic-when}
```
(receiveConditionEvent nil)
```
, is subtly different from the others. When the stop
sign is clicked, or when a project or sprite is loaded, this block
doesn’t test whether the condition in its hexagonal input slot is true,
so the script beneath it will not run, until some *other* script in the
project runs (because, for example, you click the green flag). When
generic when blocks are disabled, the stop sign

instead of octagonal. {#para-generic-when}

The other blocks in our example script are *command* blocks

corresponds to an action that [Snap]{.snap} already knows how to carry out.
For example, the block ![image9.png](../blocks/images/block_forward.png){.image-inline} 
```
(move 10)
```
tells the sprite (the arrowhead
shape on the *stage* at the right end of the window) to
move ten steps (a step is a very small unit of distance) in the
direction in which the arrowhead is pointing. We’ll see shortly that
there can be more than one sprite, and that each sprite has its own
scripts. Also, a sprite doesn’t have to look like an arrowhead, but can
have any picture as a *costume.* The shape of the
move block is meant to remind you of a Lego™ brick; a script,
the action, that the block carries out.)

The number 10 in the `move` block above is called an *input* to the block. By
clicking on the white oval, you can type any number in place of the 10.
The sample script on the previous page uses 100 as the input
 value. We’ll see later that inputs can have non-oval
shapes that accept values other than numbers. We’ll also see that you
can compute input values, instead of typing a particular value into the
oval. A block can have more than one input slot. For example, the `glide`
block located about halfway down the Motion palette has three inputs.

Most command blocks have that brick shape, but some, like the `repeat`
block in the sample script, are *C‑shaped.* Most
C-shaped blocks are found
in the Control palette. The slot inside the C
shape is a special kind of input slot that accepts a *script* as the
input.

<!-- TODO-mb: These images are a bit small on the web. -->
::: {.evenly-spaced-images layout-ncol=4}
In the sample script

![image6.png](assets/image6.png)
```
(
    (receiveGo) 
    (down) 
    (repeat 4 (
        (move 100) 
        (right 90)
    ))
)
```
the `repeat` block has two inputs: the number 4 and the script

![image11.png](assets/image11.png)
```
(
    (move 100) 
    (right 90)
)
```

C-shaped blocks can be put in a script in two ways. If you see a white
line and let go, the block will be inserted into the script like any
command block:

::: {.evenly-spaced-images layout-ncol=2}![image12.png](assets/image12.png)

![image13.png](assets/image13.png)
:::
```
(
    (move 100) 
    (repeat 10 nil) 
    (right 90)
)
```

<!-- Note until images are cleaned up 12 and 14 were identical, 13 and 15 were identical. -->

But if you see an orange halo and let go, the block will *wrap* around
the haloed blocks:

{.evenly-spaced-images layout-ncol=2}
![image16.png](assets/image16.png)

![image17.png](assets/image17.png)
```
(
    (move 100) 
    (repeat 10 
        (right 90)
    )
)
```
The halo will always extend from the cursor position to the bottom of
the script:

{.evenly-spaced-images layout-ncol=2}
![image18.png](assets/image18.png)

![image19.png](assets/image19.png)

```
(repeat 10 (
    (move 100) 
    (right 90)
))
```

If you want only some of those blocks, after wrapping you can grab the first block you don’t want wrapped, pull it down, and snap it under the C-shaped block.

For “E-shaped” blocks with more than one C-shaped slot, only the first slot
will wrap around existing blocks in a script, and only if that C-shaped
slot is empty before wrapping. (You can fill the other slots by dragging
blocks into the desired slot.)

![image24.png](assets/image24.png)
```
(ifElse 
    (mouseDown) 
    (sayFor down 2) 
    (sayFor up 2)
)
```

## Sprites and Parallelism {#sec-sprites-parallelism}

Just below the stage is the “new sprite button”
![image25.png](assets/image25.png){.image-inline}. Click the button to add a new sprite to the stage. The new
sprite will appear in a random position on the stage, with a random
color, but always facing to the right.

Each sprite has its own scripts. To see the scripts for a particular
sprite in the scripting area, click on the picture of that sprite in the
*sprite corral* in the bottom right corner of the
window. Try putting one of the following scripts in each sprite’s
scripting area:

::: {.evenly-spaced-images layout-ncol=2}
![image26.png](assets/image26.png)
```
(
    (receiveGo) 
    (repeat 50 
        (right 36)
    )
)
```

![image27.png](assets/image27.png)
```
(
    (receiveGo) 
    (repeat 50 (
        (move 180) 
        (right 180)
    ))
)
```

When you click the green flag, you should see one sprite rotate while
the other moves back and forth. This experiment illustrates the way
different scripts can run in parallel. The turning and the moving happen
together. Parallelism can be seen with multiple
scripts of a single sprite also. Try this example:

::: {.evenly-spaced-images layout-ncol=2}
![image28.png](assets/image28.png)
```
(
    (receiveKey [space]) 
    (forever 
        (move 10)
    )
)
```

![image29.png](assets/image29.png)
```
(
    (receiveKey [space]) 
    (forever 
        (right 15)
    )
)
```

When you click the green flag, the sprite should move back and forth

When you press the space key, the sprite should move forever in a
circle, because the move and turn blocks are run in parallel. (To stop
the program, click the red stop sign at the right end
of the tool bar.)

### Costumes and Sounds

To change the appearance of a sprite, paint or import a new *costume* for it. To paint a costume, click on the Costumes tab above the
scripting area, and click the paint button ![image32.png](assets/image32.png). The *Paint Editor* that
appears is explained in @sec-the-paint-editor. There are three
ways to import a costume. First select the desired sprite in the sprite
corral. Then, one way is to click on the file icon in the tool bar,
then choose ![image30.png](assets/image30.png){.image-inline} the “`Costumes…`” menu item. You will see a list of costumes
from the public media library, and can choose one. The second way, for a
costume stored on your own computer, is to click on the file icon and
choose the “Import…” menu item. You can then select a file in any
picture format (PNG, JPEG, etc.) supported by your browser. The third
way is quicker if the file you want is visible on the desktop: Just drag
the file onto the [Snap]{.snap} window. In any of these cases, the scripting
area will be replaced by something like this:

![image31.png](assets/image31.png)

Just above this part of the window is a set of three tabs: Scripts,
Costumes, and Sounds. You’ll see that the Costumes tab\index{Costumes
tab} is now selected. In this view, the sprite’s *wardrobe,*
 you can choose whether the sprite should wear its
Turtle costume or its Alonzo costume. (Alonzo, the
[Snap]{.snap} mascot, is named after Alonzo Church, a
mathematician who invented the idea of procedures as data
 is
different from Scratch.) You can give a sprite as many costumes as you like, and then choose which it will wear either by
clicking in its wardrobe or by using the 

![image35.png](../blocks/images/block_doSwitchToCostume.png){.image-inline}

```
(wear [Turtle])
```

 or ![Next Costume](../blocks/images/block_doWearNextCostume.png){.image-inline} 

```
(next)
```

block in a script.
(Every costume has a number as well as a name. The `next` costume block
selects the next costume by number; after the highest-numbered costume it
switches to costume 1. The Turtle, costume 0, is never chosen by next
costume.) The Turtle costume is the only one that
changes color to match a change in the sprite’s pen color.

{.callout-tip}
Protip: ![Switch to costumer (() - 1)](assets/image33.png){.image-inline} 
```
(wear 
    (- nil 1)
)
```
switches to the *previous* costume, wrapping like `next costume`.


In addition to its costumes, a sprite can have *sounds;* the equivalent for
sounds of the sprite’s wardrobe is called its *jukebox.*
Sound files can be imported in any format
(WAV, OGG, MP3, etc.) supported by your browser. Two blocks accomplish
the task of playing sounds. If you would like a
script to continue running while the sound is playing, use the block ![image39.png](assets/image39.png)
```
(play nil)
```
.
In contrast, you can use the block ![image38.png](assets/image38.png)
```
(playAll nil)
```
 to wait for the sound's completion
before continuing the rest of the script.

### Inter-Sprite Communication with Broadcast

Earlier we saw an example of two sprites moving at the same time. In a
more interesting program, though, the sprites on stage will *interact*
to tell a story, play a game, etc. Often one sprite will have to tell
another sprite to run a script. Here’s a simple example:

::: {#fig-broadcast-dog .evenly-spaced-images layout-ncol=4}

![image41.png](assets/image41.png)

![image42.png](assets/image42.png)
```
(
    (receiveGo) 
    (sayFor "Hi! What's your name?" 2) 
    (sendAll bark) 
    (sayFor "Hi, Woof!  What do you like to do?" 2) 
    (sendAll bark) 
    (sayFor "What a coincidence" 2)
)
```

![image43.png](assets/image43.png)

![image44.png](assets/image44.png)
```
(
    (receiveMessage bark) 
    (sayFor Woof! 2)
)
```

In the block ![image40.png](assets/image40.png){.image-inline}
```
(sendAll bark)
```
, the word “bark” is just an arbitrary name I made up. When you
click on the downward arrowhead in that input slot, one of the choices
(the only choice, the first time) is “new,” which then prompts you to
enter a name for the new broadcast. When this block is run, the chosen
message is sent to *every* sprite, which is why the block is called
“broadcast.” (But if you click the right arrow after the message name,
the block becomes ![image45.png](assets/image45.png){.image-inline}
```
(sendAll bark all)
```
, and you can change it to ![image46.png](assets/image46.png){.image-inline}
```
(sendAll bark dog)
```
 to send the message just
to one sprite.) In this program, though, only one sprite has a script to
run when that broadcast is sent, namely the dog. Because the boy’s
script uses `broadcast and wait` rather
than just broadcast, the boy doesn’t go on to his next say block until
the dog’s script finishes. That’s why the two sprites take turns
talking, instead of both talking at once. In @sec-ch07 you’ll see a more flexible
way to send a message to a specific sprite using the tell and ask
blocks.

Notice, by the way, that the say block’s first input slot is rectangular
rather than oval. This means the input can be any text string, not only
a number. In text input slots, a space character is
shown as a brown dot, so that you can count the
number of spaces between words, and in particular you can tell the
difference between an empty slot and one containing spaces. The brown
dots are *not* shown on the stage if the text is displayed.

The stage has its own scripting area. It can be selected by clicking on
the Stage icon at the left of the sprite corral. Unlike a sprite,
though, the stage can’t move. Instead of costumes, it has *backgrounds:*
pictures that fill the entire stage area. The sprites appear in front of
the current background. In a complicated project, it’s often convenient
to use a script in the stage’s scripting area as the overall director of
the action.

## Nesting Sprites: Anchors and Parts

Sometimes it’s desirable to make a sort of “super-sprite” composed of
pieces that can move together but can also be separately articulated.
The classic example is a person’s body made up of a torso, limbs, and a
head. [Snap]{.snap} allows one sprite to be designated as the *anchor*
 of the combined shape, with other sprites as its *parts.*


To set up sprite nesting , drag the sprite corral icon of a *part* sprite
onto the stage display (not the sprite corral icon!) of the desired
*anchor* sprite. The precise place where you let go of the mouse button
will be the attachment point of the part on the anchor.

Sprite nesting is shown in the sprite corral icons of both anchors and parts:
![image47.png](assets/image47.png) <!-- {width=1.63056in height=0.96528in} -->

In
this illustration, it is desired to animate Alonzo’s arm. (The arm has
been colored green in this picture to make the relationship of the two
sprites clearer, but in a real project they’d be the same color,
probably.) Sprite, representing Alonzo’s body, is the anchor; Sprite(2)
is the arm. The icon for the anchor shows small images of up to three
attached parts at the bottom. The icon for each part shows a small image
of the anchor in its top left corner, and a *synchronous*
 *dangling rotation*\index{dangling
rotation} *flag* in the top right corner. In its initial, synchronous
setting, as shown above, it means that the when the anchor sprite
rotates, the part sprite also rotates as well as revolving around the
anchor. When clicked, it changes from a circular arrow to a straight
arrow, and indicates that when the anchor sprite rotates, the part
sprite revolves around it, but does not rotate, keeping its original
orientation. (The part can also be rotated separately, using its turn
blocks.) Any change in the position or size of the anchor is always
extended to its parts. Also, cloning the anchor (see Section VII. B)
will also clone all its parts.

![image56.png](assets/image56.png) <!-- {width=1.44444in height=1.5625in} --> 
```
(
    (repeat 3 (
        (right 20) 
        (wait 0.05)
    )) 
    (repeat 3 (
        (left 20) 
        (wait 0.05)
    ))
)
```
![image48.png](assets/image48.png) <!-- {width=1.63056in height=0.96528in} -->
![image49.png](assets/image49.png) <!-- {width=1.63056in height=0.96528in} -->

*Top: turning the part: the green arm. Bottom: turning the anchor, with
the arm synchronous (left) and dangling (right).*

## Reporter Blocks and Expressions

So
far, we’ve used two kinds of blocks: hat blocks
and command blocks. Another kind is the *reporter* block,\index{Reporter
block} which has an oval shape: ![image66.png](assets/image66.png) <!-- {width=0.72917in height=0.15625in} --> 
```
(x)
```
. It’s called a “reporter” because
when it’s run, instead of carrying out an action, it reports a value
that can be used as an input to another block. If you drag a ![image65.png](assets/image65.png){.image-inline} <!-- {width=1.47in height=0.52in} --> reporter
into the scripting area by itself and click on it, the value it reports
will appear in a speech balloon next to the block:

When you drag a reporter block over another block’s input slot, a white
“halo ” appears around that input slot, analogous to the
white line that appears when snapping command blocks together:

![image67.png](assets/image67.png) <!-- {width=1.47in height=0.52in} -->
```
(move 
    (+ 5 2)
)
```

Don’t drop the input over a *red* halo:
![image71.png](assets/image71.png) <!--  style="width:2.11111in;height:0.61806in" alt="Macintosh HD:Users:bh:Desktop:Google Chrome001.png" / -->
```
(join : 
    (list 7 8 1)
)
```

That’s used for a purpose explained in @sec-recursive-calls-to-multiple-input-blocks.

Here’s a simple script that uses a reporter block:

![image72.png](assets/image72.png) <!--  style="width:2.11111in;height:0.61806in" alt="Macintosh HD:Users:bh:Desktop:Google Chrome001.png" / -->
```
(
    (receiveGo) 
    (forever (
        (move 10) 
        (right 15) 
        (sayFor 
            (+ 
                (round 
                    (x)
                ) 100
            ) 2
        )
    ))
)
```

Here the `x position` reporter provides the first input to the say block.
(The sprite’s X position is its horizontal position,
how far left (negative values) or right (positive values) it is compared
to the center of the stage. Similarly, the Y position
is measured vertically, in steps above (positive) or below (negative)
the center.)

You can do arithmetic using reporters in the
Operators palette:

![image73.png](assets/image73.png) <!--  style="width:2.11111in;height:0.61806in" alt="Macintosh HD:Users:bh:Desktop:Google Chrome001.png" / -->
```
(
    (receiveGo) 
    (forever (
        (move 10) 
        (right 15) 
        (sayFor 
            (+ 
                (round 
                    (x)
                ) 100
            ) 2
        )
    ))
)
```

The `round` block rounds 35.3905… to 35, and the `+` block adds 100 to that.
(By the way, the `round` block is in the Operators palette, just like `+`,
but in this script it’s a lighter color with black lettering because
[Snap]{.snap} alternates light and dark versions of the palette colors when a
block is nested inside another block from the same palette:

![image80.png](assets/image80.png) <!-- {width=4.85417in height=1.90625in} -->
```
(repeat 10 
    (if 
        (and 
            (< 
                (x) nil
            ) 
            (= 
                (y) nil
            )
        ) 
        (repeat 4 (
            (move 
                (* 
                    (+ 5 
                        (+ 2 3)
                    ) 
                    (- 
                        (* 3 
                            (- 2 
                                (fn [sqrt] nil)
                            )
                        ) 5
                    )
                )
            ) 
            (right 
                (join 
                    (* 3 3) 0
                )
            )
        ))
    )
)
```

This
aid to readability is called *zebra coloring.*
A reporter block with its inputs, maybe including other reporter
blocks, such as ![image81.png](assets/image81.png) <!-- {width=1.91667in height=0.23958in} -->
```
(+ 
    (round 
        (x)
    ) 100
)
```
, is called an *expression.*

##  Predicates and Conditional Evaluation {#sec-sec-predicates-and-conditional-evaluation}

Most reporters report
```
(+ nil nil)
```
,
or a text string, like
![image83.png](../blocks/images/block_reportJoinWords.png){.image-inline}
```
(join "hello " world)
```
.
A *predicate* is a special kind of reporter that
always reports true or false. Predicates have a
hexagonal shape
```
(mouseDown)
```

The special shape is a reminder that predicates don’t generally make sense
in an input slot of blocks that are expecting a number or text. You
wouldn’t say ![image84.png](assets/image84.png)
```
(move 
    (mouseDown)
)
```
, although (as you can see from the picture) [Snap]{.snap} lets
you do it if you really want. Instead, you normally use predicates in
special hexagonal input slots like this one:

![image86.png](../blocks/images/block_doIf.png){.image-4x}
```
(if nil nil)
```

The C-shaped if block runs its input script if (and only
if) the expression in its hexagonal input reports true.
![image87.png](assets/image87.png)
```(if 
    (< 
        (y) 0
    ) 
    (say "I'm below the middle!")
)

```

A really useful block in animations
 runs its input script *repeatedly* until a predicate
is satisfied: ![image89.png](assets/image89.png)
```
(
    (face Sprite2) 
    (until 
        (touch Sprite2) 
        (move 3)
    )
)
```

If, while working on a project, you want to omit temporarily some commands
in a script, but you don’t want to forget where they belong, you can say

![image88.png](assets/image88.png) <!-- {width=2.28194in height=1.46875in} -->
```
(
    (move 10) 
    (right 15) 
    (if 
        (bool f) (
        (sayFor "I'm no going to do this" 2) 
        (glide 1 0 0)
    )
    ) 
    (head 90)
)
```

Sometimes you want to take the same action whether some condition is
true or false, but with a different input value. For this purpose you
can use the *reporter* `if` block :

![image90.png](assets/image90.png) <!-- {width=4.20833in height=0.38542in} -->
```
(say 
    (join "I'm on the " 
        (ifThen 
            (< 
                (x) 0
            ) left right
        )
    )
)
```

The technical term for a true or false value is a “Boolean ”
value; it has a capital B because it’s named after a person, George
Boole, who developed the mathematical theory of
Boolean values. Don’t get confused; a hexagonal block is a *predicate,*
but the value it reports is a *Boolean.*

Another quibble about vocabulary: Many programming languages reserve the
name “procedure” for Commands (that carry out an
action) and use the name “function” for Reporters and Predicates. In
this manual, a *procedure* is any computational capability, including
those that report values and those that don’t. Commands, Reporters, and
Predicates are all procedures. The words “a Procedure type” are
shorthand for “Command type, Reporter type, or Predicate type.”

If you want to put
a *constant* Boolean value in a hexagonal slot
instead of a predicate-based expression, hover the mouse over the block
and click on the control that appears:

![image91.png](assets/image91.png){.image-inline} <!--  style="width:1.375in;height:0.24306in" alt="Macintosh HD:Users:bh:Desktop:turbo-false.png" / --> 
```
(global= "[turbo mode]" f)
```
![image92.png](assets/image92.png){.image-inline} <!--  style="width:1.375in;height:0.24306in" alt="Macintosh HD:Users:bh:Desktop:turbo-true.png" / -->
```
(global= "[turbo mode]" t)
```

## Variables

Try
this script:
![image93.png](assets/image93.png) <!-- {width=1.58333in height=1.41667in} -->
```
(
    (receiveGo) 
    (down) 
    (for i 1 200 (
        (move 
            (get i)
        ) 
        (right 92)
    ))
)
```

The
input to the move block is an orange oval. To get it there, drag the
orange oval that’s part of the `for` block :
![image94.png](assets/image94.png) <!-- {width=1.88542in height=1.4375in} -->
```
(
    (receiveGo) 
    (down) 
    (for i 1 10 
        (move 
            (get i)
        )
    )
)
```

The orange oval is a *variable:* a symbol that
represents a value. (I took this screenshot before changing the second
number input to the `for` block from the default 10 to 200, and before
dragging in a `turn` block.)
`For` runs its script input repeatedly, just
like `repeat`, but before each repetition it sets the variable
 <var>i</var> to a number starting with its first numeric input,
adding 1 for each repetition, until it reaches the second numeric input.
In this case, there will be 200 repetitions, first with <var>i</var>=1, then with
<var>i</var>=2, then <var>i</var>=3, and so on until <var>i</var>=200 for the final repetition. The result
is that each move draws a longer and longer line segment, and that’s why
the picture you see is a kind of spiral. (If you try again with a turn
of 90 degrees instead of 92, you’ll see why this picture is called a
“squiral.”)

The
variable <var>i</var> is created by the `for` block, and it can only be used in the
script inside the block’s C-slot. (By the way, if you don’t like the
name <var>i</var>, you can change it by clicking on the orange oval without
dragging it, which will pop up a dialog window in which you can enter a
different name:
![image95.png](assets/image95.png) <!-- {width=3.1875in height=1.5in} -->

“<var>I</var>” isn’t a very descriptive name; you might prefer “length” to indicate
its purpose in the script. “<var>I</var>” is traditional because mathematicians
tend to use letters between <var>i</var> and <var>n</var> to represent integer values, but in
programming languages we don’t have to restrict ourselves to
single-letter variable names.)

### Global Variable

You can create variables “by hand” that aren’t limited to being used
within a single block. At the top of the Variables palette, click the
“Make a variable” button:

![image97.png](assets/image97.png) <!-- {width=2.05208in height=2.27083in} -->

This will bring up a dialog window in which you can give your variable a
name:

![image96.png](assets/image96.png) <!-- {width=3.1875in height=1.84375in} -->

The dialog also gives you a choice to make the variable available to all
sprites (which is almost always what you want) or to make it visible
only in the current sprite. You’d do that
if you’re going to give several sprites individual variables *with the
same name,* so that you can share a script between sprites (by dragging
it from the current sprite’s scripting area to the picture of another
sprite in the sprite corral), and the different sprites will do slightly
different things when running that script because each has a different
value for that variable name.

If
you give your variable the name “name” then the Variables palette will
look like this:

![image98.png](assets/image98.png) <!-- {width=1.65833in height=2.29167in} -->

There’s
now a “Delete a variable” button, and there’s
an orange oval with the variable name in it, just like the orange oval
in the for block. You can drag the variable into any script in the
scripting area. Next to the oval is a checkbox, initially checked. When
it’s checked, you’ll also see a *variable watcher*\index{variable
watcher} on the stage: ![image99.png](assets/image99.png) <!-- {width=1.04167in height=0.40625in} -->

When you give the variable a value, the orange box in its watcher
 will display the value.

How *do* you give it a value?
You use the `set` block :
![image100.png](assets/image100.png) <!-- {width=1.92708in height=0.47917in} -->
```
(
    (doAsk "what's your name?") 
    (set name 
        (answer)
    )
)
```

Note that you *don’t* drag the variable’s oval into the `set` block! You
click on the downarrow in the first input slot, and you get a menu of
all the available variable names.

If you do choose “For this sprite only ”
when creating a variable, its block in the palette looks like this:![image101.png](assets/image101.png) <!--  style="width:0.65833in;height:0.14167in" alt="Macintosh HD:Users:bh:Desktop:local-var.png" / -->
```
(get variable)
```

The *location*-pin
 icon is a bit of a pun on a sprite-*local* variable
. It’s shown only in the palette.

### Script Variables

In the name example above, our project is going to carry on an
interaction with the user, and we want to remember
their name throughout the project. That’s a good example of a situation
in which a *global* variable (the kind you make
with the “Make a variable” button) is appropriate. Another common
example is a variable called “score” in a game project. But sometimes
you only need a variable temporarily,
during the running of a particular script. In that case you can use the
script variables block to make the
variable:

![image105.png](assets/image105.png) <!-- {width=2.08333in height=0.30208in} -->
```
(
    (receiveGo) 
    (var wiggle) 
    (set wiggle 
        (rand 1 10)
    ) 
    (down) 
    (move 50) 
    (left 
        (* 5 
            (get wiggle)
        )
    ) 
    (move 50) 
    (right 
        (* 5 
            (get wiggle)
        )
    ) 
    (move 50)
)
```

As in the `for` block, you can click on an orange oval in the script
variables block without dragging to change its name. You can also make
more than one temporary variable by clicking on the right arrow at the
end of the block to add another variable oval:

![image106.png](assets/image106.png) <!-- {width=2.08333in height=0.30208in} -->
```
(var a b c)
```

### Renaming variables

There are several reasons why you might want to change the name of a
variable:

1.  It has a default name, such as the <var>a</var> in script variables or the
    <var>i</var> in the `for` block.

2.  It conflicts with another name, such as a global variable, that you
    want to use in the same script.

3.  You just decide a different name would be more self-documenting.

In the first and third case, you probably want to change the name
everywhere it appears in that script, or even in all scripts. In the
second case, if you’ve already used both variables in the script before
realizing that they have the same name, you’ll want to look at each
instance separately to decide which ones to rename. Both of these
operations are possible by right-clicking or control-clicking on a
variable oval.

If you right-click on an
orange oval in a context in which the variable is *used,* then you are
able to rename just that one orange oval:

![image104.png](assets/image104.png) <!-- {width=2.08333in height=0.30208in} -->

If you right-click on the
place where the variable is *defined* (a script variables block, the
orange oval for a global variable in the Variables palette, or an orange
oval that’s built into a block such as the “i” in for), then you are
given two renaming options, “rename” and “rename all.” If you choose
“rename,” then the name is changed only in that one orange oval, as in
the previous case:

![image103.png](assets/image103.png) <!-- {width=2.08333in height=0.30208in} -->

But if you choose “rename
all,” then the name will be changed throughout the scope of the variable
(the script for a script variable, or everywhere for a global variable):



### Transient variables

So far we’ve talked about
variables with numeric values, or with short text strings such as
someone’s name. But there’s no limit to the amount of information you
can put in a variable; in Chapter IV you’ll see how to use *lists* to
collect many values in one data structure, and in Chapter VIII you’ll
see how to read information from web sites.

![image102.png](assets/image102.png) <!-- {width=2.08333in height=0.30208in} -->

When you use these
capabilities, your project may take up a lot of memory in
the computer. If you get close to the amount of memory available to
[Snap]{.snap}, then it may become impossible to save your project. (Extra
space is needed temporarily to convert from [Snap]{.snap}’s internal
representation to the form in which projects are exported or saved.) If
your program reads a lot of data from the outside world that will still
be available when you use it next, you might want to have values
containing a lot of data removed from memory before saving the project.
To do this, right-click or control-click on the orange oval in the
Variables palette, to see this menu: ![image114.png](assets/image114.png) <!-- {width=1.29167in height=1.05556in} -->

You already know about the rename options, and "help…" displays a help
screen about variables in general. Here we’re interested in the check
box next to transient. If you check it, this variable’s value will not
be saved when you save your project. Of course, you’ll have to ensure
that when your project is loaded, it recreates the needed value and sets
the variable to it.

## Debugging

[Snap]{.snap} provides several tools to help you debug a program. They center
around the idea of *pausing* the running of a script partway through, so
that you can examine the values of variables.

### The pause button

The simplest way to pause a
program is manually, by clicking the pause button ![image116.png](assets/image116.png) <!-- {width=0.29167in height=0.16667in} -->
in the top right corner of the window. While the program is paused, you
can run other scripts by clicking on them, show variables on stage with
the checkbox next to the variable in the Variables palette or with the
`show variable`block, and do all the other
things you can generally do, including modifying the paused scripts by
adding or removing blocks. The ![image115.png](assets/image115.png) <!-- {width=0.29167in height=0.16667in} -->  button changes shape too and clicking it
again resumes the paused scripts.

### Breakpoints

The pause button is great if your program seems to be in an infinite loop,
but more often you’ll want
to set a *breakpoint,* a particular point in a script at which you want
to pause. The ![image117.png](../blocks/images/block_doPauseAll.png){.image-inline} block
```
(pause)
```
, near the bottom of the Control palette, can be
inserted in a script to pause when it is run. So, for example, if your
program is getting an error message in a particular block, you could use
`pause all` just before that block to look at the values of variables just
before the error happens.

The `pause all` block turns
bright cyan while paused. Also, during the pause, you can right-click on
a running script and the menu that appears will give you the option to
show watchers for temporary variables of the script:

![image118.png](assets/image118.png)
```
(
    (var foo bar) 
    (set foo -5) 
    (pause) 
    (move 
        (get foo)
    )
)
```
But what if the block with the error is run many times in a loop, and it
only errors when a particular condition is true — for example, when the value of some
variable is negative, which shouldn’t ever happen. In the iteration
library (see @sec-libraries-intro for more about how to use
libraries) is a breakpoint block that lets you set a *conditional*
breakpoint, and automatically display the relevant variables before pausing. Here’s a sample use of it:

![image119.png](assets/image119.png) <!-- {width=1.19444in height=1.33333in} -->
```
(
    (var foo bar) 
    (set foo 0) 
    (if 
        (< 
            (get foo) 0
        ) (
        (showVar foo) 
        (showVar bar) 
        (pause)
    )
    ) 
    (move 
        (get foo)
    )
)
```
(In this contrived example,
variable <var>zot</var> comes from outside the script but is relevant to its
behavior.) When you continue (with the pause button), the temporary
variable watchers are removed by this breakpoint block before resuming
the script. The breakpoint block isn’t magic; you could alternatively
just put a `pause all` inside an `if`.[^2]

[^2]: The hide variable and show variable
block s can also be used to hide and show
primitives in the palette. The pulldown
menu doesn’t include primitive blocks, but there’s a generally useful
technique to give a block input values it wasn’t expecting using run or
call:![image120.png](assets/image120.png) <!-- {width=3.9375in height=0.38889in} -->
```
(run 
    (cmd 
        (hideVar nil)
    ) 
    (cmd 
        (move 10)
    )
)
```
<br>
In order to use a block as an input this way, you must explicitly put a
ring around it, by right-clicking on it and choosing ringify. More about
rings in Chapter VI.

### Visible stepping

Sometimes you’re not exactly sure where the error is, or you don’t
understand how the program got there. To understand better, you’d
like to watch the program as it runs, at human speed rather than
at computer speed. You can do this by
clicking the *visible stepping* --> ), before running a script or
while the script is paused. The button will light up ( ![image123.png](assets/image123.png) <!-- {width=0.29167in height=0.16667in} --> ) and a speed
control slider ![image122.png](assets/image122.png) <!-- {width=0.54563in height=0.15278in} --> will appear in the toolbar. When you start or continue
the script, its blocks and input slots will light up cyan one at a time:

![image124.png](assets/image124.png) <!-- {width=0.54563in height=0.15278in} -->

In this simple example, the inputs to the blocks are constant values,
but if an input were a more complicated expression involving several
reporter blocks, each of those would light up as they are called. Note
that the input to a block is evaluated before the block itself is
called, so, for example, the 100 lights up before the move.

The speed of stepping is
controlled by the slider. If you move the
slider all the way to the left, the speed is zero, the pause button
turns into a step button ![image134.png](assets/image134.png) <!-- {width=0.29167in height=0.16667in} --> , and the script takes a single step each time
you push it. The name for this is *single stepping.*\index{single
stepping}

If several scripts that are visible in the scripting area are running at
the same time, all of them are stepped in parallel. However, consider
the case of two repeat loops with different numbers of blocks. While not
stepping, each script goes through a complete cycle of its loop in each
display cycle, despite the difference in the length of a cycle. In order
to ensure that the visible result of a program on the stage is the same
when stepped as when not stepped, the shorter script will wait at the
bottom of its loop for the longer script to catch up.

When we talk about custom blocks in @sec-ch03, we’ll have more to say
about visible stepping as it affects those blocks.

## Etcetera

This manual doesn’t (yet)explain every block in detail. There are many more
motion blocks, sound blocks, costume and graphics effects blocks, and so
on. If you would like to find information on specific blocks, go to @sec-all-blocks. You can also learn what they all do by experimentation, and by
reading the “help screens” that you can get by right-clicking or
control-clicking a block and selecting “`help…`” from the menu that
appears. If you forget what palette (color) a block is, but you remember
at least part of its name, type <kbd>control-F</kbd> and enter the name in the text block that appears in the palette area.

Here are some of the primitive blocks that don’t exist in Scratch:

![image136.png](assets/image136.png)
```
(trails)
```
reports\index{pen trails
block}, a new costume consisting of everything
that’s drawn on the stage by any sprite. Right-clicking the block in the
scripting area gives the option to change it to ![image135.png](assets/image135.png)
```
(svgTrails)
```
if vector logging is enabled. See @para-log-pen-vectors.

![image137.png](assets/image137.png){.image-inline} Print
characters
```
(write Hello! 12)
```
 in the given point size on the stage, at
the sprite’s position and in its direction. The sprite moves to the end
of the text. (That’s not always what you want, but you can save the
sprite’s position before using it, and sometimes you need to know how
big the text turned out to be, in turtle steps.) If the pen is down, the
text will be underlined.

![image138.png](assets/image138.png){.image-inline}
```
(paste nil)
```

Takes a sprite as input. Like stamp except that the costume is stamped onto the selected sprite instead of onto the stage. (Does nothing if the current sprite doesn’t overlap the chosen sprite.)

![image139.png](assets/image139.png){.image-inline}
```
(cut nil)
```

Takes a sprite as input. Erases from that sprite’s costume the area that overlaps with the current sprite’s costume. (Does not affect the costume in the chosen sprite’s wardrobe, only the copy currently visible.)

![image142.png](assets/image142.png){.image-inline} See @fig-generic-when.
```
(receiveConditionEvent nil)
```

![image141.png](assets/image141.png){.image-inline} See @sec-pause-all.
```
(pause)
```

![image140.png](assets/image140.png){.image-inline} Runs only this script until finished. In the Control palette even though it’s gray.
```
(warp nil)
```

![image143.png](assets/image143.png){.image-inline} <!--  style="width:1.71in;height:0.23in" alt="Macintosh HD:Users:bh:Desktop:pix:reporter-if.png" / --> 
```
(playAll nil)
```
Reporter
version of the `if/else` primitive command block\index{if else reporter
block} . Only one of the two branches is evaluated, depending on the
value of the first input.

![image144.png](assets/image144.png){.image-inline} <!--  style="width:1.83in;height:0.61in" alt="Macintosh HD:Users:bh:Desktop:pix:for.png" / -->
```
(ifThen nil nil nil)
```
Looping block like
`repeat` but with an index variable\index{index
variable} .

![image145.png](assets/image145.png){.image-inline} <!--  style="width:1.37986in;height:0.28958in" alt="Graphical user interface, application, logo Description automatically generated" / --> 
```
(var a)
```
Declare
local variables in a script.\index{script
variables block}

![image148.png](assets/image148.png){.image-inline} See @sec-ch09.
```
(url snap.berkeley.edu)
```

![image146.png](assets/image146.png){.image-inline} reports the value of a graphics effect.
```
(effect [ghost])
```

![image147.png](assets/image147.png){.image-inline} Constant true value. See @sec-predicates-and-conditional-evaluation.
```
(bool t)
```

![image149.png](assets/image149.png){.image-inline}
```
(shown)
```

```
(down?)
```

![image153.png](assets/image153.png){.image-inline}
```
(js nil nil)
```

Create a primitive using JavaScript. (This block is
disabled by default; the user must check “Javascript extensions” in the
setting menu *each time* a project is loaded.)

::: {.evenly-spaced-images layout-ncol=2}
![image150.png](assets/image150.png){.image-inline}
```
(aspect [hue] nil)
```

The `at` block directly behind the rotation center of a sprite, the mouse, or an arbitrary (x,y) coordinate pair dropped onto the second menu slot. The first five items of the left menu let you examine the
color visible at the position. (The “RGBA” option reports a list.) The “sprites” option reports a list of all sprites, including this one, any point of which overlaps this sprite’s rotation center (behind or in front). This is a hyperblock with respect to its second input.
:::

<!-- This needs 2 columns ??? -->
![image154.png](assets/image154.png){.image-4x}

Checks the of a value.

<!-- These two need to be remade as text -->
![image151.png](assets/image151.png){.image-4x}

```
```

![image152.png](assets/image152.png){.image-4x}

```

```

::: {layout-ncol=2}
![image155.png](assets/image155.png){.image-4x}

```

```

Turn the text into a list, using the second input as the delimiter between items. The default
delimiter, indicated by the brown dot in the input slot, is a single space character. “Letter” puts each character of the text in its own list item. “Word” puts each word in an item. ( (0xd). “Csv”
 split formatted text into lists of lists; see @sec-csv. “Blocks”
takes a script as the first input, reporting a list structure  representing the structure of the script. See Chapter XI.
:::

![image170.png](assets/image170.png){.image-inline} 
```

```
For lists,
 reports true only if its two input values are the
very same list, so changing an item in one of them is visible in the
other. (For `=`, lists that look the same are the same.) For text strings,
uses case-sensitive comparison, unlike `=`, which is case-independent.

![image171.png](assets/image171.png){.image-inline}
```

```
 These *hidden* blocks can be found with the relabel option
 of any dyadic arithmetic block. They’re hidden
partly because writing them in [Snap]{.snap} is a good, pretty easy
programming exercise. Note: the two inputs to `atan2`
are Δ*x* and Δ*y* in that order, because we measure angles clockwise
from north. `max` /index{max block} and `min` /index{min block} are *variadic;* by clicking the arrowhead, you
can provide additional inputs.

![image177.png](assets/image177.png){.image-inline} 
```

```
![image178.png](assets/image178.png){.image-inline} 
```

```
![image179.png](assets/image179.png){.image-inline}
```

```

Similarly, these hidden predicates can be found by relabeling the relational predicates.

### Metaprogramming (see @sec-ch11)

![image172.png](assets/image172.png)
```

```

These blocks support *metaprogramming,* which means manipulating blocks
and scripts as data. This is not the same as manipulating procedures
(see @sec-ch06), which are what the blocks *mean;* in metaprogramming
the actual blocks, what you see on the screen, are the data. This
capability is new in version 8.0.

### First class list blocks (see @sec-ch04):

<!-- TODO: welp. this needs to be remade -->
![image173.png](assets/image173.png)
```

```

`Numbers from` will
count up or down.

![image224.png](assets/image224.png){.image-inline} ![image225.png](assets/image225.png){.image-inline}
report
```

```
the sprite or mouse position as a two-item
vector (x,y).

**First class procedure blocks (see @sec-ch06):**
 ![image226.png](assets/image226.png)
```

```

**First class continuation blocks (see @sec-ch10):**
 ![image227.png](assets/image227.png)
```

```

**First class sprite, costume, and sound blocks (see @sec-ch07):**

 ![image228.png](assets/image228.png)
```

```

 ![image229.png](assets/image229.png)
```

```

 Object is a hyperblock.

**Scenes:**

![image280.png](assets/image280.png){.image-2x}
```

```

The major new feature of version 7.0 is *scenes:* A project can include
within it sub-projects, called scenes, each with its own stage, sprites,
scripts, and so on. This block makes another scene active, replacing the
current one.

Nothing is automatically shared between scenes: no sprites, no blocks,
no variables. But the old scene can send a message to the new one, to
start it running, with optional payload as in broadcast\index{broadcast
block} (See @sec-broadcast).

![image282.png](assets/image282.png){.image-4x}
```

```

In particular, you can say

![image281.png](assets/image281.png){.image-4x}
```

```

if the new scene expects to be started with a green flag signal.

***These aren’t new blocks but they have a new feature:***
These accept two-item (x,y) lists
 as input, and have extended menus (also
including other sprites):

![image283.png](assets/image283.png)
```

```

“Center” means the center of the stage, the
point at (0,0). “Direction” is in the point in direction sense, the
direction that would leave this sprite pointing toward another sprite,
the mouse, or the center. “Ray length” is the distance from the center
of this sprite to the nearest point on the other sprite, in the current
direction.

![image284.png](assets/image284.png){.image-4x}
```

```
The `stop` block has two extra menu choices. `Stop this block` is used inside the definition of a custom block to stop just this
invocation of this custom block and continue the script that called it.
`Stop all` but this script is good at the end of a game to stop all the
game pieces from moving around, but keep running this script to provide
the user’s final score. The last two menu choices add a tab at the
bottom of the block because the current script can continue after it.

![image285.png](assets/image285.png){.image-2x}
```

```

The new “pen trails” option is true if the sprite is touching any drawn
or stamped ink on the stage. Also, `touching` will
not detect hidden sprites, but a hidden sprite can use it to detect
visible sprites.

![image305.png](assets/image305.png){.image-inline} <!--  style="width:2.43333in;height:0.3in" alt="Macintosh HD:Users:bh:Desktop:video-on.png" / --> 
```

```
The `video on` block
 that takes a
snapshot and reports it as a costume. It is hyperized with respect to its second input.

:::{.evenly-spaced-images layout-ncol=2}
![image306.png](assets/image306.png){.image-inline}
```

```

![image304.png](assets/image304.png){.image-inline} 
```

```
The “neg” option is a monadic\index{of block
(operators)} negation operator
, equivalent to “lg” is log<sub>2</sub>.
“id” is the identity function, which reports its input. “sign” reports 1
for positive input, 0 for zero input, or -1 for negative input.

:::

<!-- ::: {.callout-tip} -->
<!-- ## Two Different Length Of Blocks -->

The ![length of text block](../blocks/images/block_reportTextAttribute.png){.image-inline} 
```

```
name was changed to clarify it is different from ![length of text block](../blocks/images/block_reportListAttribute.png){.image-inline}
<!-- ::: -->
```

```

![image308.png](assets/image308.png)
```

```
`+` and `×` are *variadic*: they take two or more inputs. If
you drop a list on the arrowheads, the block name
changes to `sum` or `product`.

::: {.evenly-spaced-images layout-ncol=2}
![image309.png](assets/image309.png)
```

```

Extended mouse interaction events, sensing
clicking, dragging, hovering, etc. The “stopped” option triggers when
all scripts are stopped, as with the stop button; it is useful for
robots whose hardware interface must be told to turn off motors. A `when I am stopped` script can run only for a
limited time.
:::

::: {.evenly-spaced-images layout-ncol=2}
![image310.png](assets/image310.png)
```

```

Extended broadcast
:::

::: {.evenly-spaced-images layout-ncol=2}
![image311.png](assets/image311.png){.image-4x}
```

```

Extended `when I receive`: Click the right
arrowhead to expose a script variable (click on it to change its name,
like any script variable) that will be set to the data of a matching
broadcast. If the first input is set to “any message,” then the data
variable will be set to the message, if no payload is included with the
broadcast, or to a two-item list containing the message and the payload.
:::

![image312.png](assets/image312.png){.image-2x}

![image355.png](assets/image355.png){.image-2x}

If the input is set to “any key,” then a right arrowhead appears:
![image357.png](assets/image357.png){.image-inline-tall} and if you click it,
a script variable key is created whose value is the key that was
pressed. (If the key is one that’ represented in the input menu by a
word or phrase, e.g., “enter” or “up arrow,” then the value of key
will be that word or phrase, *except for* the space character, which
is represented as itself in key.)

![image356.png](assets/image356.png){.image-4x} <!--  style="width:2.25in;height:0.41944in"   alt="Website Description automatically generated with medium confidence" -->

The RGB(A) option accepts a single number, which
is a grayscale value 0-255; a two-number list, grayscale plus opacity
0-255; a three-item RGB list, or a four-item RGBA list.

<!-- TODO: Images like this should have index entries defined after this image. -->
![image358.png](assets/image358.png)

### Using Lists with the Ask Block {#sec-ask-lists}
These ask features and more in the Menus
library.

![image359.png](assets/image359.png)
```

```

![image360.png](assets/image360.png)
```

```

![image361.png](assets/image361.png)
```

```

![image362.png](assets/image362.png)
```

```

::: {.evenly-spaced-images layout-ncol=2}
![image363.png](assets/image363.png){.image-4x}
```

```

The `of` block has an extended menu of
attributes of a sprite. Position reports an (x,y) vector. Size reports
the percentage of normal size, as controlled by the set size block in
the Looks category. Left, right, etc. report the stage coordinates of
the corresponding edge of the sprite’s bounding box. Variables reports a
list of the names of all variables in scope (global, sprite-local, and
script variables if the right input is a script.)
:::

## Libraries {#sec-libraries-intro}

There are several collections of useful procedures that aren’t [Snap]{.snap}
primitives, but are provided as libraries. To include a library in your
project, choose the Libraries… option in the
file (![file menu icon](assets/image384.png){.image-inline}) menu.

![The import libraries dialog](assets/image385.png)

<!-- TODO: This is out of date. It is somewhat redudant with chapter 12. -->
The library menu is divided into five broad categories. The first is,
broadly, utilities: blocks that might well be primitives. They might be
useful in all kinds of projects.

The second category is blocks related to media computation: ones that
help in dealing with costumes and sounds (a/k/a Jens libraries). There
is some overlap with “big data” libraries, for dealing with large lists
of lists.

The third category is, roughly, specific to non-media applications
(a/k/a Brian libraries). Three of them are imports from other
programming languages: words and sentences from Logo, array functions
from APL, and streams from Scheme. Most of the others are to meet the
needs of the BJC curriculum.

The fourth category is major packages (extensions) provided by users.

The fifth category provides support for hardware devices such as robots,
through general interfaces, replacing specific hardware libraries in
versions before 7.0.

When you click on the one-line description of a library, you are shown
the actual blocks in the library and a longer explanation of its
purpose. You can browse the libraries to find one that will satisfy your
needs.

The libraries and their contents may change, but as of this writing the
list library has these blocks:

![image387.png](assets/image387.png){.image-4x} <!-- {width=1.84861in height=2.49236in} -->

(The lightning bolt (⚡️) before the name in several of these
blocks means that they use compiled HOFs or JavaScript primitives to achieve
optimal speed. They are officially considered experimental.) `Remove duplicates from` reports a list in
which no two items are equal. The `sort` block takes a
list and a two-input comparison predicate, such as `<`, and reports a
list with the items sorted according to that comparison. The `assoc` block
 is for looking up a key in an *association list:* a
list of two-item lists. In each two-item list, the first is a *key* and
the second is a *value.* The inputs are a key and an association list;
the block reports the first key-value pair whose key is equal to the
input key.

`For each item` is a variant of the primitive
version that provides a \# variable containing the
position in the input list of the currently considered item. `Multimap`
 is a version of `map` that allows multiple list
inputs, in which case the mapping function must take as many inputs as
there are lists; it will be called with all the first items, all the
second items, and so on. `Zip` takes any number of lists as inputs; it
reports a list of lists: all the first items, all the second items, and
so on. The `no-name` identity function reports its input.

`Sentence` and `sentence ➔ list`
 are borrowed from the [word and sentence library](#word-and-sentence-library) to serve as a variant of append that accepts non-lists
as inputs. `Printable` takes a list structure of any depth as input and
reports a compact representation of the list as a text string.

The iteration, composition library has these
blocks:

![image388.png](assets/image388.png) <!-- {width=1.68889in height=4.75in} -->
![image389.png](assets/image389.png) <!-- {width=1.04444in height=0.16111in} -->

`Catch` provide a nonlocal
exit facility. You can drag the tag from a `catch` block to a `throw` inside
its C-slot, and the throw will then jump directly out to the matching
catch without doing anything in between.

`If do and pause all` is for setting a
breakpoint while debugging code. The idea is to put show variable blocks
for local variables in the C-slot; the watchers will be deleted when the
user continues from the pause.

`Ignore` is used when you need to call a reporter but
you don’t care about the value it reports. (For example, you are writing
a script to time how long the reporter takes.)

The `cascade` blocks take an initial value and call
a function repeatedly on that value, *f*(*f*(*f*(*f*…(*x*)))).

The `compose` block takes two functions and reports
the function *f*(*g*(*x*)).

The first three repeat blocks
 are variants of the primitive `repeat until` block,
giving all four combinations of whether the first test happens before or
after the first repetition, and whether the condition must be true or
false to continue repeating. The last repeat block is like the `repeat`
primitive, but makes the number of repetitions so far available to the
repeated script. The next two blocks are variations on `for`\index{$for$
block} : the first allows an explicit step instead of using ±1, and the
second allows any values, not just numbers; inside the script you say ![image390.png](assets/image390.png){.image-inline} <!-- {width=3.15278in height=0.29861in} -->
```

```

replacing the grey block in the picture with an expression to give the next
desired value for the loop index.

`Pipe` allows reordering a nested composition with a left-to-right one:

![image392.png](assets/image392.png) <!--  style="width:3.70972in;height:1.17153in" alt="Macintosh HD:Users:bh:Desktop:untitled script pic (1).png" / --> 
```

```
![image391.png](assets/image391.png) <!--  style="width:3.44097in;height:1.36111in" alt="Macintosh HD:Users:bh:Desktop:untitled script pic (2).png" / -->
```

```

The stream library has these blocks:

![image393.png](assets/image393.png) <!-- {width=3.16111in height=2.15347in} -->
```

```

*Streams* are a special kind
of list whose items are not computed until they are needed. This makes
certain computations more efficient, and also allows the creation of
lists with infinitely many items, such as a list of all the positive
integers. The first five blocks are stream versions of the list blocks.

`in front of`, `item 1 of`\index{item 1
of stream block}, `all but first of`\index{all but first of stream
block}, `map`, and `keep`. `Show stream`
 takes a stream and a number as inputs, and
reports an ordinary list of the first *n* items of the stream. `Stream`
 is like the primitive list; it makes a finite
stream from explicit items. `Sieve` is an example
block that takes as input the stream of integers starting with 2 and
reports the stream of all the prime numbers. `Stream with numbers from` is
 like the numbers from block for
lists, except that there is no endpoint; it reports an infinite stream
of numbers.

<a name="word-and-sentence-library"></a>
The **word and sentence library** has these blocks:

<!-- TODO: Index Entries for all these blocks -->
![image394.png](assets/image394.png)

```

```

This library has the goal of recreating the Logo approach to handling text:
A text isn’t best viewed as a string of characters, but rather as a *sentence*, made of *words,*
each of which is a string of *letters.* With a few specialized
exceptions, this is why people put text into computers: The text is
sentences of natural (i.e., human) language, and the emphasis is on
words as constitutive of sentences. You barely notice the letters of the
words, and you don’t notice the spaces between them at all, unless
you’re proof-reading. (Even then: Proofreading is *diffciult,* because
you see what you expect to see, what will make the snetence make sense,
rather than the misspelling in front of of your eyes.) Internally, Logo
stores a sentence as a list of words, and a word as a string of letters.


Inexplicably, the designers of Scratch chose to abandon that tradition,
and to focus on the representation of text as a string of characters.
The one vestige of the Logo tradition from which
Scratch developed is the block named letter (1) of (world)\index{letter
(1) of (world) block} , rather than character (1) of (world). [Snap]{.snap}
inherits its text handling from Scratch.

In Logo, the visual representation of a sentence\index{visual
representation of a sentence} (a list of words) looks like a natural
language sentence: a string of words with spaces between them. In
[Snap]{.snap}, the visual representation of a list looks nothing at all like
natural language. On the other hand, representing a sentence as a string
means that the program must continually re-parse the text on every
operation, looking for spaces, treating multiple consecutive spaces as
one, and so on. Also, it’s more convenient to treat a sentence as a list
of words rather than a string of words because in the former case you
can use the higher order functions `map`, `keep`, and `combine` on them. This
library attempts to be agnostic as to the internal representation of
sentences. The sentence selectors accept any combination of lists and
strings; there are two sentence constructors, one to make a string (join
words) and one to make a list (sentence).

The selector names come from Logo, and should be self-explanatory.
However, because in a block language you don’t have to type the block
name, instead of the terse butfirst or the cryptic bf we spell out “all
but first of” and include “word” or “sentence” to indicate the intended
domain. There’s no first letter of block because `letter 1 of` serves that
need. `Join words` (the sentence-as-string constructor) is like the
primitive `join` except that it puts a space in the reported value between
each of the inputs. `Sentence` (the List-colored sentence-as-list
constructor) accepts any number of inputs, which can be words,
sentences-as-lists, or sentences-as-strings. (If inputs are lists of
lists, only one level of flattening is done.) `Sentence` reports a list of
words; there will be no empty words or words containing spaces. The four
blocks with right-arrows in their names
convert back and forth between text strings (words or sentences) and
lists. (Splitting a word into a list of letters is unusual unless you’re
a linguist investigating orthography.) `Printable`
takes a list (including a deep list) of words as input and reports a
text string in which parentheses are used to show the structure, as in
Lisp/Scheme.

The pixels library has one block:

![image395.png](assets/image395.png{.image-4x} <!-- {width=0.77917in height=0.62986in} -->

Costumes are first class data
in [Snap]{.snap}. Most of the processing of costume data is done by primitive
blocks in the Looks category. (See page
[79](#media-computation-with-costumes).) This library provides snap
, which takes a picture using your computer’s camera
and reports it as a costume.

The bar charts library has these blocks:

![image396.png](assets/image396.png) <!-- {width=3.43056in height=1.91667in} -->
```

```

`Bar chart of table`\index{bar chart
block} takes a table (typically from a CSV data set) as input and
reports a summary of the table grouped by the field in the specified
column number. The remaining three inputs are used only if the field
values are numbers, in which case they can be grouped into buckets
(e.g., decades, centuries, etc.). Those inputs specify the smallest and
largest values of interest and, most importantly, the width of a bucket
(10 for decades, 100 for centuries). If the field isn't numeric, leave
these three inputs empty or set them to zero. Each string value of the
field is its own bucket, and they appear sorted alphabetically.

`Bar chart of table` reports a new table with three columns. The first column
contains the bucket name or smallest number. The second column contains
a nonnegative integer that says how many records in the input table fall
into this bucket. The third column is a subtable containing the actual
records from the original table that fall into the bucket. `Plot bar chart`
 takes the table reported by bar chart
and graphs it on the stage, with axes labelled appropriately. The
remaining blocks are helpers for those.

If your buckets aren't of constant width, or you want to group by some
function of more than one field, load the "Frequency Distribution
Analysis" library instead.

The multi-branched conditional library\index{conditional
library:multiple-branch} has these blocks:

![image397.png](assets/image397.png) <!-- {width=1.85in height=2.47986in} -->

The `catch` and `throw` blocks duplicate ones in the iteration library, and are
included because they are used to implement the others. The `cases: if/then` block
 sets up a multi-branch conditional, similar to cond
in Lisp -family
languages. The first branch is built into the cases block; it consists
of a Boolean test in the first hexagonal slot and an action script, in
the C-slot, to be run if the test reports true. The remaining branches
go in the variadic hexagonal input at the end; each branch consists of
an `else if` block, which includes the Boolean test
and the corresponding action script, except possibly for the last
branch, which can use the unconditional `else` block.
As in other languages, once a branch succeeds, no other branches are
tested.

###

The variadic library has these blocks:

![image398.png](assets/image398.png) <!-- {width=1.19653in height=0.41667in} -->

These are
versions of the associative
operators `and`, and `or` that take any number of inputs instead of exactly
two inputs. As with any variadic input, you can also drop a list of
values onto the arrowheads instead of providing the inputs one at a time
As of version 8.0, the arithmetic operators sum, product, minimum, and
maximum are no longer included, because the primitive operators `+` `x`,
`min`, and `max` are themselves variadic.

The colors and crayons library has these blocks:

It is intended as a more powerful replacement for the primitive `set pen`
block specification as a better alternative to the HSV
that [Snap]{.snap} inherits from JavaScript; a “fair hue ”
scale that compensates for the eye’s grouping a wide range of light
frequencies as green while labelling mere slivers as orange or yellow;
the `X11/W3C standard color names`; `RGB in
hexadecimal`; a linear color scale (as in the old days, but better) based
on fair hues and including shades (darker colors) and grayscale. Another
linear scale is a curated set of 100 “crayons,” explained further on the
next page.

![image412.png](assets/image412.png) <!--  style="width:1.13333in;height:0.23333in" alt="Macintosh HD:Users:bh:Desktop:pen-color.png" / -->

Colors are
created by the ![image414.png](assets/image414.png){.image-inline} <!--  style="width:0.95in;height:0.225in" alt="Macintosh HD:Users:bh:Desktop:color picker.png" / --> block (for direct user selection), the `color from`
 <!--  style="width:1.13333in;height:0.23333in" alt="Macintosh HD:Users:bh:Desktop:pen-color.png" / --> , which
reports the color currently in use by the pen. The `from color` block
 reports names or numbers associated with a
color:

![image411.png](assets/image411.png){.image-4x} <!--  style="width:0.95in;height:0.225in" alt="Macintosh HD:Users:bh:Desktop:color picker.png" / -->

Colors can be created from
other colors:
![image415.png](assets/image415.png) <!-- {width=4.83333in height=0.43056in} -->

The three blocks with pen in their names are improved versions of
primitive Pen blocks. In principle `set pen`, for
example, could be implemented using a (hypothetical) `set pen` to color
composed with the `color from` block, but in fact `set pen` benefits from
knowing how the pen color was set in its previous invocation, so it’s
implemented separately from `color from`. Details in Appendix A.

The
recommended way to choose a color is from one of two linear scales: the
continuous *color numbers* and the discrete *crayons:*

![image416.png](assets/image416.png) <!-- {width=7.5in height=0.25in} -->

![image417.png](assets/image417.png) <!-- {width=7.5in height=0.25in} -->

Color numbers are based on *fair hues,* a modification
of the spectrum (rainbow) hue scale that devotes less space to green and
more to orange and yellow, as well as promoting brown to a real color.
Here is the normal hue scale, for reference:

![image418.png](assets/image418.png) <!-- {width=4in height=0.20833in} -->

Here is the fair hue scale:

![image419.png](assets/image419.png) <!-- {width=4in height=0.20833in} -->

Here is the color number scale:

![image416.png](assets/image416.png) <!-- {width=5in height=0.20833in} -->

(The picture is wider so that pure spectral colors line up with the fair
hue scale.)

 And
here are the 100 crayons :

![image417.png](assets/image417.png) <!-- {width=5in height=0.20833in} -->

The `color from` block, for example, provides different pulldown menus
depending on which scale you choose:

![image410.png](assets/image410.png) <!--  style="width:2.41667in;height:0.34444in" alt="Macintosh HD:Users:bh:Desktop:color-by-name.png" / -->

 You can also
type the crayon name:

![image420.png](assets/image420.png) <!--  style="width:2.41667in;height:0.34444in" alt="Macintosh HD:Users:bh:Desktop:color-by-name.png" / -->

There are many scales:

![image427.png](assets/image427.png) <!-- {width=4.29167in height=1.90972in} -->

The white slot at the end of some of the blocks has two purposes. It can
be used to add a transparency to a color (0=opaque,
100=transparent):

![image428.png](assets/image428.png) <!-- {width=4.29167in height=1.90972in} -->

or it can be expanded to enter three or four numbers for a vector
directly into the block, so these are equivalent:

![image429.png](assets/image429.png) <!-- {width=4.29167in height=1.90972in} -->

But note that a transparency number in a four-number RGBA vector is on
the scale 255=opaque, 0=transparent, so the following are *not*
equivalent:

![image430.png](assets/image430.png)

`Set pen crayon to` provides the equivalent of a box of 100 crayons. They
are divided into color groups, so the menu in the set pen crayon to
input slot has submenus. The colors are
chosen so that starting
from crayon 0, `change pen crayon by` 10 rotates through an interesting,
basic set of ten colors:

![image440.png](assets/image440.png)

Using `change pen crayon by` 5 instead gives ten more colors, for a total of 20:

![image441.png](assets/image441.png)

(Why didn’t we use the colors of the 100-crayon Crayola™ box? A few
reasons, one of which is that some Crayola colors aren’t representable
on RGB screens. Some year when you have nothing else to do, look up
“color space” on Wikipedia. Also “crayon.” Oh, it’s deliberate that
`change pen crayon by` 5 doesn’t include white, since that’s the usual
stage background color. White is crayon 14.) Note that crayon 43 is
“Variables”; all the standard block colors are included.

See Appendix A (@sec-crayons-and-color-numbers) for more information.

The **crayon library** has only the crayon features,
without the rest of the colors package.

![image442.png](assets/image442.png)

The catch errors library has these blocks:

![image444.png](assets/image444.png)

The `safely try` block
 allows you to handle errors that happen when
your program is run within the program, instead of stopping the script
with a red halo and an obscure error message. The block runs the script
in its first C-slot. If it finishes without an error, nothing else
happens. But if an error happens, the code in the second C-slot is run.
While that second script is running, the variable ![image443.png](assets/image443.png) <!-- {width=0.43056in height=0.15278in} -->  contains the text of
the error message that would have been displayed if you weren’t catching
the error. The `error` block is sort of the opposite:
it lets your program *generate* an error message, which will be
displayed with a red halo unless it is caught by `safely try`. `Safely try reporting` is the reporter version of `safely try`.

The text costumes library has only two
blocks:

 ![image446.png](assets/image446.png) <!--  style="width:1.92in;height:0.45078in" alt="Macintosh HD:Users:bh:Desktop:textcostume.png" / -->
 ![image447.png](assets/image447.png){.image-4x} <!-- {width=3.25972in height=0.18958in} -->

`Costume from text`
reports a costume that can be used with
the `switch to costume` block to make a
button:

![image445.png](assets/image445.png) <!--  style="width:0.53472in;height:0.20833in" alt="Macintosh HD:Users:bh:Desktop:Snaplabel.png" / -->

`Costume with background` reports a
costume made from another costume by coloring its background, taking a
color input like the `set pen color to RGB(A)` block and a number of
turtle steps of padding around the original costume. These two blocks
work together to make even better buttons:

![image448.png](assets/image448.png) <!-- {width=5.51in height=0.68in} -->

The text to speech library has these
blocks:

![image449.png](assets/image449.png) <!--  style="width:2.275in;height:0.8in" alt="Macintosh HD:Users:bh:Desktop:speechlib.png" / -->

This library
interfaces with a capability in up-to-date browsers, so it might not
work for you. It works best if the accent matches
the text!

The parallelization library contains
these blocks:

![image450.png](assets/image450.png) <!-- {width=1.17986in height=1.25972in} -->

The two `do in parallel`blocks
 take any number of scripts as inputs.
Those scripts will be run in parallel, like ordinary independent scripts
in the scripting area. `The do in parallel and wait` version waits until all of those
scripts have finished before continuing the script below the block.

The create variables library


![image451.png](assets/image451.png) <!-- {width=1.37778in height=1.48333in} -->

These blocks allow a program to perform the same operation as the
button, making global, sprite local, or script variables, but allowing
the program to compute the variable name(s). It can also set and find
the values of these variables, show and hide their stage watchers,
delete them, and find out if they already exist.

The getters and setters library has these
blocks:

![image452.png](assets/image452.png) <!-- {width=1.875in height=1.05in} -->

The purpose of this library
is to allow program access to the settings controlled by user interface
elements, such as the settings menu ![image453.png](assets/image453.png). The `setting` block\index{setting
block} reports a setting; the `set flag` block sets
yes-or-no options that have checkboxes in the user interface, while the
`set value` block controls settings with numeric
or text values, such as project name.

Certain settings are ordinarily remembered on a per-user basis, such as
the “zoom blocks” value. But when these settings are changed by this
library, the change is in effect only while the project using the
library is loaded. No permanent changes are made. Note: this library has
not been converted for version 7.0, so you’ll have to enable Javascript
extensions to use it.

The bignums, rationals, complex \#s library\index{infinite precision
integer library} has these blocks:

![image454.png](assets/image454.png)

The `USE BIGNUMS` block takes a Boolean input, to turn
the infinite precision feature on or off. When on, all of the arithmetic
operators are redefined to accept and report integers of any number of
digits (limited only by the memory of your computer) and, in fact, the
entire Scheme numeric tower, with exact rationals and with complex
numbers. The `Scheme number` block has a list
of functions applicable to Scheme numbers, including subtype predicates
such as rational? and infinite?, and selectors such as numerator and
real-part.

<!-- I cannot figure out an index format that compiles this...  -->
The `!` block computes the factorial function, useful to test whether bignums are turned on. Without bignums:

![image455.png](assets/image455.png) <!-- {width=0.29167in height=0.16667in} -->

With bignums:

![image456.png](assets/image456.png) <!-- {width=0.29167in height=0.16667in} -->

The 375-digit value of 200! isn’t readable on this page, but if you
right-click on the block and choose “result pic,” you can open the
resulting picture in a browser window and scroll through it. (These
values end with a bunch of zero digits. That’s not roundoff error; the
prime factors of 100! and 200! include many copies of 2 and 5.) The
block with no name is a way to enter things
like 3/4 and 4+7i into numeric input slots by converting the slot to Any
type.

The strings, multi-line input library
provides these blocks:

![image463.png](assets/image463.png) <!-- {width=3.9375in height=2.04167in} -->

All
of these could be written in [Snap]{.snap} itself, but these are implemented
using the corresponding JavaScript library functions directly, so they
run fast. They can be used, for example, in scraping data from a web
site. The command use case-independent comparisons applies only to this
library. The `multiline` block accepts and reports
a text input that can include newline characters.

The animation library has these blocks:

![image464.png](assets/image464.png) <!-- {width=4.0125in height=2.33125in} -->

Despite the name, this isn’t only about graphics; you can animate the values
of a variable, or anything else that’s expressed numerically.


The central idea of this library is an *easing function* *,* a
reporter whose domain and range are real numbers between 0 and 1
inclusive. The function represents what fraction of the “distance” (in
quotes because it might be any numeric value, such as temperature in a
simulation of weather) from here to there should be covered in what
fraction of the time. A linear easing function
means steady progression. A quadratic easing function means starting
slowly and accelerating. (Note that, since it’s a requirement that
*f*(0)=0 and *f*(1)=1, there is only one linear easing function,
*f*(*x*)=*x*, and similarly for other categories.) The ![image465.png](assets/image465.png) block reports some of the common easing functions.

The two Motion blocks in this library animate a sprite. `Glide` always animates
the sprite’s motion. `Animate's` first pulldown menu input allows you to
animate horizontal or vertical motion, but will also animate the
sprite’s direction or size. The `animate setter` block in
Control lets you animate any numeric quantity with any easing function.
The getter and setter inputs are best explained by example:

![image466.png](assets/image466.png) <!--  style="width:4.63194in;height:0.63194in" alt="Macintosh HD:Users:bh:Desktop:pix:animate-control.png" / -->

is equivalent to

![image467.png](assets/image467.png) <!--  style="width:3.40972in;height:0.25694in" alt="Macintosh HD:Users:bh:Desktop:pix:animate-motion.png" / -->

The other blocks in the library are helpers for these four.

The serial ports library contains these
blocks:

![image468.png](assets/image468.png) <!--  style="width:1.73264in;height:1.03472in" -->

It
is used to allow hardware developers to control devices such as robots
that are
connected to your computer via a serial port.

The frequency distribution analysis library\index{frequency
distribution analysis library} has these blocks:

![image469.png](assets/image469.png) <!-- {width=4.02708in height=2.39583in} -->

This is a collection of tools for analyzing large data sets and plotting
histogram s of how often some value is found in some
column of the table holding the data.

For more information go here:

https://tinyurl.com/jens-data

The audio comp library includes these
blocks:

![image470.png](assets/image470.png) <!-- {width=3.54167in height=2.98125in} -->

This library takes a sound,
one that you record or one from our collection of sounds, and
manipulates it by systematically changing the intensity of the samples
in the sound and by changing the sampling rate at which the sound is
reproduced. Many of the blocks are helpers for the `plot sound` block,
used to plot the waveform of a sound plays a sound. \_\_ `Hz for`
 reports a sine wave as a list of samples.

The web services library has these blocks:

![image471.png](assets/image471.png)

The first block is a generalization of the primitive
`url` block , allowing more control over the various
options in web requests:
`GET`, `POST`, `PUT`, and `DELETE`, and fine control over the content of the
message sent to the server. `Current location`\index{current location
block} reports your latitude and longitude. `Listify`\index{listify
block} takes some text in JSON format (see page
[54](#multi-dimensional-lists-and-json)) and converts it to a structured
list. `Value at key` looks up a key-value pair
in a (listified) JSON dictionary. The `key:value:` block
 is just a constructor for an abstract data
type used with the other blocks

The database library contains these blocks:

![image472.png](assets/image472.png)

It is used to keep data that persist from one [Snap]{.snap} session
 to the next, if you use the same browser and the same login.

The world map library has these blocks:

![image473.png](assets/image473.png) <!-- {width=2.44236in height=3.40278in} -->

Using any of the command
blocks puts a map on the screen, in a layer in front of the stage’s
background but behind the pen trails layer (which is in turn behind all
the sprites). The first block asks your browser for your current
physical location, for which you may be asked to give permission. The
next two blocks get and set the map’s zoom amount; the default zoom of
10 ﬁts from San Francisco not quite down to Palo Alto on the screen. A
zoom of 1 ﬁts almost the entire world. A zoom of 3 fits the United
States; a zoom of 5 ﬁts Germany. The zoom can be changed in half steps,
i.e., 5.5 is different from 5, but 5.25 isn’t.

The next five blocks convert between stage coordinates (pixels) and
Earth coordinates (latitude and longitude). The change by x: y: block
shifts the map relative to the stage. The distance to block measures the
map distance (in meters) between two sprites. The three reporters with
current in their names find *your* actual location, again supposing that
geolocation is enabled on your device. Update redraws the map; as
costume reports the visible section of the map as a costume. `Set style`
allows things like satellite pictures.

The APL primitives library contains these blocks:

![image474.png](assets/image474.png)

![image475.png](assets/image475.png)

For more information about APL, see @sec-appendix-b-apl).

The  **list comprehension library** has one block, `zip`:

![image476.png](assets/image476.png)

Its first input is a function of two inputs. The two Any-type inputs are
deep lists (lists of lists of…) interpreted as trees, and the function
is called with every possible combination of a leaf node of the first
tree and a leaf node of the second tree. But instead of taking atoms
(non-lists) as the leaves, `zip` allows the leaves of each tree to be
vectors (one-dimensional lists), matrices (two-dimensional lists), etc.
The Number-type inputs specify the leaf dimension for each tree, so the
function input might be called with a vector from the first tree and an
atom from the second tree.

The **bitwise library** provides bitwise
logic functions; each bit of
the reported value is the result of applying the corresponding Boolean
function to the corresponding bits of the input(s). The Boolean
functions are `not for ¬`, ` and for ∧`, ` or for ∨`, and `xor (exclusive or) for
⊻` . The remaining functions shift their first input left or right by the
number of bits given by the second input. `\<\<` is left shift, `\>\>` is
arithmetic right shift (shifting in one bits from the left), and `\>\>\>`
is logical right shift (shifting in zero bits from the left). If you
don’t already know what these mean, find a tutorial online.

![image477.png](assets/image477.png)

The **MQTT library** supports the Message Queuing
Telemetry Transport protocol, for connecting with IOT devices. See
<https://mqtt.org/> for more information.

![image487.png](assets/image487.png)

The **Signada library** allows you to control a
microBit or similar device that works with the Signada MicroBlocks
project.

![image488.png](assets/image488.png)

The **menus library** provides the ability to
display hierarchical menus on the stage, using the ask block’s ability
to take lists as inputs. See @sec-ask-lists.

![image486.png](assets/image486.png)

The **Sci[Snap]{.snap} library** and the **TuneScope
library** are too big to discuss here and are
documented separately at
<http://emu-online.de/ProgrammingWithSciSnap.pdf> and
<https://maketolearn.org/creating-art-animations-and-music/>
respectively.
