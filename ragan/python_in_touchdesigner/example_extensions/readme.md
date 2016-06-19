# Python in TouchDesigner #

## Programmer / Artist ##

**Matthew Ragan** | [ matthewragan.com](http://matthewragan.com)  

## example_executes ##

Now that we know a little more about how functions work we're ready to dig in a little deeper when it comes to working with execute DATs. There are a number of different executes, and they all work on a similar principle - a target operator is watched for changes, and when a change occurs a function is executed. Let's first look at a very simple example with a CHOP execute.

### The CHOP Execute DAT ###

Lets start by adding a Constant CHOP to our network, and then adding a CHOP Execute DAT. Next we drag the Constant onto the CHOP Execute DAT to specify that it's our target CHOP. Okay... now what? Well right away we should see there are a number of functions in our CHOP Execute (some of this is redundant from the previous tutorial, so bear with me because it's frightfully important).

As a quick note, you may see the functions in these DATs referred to as Methods. The semantics around function and method are nuanced in Python, and for the sake of clarity I'll mostly refer to them as functions. The important thing to consider is that methods are functions - that happen to belong to a class. If this feels strange, we can remember that all squares are rectangles - but being square carries a particular classification. All of that to say that for right now, we can think of these as functions. 

```Python
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

Right away we should notice that we have a set of five functions in our DAT:
* offToOn()
* whileOn()
* onToOff()
* whileOff()
* valueChange()

Okay. Let's start by first unpacking what these functions do. As their names suggest, these are the conditions under which the function is called - that is to say when it will be executed. So what does that mean? Let's take the example of offToOn(). In this case, the function offToOn is called when the CHOP's value moves from the off position to the on position. In TouchDesigner, we can think of on as being any value that's greater than 0. That means that anytime our value crosses the boundary of 0 to a positive number, this particular function will be called. To understand what that means we might make a simple change to the function like this:

```Python
def offToOn(channel, sampleIndex, val, prev):
    
    print( 'Hello there mischief maker' )

    return
```

Next we need to make sure our text port is open, and then we can move our Constant value from 0 to any positive number. We'll see that every time we cross the 0 boundary, we get line printed to our text port. DAT Execute magic.

If offToOn() fires in the crossing from 0 into positive numbers, it's not a stretch to realize that onToOff() fires when crossing into negative numbers. valueChange() will run whenever there's a change in the value; whileOn() fires only when the value is above 0; whileOff() fires only when the value is below zero. If this still isn't feeling useful yet, that's okay - hang in there because it's gonna get good.

That's all well and good, but to better take advantage of our CHOP execute we should take a closer look at what's happening. We'll notice that each function has four arguments:
* channel
* sampleIndex
* val
* prev

So what are these things? Arguments are passed into the function and can be used in any way we like. In the header portion of our CHOP execute we have the following to give us a little guidance:

```Python
# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.
```

Here we can see that this arguments are objects, and values in their own right. Okay, so what can we do with these things? The answer is, of course, nuanced. Before we get too lost in the abstract possibilities of what we might do with these things, we should first return to our roots and do a little bit of printing to figure out what on earth we're actually getting out of these arguments.

For starters we're going to write out a little chunk of text with placeholders to values:

```Python
execute_text = '''
The channel is {}
The sampleIndex is {}
The val is {}
The prev is {}
'''
```

We'll remember from earlier that we can use execute_text.format() to pass in some values to see printed out. If this is feeling only vaguely familiar you can [revisit that tutorial here](http://matthewragan.com/2015/10/14/python-in-touchdesigner-printing-touchdesigner/).

Okay. Next, let's add a one-line print statement to our offToOn() function:

```Python
print( execute_text.format( channel, sampleIndex, val, prev ) )
```

That means we should have a DAT that looks something like this:

```Python
# Our first CHOP execute!

# Here we'll only look at the first function - offToOn.
# We already learned a little bit about functions, so we know
# that we have access to a set of arguments. Let's just print 
# those out so we can see what they are.

# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

execute_text = '''\
The channel is {}
The sampleIndex is {}
The val is {}
The prev is {}
'''

def offToOn(channel, sampleIndex, val, prev):
    
    print( execute_text.format( channel , sampleIndex , val , prev ) )
    
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

Now let's change out constant CHOP a bit. Every time we cross from 0 to a positive number we should see a print statement that looks something like:

```Python
python >>> 
The channel is 0.05
The sampleIndex is 0
The val is 0.05000000074505806
The prev is 0.0
```

At first glance, channel and val are looking pretty similar. So what gives? Well, if we look back at our DAT we should see one particular line that tells us something very interesting:

