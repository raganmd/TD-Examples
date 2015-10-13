# Python in TouchDesigner #

## Programmer / Artist ##

**Matthew Ragan** | [ matthewragan.com](http://matthewragan.com)  

## example_references ##

References are one of the engines of TouchDesgner. They're how we connect elements, and move information between operator families (and many other things as well.) I've written a good chunk already about understanding references - [check out understanding referencingg](http://matthewragan.com/2014/06/01/understanding-referencing-touchdesigner/), and [understanding referencing part 2](http://matthewragan.com/2014/06/27/understanding-referencing-part-ii-touchdesigner/) - so I'm not going to do my best not to revisit all of that same information. 

I do, however, want to look at referencing from the stand point of Python. The most important thing we might do is understand the anatomy of a python expression used in as a reference to another operator. Let's start with a simple example. Let's say I have an LFO CHOP (let's say that it's lfo1, and has a single channel, chan1) that's oscillating between -0.5 and 0.5. I want to use this changing number to alter the position of a circle. In the Center X parameter of the circle I can use the following expression:

```python
op( 'lfo1' )[ 'chan1' ]
```

Here I've specified that I'm looking at an operator. I know this because I started my expression with:

```python
op(  )
```

Inside of that I've placed the string name - remember that we now know it's a string as we can see that it's encased in quote marks - of the operator:

```python
op( 'lfo1' )
```

Next I've indicated which channel in that operator I want to use - [ 'chan1' ]:

```python
op( 'lfo1' )[ 'chan1' ]
```

We'll notice that this name is inside of square brackets. In the case above, we referenced the channel we were interested in by using the name of the channel. We could also have used the expression:

```python
op( 'lfo1' )[ 0 ]
```

In this case we've accessed the same channel, but by using it's index rather than it's name. We might imagine that our channels are like good little school children heading out to recess all in a line. These lovely kiddos both have a name, and an order that they occupy in the line. 

So why 0?

In Python, and in fact in many programming languages, 0 is still used as a number that represents a place. 0 is the first item in a sequence. We're accustomed to thinking of numbers as quantities and not as distances or sequences. If we think of this in terms of distance rather than quantity it makes a little more sense. If we're 1 mile (or kilometer) away from our destination, we're not there yet... we still have one more mile (or kilometer) to travel. This takes a bit of getting used to, but the longer you work with any programming language the more this will make sense.

Alright. This is great, so let's think about a table of information as well while we're here. 

**Sample Table**

|     |0      | 1        |
|----:|------:|---------:|
|    0| Color | Quantity |
|    1| red   | 10       |
|    2| blue  | 5        |

Above we have a table that exposes the index values for the rows and columns. Here we can see that the word "Color" is in row 0, column 0. That will become important here in just one moment. Let's imagine that our table is called "marbles." We'd like to write a reference to the quantity of red marbles. We can access the contents of this cell several ways. Just like with Channel Operators, in DATs we can use the index values of our table, or we can use the header names. Let's look at what that means.

Using the name of the row and column we could write the following reference:

```python
op( 'marbles' )[ 'red' , 'Quantity' ]
```

We could also write this expression by using only the index values of the table:

```python
op( 'marbles' )[ 1 , 1 ]
```

Finally, we can also mix and match these approaches and use either of these expressions for the same result:

```python
op( 'marbles' )[ 1 , 'Quantity' ]
op( 'marbles' )[ 'red' , 1 ]
```
