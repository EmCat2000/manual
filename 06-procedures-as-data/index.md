# Procedures as Data

## Call and Run

 In the for block\index{for
block} example above, the input named <var>action</var> has been declared as type
"\\`Command (C-shaped)\\`"; that’s why the finished block is C-shaped. But how
does the block actually tell [Snap]{.snap} to carry out the commands inside
the C-slot? Here is a simple version of the block script:

![image692.png](assets/image692.png) <!--  style="width:3.67292in;height:1.58333in" / -->

This is simplified because it assumes, without checking, that the ending
value is greater than the starting value; if not, the block should
(depending on the designer’s purposes) either not run at all, or change
the variable by −1 for each repetition instead of by 1.

 The
important part of this script is the <code>run</code> block\index{run block} near
the end. This is a [Snap]{.snap} built-in command block that takes a
Command-type value (a script) as its input, and carries out its
instructions. (In this example, the value of the input ![image693.png](assets/image693.png) <!--  style="width:0.5in;height:0.15625in" / --> is the script
that the user puts in the C-slot of the <code>my for</code> block.) There is a
similar <code>call</code> reporter block for invoking a Reporter or Predicate block.
The <code>call</code>\index{call block } and <code>run</code> blocks are at the heart of
[Snap]{.snap}’s ﬁrst class procedure\index{first class procedures} feature;
they allow scripts and blocks to be used as data—in this example, as an
input to a block—and eventually carried out under control of the user’s
program.

