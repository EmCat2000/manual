#  Object Oriented Programming with Sprites

Object oriented programming\index{object oriented programming} is a
style based around the abstraction *object:* a collection of *data* and
\index{method} *methods* (procedures, which from our point of view are
just more data) that you interact with by sending it a\index{message}
*message* (just a name, maybe in the form of a text string, and perhaps
additional inputs). The object responds to the message by carrying out a
method, which may or may not report a value back to the asker. Some
people emphasize the\index{data hiding} *data hiding* aspect of [OOP]{.mono}
(because each object has local variables that other objects can access
only by sending request messages to the owning object) while others
emphasize the *simulation* aspect (in which each object abstractly
represents something in the world, and the interactions of objects in
the program model real interactions of real people or things). Data
hiding is important for large multi-programmer industrial projects, but
for [Snap]{.snap} users it’s the simulation\index{simulation} aspect that’s
important. Our approach is therefore less restrictive than that of some
other [OOP]{.mono} languages; we give objects easy access to each others’ data
and methods.

Technically, object oriented programming rests on three legs: 

1. \index{message passing} *Message passing:* There is a notation by which
any object can send a message to another object. 

2. \index{local state}

*Local state:* Each object can remember the important past history of
the computation it has performed. (“Important” means that it need not
remember every message it has handled, but only the lasting effects of
those messages that will affect later computation.)

3. \index{inheritance} *Inheritance:* It would be impractical if each
individual object had to contain methods, many of them identical to
those of other objects, for all of the messages it can accept. Instead,
we need a way to say that this new object is just like that old object
except for a few differences, so that only those differences need be
programmed explicitly.

##  First Class Sprites

Like Scratch, [Snap]{.snap} comes with things that are natural objects: its
sprites\index{sprite}. Each sprite can own local variables; each
sprite has its own scripts (methods). A Scratch animation is plainly a
simulation of the interaction of characters in a play. There are two
ways in which Scratch sprites are less versatile than the objects of an 
[OOP]{.mono}language. First, Scratch message passing is weak in three respects:
Messages can only be <code>broadcast</code>\index{broadcast block}, not addressed
to an individual sprite; messages can’t take inputs; and methods can’t
return values to their caller. Second, and more basic, in the [OOP]{.mono}
paradigm objects are *data;* they can be the value of a variable, an
element of a list, and so on, but that’s not the case for Scratch
sprites.

[Snap]{.snap} sprites are first class\index{first class sprites} data. They can
be created and deleted by a script, stored in a variable or list, and
sent messages individually. The children of a sprite can inherit
sprite-local variables, methods (sprite-local procedures), and other
attributes (e.g., <code>x position</code>).

The fundamental means by which programs get access to sprites is the <code>my ( )</code> reporter
block\index{my}. It has a dropdown-menu input slot that, when clicked,
gives access to all the sprites, plus the stage\index{stage}.
![my self](assets/image745.png){.image-inline} reports a
single sprite, the one asking the question. ![image744.png](assets/image744.png) <!--  style="width:1.08333in;height:0.19444in" / -->   reports a list of all
sprites other than the one asking the question. ![image743.png](assets/image743.png) <!--  style="width:0.96528in;height:0.19444in" / -->  reports a list of all
sprites that are *near* the one asking—the ones that are candidates for
having collided with this one, for example. The <code>my ( )</code> block\index{my
block} has many other options, discussed below. If you know the name of
a particular sprite, the object reporter will report the sprite itself.

<!-- ![image746.png](assets/image746.png) style="width:3.55208in;height:0.51042in" / ![image747.png](assets/image747.png)   style="width:2.69143in;height:1.25in" alt="C:\Documents and Settings\bh\Desktop\Scratch002.png" / -->

An object or
list of objects reported by <code>my ( )</code> or <code>object ( )</code> can be used as input to any
block that accepts any input type, such as set’s (<code>set ( ) to ( )</code>) second input. If you
<code>say ( )</code> an object, the resulting speech balloon will contain a smaller image
of the object’s costume or (for the stage) background.

![image742.png](assets/image742.png) <!--  style="width:3.54514in;height:0.82639in" / -->

##  Permanent and Temporary Clones

The ![image748.png](assets/image748.png) <!--  style="width:1.51389in;height:0.19444in" alt="Macintosh HD:Users:bh:Desktop:pix:clone-block.png" / --> block is
used to create and report an instance (a clone) of any sprite. (There is
also a command version, for historical reasons.) There are two different
kinds of situations in which clones are used. One is that you’ve made an
example sprite and, when you start the project, you want a fairly large
number of essentially identical sprites that behave like the example.
(Hereafter we’ll call the example sprite the “parent” and the others the
“children.”) Once the game or animation is over, you don’t need the
copies any more. (As we’ll see, “copies” is the wrong word because the
parent and the children *share* a lot of properties. That’s why we use
the word “clones” to describe the children rather than “copies.”) These
are *[temporary]{.mono}* clones\index{temporary clone}. They are automatically
deleted when the user presses either the "\\`green flag\\`" or the "\\`red stop sign\\`". In Scratch 2.0 and later, all clones\index{clone temporary} are
temporary.

