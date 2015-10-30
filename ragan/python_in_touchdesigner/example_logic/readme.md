# Python in TouchDesigner #

## Programmer / Artist ##

**Matthew Ragan** | [ matthewragan.com](http://matthewragan.com)  

## example_logic ##

Logical statements are profoundly helpful for us when we're trying to convert an idea from what we understand, into something that a machine can interpret and act upon. Keeping that in mind, we need ways to distill ideas to their most fundamental pieces. What on earth do I mean? Well, we might think about ideas like greater than '>' , less than '<' , equal to '==' , and not equal to '!='. Further, we need to consider how we indicate when something might happen. This this set of examples we're going to focus on 'if' and 'else', as well as 'if' and 'elif' statements. What does all of that mean, well lets dig in and find out.

'if' and 'else' go hand in hand when we're thing about logical operations. The broad concept is that we're indicating what should happen if a particular condition is met, as well as what should happen when that condition isn't met. If we were to write this out as a set of instructions what we're really considering is what happens when a condition is met, and when it isn't met. Often when thinking about these kinds of situations it's easy for us to assume in action if our condition isn't met, which is a fine human assumption, but less fine when working with a machine.

Let's look at a simple let's imagine you want to know when a number is equal to another number. This happens all the time when we're programming, so we can start here.

First we need to do a bit of housekeeping and set ourselves up:

```python
#deine a varaible
my_int1 = 5
```

Next we can start to look at the syntax of our logical test. Our tests starts with a lower case 'if' followed by the test. We end our statement with colon ':' and indented on the next line we indicate what should happen if our test is met.

```python
if my_int1 >= 6:
    print( 'This number is greater than or equal to 6' )
```

Now, we're not done yet. We also need to indicate what should happen in all of the other circumstances... what happens if our number isn't great than or equal to? For this we use 'else:', and indented on the next line we indicate what should happen in this circumstance.

```python
else:
    print( 'This number is less than or equal to 6' )
```

Okay, that means that the whole python party looks like this:

```python
# define our variables
my_int1 = 5

# a simple logical test
if my_int1 >= 6:
    print( 'This number is great than or equal to 6' )

else:
    print( 'This number is less than or equal to 6' )
```

That's all well and good... most of the time. BUT, what if we don't want to do anything if our test isn't true? Surely there's a way to handle that circumstance... right? There is indeed. We can use the 'pass' statement as a null operation. Meaning that nothing happens when we call pass. We can change the code above to instead be this:

```python
# define our variables
my_int1 = 5

# a simple logical test
if my_int1 >= 6:
    print( 'This number is great than or equal to 6' )

else:
    pass
```

That's alright, but what if we want to live in more than an if else world? What if I want to explore a lot of possibilities? Well, one thing we might use is 'elif'. 'elif' allows us to insert another if statement before we get to our final else. In English this might be something like, try this - did that work? If it didn't, try this other thing. Did that work? Okay, then do this. Let's look at what that might mean in Python:

```python
# define our variables
my_int1 = 5

if my_int1 == 5:
    print( "This number is 5" )

elif my_int1 > 4 and my_int1 < 6:
    print( "This number is greater than 4, but less than 6" )

else:
    print( "This number is less than 4 or greter than 6" )
```

That's pretty great. But what if we want to test the same number twice? For example, what if I wanted to know if the number was greater than 4 and less than 6? How could I write that? In that case we could use 'and' in our logical test. Let's look at what that might look like:

```python
# define our variables
my_int1 = 5

if my_int1 > 4 and my_int1 < 6:
    print( "This number is greater than 4, but less than 6" )

else:
    print( "This number is less than 4 or greater than 6" )
```

This this case, BOTH conditions must be met in order for our print statement to pass the test.

What about if I have a circumstance where I have two possible circumstances I want to be treated the same? What if I want to print out a line if my number is greater than 4 or if it is exactly equal to -5? In this case we might use 'or'.

```python
# define our variables
my_int1 = -5

if my_int1 > 4 or my_int1 == -5:
    print( "This number is greater than 4 or it's -5" )

else:
    print( "This number is less than 4 or greter than 6" )
```

At this point surely you're rolling your eyes thinking "this is all well and good for Python, but what does it mean in TouchDesigner?!" That's an excellent question, and the magic here goes back to what we learned when thinking about references. Because Python variables can point to objects in TouchDesigner, we can move away from hardcoding our scripts, and instead let CHOPs stand in for our variables. For example, let's say we want to compare two numbers, we can use references to CHOPs to do just this. First let's make a constant CHOP with two channels, then we can write this bit of Python:

```python
# define our variables
my_int1 = op( 'constant1' )[ 'chan1' ]
my_int2 = op( 'constant1' )[ 'chan2' ]

if my_int1 == my_int2:
    print( "These values are equal!" )

elif my_int1 > my_int2:
    print( "Integer 1 is greater than integer 2" )

elif my_int1 < my_int2:
    print( "Integer 1 is less than integer 2" )
```

This is still the tip of the iceberg as it were. The fun stuff starts to happen in a few more lessons. I know that might feel frustrating, but stick with me. The better our understanding of the fundamentals and printing, the happier we'll be when it comes time to do the fancier foot work of making our networks hum. We need to know a little more about data structures first, and then we'll start to get to the magic of executes... and loops. Then we'll really be screaming along. Before you know it you'll be writing whole functions, and then using them as modules. It's all coming - so hang on tight.

[Find Python lessons at Learn Python the Hard Way](http://learnpythonthehardway.org/book/)

_documentation written in markdown_