# Python in TouchDesigner #

## Programmer / Artist ##

**Matthew Ragan** | [ matthewragan.com](http://matthewragan.com)  

## example_intro_to_functions ##

Before we can tackle CHOP executes we need to take a moment to learn about functions. There's a lot to learn about with functions, so we're not going to dive too deep just yet... yet. We are, however, going to peer into this idea so we can better understand part of what we'll see next as we move into the exciting world of executes.

Let's start by looking at what a function actually is:

"A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

As you already know, Python gives you many built-in functions like print(), etc. but you can also create your own functions."
 -- [Tutorials Point](http://www.tutorialspoint.com/python/python_functions.htm)

Great! But... how can we better understand that? For a moment let's first appreciate that we have a wide variety of functions that we do on a regular basis... we just don't think of them as functions. Most of us know how to calculate a tip, or gas mileage, or estimate travel time, or pack a suitcase, or make lunch, or or or, and and and. We don't think of these as functions, but if we had to write out very specific instructions about how to complete one of these tasks we'd actually be close to starting to wrestle with the idea of what a function is - it's okay if that doesn't make sense yet. Hang on tight, because we're gonna get there.

Let's first look at a simple example that examines the anatomy of a function. Next we'll write a few simple functions. Then we'll look at why that's important when it comes to thinking about CHOP executes. 

Starting with Anatomy.

Here we go, we're going to write a dead simple function:

```python
def first_function():
    
    print( 'Hello World' )

    return
```

There we go. We did it. Now, if we were to run this in TouchDesigner, nothing would happen... so at first glance it would seem like we didn't really write a function after all. That might be a good guess, but the reason nothing happened is because we never actually called our function, we just defined it - we wrote out all of the instructions, but we never asked TouchDesigner to actually run the function. To see anything happen, we need to actually call the function - we need to tell TouchDesigner that we need to run it. Let's modify our example to see what that would look like.

```python
def first_function():
    
    print( 'Hello World' )

    return

first_function()
```

Okay... time to take this all apart and see what makes it tick.
* We're started out by indicating that we were going to define a function... that's really what we meant when we wrote "def." 
* Next we gave that function a name, in our case we called it "first_function." 
* Next we specified that we weren't going to pass in any arguments or parameters by writing "()" - don't worry, we're going to learn more about that in a second.
* Then we indicated that we were going to outline what was in the function with our ":"
* The next line is indented one tab space and here we print out "Hello World"
* We ended the function with a return statement, which in this case didn't return anything.
* Finally, we summoned our function into action by saying its name... well, writing its name "first_function()"

At this point we've written a very simple function that just prints out "Hello World." We started with this simple example so we could just talk about its anatomy. Before we can move on to something a little more interesting, we need to unpack a few things. Specifically, we need to talk more about what it means to *return* something, and what an argument or parameter is when it comes to functions.

Let's start with *return*. Like it's name suggests, to return something is to give it back, or deliver something. Seems straightforward enough, right? We might imagine that sometimes we don't want to print out the result of a function, but we do want to get something out the other side to use in another process. In this case, we want something returned to us after the function has run. Let's look at that in a concrete way. 

We're going to use our same example first function, but make a few changes. 

```python
def first_function():
    
   text = 'Hello World'

    return text

first_function()
```

Okay, here we can see that we changed our function so we don't actually print out "Hello World" anymore, instead we return it at the end. If we run our function, we encounter our same problem that we saw earlier... it would seem as if nothing happened. What gives. Let's change our function in one small way and see what we end up with:

```python
def first_function():
    
   text = 'Hello World'

    return text

print( first_function() )
```

The small change to print out first_function() means that we're now printing out what's returned from this function. It might feel like a small difference, but it means that we're able to control what comes out of our function when we summon it into action. That's actually a very important thing, and we'll see why shortly. 

If we can control what comes out of our functions, surely we can control what goes into them... right? In fact, you are right. 

Now that we now how to get something out of our function, let's pass it some information do to something with. We're going to write another simple function, this time to do some simple math. 

```python
def percent( val1 ):
    
    calculation = val1 * 0.01

    return calculation

print( percent( 50 ) )
```

Alright, what do we have here? Let's imagine we want to change an integer into it's float equivalent as a percentage. 50% as becomes 0.5, 10% would be 0.1, and so on and so on. Here we've written a function to do just that. In this case we've specified that our function accepts one argument which is named val1. We later see in our function that "calculation" is val1 * 0.01. Finally, we return calculation. This means we can give percent any number, and get a float value in return. Not bad.

Okay, let's look at two more examples. Next we'll write a simple function to calculate a tip based on a total bill. At the end of this we want to see our tip and our total bill - using our new found lingo, we're going to return these values.

Okay, let's make some Python magic happen. If you're playing along at home, trying writing this yourself before you look at how I did it.

```python
def tip_calculator( total , tip_percentage  ):

    tip = total * ( tip_percentage / 100 )
    total_bill = total + tip

    return tip , total_bill

print( tip_calculator( 50 , 15 ) )
```

Here we want two things back, our tip and our total_bill. We start by calculating the tip, and then by adding that to our total. Finally we return these two values. 

Let's try one more idea on for size. This next time around you're challenge is to use the function we just wrote, and to write another function as a compliment. This second function is going to print out these values to our text port so we can see them. By writing this as two separate functions we decide when we want to print out our results, and when we want to just return our tip and total_bill. As an extra challenge, see if you can write your new function to accept only a single argument.

Okay, let's look at how you might solve this problem:

```python
def tip_calculator( total , tip_percentage  ):

    tip = total * ( tip_percentage / 100 )
    total_bill = total + tip

    return tip , total_bill

def display_total( tip_and_total_bill ):

    dotted_line = '- ' * 10
    tip_text = "Your total tip is {}"
    total_bill_text = "Your total bill is {}"
    
    print( dotted_line )
    print( tip_text.format( tip_and_total_bill[ 0 ] ) )
    print( total_bill_text.format( tip_and_total_bill[ 1 ] ) )
    print( dotted_line )

    return

total = 100
tip_percentage = 20

print( tip_calculator( total , tip_percentage ) )

display_total( tip_calculator( total , tip_percentage ) )
```

How did you do? We can see that our first function stayed the same. Our second function accepts a single argument - tip_and_total_bill. This tuple ([a series of values](https://en.wikipedia.org/wiki/Tuple)) is then used by our second function when printing out to our textport. This probably isn't the best way to solve this problem... but for the sake of a simple example our chances of getting into trouble are pretty slim.

Okay, so why do all of this?! Well, let's take a sneak peak at what's coming next. If we look at the contents of a CHOP execute we see:

```python
# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

def offToOn(channel, sampleIndex, val, prev):
    return

def whileOn(channel, sampleIndex, val, prev):
    return

def onToOff(channel, sampleIndex, val, prev):
    return

def whileOff(channel, sampleIndex, val, prev):
    return

def valueChange(channel, sampleIndex, val, prev):
    return
```

We should now recognize the contents of these DATs as functions... and not only are they functions, they're functions with four named incoming arguments. Now we can really start to have fun.

[Learn more about functions in Python](http://www.tutorialspoint.com/python/python_functions.htm)