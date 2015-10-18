# Python in TouchDesigner #

## Programmer / Artist ##

**Matthew Ragan** | [ matthewragan.com](http://matthewragan.com)  

## data_structures_list ##

Lists are the bees knees, they're the cat's pajamas, they're almost better than sliced bread. There are a few important things for us to think about before we dive into the Python of lists. Python lists are just like the lists you might make on a piece of paper. They're a sequential ordering of items. A grocery list might be:
* eggs
* milk
* bread
* butter
* coffee

We often make lists, and while the order of our grocery list might be arbitrary, there are plenty of lists that are not. Frequently a todo list has a specific order:
1. Have preliminary discussion with collaborators
2. Check schedule for availability
3. Block off time for new project
4. Coordinate schedules
5. Build a preliminary budget
6. Draft contracts
7. Confirm costs
8. Book space
9. Purchase equipment

While this is a silly example, the important consideration is that here you wouldn't purchase equipment before you started a preliminary discussion with your collaborators. Of course that seems obvious - but remember that you have a sense of linearity, a sense of time, a sense of order, and a idiomatic frame that you subconsciously constructed based on the content of the list items. Alright, [semiotics](https://en.wikipedia.org/wiki/Sign_(semiotics)) aside, the more important idea here is that lists have order. Now while that may seem obvious, we'll see later that dictionaries don't necessarily work in the way - and in fact this is an important distinction we need to make early on. 

Let's go back to our grocery list. What might that look like in Python?

```python
grocery_list = [ 'eggs' , 'milk' , 'bread' , 'butter', 'coffee' ]
```

You'll notice that our items are enclosed in matching foot or inch marks: '' or "". We can remember back to our first lesson on printing that this helps us see that these are strings. That's wonderful. What if we want to print the whole list? Well we can do this:

```python
print( grocery_list )
```

That prints our whole list. That's pretty swanky, but what if we just want a single item from our list? How can we just print that? Well, we'll remember that 0 is still a number for us here in Python. That means the indexing of our list items looks like: 0 1 2 3 4

We can print a single item in our list by indicating the index of the item we want:

``` python
print( grocery_list[ 0 ] )
```

Let's look at that a little more closely and print out all of the items we have in our list:

``` python
print( grocery_list[ 0 ] )
print( grocery_list[ 1 ] )
print( grocery_list[ 2 ] )
print( grocery_list[ 3 ] )
print( grocery_list[ 4 ] )
```

Let's go one step further and really make that as explicit as possible - just to make sure we understand.

``` python
print( "The item in the 0 position of our list is %r" % grocery_list[ 0 ] )
print( "The item in the 1 position of our list is %r" % grocery_list[ 1 ] )
print( "The item in the 2 position of our list is %r" % grocery_list[ 2 ] )
print( "The item in the 3 position of our list is %r" % grocery_list[ 3 ] )
print( "The item in the 4 position of our list is %r" % grocery_list[ 4 ] )
```

We can make lists out of just about anything. Let's make a list out of all of the data types we've talked about so far:

```python
my_int_list = [ 1 , 2 , 3 , 4 ]
my_float_list = [ 1.235 , 1.5679 , 9.454 , 4.23485 ]
my_string_list = [ 'apple' , 'kiwi' , 'orange' , 'pineapple' ]
my_bool_list = [ True , True , False , True, False ]
my_mixed_list = [ 1.234 , 5 , 'apple' , True , 3.45 ]
```

One question we might have is how long is our list? Well, there happens to be an easy way for us to figure that out with len() - as in length.

```python
len( my_int_list )
```

Practice printing the length of all of your lists.

We can also build lists from scratch. First we need to create an empty list.

```python
my_list = []

print( 'As we go, we will print our list at each' )
print( 'step along the way' )
print( 'My List' ,  my_list )
```

Next we can add items to our list with .append( theValueOrStringToBeAddedHere ).

```python
my_list.append( 1 )

print( '\n' )

print( 'So we just added a single number out our list' )
print( 'what does that look like now?' )
print( 'My List' ,  my_list )
```

We can even add multiple items at once with .extend( aListofItemsHere ):

```python
my_list.extend( [ 45 , 2 , 100 , 6 ] )

print( '\n' )

print( 'Can we add multiple items at once?' )
print( 'My List' ,  my_list )

print( 'We sure can, we just need to use .extend' )
print( 'instead of .append' )
```

That's great... but what does this mean for me in TouchDesigner? Well, in Touch many things are returned as lists. Samples in CHOPs are often a list, as are points in a SOP. Once we have a fundamental understanding of lists as a data structure we can start to really have a lot of fun. 

Let's look at CHOPs first.
First, make sure you add a noise CHOP to your network called noise1.

```python
# define some variables
noise1 = op( 'noise1' )

# understanding the channel operator make
# a big difference in the way we use TouchDesigner

# lets start by just printing our variable

print( 'If we just print our noise1 variable we see this' )
print( noise1 )

print( 'If we print chan1 in noise1 one we see this' )
print( noise1[ 'chan1' ] )

print( 'we can also access this by using .chan( channelIndexHere )' )
print( noise1.chan( 0 ) )

print( 'Finally, we can see the whole list of values if we use' )
print( '.vals as we... that looks like') 
print( 'noise1.( channelIndexHere ).vals' )
print( noise1.chan( 0 ).vals )
```

That's pretty fun... but let's take that a step further.

```python
# okay, but why do we care?

# define some variables
noise1 = op( 'noise1' )

# we can use what we've learned working with the .chans().vals
# to help us understand a little bit more about our CHOP
# for example, if our channel is a list of values, we can
# access those values just like we might in a list

print( noise1[ 'chan1' ][ 0 ] )
print( noise1[ 'chan1' ][ 1 ] )
print( noise1[ 'chan1' ][ 2 ] )

# we can even do the same things we might do in python here
print( len( noise1[ 'chan1' ] ) )

# though if we look at the wiki, we'll find that there's already
# a method to do just this called .numSamples
# and a method called numChans - which tells us how many channels
# If we think of our CHOP as a list of lists... then we can both
# see how many lists, and the length of the lists.

print( noise1.numSamples )
print( noise1.numChans )
```

Next let's add a rectangle SOP to our network.

```python
# define some variables
rectangle1 = op( 'rectangle1' )

# That's great... but what about geometry?
# Let's take a closer look at SOPs

print( 'Like with a sop we can print the path to rectangle1 operator' )
print( rectangle1 )

print( 'We can also look at the member .points' )
print( rectangle1.points )

print( 'Seeing that it is an object by itself, means we can look closer' )
print( 'What happens if we just ask for the first item in this object?' )
print( rectangle1.points[ 0 ] )

print( 'What if we ask to make the whole object a list, and the print it out?' )
print( list( rectangle1.points ) )
```

While CHOPs and SOPs seem like obvious operators that might have lists, they're certainly not the only ones. The method .findChildren returns a list of operators when dealing with COMPs. Let's take a closer look at that while we're at it. I started by making a container and adding three buttons inside. Make sure that you look at the example file to see what I've done to get started.

```python
# define some variables
radio_buttons = op( 'container_radio_buttons' )

# Let's take a look at findChildren
# we can see all of the ops inside of our container with:
print( radio_buttons.findChildren() )

# What if we only wanted to see the buttons??
print( radio_buttons.findChildren( depth = 1 ) )

# That's fine as long as there aren't any other operators
# inside of our conatiner. If we wanted to make sure we only
# got a list of buttons, we could be even more specific with

print( radio_buttons.findChildren( type = buttonCOMP , depth = 1 ) )

# Okay... so?
# Well, what we get back is a list, so what if we did this?

print( radio_buttons.findChildren( type = buttonCOMP , depth = 1 )[ 0 ] )

# Maybe we don't want to see the whole path, we just want to see it's name
print( radio_buttons.findChildren( type = buttonCOMP , depth = 1 )[ 0 ].name )

# Or maybe just its digits
print( radio_buttons.findChildren( type = buttonCOMP , depth = 1 )[ 0 ].digits )

# We could even click on one of our buttons this way
radio_buttons.findChildren( type = buttonCOMP , depth = 1 )[ 0 ].click()
```

Lists are powerful and also flexible data structures. And this is only the start of what we can do with them. Practice making some lists, accessing their contents, and printing out pieces of them. 

[Learn more about data structures in Python](https://docs.python.org/3.3/tutorial/datastructures.html)