```Python
# channel - the Channel object which has changed
```

Channel isn't just a value, it's an entire Python object. To better understand what that means we might want to look a little closer at the [Channel Class page on the wiki](http://www.derivative.ca/wiki088/index.php?title=Channel_Class). With a little closer inspection we can see that we can get all sorts of interesting information here: valid, index, name, owner, vals. These are all members of the Channel class, which means we can use dot notation to retrieve these. So, for example, we might change channel to channel.name in our simple example:

```Python
 print( execute_text.format( channel.name , sampleIndex , val , prev ) )
 ```

 This means that now when we print we instead get this:

 ```Python
python >>> 
The channel is chan1
The sampleIndex is 0
The val is 0.25
The prev is 0.0
```

That might not yet seem important, but it means that we can use conditional statements in our functions to determine what happens. If we had a CHOP with 15 Channels, for example, but only wanted to run a particular portion of our function with 'chan4' changed, we now have a way to separate out this particular event.

Okay. That's all well and fine, but what can we do with our new found python incantations? Let's pause for a moment and think for about how we build networks in TouchDesigner, and how cooking works. Cooking, the nomenclature for calculation, is pull based instead of push based in Touch. This means that the last element in a chain pulls changes from upstream. This is often much more efficient, but it also means that we need to think carefully about how we program. Let's consider a filter CHOP. The filter CHOP needs to always cook. Why?! Well, the filter CHOP's job is to interpolate between two values, and in order to do that it needs to constantly be calculating changes. The result of this CHOP cooking constant means that any downstream node will also cook, always - even when it isn't changing. In some circumstances this can cause challenges in facing efficiency in a network - especially if your filter CHOP is high up along the chain. Let's look at a simple example.

Let's add a few ingredients to our network, a buttom COMP, a filter CHOP, and a null CHOP. We can start by connecting these elements. Next let's use the resulting single to drive an opacity change in a level TOP. If we used an expression or an export we can see out our export / expression line is constantly moving (meaning that it's constantly cooking). We can also see that any operator downstream of our level CHOP (go crazy, and a few more TOPs to your network) is also cooking. That means by adding our single filter CHOP we've suddenly ended up with constantly cooking network. You may well throw your hands up in the air, and feel like them's the breaks. But, that's not the case. We can, instead, use a CHOP execute to drive a change in our Level TOP. 

How?! If we remember that we can target parameters in operators, this suddenly becomes very easy. If you're following along with our example network you'll see that I want to target a TOP called 'level2'. Let's drop in a CHOP execute DAT, drag our null CHOP onto our DAT, and get to updating our function. I'm going to make the following change to our function:

```Python

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
    
    op( 'level2' ).par.opacity = val
    
    return
```

Did you catch it? It's in the valueChange function, and it's just a single line:

```Python
op( 'level2' ).par.opacity = val
```

Easy. This means that we're only going to change that target parameter when the value changes from our target CHOP. Doing this we can see that we've now stopped forcing our TOP chain to cook constantly. 

We might also think about using CHOP Executes to do things that simplify our networks. Let's consider the following situation: we have a bank of movies that we want to switch between using a single button. Our button is connected to a count CHOP, and we'd like to cycle back through our four movies / images. One way to tackle this would be with a series of various CHOPs and DATs. In the example TOX I've used a count CHOP to cycle from 1 to 4. Next I converted this to a DAT, then inserted some text to match the format of our moviefile in TOPs, and finally converted to a text DAT before using this to drive a select TOP (that last step is a bit of a stretch, but I can see a situation where I might do something like that in a pinch). The resulting chain of operators all cook constantly. This happens, in part, because of our conversion from CHOP to DAT. Since our chopTo DAT is always cooking, this also means that everything down stream is cooking - always. How else might we solve this problem? Again, we might tackle this with a chop Execute DAT. In this case I'm going the use the integer value from the CHOP to help inform how I change the select TOP. Looking closer you can see the changes I've made to the value change function:

```Python
def valueChange(channel, sampleIndex, val, prev):

    target_path_v2 = 'moviefilein_picker_{}'
    op( 'select1' ).par.top = target_path_v2.format( int( val ) )

    return
```

Here I started by write a string with a placeholder for an inserted value:
```Python
target_path_v2 = 'moviefilein_picker_{}'
```

You'll notice that all of the moviefilein TOPs have been renamed to "moviefilein_picker_1-4".

The next sets the target select TOP with a path that's formatted with an integer of the value from the chop - channels are floats by default, and we need to specifically convert this to an integer to make sure that our string formatting is correct.

```Python
op( 'select1' ).par.top = target_path_v2.format( int( val ) )
```

### The Panel Execute DAT ###

The CHOP execute DAT is excellent, but it's not the only execute option. The Panel Execute is one of my favorites, and an operator that I continually return to for all sorts of situations. Like the CHOP execute it fires based on a change in a target operator, in this case any COMP with a panel component - buttons, sliders, containers, tables, lists, etc. In the Panel Execute DAT we see the following when we plunk it down in a network:

```Python
# me - this DAT
# panelValue - the PanelValue object that changed
# 
# Make sure the corresponding toggle is enabled in the Panel Execute DAT.

def offToOn(panelValue):
    return

def whileOn(panelValue):
    return

def onToOff(panelValue):
    return

def whileOff(panelValue):
    return

def valueChange(panelValue):
    return
```

This should all look pretty familiar - after all it's almost the same thing we saw in the CHOP execute. There is, of course, something we should pay close attention to right out the gate, our passed argument:

```Python
# panelValue - the PanelValue object that changed
```

Again, we can see that we're actually passed an entire object, not just a single value. Looking at the wiki we can see that the [panelValue is a class in it's own right](http://www.derivative.ca/wiki088/index.php?title=PanelValue_Class). This means we have access to the name, owner, and val. 

For starters let's add a button COMP to our network, set it to momentary, and add a panel execute DAT. Next we can write a similar print statement to see what that means for us as we're using the panel execute DAT:

```Python
# me - this DAT
# panelValue - the PanelValue object that changed
# 
# Make sure the corresponding toggle is enabled in the Panel Execute DAT.

def offToOn(panelValue):
    return

def whileOn(panelValue):
    return

def onToOff(panelValue):
    return

def whileOff(panelValue):
    return

def valueChange(panelValue):
    
    exec_text = '''\
-------------------------------
The PanelValue object contains:

panelValue.name = {}
panelValue.owner = {}
panelValue.val = {}
-------------------------------
'''
    
    print( exec_text.format( 
        panelValue.name,
        panelValue.owner,
        panelValue.val
         ) )
    
    return
```

Now when we click our button we should see something like the following printed:

```Python
The PanelValue object contains:

panelValue.name = v
panelValue.owner = /python_in_touchdesigner/example_executes/button3
panelValue.val = 0.3068181818181818
-------------------------------
```

Fancy! Again, this suddenly gives us access to a whole litany of possible directions to head when using this execute. 

Last but by no means least, let's look at how we might use several of these functions together. In this case I'm going to focus more on what's happening in panel execute than the entire mechanics of what we're up to. To understand what's happening in terms of the idea, let's consider that we want to do the following. I'd like to have a UI element where I can draw a shape that I then turn into a piece of geometry. There are any number of ways I might go about thinking through that problem. In this case I'm going to use a panel execute to set the position of a control element and extract the u and v values and append them to a table. I'm going to use those values to draw a box by converting CHOP data into a SOP. Finally, every time I start a new interaction on my UI, I'd like to clear the old data. 

We start by first adding a container COMP, and then a smaller container COMP inside with a different color. If you've looked at how the slider COMP works, it's the same idea at play here. We also need to add a table DAT where we can append some values. Next we'll use the panel execute to make some magic happen. Let's take a look at what we might write in order to get some interesting results.

```Python
# me - this DAT
# panelValue - the PanelValue object that changed
# 
# Make sure the corresponding toggle is enabled in the Panel Execute DAT.

# define some variables
ui = op( 'container1' )
box = op( 'container1/container_control' )
table = op( 'table4' )

def offToOn(panelValue):
    
    # clear our table when we start drawing a new shape
    table.clear()

    return

def whileOn(panelValue):
    
    # change the position of our contorl knob
    box.par.x = ui.panel.u  * ui.par.w - ( box.par.w * 0.5 )
    box.par.y = ui.panel.v  * ui.par.h - ( box.par.h * 0.5 )

    # add coordinates to a table to be turned into geometry
    table.appendRow( [ ui.panel.u , ui.panel.v ] )

    return

def onToOff(panelValue):
    return

def whileOff(panelValue):
    return

def valueChange(panelValue):
    return
```

The rest of this idea is then just about converting our table to a CHOP, and using a CHOP to SOP to further convert our data into geometry. At it's heart, this is a simple idea, but without a panel execute DAT it might be a bit of headache to get functioning the way we want.

This, however, is just the tip of the iceberg - as it were. There are also DAT Executes (when tables changes), Parameter Executes (when parameters change), Executes (at start, and close of TouchDesigner), and OP executes (for changes in operator flags, names, etc.). Once you get started doing a little bit of Python scripting, the world is your oyster. Well, at least TouchDesigner is your Oyster. 