The other kind of situation is what happens when you want
specializations of sprites. For example, let’s say you have a sprite
named <var>Dog</var>. It has certain behaviors, such as running up to a person who
comes near it. Now you decide that the family in your story really likes
dogs, so they adopt a lot of them. Some are cocker spaniels, who wag
their tails when they see you. Others are rottweilers, who growl at you
when they see you. So you make a clone of <var>Dog</var>, perhaps rename it Cocker
Spaniel, and give it a new costume and a script for what to do when
someone gets near. You make another clone of <var>Dog</var>, perhaps rename it
Rottweiler, and give it a new costume, etc. Then you make three clones
of <var>Cocker Spaniel</var> (so there are four altogether) and two clones of
<var>Rottweiler</var>. Maybe you hide the <var>Dog</var> sprite after all this, since it’s no
breed in particular. Each dog has its own position, special behaviors,
and so on. You want to save all of these dogs in the project. These are
*[permanent]{.mono}* clones\index{permanent clone}. In [BYOB 3.1]{.mono}, the
predecessor to [Snap]{.snap}, all clones\index{clone!permanent} are
permanent.

 One advantage
of temporary clones is that they don’t slow down [Snap]{.snap} even when you
have a lot of them. (If you’re curious, one reason is that permanent
clones appear in the sprite corral, where their pictures have to be
updated to reflect the clone’s current costume, direction, and so on.)
We have tried to anticipate your needs, as follows: When you make a
clone in a script, using the ![image748.png](assets/image748.png) <!--  style="width:1.51389in;height:0.19444in" alt="Macintosh HD:Users:bh:Desktop:pix:clone-block.png" / --> block, it is “born” temporary. But when you
make a clone from the user interface, for example by right-clicking on a
sprite and choosing "\\`cline\\`", it is born permanent. The reason this makes
sense is that you don’t create 100 *kinds* of dogs automatically. Each
kind has many different characteristics, programmed by hand. But when
your project is running, it might create 100 rottweilers, and those will
be identical unless you change them in the program.

You can change a
temporary sprite to permanent by right-clicking it and choosing "\\`edit.\\`"
(It’s called "\\`edit\\`" rather than, say, “permanent” because it also shifts
the scripting area to reflect that sprite, as if you’d pressed its
button in the sprite corral.) You can change a permanent sprite to
temporary by right-clicking it and choosing "\\`release.\\`" You can also
change the status of a clone in your program with ![image749.png](assets/image749.png) <!--  style="width:1.51389in;height:0.25694in" alt="Macintosh HD:Users:bh:Desktop:set-my-temp.png" / --> with true or false as
the second input.

##  Sending Messages to Sprites

The messages that a sprite accepts are the blocks in its palettes,
including both "\\`all sprites\\`" and "\\`this sprite only\\`" blocks. (For custom
blocks, the corresponding methods are the scripts as seen in the Block
Editor.)

The way to send a message to a sprite (or the stage) is with the <code>tell ( ) to ( )</code>
block (for command messages) or the <code>say ( )</code> block (for reporter messages).

![image749.png](assets/image749.png) <!--  style="width:3.54514in;height:0.82639in" / -->

![image750.png](assets/image750.png) <!--  style="width:3.54514in;height:0.82639in" / -->

A small point to note in the examples above: all dropdown menus include
an empty entry at the top, which can be selected for use in higher order
procedures like the <code>for each</code> and <code>map</code> examples. Each of the sprites in <code>my
(neighbors)</code> or <code>my (other sprites)</code> is used to fill the blank space in turn.

By the way, if you want a list of *all* the sprites, including this
sprite, you can use either of these:

![image751.png](assets/image751.png) <!--  style="width:3.54514in;height:0.82639in" / -->

<code>Tell ( )</code> and <code>ask ( ) and wait</code> wait until the
other sprite has carried out its method before this sprite’s script
continues. (That has to be the case for <code>ask ( ) and wait</code>, since we want to do
something with the value it reports.) So <code>tell ( )</code> is analogous to <code>broadcast ( )
and wait</code>. Sometimes the other sprite’s method may take a long time, or
may even be a forever loop, so you want the originating script to
continue without waiting. For this purpose we have the <code>launch ( )</code> block:

![image762.png](assets/image762.png) <!--  style="width:3.54514in;height:0.82639in" / -->

