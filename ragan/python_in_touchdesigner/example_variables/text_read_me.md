# Python in TouchDesigner #

## Programmer / Artist ##

**Matthew Ragan** | [ matthewragan.com](http://matthewragan.com)  

## example_variables ##

There are lots of resources on the web that describe variables better than I might:
* [Variable - Computer Science](https://en.wikipedia.org/wiki/Variable_(computer_science))
* [Python Programmingg](\https://en.wikibooks.org/wiki/Python_Programming/Variables_and_Strings)
* [Python Basics](http://www.astro.ufl.edu/~warner/prog/python.html)

The essential idea here, however, is that you have something that you want to reference by name. That something might be a sentence, it might be a quantity, it could be anything really. Again, it's more important for us in this moment to consider that our something (whatever it is) happens to be a piece of information that we want re-use.

Let's look at a dead simple example, to help us get started. If variables aren't new to you feel free to skip ahead.

Let's imagine you own a toy store. That toy store happens to sell marbles. That's great, good for you - you're a marvelous little capitalist. Now, let's imagine that you want to do an inventory of all of your marbles. You have several different varieties of marbles, and you'd like to be able to think of them as different, while also having a total count. In this situation we might keep track of your marbles by using some variables:

```python
red_marbles = 10
blue_marbles = 5
green_cat_eyes = 6
blue_cat_eyes = 12
```

Nice work. Now, we can print out each one of those, and get back our stored quantity. We could also do something like this:

```python
total_marbles = red_marbles + blue_marbles + green_cat_eyes + blue_cat_eyes
```

Now we also know the total quantity of marbles. Super. Finally, we might want to see all of that. Let's look at what that might look like:

```python
print( "Currently in your inventory you have:" )
print( "%d red marbles" % red_marbles )
print( "%d blue marbles" % blue_marbles )
print( "%d green cat eye marbles" % green_cat_eyes )
print( "%d blue cat eye marbles" % blue_cat_eyes )
print( "-" * 10 )
print( "That makes for %d total marbles" % total_marbles )
```

That's great, and hopefully you're a careful shop keeper and you don't loose any of your marbles... it was a long set-up for that bad joke.

What does this do for us here in TouchDesigner? When we're scripting in Touch it's often useful to be able to assign variables for all sorts of things. This especially useful when referencing operators.

Let's quickly consider one example. We might, have a level TOP that we want to make changes to. Starting with a simple task, lets imagine we want to use a script to change the opacity of a level TOP to 0. We could easily write something like this to solve this need:

```python
op( 'level1' ).par.opacity = 0
```

That's short and simple and gets the job done. Love it. Now, let's imagine a slightly more complicated world where I want to change lots of parameters for this operator. I want to change the invert, black level, brightness 1, gamma 1, contrast, and opacity. That's great. Let's write all of that out and see what we end up with:

```python
op( 'level1' ).par.invert = 0.31
op( 'level1' ).par.blacklevel = 0.27
op( 'level1' ).par.brightness1 = 1.45
op( 'level1' ).par.gamma1 = 0.5
op( 'level1' ).par.contrast = 1.76
op( 'level1' ).par.opacity = 0.782
```

That's not too bad, but we could make that a little less error prone if we were to simplify some of our script:

```python
level = op( 'level1' )

level.par.invert = 0.31
level.par.blacklevel = 0.27
level.par.brightness1 = 1.45
level.par.gamma1 = 0.5
level.par.contrast = 1.76
level.par.opacity = 0.782
```

That's pretty swanky, but let's imagine a situation where I've made a table full of presets that I want to be able to reference. Let's look at how we might tackle something like that:

```python
# define our variables:
presets = op( 'table_presets' )
level = op( 'level1' )
row_ref = 'preset1'

# change some parameters
level.par.invert = presets[ row_ref , 'invert' ]
level.par.blacklevel = presets[ row_ref , 'blacklevel' ]
level.par.brightness1 = presets[ row_ref , 'brightness1' ]
level.par.gamma1 = presets[ row_ref , 'gamma1' ]
level.par.contrast = presets[ row_ref , 'contrast' ]
level.par.opacity = presets[ row_ref , 'opacity' ]
```

Okay... so what happened here? First we defined created a variable called "presets" that stands in for op( 'table_presets' ). We also made one called "level" and one called "row_ref". 

Next we wrote a generalized set of instructions to change some parameters using our variables. For the sake of seeing it all written out let's look write it out long-form:

```python
op( 'level1' ).par.invert = op( 'table_presets' )[ 'preset1' , 'invert' ]
op( 'level1' ).par.blacklevel = op( 'table_presets' )[ 'preset1' , 'blacklevel' ]
op( 'level1' ).par.brightness1 = op( 'table_presets' )[ 'preset1' , 'brightness1' ]
op( 'level1' ).par.gamma1 = op( 'table_presets' )[ 'preset1' , 'gamma1' ]
op( 'level1' ).par.contrast = op( 'table_presets' )[ 'preset1' , 'contrast' ]
op( 'level1' ).par.opacity = op( 'table_presets' )[ 'preset1' , 'opacity' ]
```

This works just the same... so why use variables. Well, in this case I used variables to keep my code a little more tidy. I also did this because it means I'm less likely to make an error if I'm using shorter names. Most importantly, we did this because we've now created a variable called row_ref. This means we can change how this script works, just by altering this single variable. Let's say that we have two different presets. It would be far less fun to write the same set of scripts all over again just to reference a different preset. Instead, we can just change our variable to indicate which preset to use. That means that by making this single change:

```python
row_ref = 'preset2'
```

We've actually made this change:

```python
op( 'level1' ).par.invert = op( 'table_presets' )[ 'preset2' , 'invert' ]
op( 'level1' ).par.blacklevel = op( 'table_presets' )[ 'preset2' , 'blacklevel' ]
op( 'level1' ).par.brightness1 = op( 'table_presets' )[ 'preset2' , 'brightness1' ]
op( 'level1' ).par.gamma1 = op( 'table_presets' )[ 'preset2' , 'gamma1' ]
op( 'level1' ).par.contrast = op( 'table_presets' )[ 'preset2' , 'contrast' ]
op( 'level1' ).par.opacity = op( 'table_presets' )[ 'preset2' , 'opacity' ]
```

This is only the tip of the iceberg, but helps us see how useful using variables in Python can be.