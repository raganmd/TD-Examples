# Python in TouchDesigner #

## Programmer / Artist ##

**Matthew Ragan** | [ matthewragan.com](http://matthewragan.com)  

## example_for_loop ##

Loops are an indispensable concept when it comes to programming and there are a virtually endless number of uses for them that we might encounter. What exactly is a loop then? A loop is a way of thinking about any kind of process that's repeated. Let's first consider a simple example all of us might have encountered - washing dishes. This processes looks the same to all of us who may have found a sink full of dirty dishes waiting for attention. What do you do in this situation? Let's assume that we don't have dishwasher, and for the sake of simplicity let's imagine that the act of washing the dishes is the same even if the dishes themselves are different. One by one, each dish is washed, rinsed, and dried. Let's imagine that we already have functions for washing and drying dishes. If we were going to do this programatically for four dishes it might look like:

```python
wash( dish1 )
dry( dish1 )

wash( dish2 )
dry( dish2 )

wash( dish3 )
dry( dish3 )

wash( dish4 )
dry( dish4 )
```

That's not so bad, but what if we had 100 dishes, or 1000, or 10,000?
That's a lot of hard coding.

What if, instead, we could just make a list of our dishes:

```python
[ dish1, dish2, dish3, dish4 ]
```

And then use a function to repeat the same procedure for every item in the list? Well, that's what a loop is for. In this case, this is what a _for loop_ is good for. A _for loop_ will do the same thing, for every item in a list, or for every number in a range. In the case of our dishes let's look at what that would mean for a list of dishes.

```python
dishes = [ dish1, dish2, dish3, dish4 ]

for item in dishes:
    wash( item )
    dry( item )
```

And that's it. If the list is 1 item long, or 10,000 items long, we don't have to write any more code than that. Easy. 

Okay, but what is a for loop?!

We might think of a for loop is a simple function that simply repeats the same series of actions in an iterative process - each successive item at a time. It's easy for us to start by thinking of loops as being connected to lists, but they don't have to be. They can be attached to a range - a range being a start and end point represented as integers. Instead of having a list of dishes, what if we only knew the number of dishes in the sink? How could we write this loop?

```python
for item in range( 10 ):
    wash( item )
    dry( item )
```

Okay. That's all well and good, but how can we start to think about this in a context that will help us? 

Lets first make a simple list so we have something to work with

```python
simple_list = [ 'apple', 'kiwi', 'orange', 'grape', 'pineapple' ]
```
The anatomy of our for loop can be a little confusing at first but once we get the hang of it, they're very powerful.

Okay, so what does that syntax look like:

python
for stand_in_variable in a_list_or_range:
    do each of these operations

let's first imagine that we want to print out each
of the items in our list

```python
for item in simple_list:
    print( item )
```

Here we can see that 'item' is our stand in variable. For reach positional item in our simple_list, we print out that item.

What if we don't have a list, and instead just want to run a loop a set number of times. Surely that's possible, right?

In fact it is!

```python
loop_count  = 10

print( "This is our first loop" )
for item in range( loop_count ):
    print( item )
```

That works great, but what's a range?! Let's print one out so we can better
see what that's about:

```python
print( '\n' )
print( "This is the range of our loop_count" )
print( range( loop_count ) )
```
Printing this out we can see what we get a tuple with a starting and ending position in the list this might seem to imply that we can use a range, or list, but start at a position other than the first item.

```python
print( '\n' )
print( "This is loop starting at position 5 going to the end" )
for item in range( loop_count )[ 5: ]:
    print( item )

print( '\n' )
print( "This is loop starting at the beginning and going to postiion 5" )
for item in range( loop_count )[ :5 ]:
    print( item )
```

Our simple list

```python
simple_list = [ 'apple', 'kiwi', 'orange', 'grape', 'pineapple' ]
```

Sometimes we want to use the contents of a list but we also need to know the position of the item in the list. For that we can use the enumerate method that's built into python. Let's see it in action to better understand what we're getting when we use enumerate.

```python
print( "Here's our enumerated list" )
for item in enumerate( simple_list ):
    print( item )
```

Alright, that's great, we can see here that we get a tuple of our list position, and our list item. That's great, but how can we use that?

```python
print( '\n' )
print( "Here's our enumerated list broken up a bit" )
for item in enumerate( simple_list ):
    print( item[ 0 ], item[ 1 ] )
```

Let's imagine that we want to fill in something like a sentence with the information from our list.

```python
message = "Item list position {}, actual item {}"

print( '\n' )
print( "Here's our enumerated list used with format" )
for item in enumerate( simple_list ):
    print( message.format( item[ 0 ], item[ 1 ] ) )
```

table   = op( 'table_simple_table' )

Lists are all well and good, but how do we use them in TouchDesigner? First lets look at how we might use some tables.

One way to loop through our table's rows would be to use the number of rows to define a range, then use our references to tables to move through its contents

```python
print( "Here's one way to loop through our table" )
for item in range( table.numRows ):
    print( table[ item, 0 ] )
```

Another way to loop through our table would be to use the .col() method. This returns an object that's a list of rows. To get the content of the cell, we need to use .val.

```python
print( '\n' )
print( "Here's another way to loop through our table" )
for item in table.col( 0 ):
    print( item.val )
```

If we remember that channels are arrays of numbers, we can quickly see how we might move through one of this arrays with a loop.

First let's remember that we can access the number of samples in a CHOP with .numSamples. We can use this value to determine our range.

We should take a quick moment to think about how we can access a single sample in a CHOP:

```python
print( "let's look at the value at position 0" )
print( op( 'pattern1' )[ 'chan1' ][ 0 ] )
```

Let's start with a simple task like printing out the value of each sample in a pattern CHOP.

First let's simplify our code by using a variable to reference our pattern CHOP.

```python
pattern = op( 'pattern1' )
```

Next we'll write a simple for loop that runs based on the number of samples in a CHOP.

```python
print( '\n' )
print( "let's print out every sample" )
for sample in range( pattern.numSamples ):
    print( pattern[ 'chan1' ][ sample ] )
```

Let's go one step further and use .format() one more time to make for print statements that make more sense.

```python
message = "{} is the value in the {} position"
noise   = op( 'noise1' )

print( '\n' )
print( "let's print out every sample in noise" )
for sample in range( noise.numSamples ):
    print( message.format( 
            round( noise[ 'chan1' ][ sample ], 3 ) , 
            sample
            )
        )
```

How else might we use for loops? We've seen how they might work with CHOPs and DATs, but what about TOPs?

We might imagine a circumstance where we wanted to fill a texture 3D - maybe for instancing, UI building or any number of things.

We can do this with a for loop easily, with just a little bit of thought.

```python
# define some variables
text_DAT        = op( 'table_tex3d' )
text_TOP        = op( 'text1' )
tex3d_TOP       = op( 'tex3d1' )

for item in range( text_DAT.numRows ):
    # change the text 
    text_TOP.par.text               = text_DAT[ item, 0 ]
    
    # use a random number to set the background color
    text_TOP.par.bgcolorr           = tdu.rand( item )
    text_TOP.par.bgcolorg           = tdu.rand( item + 1 )
    text_TOP.par.bgcolorb           = tdu.rand( item + 2 )

    # set the repalce index to match the row
    tex3d_TOP.par.replaceindex      = item
    
    # pulse fill the texture 3D
    tex3d_TOP.par.resetsinglepulse.pulse()
```

Loops are useful for any number of processes. Let's imagine that we want to fill up a table with the RGBA values from a TOP.

We could certainly use a TOP to CHOP, and then a CHOP to DAT, but we might imagine a circumstance where we don't want this operation to happen all the time, only at times that we specify.

Or we might want to sample an image for colors to use for another process, and we don't need a dedicated series of operators for this.

At any rate, lets look at how we might do this.

In this case I've set up a noise TOP to be 20 pixels tall, and 1 pixel wide. We can think of the number of pixels vertically as the range for our loop. 

We'll clear a table, and then append the contents for every pixel in our TOP. Easy.

First let's use some variables to make writing our loop easeir:

```python
nosie_TOP           = op( 'noise2' )
pixel_vals_DAT      = op( 'table1' )
header              = [ 'r', 'g', 'b', 'a' ]
```

In case there's anything left in our table, let's clear its contents first.

```python
pixel_vals_DAT.clear()
```

Next let's put some header information back into our dat, so we know what each colum is:

```python
pixel_vals_DAT.appendRow( header )
```

Now we can loop through our pixels and append their values to our table.

```python
for pixel in range( nosie_TOP.height ):
    pixel_vals_DAT.appendRow( nosie_TOP.sample( x = 0, y = pixel ) )
```

List comprehensions are a powerful means of constructing lists quickly. These might feel familiar from math courses you've taken or they may feel totally unfamiliar. In either case, they're a wonderful tool to be able to use, and can make fast work for building or changing lists.

Let's make a fast list so we can see the initial mechanics of list comprehensions

```python
my_list = [ 5, 10 , 4 , 6 , 20, 13, 7, 31 ]
```

First let's look at how we can print the contents of a list from inside the list.

```python
print( "Let's start by just printing out the contents of the list" )
print( "- - - - - - - - - -" )
new_list1 = [ print( item ) for item in my_list ]
```

We can also print out the index of our item as we go

```python
print( "\n" )
print( "Now lets look at how we can see the index of the items in our list" )
print( "- - - - - - - - - -" )
new_list2 = [ print( my_list.index( item ) ) for item in my_list ]
```

With a little bit of careful writing we can do both at the same time

```python
print( "\n" )
print( "Now let's print both together" )
print( "- - - - - - - - - -" )
new_list3 = [ 
                print( 'the index of this item is: ' + str( my_list.index( item ) ) , 
                        'the acutal list item is: ' + str( item ) ) for item in my_list 
            ]
```

We can also construct a list from scratch, in this case we'll 
make a list of each number in the list * 2 for the range of 10
If we write that out by hand we can see what we'll expect from 
our comprehension:
0 * 2 = 0
1 * 2 = 2
2 * 2 = 4
3 * 2 = 6
4 * 2 = 8
5 * 2 = 10
6 * 2 = 12
7 * 2 = 14
8 * 2 = 16
9 * 2 = 18

Now that we know what we're expecting to see, let's see if it works the way we want

```python
print( "\n" )
print( """Let's see how we can construct a list 
from scratch with a list comprehension""" )
print( "- - - - - - - - - -" )
list_from_scratch = [ item * 2 for item in range( 10 )  ]
print( list_from_scratch )
```

We can also construct a new list from a previous one. In this case let's see if we can construct a list that's only the even numbers from our first list.

```python
print( "\n" )
print( "Let's see how we can construct a new list from an old one" )
print( "In this case, let's see if we can build one that's only even numbers" )
print( "- - - - - - - - - -" )
evens_only = [ item for item in my_list if item % 2 == 0 ]
print( evens_only )
```

We can also use loops to do all sorts of exciting things like create and place operators.

What we'll quickly realize here is that for loops and the replicator COMP look very similar in the way they operate when it comes to creating ops!

You might feel like the replicator is good enough, so why learn how this work?! Sometimes knowing exactly how a process works can help us better understand another process. 

In this case, setting up our own replicator script can teach us a lot about the replicator. 

```python
new_ops_list = [
    'text_newop1' ,
    'text_newop2' ,
    'text_newop3'
    ]
```

We'll use this to determine the space between operators.

```python
node_distance = 100
```

Loop through list

```python
for item in enumerate( new_ops_list ):
    # create and name op 
    new_op = parent().create( textDAT , item[ 1 ] )

    # set location of nodes ( x or y )
    new_op.nodeX = me.nodeX
    new_op.nodeY = - ( item[ 0 ] * node_distance )
```

While we haven't yet talked about the pars() we can take advantage of this member of the page class.

Any given operator with parameters has a page of parameters, with names and values. Knowing this we can find our way to the paramters of an op with some clever programming.

Let's look at the anatomy of something like:
```python
op( 'constant_pars_target' ).pars( 'name0' )[ 0 ]
```

pars() returns a list of parameters. For us, we can think of the above in plain english as the first list element in the parameter 'name0' from constant_pars_target.

Okay, so what can we do with that information?

Well, we might make a table of par names and values, and set them by looping through our table. Let's take a look at how that might work.

First we'll make a table called 'table_pars_preset1'. Let's fill that table with par names in one column, and par values in another.

Next we'll create a stand in table where we can indicate which preset we want to use. Let's call that 'table_preset_selection'.

In the first cell let's write 'table_pars_preset1'. Alright, we're almost ready to write our for loop.

Finally let's add a constant CHOP called 'constant_pars_target'

Now let's write a loop!

First we'll start with some variable names:

```python
preset                              = op( 'table_preset_selection' )[ 0, 0 ]
target                              = op( 'constant_pars_target' )
```

Here in our loop is where things get intersting.
For starters we're going to use the op string name we've defined in our 
preset table. 

```python
for item in range( op( preset ).numRows )[ 1: ]:

    # As we go through the loop we'll use two variables one as our 
    # targed op_parameter, and another as a our parameter_value
    op_par                          = op( preset )[ item, 0 ]
    par_val                         = op( preset )[ item, 1 ]
    
    # Finally, we'll use those two varibles to change some varibles.
    target.pars( op_par )[ 0 ].val  =   par_val
    
    # We can use our preset statement to see how those two work together:
    print( 'target parameter: ', op_par )
    print( 'target value: ', par_val )

    # Let's also look at what that script would be if we were to write it
    # out by hand:
    script = 'op( "{op}" ).{par} = {par_val}'
    
    print( 'The script we run each loop:' )
    print( script.format( op = target.name, par = op_par, par_val = par_val ) )

    print( '\n' )
```

[Learn more about loops from Learn Python the Hard Way(http://learnpythonthehardway.org/book/ex32.html)]

[Learn more about lists](https://docs.python.org/3.3/tutorial/datastructures.html)