<code>Launch ( )</code> is analogous to <code>broadcast</code> without the “wait.”

[Snap]{.snap} [4.1]{.mono}, following [BYOB 3.1]{.mono}, used an extension of the of block to
provide access to other sprites’ methods. That interface was designed
back when we were trying hard to avoid adding new primitive blocks; it
allowed us to write <code>ask ( ) and wait</code> and <code>tell ( )</code> as tool procedures in [Snap]{.snap} itself.
That technique still works, but is deprecated, because nobody understood
it, and now we have the more straightforward primitives.

### Polymorphism\index{polymorphism}

Suppose you have a [Dog]{.mono} sprite
with two clones CockerSpaniel and PitBull. In the [Dog]{.mono} sprite you define
this method\index{method} ("\\`For this sprite only\\` block
\index{block!sprite-local} ):

![image763.png](assets/image763.png) <!--  style="width:1.67361in;height:1.40208in" / -->

Note the *loca*tion ([map-pin]{.mono}) symbol\index{map-pin symbol} before the
block’s name. The symbol is not part of the block title; it’s a visual
reminder that this is a sprite-*loca*l block. Sprite-local variables are
similarly marked.

But you don’t define <code>greet ( ) as friend</code> or <code>greet ( ) as enemy</code> in Dog. Each kind
of dog has a different behavior. Here’s what a CockerSpaniel does:

![image764.png](assets/image764.png) <!--  style="width:1.67361in;height:1.40208in" / -->

And here’s what a PitBull does:

![image765.png](assets/image765.png) <!--  style="width:1.67361in;height:1.40208in" / -->

<code>Greet ( )</code> is defined in the [Dog]{.mono} sprite. 
If Fido is a particular cocker
spaniel, and you ask Fido to <code>greet</code> someone, Fido inherits the <code>greet ( )</code>
method from [Dog]{.mono}, but [Dog]{.mono} itself couldn’t actually run that method,
because [Dog]{.mono} doesn’t have <code>greet ( ) as friend</code> or <code>greet ( ) as enemy</code>. And perhaps
only individual dogs such as Fido have <code>friend? ( )</code> methods. Even though the
<code>greet ( )</code> method is defined in the [Dog]{.mono} sprite, when it’s running it
remembers what specific dog sprite called it, so it knows which <code>greet ( ) as
friend</code> to use. [Dog]{.mono}’s <code>greet ( )</code> block is called a *polymorphic* method,
because it means different things to different dogs, even though they
all share the same script.

##  Local State in Sprites: Variables and Attributes

A sprite’s memory of its own past history takes two main forms. It has
*variables,* created explicitly by the user with the "\\`Make a variable\\`"
\index{variable} button; it also has *attributes,* the qualities every
sprite has automatically, such as <code>position</code>, <code>direction</code>, and <code>pen color</code>.
Each variable can be examined using its own orange oval block; there is
one <code>set ( ) to ( )</code> block to modify all variables. Attributes, however, have a less
uniform programming interface in Scratch:

- A sprite’s *direction* can be examined with the <code>direction</code> block, and
  modified with the <code>point in direction ( )</code> block. It can also be modified
  less directly using the blocks <code>turn ( )</code>, <code>point towards ( )</code>, and <code>if on edge, bounce</code>.

- There is no way for a script to examine a sprite’s *pen color,* but
  there are blocks <code>set pen color to (\<color\>)</code>, <code>set pen color to
  (\<number\>)</code>, and <code>change pen color to ( )</code> modify it.

- A sprite’s *name* can be neither examined nor modified by scripts; it
  can be modified by typing a new name directly into the box that
  displays the name, above the scripting area.

The block, if any, that examines a variable or attribute
\index{attribute} is called its\index{getter} *getter;* a block (there
may be more than one, as in the direction example above) that modifies a
variable or attribute is called a\index{setter} *setter.*