Here’s another example, this time using a Reporter-type input in a <code>map</code>
block (see page [50](#map)):\index{map block}

![image743.png](assets/image743.png) <!--  style="width:0.5in;height:0.15625in" / -->

Here we are calling the Reporter <code>multiply by (10)<code> three times, once with
each item of the given list as its input, and collecting the results as
a list. (The reported list will always be the same length as the input
list.) Note that the <code>multiplication</code> block has two inputs, but here we
have specified a particular value for one of them (10), so the <code>call</code>
block knows to use the input value given to it just to fill the other
(empty) input slot in the <code>multiplication</code> block. In the <code>my map</code>
definition, the input <var>function</var> is declared to be type Reporter, and <var>data</var>
is of type List.

### Call/Run with inputs

 The
<code>call</code> block (like the <code>run</code> block) has a right arrowhead at the end;
clicking on it adds the phrase "\\`with inputs\\`" and then a slot into which
an input can be inserted:

![image698.png](assets/image698.png) <!--  style="width:1.8125in;height:0.20833in" / -->

If the left arrowhead is used to remove the last input slot, the "\\`with inputs\\`"\index{with inputs} disappears also. The right arrowhead can be
clicked as many times as needed for the number of inputs required by the
reporter block being called.

 If the number of inputs given
to <code>call</code> (not counting the Reporter-type input that comes first) is the
same as the number of empty input slots\index{empty input slots,
filling}, then the empty slots are filled from left to right with the
given input values. If <code>call</code> is given exactly one input, then *every*
empty input slot of the called block is filled with the same value:

![image699.png](assets/image699.png) <!--  style="width:2.72917in;height:0.31806in" / -->

If the number of inputs provided is neither one nor the number of empty
slots, then there is no automatic filling of empty slots. (Instead you
must use explicit parameters in the ring, as discussed in Section C
below.)

An even more important thing to notice about these examples is the
*<code>ring</code>*\index{ring, gray} around the Reporter-type input slots in <code>call</code>
and <code>map</code> above. This notation indicates that *the block itself,* not the
number or other value that the block would report when called, is the
input. If you want to use a block itself in a non-Reporter-type (e.g.,
Any-type) input slot, you can enclose it explicitly in a ring, found at
the top of the [Operators]{.mono} palette.

![image744.png](assets/image744.png) <!--  style="width:0.5in;height:0.15625in" / -->

As a shortcut, if you right-click or control-click on a block (such as
the <code>( ) + ( ) </code> block in this example), one of the choices in the menu that
appears is "\\`ringify\\`"\index{ringify} and/or "\\`unringify\\`"
\index{unringify}. The <code>ring</code> indicating a Reporter-type or
Predicate-type input slot is essentially the same idea for reporters as
the C-shaped input slot with which you’re already familiar; with a
C-shaped slot, it’s *the script* you put in the slot that becomes the
input to the C-shaped block.

There are three <code>ring</code> shapes. All are oval on the outside, indicating
that the <code>ring</code> reports a value, the block or script inside it, but the
inside shapes are command, reporter, or predicate, indicating what kind
of block or script is expected. Sometimes you want to put something more
complicated than a single reporter inside a reporter <code>ring</code>; if so, you
can use a script, but the script must <code>report</code> a value, as in a custom
reporter definition.

### Variables in Ring Slots

Note that the <code>run</code> block\index{variables in ring slots} in the
definition of the <code>my for</code> block (page [65](#call-and-run)) doesn’t have a
<code>ring</code> around its input variable <var>action</var>. When you drag a variable into a
ringed input slot, you generally *do* want to use *the value of* the
variable, which will be the block or script you’re trying to run or
call, rather than the orange variable reporter itself. So [Snap]{.snap}
automatically removes the ring in this case. If you ever do want to use
the variable *block itself,* rather than the value of the variable, as a
Procedure-type input, you can drag the variable into the input slot,
then control-click or right-click it and choose "\\`ringify\\`" from the menu
that appears. (Similarly, if you ever want to call a function that will
report a block to use as the input, such as <code>item (1) of ( ) </code> applied to a list
*of blocks,* you can choose "\\`unringify\\`" from the menu. Almost all the
time, though, [Snap]{.snap} does what you mean without help.)

## Writing Higher Order Procedures

A *higher order procedure*\index{higher order procedure} is one that
takes another procedure as an input, or that reports a procedure. In
this document, the word "\\`procedure\\`"\index{procedure} encompasses
scripts, individual blocks, and nested reporters. (Unless specified
otherwise, “reporter” includes predicates. When the word is capitalized
inside a sentence, it means specifically oval-shaped blocks. So, “nested
reporters” includes predicates, but “a Reporter-type input” doesn’t.)

Although an [Any-type]{.mono} input slot (what you get if you use the small
input-name dialog box) will accept a procedure input, it doesn’t
automatically ring the input as described above. So the declaration of
[Procedure-type]{.mono} inputs makes the use of your custom higher order block
much more convenient.

Why
would you want a block to take a procedure as input? This is actually
not an obscure thing to do; the primitive conditional and looping blocks
(the C-shaped ones in the Control palette) take a script as input. Users
just don’t usually think about it in those terms! We could write the
<code>repeat</code> block\index{repeat block} as a custom block this way, if [Snap]{.snap}
didn’t already have one:

![image708.png](assets/image708.png) <!--  style="width:2.375in;height:1.35417in" / -->

The lambda ("\\`λ\\`") next to <var>action</var> in the prototype indicates that this is a
C-shaped block\index{C-shaped block}, and that the script enclosed by
the C when the block is used is the input named <var>action</var> in the body of
the script. The only way to make sense of the variable <var>action</var> is to
understand that its value is a script.

To declare an input to be
[Procedure-type]{.mono}, open the input name dialog as usual, and click on the
arrowhead:

![image509.png](assets/image509.png) <!--  style="width:2.58333in;height:1.60417in" / -->

Then, in the long dialog, choose the appropriate Procedure type. The
third row of input types has a ring in the shape of each block type
(jigsaw for Commands, oval for Reporters, and hexagonal for Predicates).
In practice, though, in the case of Commands it’s more common to choose
the C-shaped slot on the fourth row, because this “container” for
command scripts is familiar to Scratch users. Technically the C-shaped
slot is an *unevaluated* procedure type, something discussed in Section
E below. The two Command-related input types (inline and C-shaped) are
connected by the fact that if a variable, an <code>item ( ) of ( )</code> block,
or a custom Reporter block is dropped onto a C-shaped slot of a custom
block, it turns into an inline slot, as in the <code>repeater</code> block’s
recursive call above. (Other built-in Reporters can’t report scripts, so
they aren’t accepted in a C-shaped slot.)

 ![image709.png](assets/image709.png) <!--  style="width:3.65278in;height:2.75455in" / -->


Why would you ever choose an inline Command slot rather than a C shape?
Other than the <code>run</code> block discussed below, the only
case I can think of is something like the C\index{C programming
language} /C++/Java\index{Java programming language} <code>for</code> loop, which
actually has *three* command script inputs (and one predicate input),
only one of which is the “featured” loop body:

![image710.png](assets/image710.png) <!--  style="width:2.11458in;height:0.46875in" / -->

Okay, now that we have procedures as inputs to our blocks, how do we use
them? We use the blocks <code>run</code>\index{run block} (for commands) and <code>call</code>
\index{call block } (for reporters). The <code>run</code> block’s script input is an
inline <code>ring</code>, not C-shaped, because we anticipate that it will be rare to
use a specific, literal script as the input. Instead, the input will
generally be a variable whose *value* is a script.

The <code>run and <code>call blocks have arrowheads at the end that can be used to
open slots for inputs to the called procedures. How does [Snap]{.snap} know
where to use those inputs? If the called procedure (block or script) has
empty input slots, [Snap]{.snap} “does the right thing.” This has several
possible meanings:

1. If the number of empty
slots\index{empty input slots, filling} is exactly equal to the number
of inputs provided, then [Snap]{.snap} fills the empty slots from left to
right:

![image711.png](assets/image711.png) <!--  style="width:3.44792in;height:0.34406in" / -->

2. If exactly one input is provided, [Snap]{.snap} will fill any number of
empty slots with it:

![image712.png](assets/image712.png) <!--  style="width:2.80208in;height:0.30694in" / -->

3. Otherwise, [Snap]{.snap} won’t fill any slots, because the user’s
intention is unclear.

If the user wants to override these rules, the solution is to use a <code>ring</code>
\index{ring, gray} with explicit input names that can be put into the
given block or script to indicate how inputs are to be used. This will
be discussed more fully below.

### Recursive Calls to Multiple-Input Blocks

A relatively rare situation not yet considered here is the case of a
recursive block that has a variable number of inputs. Let’s say the user
of your project calls your block with five inputs one time, and 87
inputs another time. How do you write the recursive call
\index{recursive call} to your block when you don’t know how many inputs
to give it? The answer is that you collect the inputs in a list
\index{input list} (recall that, when you declare an input name to
represent a variable number of inputs, your block sees those inputs as a
list of values in the first place), and then, in the recursive call, you
drop that input list *onto the arrowheads* that indicate a
variable-input slot\index{variable-input slot}, rather than onto the
input slot:

![image715.png](assets/image715.png) <!--  style="width:2.27569in;height:1.59722in" / -->


Note that the halo\index{halo!red} you see while dragging onto the
arrowheads\index{arrowheads} is red\index{red halo} instead of white,
and covers the input slot as well as the arrowheads. And when you drop
the expression onto the arrowheads, the words "\\`input list:\\`"\index{input
list} are added to the block text and the arrowheads disappear (in
this invocation only) to remind you that the list represents all of the
multiple inputs, not just a single input. The items in the list are
taken *individually* as inputs to the script. Since <var>numbers</var> is a list of
numbers, each individual item is a number, just what <code>sizes</code> wants. This
block will take any number of numbers as inputs, and will make the
sprite grow and shrink accordingly:

![image716.png](assets/image716.png) <!--  style="width:2.95833in;height:0.6875in" / -->

The
user of this block calls it with any number of *individual numbers* as
inputs. But inside the definition of the block, all of those numbers
form *a list* that has a single input name, <var>numbers</var>. This recursive
definition ﬁrst checks to make sure there are any inputs at all. If so,
it processes the ﬁrst input (<code>item (1) of ( )</code>the list), then it wants to make
a recursive call with all but the ﬁrst number (<code>all but first of ( )</code>). But <code>sizes</code> doesn’t take a
list as input; it takes numbers as inputs! So this would be wrong:

![image722.png](assets/image722.png) <!--  style="width:2.95833in;height:0.6875in" / -->

## Formal Parameters

The <code>rings</code> around Procedure-type inputs\index{input name} have an
arrowhead at the right. Clicking the arrowhead allows you to give the
inputs to a block or script explicit names\index{name, input}, instead
of using empty input slots as we’ve done until now.

![image730.png](assets/image730.png) <!--  style="width:4.32292in;height:0.45417in" / -->

The names <var>\#1</var>\index{\#1}, <var>\#2</var>, etc. are provided by default, but you
can change a name by clicking on its orange oval in the "\\`input names\\`"
list. Be careful not to *drag* the oval when clicking; that’s how you
use the input inside the <code>ring</code>. The names of the input variables are
called the *formal parameters*\index{formal parameters} of the
encapsulated procedure.

Here’s a simple but contrived
example using explicit names to control which input goes where inside
the <code>ring</code>:


![image731.png](assets/image731.png) <!--  style="width:4.32292in;height:0.45417in" / -->

Here we just want to put one of the inputs into two different slots. If
we left all three slots empty, [Snap]{.snap} would not fill any of them,
because the number of inputs provided (2) would not match the number of
empty slots (3).

 Here is a more realistic,
much more advanced example\index{crossproduct} : ![image733.png](assets/image733.png) <!--  style="width:4.34722in;height:1.40278in" / -->

![image732.png](assets/image732.png) <!--  style="width:4.67986in;height:3.01806in" / -->

This is the definition of a block that takes any number of lists, and
reports the list of all possible combinations of one item from each
list. The important part for this discussion is that near the bottom
there are two *nested* calls\index{nested calls} to <code>map</code>, the higher
order function\index{higher order function} that applies an input
function to each item of an input list. In the inner block, the function
being mapped is <code>( ) in front of ( )</code>, and that block takes two inputs. The
second, the empty List-type slot, will get its value in each call from
an item of the inner <code>map</code>’s list input. But there is no way for the outer
<code>map</code> to communicate values to empty slots of the <code>( ) in front of ( )</code> block. We
must give an explicit name, <var>newitem</var>, to the value that the outer <code>map</code> is
giving to the inner one, then drag that variable into the <code>( ) in front of ( )</code>
block.

By the way, once the called block provides names for its inputs, [Snap]{.snap}
will not automatically fill empty slots\index{empty input slots,
filling}, on the theory that the user has taken control. In fact,
that’s another reason you might want to name the inputs explicitly: to
stop [Snap]{.snap} from filling a slot that should really remain empty.

## Procedures as Data

Here’s
an example of a situation in which a procedure must be explicitly marked
as data by pulling a <code>ring</code> from the [Operators]{.mono} palette and putting the
procedure (block or script) inside it:

![image734.png](assets/image734.png) <!--  style="width:5.1875in;height:1.65625in" / -->

Here, we are making a list of procedures\index{list of procedures}.
But the <code>list</code> block accepts inputs of any type, so its input slots are
not ringed. We must say explicitly that we want the block *itself* as
the input, rather than whatever value would result from evaluating the
block.

Besides the <code>list</code> block in the
example above, other blocks into which you may want to put procedures
are <code>set ( ) to ( )</code> (to set the value of a variable to a procedure), <code>say ( )</code>and <code>think ( )</code>
(to display a procedure to the user), and <code>report ( )</code>(for a reporter that
reports a procedure):

![image735.png](assets/image735.png) <!--  style="width:3.83333in;height:0.84375in" / -->

## Special Forms

 The primitive <code>if else</code>
\index{if else block } block has two C-shaped command slots and chooses
one or the other depending on a Boolean test. Because Scratch doesn’t
emphasize functional programming, it lacks a corresponding reporter
block to choose between two expressions. [Snap]{.snap} has one, but we could
write our own:

![image736.png](assets/image736.png) <!--  style="width:2.49931in;height:0.27847in" / --> ![image737.png](assets/image737.png) <!--  style="width:2.40208in;height:1.42708in" / --> ![image739.png](assets/image739.png) <!--  style="width:3.81899in;height:0.27433in" / -->

Our block works for these
simple examples, but if we try to use it in writing a recursive operator
\index{recursive operator}, it’ll fail:

![image738.png](assets/image738.png) <!--  style="width:4.29167in;height:0.84861in" / -->

The problem is that when any block is called, all of its inputs are
computed (evaluated) before the block itself runs. The block itself
knows only the values of its inputs, not what expressions were used to
compute them. In particular, all of the inputs to <code>my if then else</code> block
are evaluated ﬁrst thing. That means that even in the base case,
<code>factorial</code>\index{factorial} will try to call itself recursively, causing
an infinite loop. We need <code>my if then else</code> block to be able to select
only one of the two alternatives to be evaluated.

We have a mechanism to allow that: declare the then variable <var>yes</var> and else variable <var>no</var> inputs to
be of type [Reporter]{.mono} rather than type [Any]{.mono}. Then, when calling the block,
those inputs will be enclosed in a <code>ring</code> so that the expressions
themselves, rather than their values, become the inputs:

![image740.png](assets/image740.png) <!--  style="width:1.11458in;height:0.69792in" / --> ![image742.png](assets/image742.png) <!--  style="width:2.61736in;height:1.51042in" / --> ![image741.png](assets/image741.png) <!--  style="width:4.52083in;height:1.02292in" / -->

In this version, the program works, with no infinite loop. But we’ve
paid a heavy price: this <code>reporter-if</code> is no longer as intuitively obvious
as the Scratch command-<code>if</code>. You have to know about procedures as data,
about <code>rings</code>, and about a trick to get a constant value in a ringed slot
\index{constant functions}. (The <code>id ( )</code> block\index{id block} implements
the identity function\index{identity function}, which reports its
input.[^6] We need it because <code>rings</code> take only reporters as input, not
numbers.) What we’d like is a <code>reporter-if</code> that *behaves* like this one,
delaying the evaluation of its inputs, but *looks* like our ﬁrst
version, which was easy to use except that it didn’t work.

[^6]: There is a primitive id function in the menu of the sqrt of block,
but we think seeing its (very simple) implementation will make this
example easier to understand.

Such blocks are indeed possible. A block that seems to take a simple
expression as input, but delays the evaluation of that input by wrapping
an “invisible ring” around it (and, if necessary, an <code>id ( )</code>-like
transformation of constant data into constant functions) is called a
*special form*\index{special form}. To turn our <code>if</code> block into a
special form, we edit the block’s prototype, declaring the inputs <var>yes</var>
and <var>no</var> to be of type "\\`Any (unevaluated)\\`"\index{Any (unevaluated) type}
instead of type [Reporter]{.mono}. The script for the block is still that of the
second version, including the use of <code>call</code> to evaluate either <var>yes</var> or <var>no</var>
but not both. But the slots appear as white [Any-type]{.mono} rectangles, not
[Reporter-type]{.mono} rings, and the factorial block will look like our ﬁrst
attempt.

In a special form’s prototype, the unevaluated\index{unevaluated type}
input slot(s) are indicated by a lambda ("\\`λ\\`") next to the input name, just
as if they were declared as [Procedure]{.mono} type\index{Procedure type}. They
*are* [Procedure]{.mono} type, really; they’re just disguised to the user of the
block.

Special forms trade off implementor sophistication
\index{sophistication} for user sophistication. That is, you have to
understand all about procedures as data to make sense of the special
form implementation of <code>my if then else</code>. But any experienced Scratch
programmer can *use* <code>my if then else</code> without thinking at all about how
it works internally.

### Special Forms in Scratch

Special forms are actually not a new invention in [Snap]{.snap}. Many of
Scratch’s conditional and looping blocks are really special forms. The
hexagonal input slot in the <code>if</code> block is a straightforward Boolean value,
because the value can be computed once, before the <code>if</code> block makes its
decision about whether or not to run its action input. But the <code>forever
if</code>, <code>repeat until ( )</code>, and <code>wait until ( )</code> blocks’ inputs can’t be Booleans; they
have to be of type “Boolean (unevaluated)\index{Boolean (unevaluated)
type},” so that Scratch can evaluate them over and over again. Since
Scratch doesn’t have custom C‑shaped blocks, it can afford to handwave
away the distinction between evaluated and unevaluated Booleans, but
[Snap]{.snap} can’t. The pedagogic value of special forms is proven by the
fact that no Scratcher ever notices that there’s anything strange about
the way in which the hexagonal inputs in the [Control]{.mono} blocks are
evaluated.

Also, the C-shaped slot\index{C-shaped slot} familiar to Scratch users
is an unevaluated procedure type; you don’t have to use a <code>ring</code> to keep
the commands in the C-slot from being run before the C-shaped block is
run. Those commands themselves, not the result of running them, are the
input to the C-shaped [Control]{.mono} block. (This is taken for granted by
Scratch users, especially because Scratchers don’t think of the contents
of a C-slot as an input at all.) This is why it makes sense that
“C‑shaped” is on the fourth row of types in the long form input dialog,
with other unevaluated types.