In [Snap]{.snap} we allow virtually all attributes to be examined. But instead
of adding dozens of reporters, we use a more uniform interface for
attributes: The my block\index{my block}’s menu (in [Sensing]{.mono}; see page
[78](#attrib.pnglist-of-attributes)) includes many of the attributes of
a sprite. It serves as a general getter for those attributes, e.g., <code>my
(\[anchor\])</code> to find the sprite, if any, to which this sprite is attached
in a nesting arrangement (see page
[10](#nesting-sprites-anchors-and-parts)). Similarly, the same <code>set ( ) to ( )</code> block
used to set variable values allows setting some sprite attributes.

![image766.png](assets/image766.png) <!--  style="width:1.67361in;height:1.40208in" / -->

##  Prototyping: Parents and Children

Most current [OOP]{.mono} languages use a *class/instance* approach to creating
objects. A class is a particular *kind of object,* and an instance is an
*actual object* of that type. For example, there might be a Dog class,
and several instances Fido, Spot, and Runt. The class typically
specifies the methods shared by all dogs (RollOver, SitUpAndBeg, Fetch,
and so on), and the instances contain data such as species, color, and
friendliness. [Snap]{.snap} uses a different approach called *prototyping,* in
which there is no distinction between classes and instances. Prototyping
\index{prototyping} is better suited to an experimental, tinkering style
of work: You make a single dog sprite, with both methods (blocks) and
data (variables); you can actually watch it and interact with it on the
stage; and when you like it, you use it as the prototype from which to
clone other dogs. If you later discover a bug in the behavior of dogs,
you can edit a method in the parent, and all of the children will
automatically share the new version of the method block. Experienced
class/instance\index{class/instance} programmers may find prototyping
\index{prototyping} strange at first, but it is actually a more
expressive system, because you can easily simulate a class/instance
hierarchy by hiding the prototype sprite! Prototyping is also a better
fit with the Scratch design principle\index{design principle} that
everything in a project should be concrete and visible on the stage; in
class/instance [OOP]{.mono} the programming process begins with an abstract,
invisible entity, the class, that must be designed before any concrete
objects can be made.[^7]

[^7]: Some languages popular in the “real world” today, such as
JavaScript, claim to use prototyping, but their object system is much
more complicated than what we are describing (we’re guessing it’s
because they were designed by people too familiar with class/instance
programming); that has, in some circles, given prototyping a bad name.
Our prototyping design comes from Object Logo\index{Object Logo}, and
before that, from Henry Lieberman\index{Lieberman, Henry}.
\[Lieberman, H., Using Prototypical Objects to Implement Shared Behavior
in Object-Oriented Systems, First Conference on Object-Oriented
Programming Languages, Systems, and Applications \[OOPSLA-86\], ACM
SigCHI, Portland, OR, September, 1986. Also in *Object-Oriented
Computing,* Gerald Peterson, Ed., IEEE Computer Society Press, 1987.\]

There are three ways to make a child sprite. If you [control-click]{.mono} or
[right-click]{.mono} on a sprite in the “sprite corral” at the bottom right
corner of the window, you get a menu that includes "\\`clone\\`" as one of the
choices. There is an <code>a new clone of ( )</code> block\index{a new clone of block}
in the [Control]{.mono} palette that creates and reports a child sprite. And
sprites have a “parent” attribute\index{parent attribute} that can be
set, like any attribute, thereby *changing* the parent of an existing
sprite.

![image766.png](assets/image766.png) <!--  style="width:1.67361in;height:1.40208in" / -->

## Inheritance by Delegation

A clone *inherits* properties of its parent. “Properties” include
scripts, custom blocks, variables, named lists, system attributes,
costumes, and sounds. Each individual property can be shared between
parent and child, or not shared (with a separate one in the child). The
getter block for a shared property, in the child’s palette, is displayed
in a lighter color; separate properties of the child are displayed in
the traditional colors.

When a new clone is created, by default it shares only its methods, 
wardrobe, and jukebox with its parent. All other properties are copied 
to the clone, but not shared. (One exception is that a new *permanent* 
clone is given a random position. Another is that *temporary* clones 
share the scripts in their parent’s scripting area. A third is that 
sprite-local variables that the parent creates *after* cloning are 
shared with its children.) If the value of a shared property is 
changed in the parent, then the children see the new value. If the 
value of a shared property is changed in the *child*, then the sharing 
link is broken, and a new private version is created in that child. 
(This is the mechanism by which a child chooses not to share a property with its parent.) “Changed” in this context means using the 
<code>set ( ) to ( )</code> or <code>change ( ) by ( )</code> block for a variable, editing a block in the Block Editor, editing a costume or sound, or inserting, deleting, or reordering costumes or sounds. To change a property from unshared to shared, the child uses the <code>inherit</code> command block. The pulldown menu in the block lists all the things this sprite can inherit from its parent (which might be nothing, if this sprite has no parent) and is not already inheriting. But that would prevent <code>tell</code>ing a child to inherit, so if the <code>inherit</code> block\index{inherit block} is inside a <code>ring</code>, its pulldown menu includes all the things a child could inherit from this sprite. [Right-clicking]{.mono} on the scripting area of a permanent clone gives a menu option to share the entire collection of scripts from its parent, as a temporary clone does.

The rules are full of details, but the basic idea is simple: Parents can
change their children, but children can’t directly change their parents.
That’s what you’d expect from the word “inherit”: the influence just
goes in one direction. When a child changes some property, it’s
declaring independence from its parent (with respect to that one
property). What if you really want the child to be able to make a change
in the parent (and therefore in itself and all its siblings)? Remember
that in this system any object can <code>tell</code> any other object to do
something:

![image779.png](assets/image779.png) <!--  style="width:5.07292in;height:0.58333in" / -->

When a sprite gets a message
for which it doesn’t have a corresponding block, the message is
*delegated* to that sprite’s parent. When a sprite does have the
corresponding block, then the message is not delegated. If the script
that implements a delegated message refers to <code>my (self)</code>, it means the
child to which the message was originally sent, not the parent to which
the message was delegated.

![image780.png](assets/image780.png) <!--  style="width:0.78958in;height:3.46806in" alt="attrib.png" / -->

##  List of attributes

<!-- ![image781.png](assets/image781.png) ![image782.png](assets/image782.png)  -->

At the right is a picture of the dropdown menu of attributes\index{attributes, list of} in the <code>my ( )</code> block.

![image770.png](assets/image770.png) <!--  style="width:5.07292in;height:0.58333in" / -->

Several of these are not real attributes, but things related to
attributes:

- <code>self</code>\index{self (in my block)} : this sprite

- <code>neighbors</code>\index{neighbors (in my block)} : a list of *nearby*
  sprites[^8]

- <code>other sprites</code>\index{other sprites (in my block)} : a list of all
  sprites except myself

- <code>stage</code>\index{stage (in my block)} : the stage, which is first-class,
  like a sprite

- <code>clones</code>\index{clones (in my block)} : a list of my *temporary* clones

- <code>other clones</code>\index{other clones (in my block)} : a list of my
  *temporary* siblings

- <code>parts</code>\index{parts (in my block)} : a list of sprites whose anchor
  attribute is this sprite

- <code>children</code>\index{children (in my block)} : a list of all my clones,
  temporary and permanent

The others are individual attributes:

- <code>anchor</code>\index{anchor (in my block)} : the sprite of which I am a
  (nested) part

- <code>parent</code>\index{parent (in my block)} : the sprite of which I am a clone

- <code>temporary?</code>: am I a temporary clone?

- <code>name</code>\index{name (in my block)} : my name (same as parent’s name if
  I’m temporary)

- <code>costumes</code>\index{costumes (in my block)} : a list of the sprite’s
  costumes

- <code>sounds</code>\index{sounds (in my block)} : a list of the sprite’s sounds

- <code>blocks</code>: a list of the blocks visible in this sprite

- <code>categories</code>: a list of all the block category names

- <code>dangling?</code>\index{dangling? (in my block)} : True if I am a part and
  not in synchronous orbit

- <code>draggable?</code>: True if the user can move me with the mouse

- <code>width, height, left, right, top, bottom</code>: The width or height of my
  costume *as seen right now,* or the left, etc., edge of my bounding
  box, taking rotation into account.

- <code>rotation x\index{rotation x (in my block)}, rotation y
 \index{rotation y</code> (in my block)} : when reading with <code>my ( )</code>, the same as <code>x
  position, y position</code>. When <code>set ( ) to ( )</code>, changes the sprite’s rotation center
  *without moving the sprite,* like dragging the rotation center in the
  paint editor.

- <code>center x\index{center x (in my block)}, center y\index{center y (in
  my block)}</code>: the x and y position of the center of my bounding box, rounded off–the geometric center of the costume.

[^8]: *<code>Neighbors</code>* are all other sprites whose bounding boxes intersect the
doubled dimensions of the requesting sprite's bounds.

## First Class Costumes and Sounds

Costumes and sounds don’t have methods, as sprites do; you can’t ask
them to do things. But they *are* first class:\index{costumes, first
class} you can make a list of them, put them in variables, use them as
input to a procedure, and so on. <code>My (costumes)</code> and <code>my (sounds)</code>
report lists of them.

### Media Computation with Costumes

The components of a
costume are its name, width, height, and pixels. The ![image783.png](assets/image783.png) <!--  style="width:1.63194in;height:0.1875in" alt="Macintosh HD:Users:bh:Desktop:ofcostume.png" / -->  block gives access
to these components\index{of costume block} using its left menu. From
its right menu you can choose the current costume, the Turtle costume,
or any costume in the sprite’s wardrobe. Since costumes are first class,
you can also drop an expression whose value is a costume, or a list of
costumes, on that second input slot. (Due to a misfeature, even though
you can select Turtle in the right menu, the block reports 0 for its
width and height, and an empty string for the other components.) The
costume’s width and height are in its standard orientation, regardless
of the sprite’s current direction. (This is different from the
*sprite’s* width and height, reported by the <code>my ( )</code> block.)

But the really interesting part of a costume is its bitmap
\index{bitmap}, a list of *pixels*. (A pixel\index{pixel}, short for
“picture element,” represents one dot on your display.) Each pixel is
itself a list of four items, the red, green, and blue components of its
color (in the range 0-255) and what is standardly called its
“transparency\index{transparency} ” but should be called its opacity,
also in the range 0-255, in which 0 means that the pixel is invisible
and 255 means that it’s fully opaque: you can’t see anything from a
rearward layer at that point on the stage. (Costume pixels typically
have an opacity of 0 only for points inside the bounding box of the
costume but not actually part of the costume; points in the interior of
a costume typically have an opacity of 255.) Intermediate values appear
mainly at the edge of a costume, or at sharp boundaries between colors
inside the costume, where they are used to reduce “jaggies
\index{jaggies} ”: the stairstep-like shape of a diagonal line displayed
on an array of discrete rectangular screen coordinates. Note that the
opacity of a *sprite* pixel is determined by combining the costume’s
opacity with the sprite’s <code>ghost effect</code>. (The latter really is a measure
of transparency: 0 means opaque and 100 means invisible.)

The bitmap is a one-dimensional list of pixels, not an array of *height*
rows of *width* pixels each. That’s why the pixel list has to be
combined with the dimensions to produce a costume. This choice partly
reflects the way bitmaps are stored in the computer’s hardware and
operating system, but also makes it easy to produce transformations of a
costume with <code>map</code>:

![image784.png](assets/image784.png) <!--  style="width:1.63194in;height:0.1875in" alt="Macintosh HD:Users:bh:Desktop:ofcostume.png" / -->

In this simplest possible transformation, the red value of all the
pixels have been changed to a constant 150. Colors that were red in the
original (such as the logo printed on the t-shirt) become closer to
black (the other color components being near zero); the blue jeans
become purple (blue plus red); perhaps counterintuitively, the white
t-shirt, which has the maximum value for all three color components,
loses some of its red and becomes cyan, the color opposite red on the
color wheel. In reading the code, note that the function that is the
first input to <code>map</code> is applied to a single pixel, whose first item is its
red component. Also note that this process works only on bitmap
costumes; if you call <code>(pixels) of a costume ( )</code> on a vector costume (one with “svg” in
the corner of its picture), it will be converted to pixels first.

One important
point to see here is that a bitmap (list of pixels) is not, by itself, a
costume. The <code>new costume ( ) width ( ) height ( )</code> block\index{new costume block} creates a
costume by combining a bitmap, a width, and a height. But, as in the
example above, <code>switch to costume ( )</code> will accept a bitmap as input and will
automatically use the width and height of the current costume. Note that
there’s no <var>name</var> input; costumes computed in this way are all named
<var>costume</var>. Note also that the use of switch to costume does *not* add the
computed costume to the sprite’s wardrobe; to do that, say

![image790.png](assets/image790.png) <!--  style="width:2.25694in;height:0.28472in" alt="Macintosh HD:Users:bh:Desktop:add-to-wardrobe.png" / -->

Here’s a more interesting example of color manipulation:

![image791.png](assets/image791.png) <!--  style="width:2.25694in;height:0.28472in" alt="Macintosh HD:Users:bh:Desktop:add-to-wardrobe.png" / -->

Each
color value is constrained to be 0, 80, 160, or 240. This gives the
picture a more cartoonish look. Alternatively, you can do the
computation taking advantage of hyperblocks:

![image797.png](assets/image797.png) <!--  style="width:2.25694in;height:0.28472in" alt="Macintosh HD:Users:bh:Desktop:add-to-wardrobe.png" / -->

Here’s one way to exchange red and green values:

![image798.png](assets/image798.png) <!--  style="width:2.25694in;height:0.28472in" alt="Macintosh HD:Users:bh:Desktop:add-to-wardrobe.png" / -->

It’s the ![image804.png](assets/image804.png) <!--  style="width:0.95833in;height:0.18056in" alt="Macintosh HD:Users:bh:Desktop:2-1-3-4.png" / --> list that
determines the rearrangement of colors: green➔red, red➔green, and the
other two unchanged. That <code>list</code> is inside another <code>list</code> because otherwise
it would be selecting *rows* of the pixel array, and we want to select
columns. We use pixels of costume current rather than costume apple
because the latter is always a red apple, so this little program would
get stuck turning it green, instead of alternating colors.

The stretch block
\index{stretch block} takes a costume as its first input, either by
selecting a costume from the menu or by dropping a costume-valued
expression such as ![image809.png](assets/image809.png) <!--  style="width:1.72222in;height:0.22917in" alt="Macintosh HD:Users:bh:Desktop:a-costume.png" / -->  onto it. The other two inputs are percents of the
original width and height, as advertised, so you can make fun house
mirror versions of costumes:

![image805.png](assets/image805.png) <!--  style="width:0.95833in;height:0.18056in" alt="Macintosh HD:Users:bh:Desktop:2-1-3-4.png" / -->

The resulting costumes can be used with switch to costume and so on.

Finally, you can use pictures from your computer’s camera in your
projects using these blocks:



Using the
video on block\index{video on block} turns on the camera and displays
what it sees on the stage, regardless of the inputs given. The camera
remains on until you click the red stop button, your program runs the
stop all block, or you turn it off explicitly with the  ![image814.png](assets/image814.png) <!--  style="width:1.40278in;height:0.24306in" alt="Macintosh HD:Users:bh:Desktop:mirror-video.png" / --> block. The video
image on the stage is partly ghosted, to an extent determined by the ![image813.png](assets/image813.png) <!--  style="width:1.47222in;height:0.24306in" alt="Macintosh HD:Users:bh:Desktop:Jump! script pic.png" / --> set
video transparency block, whose input really is transparency and not
opacity. (Small numbers make the video more visible.) By default, the
video image is mirrored, like the selfie camera on your cell phone: When
you raise your left hand, your image raises its right hand. You can
control this
 mirroring with
the block.

The
video snap on block then takes a still picture from the camera, and
trims it to fit on the selected sprite. (Video snap on stage means to
use the entire stage-sized rectangle.) For example, here’s a camera
snapshot trimmed to fit Alonzo:

![image815.png](assets/image815.png) <!--  style="width:1.20417in;height:1.6125in" / -->

 The
“Video Capture” project in the Examples collection repeatedly takes such
trimmed snapshots and has the Alonzo sprite use the current snapshot as
its costume, so it looks like this:

![image816.png](assets/image816.png) <!--  style="width:2.67014in;height:1.29861in" alt="Macintosh HD:Users:bh:Desktop:Video Capture script 1.png" / -->

![image818.png](assets/image818.png) <!--  style="width:3.33333in;height:2.5in" alt="Macintosh HD:Users:bh:Desktop:video.png" / -->

 (The picture above was
actually taken with transparency set to 50, to make the background more
visible for printing.) Because the sprite is always still in the place
where the snapshot was taken, its costume exactly fits in with the rest
of the full-stage video. If you were to add a move 100 steps block after
the switch to costume, you’d see something like this:

![image817.png](assets/image817.png) <!--  style="width:2.66667in;height:2in" alt="Macintosh HD:Users:bh:Desktop:offset-video.png" / -->

This time, the sprite’s costume was captured at one position, and then
the sprite is shown at a different position. (You probably wouldn’t want
to do this, but perhaps it’s helpful for explanatory purposes.)

What you *would* want to do is push the sprite around the stage:

![image819.png](assets/image819.png) <!--  style="width:2.66667in;height:2in" alt="Macintosh HD:Users:bh:Desktop:offset-video.png" / -->

(Really these
should be Jens’s picture; it’s his project. But he’s vacationing. ☺)
Video motion compares two snapshots a moment apart, looking only at the
part within the given trim (here myself, meaning the current sprite, not
the person looking into the camera), to detect a difference between
them. It reports a number, measuring the number of pixels through which
some part of the picture has moved. Video direction also compares two
snapshots to detect motion, but what it reports is the direction (in the
point in direction sense) of the motion. So the script above moves the
sprite in the direction in which it’s being pushed, but only if a
significant amount of motion is found; otherwise the sprite would jiggle
around too much. And yes, you can run the second script without the
first to push a balloon around the stage.

### Media Computation with Sounds

The starting point for computation with sound\index{sound} is the
microphone block\index{microphone block}. It starts by recording a
brief burst of sound from your microphone\index{microphone}. (How
brief? On my computer, 0.010667 seconds, but you’ll see shortly how to
ﬁnd out or control the sample size on your computer.)

![image825.png](assets/image825.png) <!--  style="width:3.09028in;height:1.92361in" alt="Macintosh HD:Users:bh:Desktop:microphone.png" / -->

Just as the *pixel* is
the smallest piece of a picture, the *sample* is the smallest piece of a
sound ![image826.png](assets/image826.png) <!--  style="width:1.96528in;height:0.25694in" alt="Macintosh HD:Users:bh:Desktop:sample-rate.png" / --> . It says here: that on my computer, 48,000 samples are recorded
per second, so each sample\index{sample} is 1/48,000 of a second. The
value of a sample is between -1 and 1, and represents the sound pressure
on the microphone—how hard the air is pushing—at that instant. (You can
skip the next page or so if you know about Fourier analysis.) Here’s a
picture of 400 samples:

![image827.png](assets/image827.png) <!--  style="width:5.99931in;height:2.62014in" alt="Macintosh HD:Users:bh:Desktop:samples.png" / -->

In this graph, the *x* axis represents the time at which each sample was
measured; the *y* axis measures the value of the sample at that time.
The first obvious thing about this graph is that it has a lot of ups and
downs. The most basic up-and-down function is the *sine wave:*

Every periodic function (more or less, any sample that sounds like music
rather than sounding like static) is composed of a sum of sine wave
\index{sine wave} s of different frequencies.

![image829.png](assets/image829.png) <!--  style="width:2.78472in;height:1.04861in" alt="Macintosh HD:Users:bh:Desktop:sine.png" / -->

Look back at the graph of our sampled sound. There is a green dot every
seven samples. There’s nothing magic about the number seven; I tried
different values until I found one that looked right. What “right” means
is that, for the first few dots at least, they coincide almost perfectly
with the high points and low points of the graph. Near the middle
(horizontally) of the graph, the green dots don’t seem anywhere near the
high and low points, but if you find the very lowest point of the graph,
about 2/3 of the way along, the dots start lining up almost perfectly
again.

The red graph above shows two *cycles* of a sine wave. One cycle goes
up, then down, then up again. The amount of time taken for one cycle is
the *period* of the sine function. If the green dots match both ups and
downs in the captured sound, then two dots—14 samples, or 14/48000 of a
second—represent the period. The first cycle and a half of the graph
looks like it could be a pure sine wave, but after that, the tops and
bottoms don’t line up, and there are peculiar little jiggles, such as
the one before the fifth green dot. This happens because sine waves of
different periods are added together.

It turns out to be more useful to measure the reciprocal of the period,
in our case, 48000/14 or about 3429 *cycles per second.* Another name
for “cycles per second” is “Hertz,” abbreviated Hz, so our sound has a
component at 3249 Hz. As a musical note, that’s about an A (a little
flat), four octaves above middle C. (Don’t worry too much about the note
being a little off; remember that the 14-sample period was just
eyeballed and is unlikely to be exactly right.)

Four octaves above middle C is really high! That would be a
shrill-sounding note. But remember that a complex waveform is the sum of
multiple sine waves at different frequency. Here’s a different
up-and-down regularity:

![image828.png](assets/image828.png) <!--  style="width:2.79514in;height:1.22222in" alt="Macintosh HD:Users:bh:Desktop:red-sine.png" / -->

It’s not obvious, but in
the left part of the graph, the signal is more above the *x* axis than
below it. Toward the right, it seems to be more below than above the
axis. At the very right it looks like it might be climbing again.

The period of the red sine wave is 340 samples, or 340/48000 second.
That’s a frequency of about 141 Hz, about D below middle C. Again, this
is measuring by eyeball, but likely to be close to the right frequency.

All this eyeballing doesn’t seem very scientific. Can’t we just get the
computer to find all the relevant frequencies? Yes, we can, using a
mathematical technique called *Fourier analysis.* (Jean-Baptiste Joseph
Fourier, 1768–1830, made many contributions to mathematics and physics,
but is best known for working out the nature of periodic functions as a
sum of sine waves.) Luckily we don’t have to do the math; the microphone
block will do it for us, if we ask for microphone spectrum:

![image830.png](assets/image830.png) <!--  style="width:2.79514in;height:1.22222in" alt="Macintosh HD:Users:bh:Desktop:red-sine.png" / -->

These are frequency spectra from (samples of) three different songs. The
most obvious thing about these graphs is that their overall slope is
downward; the loudest frequency is the lowest frequency. That’s typical
of music.

The next thing to notice is that there’s a regularity in the spacing of
spikes in the graph. This is partly just an artifact; the frequency
(horizontal) axis isn’t continuous. There are a finite number of
“buckets” (default: 512), and all the frequencies within a bucket
contribute to the amplitude (vertical axis) of that bucket. The spectrum
is a list of that many amplitudes. But the patterns of alternating
rising and falling values are real; the frequencies that are multiples
of the main note being sampled will have higher amplitude than other
frequencies.

Samples and spectrum are the two most detailed representations of a
sound. But the microphone block has other, simpler options also:

- volume: the instantaneous volume when the block is called

- note: the MIDI note number (as in play note) of the main note heard

- frequency: the frequency in Hz of the main note heard

- sample rate: the number of samples being collected per second

- resolution: the size
of the array in which data are collected (typically 512, must be a power
of 2).

The block for sounds that corresponds to new picture for pictures is ![image258.png](assets/image258.png) <!--  style="width:2.91667in;height:0.28125in" alt="Macintosh HD:Users:bh:Desktop:new-sound.png" / -->
\index{new sound block}. Its first input is a list of samples, and its second input specifies how
many samples occupy one second.
