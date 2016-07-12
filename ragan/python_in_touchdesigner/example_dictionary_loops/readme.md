# Python in TouchDesigner #

## Programmer / Artist ##

**Matthew Ragan** | [matthewragan.com](http://matthewragan.com)  

## dictionary_loops_variables ##
We've looked at dictionaries as data structures already, and have gotten a peak into how powerful then can be for storing and manipulating data. That's all well and good, but wouldn't it be lovely if we could loop through the contents of our dictionaries the same way we can loop through list items? 

In fact, we can.

There are lots of ways to get there, so we'll take a look at a variety of approaches to help us make this happen.

In this set of examples we're going to use modules on demand as a fast way to get to our dictionaries that are stored in text DATs. We'll take a closer look at how modules work later on, so for now let's look at how we're going to use them in this set of examples. 

Here we can use the syntax:
```python
mod( 'our_target_text_dat_here' ).our_target_variable
```
What does that mean exactly? This means we can put a python variable in a text DAT, and retrieve it with a mod call. For example, let's say we have the following in a text DAT called "simple_mod_example":
```python
my_int = 5
my_float = 0.5
my_stirng = 'Hello there'
```
We can access these variables from any other operation with:
mod( 'simple_mod_example' ).my_int
mod( 'simple_mod_example' ).my_float
mod( 'simple_mod_example' ).my_string

A little later one we'll use some actual JSON that's not in a module on demand as well - so with any luck by the end of this we'll have a sense of how dictionaries work through and through. It's also worth pointing out that python storage can also take advantage of dictionaries for fast variable access. So, once you have a handle on how this data structure works you'll have a whole new world of options available to you.

Let's first start with a a simple dictionary:
```python
inventory = {
    "fruit" : {
        "apples" : 22 ,
        "kiwis" : 28 ,
        "grapes" : 11 ,
        "oranges" : 65 ,
        "grapefruit" : 75
    } ,
    "vegetables" : {
        "carrots" : 10 ,
        "potatoes" : 8 , 
        "onions" : 50 ,
        "kale" : 10
    } , 
    "beer" : {
        "ipa" : 32 ,
        "stout" : 46 ,
        "ale" : 56 ,
    }
}
```

Dictionaries are made of key and value pairs - the key being a string, and it's pair being any data type of your choice. You start the construction of a dictionary with curly braces. Key value pairs are separated by a colon, and new entires are separated by commas. You'll notice in the example above that we actually have a three dictionaries inside of a dictionary.

Let's start by looking at just one:
```python
fruit = {
    "apples" : 22 ,
    "kiwis" : 28 ,
    "grapes" : 11 ,
    "oranges" : 65 ,
    "grapefruit" : 75
}
```
This would be a fine way to create a single dictionary called fruit, with five entires, each with a quantity associated with them. 

If we keep this in mind, looking back at our first example we can see that we have a single dictionary called "inventory" which contains a dictionary for fruit, vegetables, and beer. This nesting of key value pairs is a part of what makes these data structure so powerful. Where lists rely on an index based system to find an entry, dictionaries rely on keys. The major difference we can think about is that lists are ordered, and dictionaries are orderless. At first glance it might seem like an orderless data structure might not be useful, but the more we use them the more we'll see how powerful they are. 

Let's look at our first code example, using modules means that we can use our dot notation to access an object inside of our text DAT. 

```python
inventory = mod( 'text_test_dictionary' ).inventory

# list of dictionary keys and their position
dictionary_keys = list( enumerate( inventory ) )

# let's get a feeling for how this works before we
# write a sentence
for item in dictionary_keys:
    print( item[ 0 ] , item[ 1 ] )

# loop through list and print the key and its
# list position
sentence = "The key {key} is in the {position} position of the list"

for item in dictionary_keys:
    print( sentence.format( key = item[ 1 ] , position = item[ 0 ] ) )
```

Okay, so what did we just do exactly?
Well, we first made a list out of our dictionary keys, then we enumerated that list so we had an ordered construction with both the dictionary keys and a position, and then we printed all of that out. Why? We started by looking at how we might do this if we were working with a list. Isn't that exactly what we're trying to avoid? Yes, but since we already know how lists work this is a good place to get started so we can begin to better understand how these two things are different. 

Okay, now that we've seen how this might work with an enumerated list, let's look at key value loop. We're going to use .items() to get the items out of our dictionary. We'll first just look at how to get to the keys in our dictionary.

```python
inventory = mod( 'text_test_dictionary' ).inventory

for dictionary_key , dictionary_value in inventory.items():
    print( "this dictionary key is: " , dictionary_key )
```

That's a pretty good start, and makes it easy to see how keys work. But this is a different kind of loop here, so what else can we do? Let's look at printing both our key and value this time around.

```python
# define our variables
# using modules means that we can use our dot notation to
# access an object inside of our text DAT
inventory = mod( 'text_test_dictionary' ).inventory

for dictionary_key , dictionary_value in inventory.items():
    print( "this dictionary key is: " , dictionary_key )
    print( "the dictionary value for this key is: " , dictionary_value )
```

Alright, that's pretty slick but our formatting still leaves something to be desired. Let's add a few more lines and see if we can print out something a little nicer.

```python
# define our variables
# using modules means that we can use our dot notation to
# access an object inside of our text DAT
inventory = mod( 'text_test_dictionary' ).inventory

# loop through the dictionary and print out contents
for dictionary_key , dictionary_value in inventory.items():
    # print out the first key depth in the dictionary   
    print( "- " * 10 )
    print( "this dictionary key is: " , dictionary_key )
    print( "in this dictionary we have:" )
    
    # loop through second dictionary layer
    for inventory_key , inventory_quantity in dictionary_value.items():
        # print out the key and value pairs from the second level
        print( '\t' , inventory_key , inventory_quantity )
```

Alright, not bad. Not bad at all. Here we can see that we ended up with a loop nested inside of our first loop. We started by printing out keys, then we run another loop to print out items and their quantities. 

## Recalling Presets ##

Okay, this is all well and good but what can we do with our new found tricks? Let's start by doing something seemingly simple - filling out a table with the contents of our dictionary. Why put things into a table?! At some point you'll certainly want to fill up a table with the contents of a dictionary... so we might as well look at how to do this early on.

```python
# define our variables
# using modules means that we can use our dot notation to
# access an object inside of our text DAT
inventory = mod( 'text_test_dictionary' ).inventory
table = op( 'table_inventory' )
table_length = []
place_holder = 1

# first things first, let's clear out the contents of the table
table.clear()

# loop through the dictionary and add headers
for dictionary_key , dictionary_value in inventory.items():
    table.appendCol( [ dictionary_key ] )
    # add a blank column for next set of data points
    table.appendCol()

    # add to the list so we can determine the max length of the table
    table_length.append( len( dictionary_value ) )

# set the table length based on the maximum number of dictionary entries
table.setSize( max( table_length ) + 1 , table.numCols )

# loop through dictionary again to fill in table
for dictionary_key , dictionary_value in inventory.items():

# generate an enumerated list to loop through
    value_list = list( enumerate( dictionary_value ) )

# use enumerated list to fill in table 
    for item in value_list:
        table[ item[ 0 ] + 1 , dictionary_key  ] = item[ 1 ]
        table[ item[ 0 ] + 1 , place_holder ] = inventory[ dictionary_key ][ item[ 1 ] ]

# increment placeholder to ensure that our data goes in the right place
    place_holder += 2
```

Okay. Great. But how can we use this to actually do some interesting work?! Well, let's begin by looking at how we might use these as presets. To get started let's build out a simple little example. First we'll add a movie file in TOP and call it 'moviefilein_a', connect this to a mono TOP called 'mono_a', and finally to a level TOP called 'level_a'. We're going to build out two sets of modules on demand for this example. First up is a set of default parameters for our TOPs. This is going to make sure that we can come back to a default position in our presents where nothing is on / nothing has changed in our pipeline. The idea here is that we can figure out the values to make sure that our chain of TOPs is not having any affect on our input texture.

```python
level_defaults = {
    "invert" : 0,
    "blacklevel" : 0,
    "brightness1" : 1,
    "gamma1" : 1,
    "contrast" : 1,
    "gamma2" : 1,
    "opacity" : 1,
    "brightness2" : 1
}

mono_defaults = {
    "mono" : 0,
    "rgb" : 0,
    "alpha" : 4
}
```

Next let's build out a set of cues that we can use to configure our little chain of TOPs.

```python
cue_list = {
    "cue1" : {
        "file" : '/Map/Banana.tif',
        "mono" : 0 ,
        "invert" : 1,
        "brightness" : 0.71,
        "blacklevel" : 0.51,
        "contrast" : 1.93 
    } ,
    "cue2" : {
        "file" : '/Map/Smiley.tif',
        "mono" : 1 ,
        "invert" : 0,
        "brightness" : 1,
        "blacklevel" : 0.51,
        "contrast" : 1.5 
    } ,
    "cue3" : {
        "file" : '/Map/OilDrums.jpg',
        "mono" : 0,
        "invert" : 1,
        "brightness" : 0.71,
        "blacklevel" : 0.51,
        "contrast" : 1.93 
    }
}
```

You'll notice that we've used two different approaches to name space here - that's intentional. In our defaults we can see that we've made sure our key names match exactly to the parameter names on our TOPs. In our cues we can see that we've deviated from that a little. Why? Well, this will let us look at two different ways that we can target parameters when we're using loops.

If we [look back to our experiments with .pars()](https://matthewragan.com/2016/07/06/python-in-touchdesigner-for-loop-touchdesigner/) in looking at for loops, you might remember that we were able to us .pars() to quickly fill in a constant CHOP by ensuring that the contents of our table matched in terms of parameter names. This time around we can do the same thing by using our dictionary as our data structure instead of a table. We can then also quickly loop through the contents of our dictionary and assign values based on key names. 

Let's look briefly at how that might work.

First let's look at how we might build a string to execute:

```python
mono_defaults = mod( op( 'text_defaults' ) ).mono_defaults
level_defaults = mod( op( 'text_defaults' ) ).level_defaults

for keys, values in mono_defaults.items():
    
    #reset mono defaults for A 
    exec( "op( 'mono_a' ).par." + keys + " = " + str( values ) )
    
    # debut print so you can see what this is actually doing
    # print( "op( 'mono_a.par' )." + keys + " = " + str( values ) )

for keys, values in level_defaults.items():
            
    #reset mono defaults for A 
    exec( "op( 'level_a' ).par." + keys + " = " + str( values ) )
```

That works well, but as someone pointed out on the facebook help group, using exec() can cause a set of problems. It's useful to know that we can build an expression as a string, and then execute that command - all dynamically, but we can also use pars():

```python
mono_defaults       = mod( op( 'text_defaults' ) ).mono_defaults
level_defaults      = mod( op( 'text_defaults' ) ).level_defaults

for keys, values in mono_defaults.items():

    #reset mono defaults for A 
    op( 'mono_a' ).pars( keys )[ 0 ].val = values   
    
    # debut print so you can see what this is actually doing
    # print( "op( 'mono_a.par' )." + keys + " = " + str( values ) )

for keys, values in level_defaults.items():
            
#   #reset level defaults for A 
    op( 'level_a' ).pars( keys )[ 0 ].val = values  
```

So far those seem like the same thing?! In this case, they're pretty close. Because our key name matches our parameter name things are pretty straightforward here. Where it gets complicated is when our key names and parameter names don't match. 

Let's use our cue_list dictionary to see how it might be different. Let's imagine that we want to use cue2 as a preset. Now, because our key names and our parameter names don't match, we have to write something like this:

```python
movie_a                     = op( 'moviefilein_a' )
mono_a                      = op( 'mono_a' )
level_a                     = op( 'level_a' )
cue_list                    = mod( op( 'text_cue_list' ) ).cue_list

cue                         = 'cue2'

movie_a.par.file            = app.samplesFolder + cue_list[ cue ][ 'file' ]
mono_a.par.mono             = cue_list[ cue ][ 'mono' ]
level_a.par.invert          = cue_list[ cue ][ 'invert' ]
level_a.par.brightness1     = cue_list[ cue ][ 'brightness' ]
level_a.par.blacklevel      = cue_list[ cue ][ 'blacklevel' ]
level_a.par.contrast        = cue_list[ cue ][ 'contrast' ]
```

You'll notice in the example above, we have to specify how each key and parameter relate to one another. In some cases this might be desirable. How?! You might ask. Well, lets' imagine you have an AB system. In addition to our current set of operators, we'd also have movie_b, mono_b, and level_b. In this case it might be a little more tricky to know when to assign which parameter to which TOP. We might also end up in a situation where there are multiple level tops, so knowing when to target level1 vs. level2 might get a little more complicated. There are lots of ways you might solve these problems cleverly while still using pars(). It's also worth pointing out that sometimes you want to be explicit in your code (probably more often than not), so you know exactly what's happening. The important thing to remember here is that there's a balance to find. You might not find it the first time you write your function or for loop, and it's always okay to refactor your code to make it better. 

Alright, let's put some of these skills to use in an interesting way! We've used dictionaries as data structures, and we just learned how to loop through dictionaries. Let's build out a set of buttons to recall our presets. I'm not going to go through how to make our buttons in detail - here are the cliff notes. Create a new container, add a button0 and give it the name "defaults", next setup a replicator network to make three presets. Let's make sure that our operator prefix is set to "preset" for our operator names when they get replicated. Finally, let's make sure our buttons are set to radio. If all of this sounds like greek to you, make sure you go back and look at how replicators work first, and then look inside the example panel to get a better sense of how I set things up.

Okay! Now we'll use a panel execute DAT (we just learned about panel executes) to recall our presets. We'll use a logic test to run different loops depending on which button is pressed. In our case, Preset 1 - 3 will fill in our chain of operators with the presets from our cue_list dictionary. Clicking in the defaults button will return our chain of operators back to its default state. We can use the scripts we already wrote, and use the panel idea of the radio button selected to make this work. Let's look at what that looks like:

```python
# me - this DAT
# panelValue - the PanelValue object that changed
# 
# Make sure the corresponding toggle is enabled in the Panel Execute DAT.

mono_defaults       = mod( op( 'text_defaults' ) ).mono_defaults
level_defaults      = mod( op( 'text_defaults' ) ).level_defaults

movie_a             = op( 'moviefilein_a' )
mono_a              = op( 'mono_a' )
level_a             = op( 'level_a' )
cue_list            = mod( op( 'text_cue_list' ) ).cue_list

def offToOn(panelValue):
    return

def whileOn(panelValue):
    return

def onToOff(panelValue):
    return

def whileOff(panelValue):
    return

def valueChange(panelValue):
    # default radio button
    if panelValue == 0:
        for keys, values in mono_defaults.items():
            #reset mono defaults for A 
            op( 'mono_a' ).pars( keys )[ 0 ].val = values   
            
        for keys, values in level_defaults.items():                 
        #   #reset level defaults for A 
            op( 'level_a' ).pars( keys )[ 0 ].val = values  

    # for any of our preset buttons
    else:
        cue = 'cue' + str( panelValue )

        movie_a.par.file            = app.samplesFolder + cue_list[ cue ][ 'file' ]
        mono_a.par.mono             = cue_list[ cue ][ 'mono' ]
        level_a.par.invert          = cue_list[ cue ][ 'invert' ]
        level_a.par.brightness1     = cue_list[ cue ][ 'brightness' ]
        level_a.par.blacklevel      = cue_list[ cue ][ 'blacklevel' ]
        level_a.par.contrast        = cue_list[ cue ][ 'contrast' ]
    
    return 
```

I know it's seems like it's been a long journey, but we're now starting to see the real power of python in TouchDesigner. 

## Auto Configuration ##
Let's quickly remember that with the [Op Class we saw how we could create and destroy nodes](https://matthewragan.com/2016/07/06/python-in-touchdesigner-op-class-touchdesigner/). If we combine that with what we've just learned about using data structures and loops, we can begin to look at how we can automate the organization of a network. 

Let's imagine that we want to create a one toe file, and then depending on the IP address of a given machine we want TouchDesigner to set up different configurations. On one machine we might have two projectors, another might have three, another still might be our control machine. How can we make this work? Well, in this case we can store all of that information in a data structure like a python dictionary (you might also use JSON, or XML, or any data structure that you like). Next we'll create a table based on our IP address, next we'll loop through that table and then create our operators. Once you get a feeling for how this works with a table, you'll quickly see how you could skip that step and just do this from the loop itself.

At the heart of this idea is the fact that you can store settings in your data structure, then build out your network based on that information. Alright, let's dig in and get started.

A few things to keep in mind. Your IP address is going to matter. Remember that as you follow long here you'll need to use your own IP address. You'll notice that I've put a "default" address into a text DAT... this is so we can practice, but if you're going to use this idea on a project you'll need to familiarize yourself with the IP addresses, and have some control over how your machines are addressed. 

Okay, to get started lets look at the configuration data we've set up:

```python
uri = {
    "10.0.0.2" : {
        "name" : "mission_control" ,
        "role" : "controller" ,
        "displays" : [
            "control01" 
        ]
    },
    "10.0.0.3" : {
        "name" : "eyes" ,
        "role" : "node" ,
        "displays" : [
            "projector01" , 
            "projector02" 
        ]
    }
}

displays = {
    "control01" : {
        "width" : 1920 ,
        "height" : 1080 ,
        "orientation" : 0
    },
    "projector01" : {
        "width" : 1920 ,
        "height" : 1080 ,
        "orientation" : 0
    },
    "projector02" : {
        "width" : 1920 ,
        "height" : 1080 ,
        "orientation" : 1
    }
}
```

At a glance we can see that we're working with two dictionaries - one called *uri* and the other called *displays*. These dictionaries have their own dictionaries nested inside, and have lists embedded inside as well. What's going on here?! Our URI (uniform resource identifier) is a string key that corresponds to an IP address on a given machine. This key's value pair is a dictionary instead of a single value. The contents of this dictionary are a name, a role, and a list of displays. For more complex configurations you might a much larger number of keys, but for now this should help us see what we're up to. We also have a dictionary of displays. These contain keys related to resolution and orientation. 

Alright, let's put this information to good use. Before we get started we're going to first add two more operators to our network. A table DAT called *table_replicator_info* and a text DAT called *text_default_ip*. We will fill in our table with the contents from our for loop process. For now we will use our default IP to see how this works.

Okay! Now let's write a script to build out a network of ops:

```python
# import any necessary modules

import socket

# define some variables

pos_x               = 3300
pos_y               = 0
replicator_table    = op( 'table_replicator_info' )
system_config       = mod( 'text_data' ).uri
displays            = mod( 'text_data' ).displays
local_ip            = socket.gethostbyname( socket.gethostname() )
default_ip          = op( 'text_default_ip' ).text
local_config        = {}
container_COMPs     = parent().findChildren( type = COMP , depth = 1 )

# clear contents of replicator_table
replicator_table.clear()

# delete existing container COMPs
for items in container_COMPs:
    if op( items ).name != 'container_presets':
        op( items ).destroy()
    else:
        pass

# Test for local_ip in system config
in_system_config = local_ip in system_config

# if our IP matches with a URI in the system config, then we
# fill our dictionary with keys based on the system config file
if in_system_config == True:
    local_config[ 'name' ]      = system_config[ local_ip ][ 'name' ]
    local_config[ 'role' ]      = system_config[ local_ip ][ 'role' ]
    local_config[ 'displays' ]  = system_config[ local_ip ][ 'displays' ]
    local_config[ 'uri' ]       = local_ip

# if our IP doesn't match our system config file, then we fill our
# dictionary with keys based on the default IP address, which is 
# entered in the text dat called 'text_default_ip'
else:
    # assign ip address
    local_ip = default_ip
    local_config[ 'name' ]      = system_config[ local_ip ][ 'name' ]
    local_config[ 'role' ]      = system_config[ local_ip ][ 'role' ]
    local_config[ 'displays' ]  = system_config[ local_ip ][ 'displays' ]
    local_config[ 'uri' ]       = local_ip

# fill table with display information
for items in local_config[ 'displays' ]:
    replicator_table.appendRow( [ 
        items , 
        displays[ items ][ 'width' ] , 
        displays[ items ][ 'height' ] , 
        displays[ items ][ 'orientation' ] 
        ] )

# check and correct height / width based on orientation flag
for row in range( replicator_table.numRows ):
    # create a temporary variable to store the width and height of the display
    width_height = [ replicator_table[ row , 1 ].val , replicator_table[ row , 2 ].val ]

    # test for orientation flag
    # if true, swap height and width
    if replicator_table[ row , 3 ] ==  1:
        replicator_table[ row , 1 ] = width_height[ 1 ]
        replicator_table[ row , 2 ] = width_height[ 0 ]

    # if false, we pass and do nothing
    else:
        pass

# create container COMPs based on our replicator table
for row in range( replicator_table.numRows ):
    # create our new container COMP, give it a name from our replciator table
    new_op = parent().create( containerCOMP , replicator_table[ row , 0 ] )
    
    # set the x position of the new container
    new_op.nodeX = pos_x
    
    # set the y position of the new container
    new_op.nodeY = pos_y

    # set the width of the new node based on the replicator table
    new_op.par.w = replicator_table[ row , 1 ]

    # set the height of the new node based on the replicator table
    new_op.par.h = replicator_table[ row , 2 ]

    # turn on the viewer flag
    new_op.viewer = True

    # increment the y position for the next loop
    pos_y -= 200
```

Why not just use a replicator?! That's an excellent question. This might work just as well using a replicator - but, if we want to know exactly what order a set of operations happens in, and if we want to control when that operation fires then we need to write out a script to do just what we want. It might well seem like some additional work, but being able to work through the process line by line is worth at least learning even if you don't end up using it much.

## JSON ##

JSON, as a format is very similar to python dictionaries, so similar in fact there's a very simple way to work with it. 

If you're already working with dictionaries this will feel like an easy transition. There are, however, a few things you need to keep in mind.

We need to make sure that our JSON is correctly formatted. If you compare the in our final example, with our first example you can see that we've enclosed our entire dictionary in curly brackets {}. You can also see that we've replaced our first variable with a key-value pair.

Let's take a closer look:

```python
# First we need to import the json module. 

import json

# next we're going to use just the text from our text dat
imported_dict       = op( 'text_simple_json' ).text

# next we'll use json.loads to import that as a python dictionary
dict_from_json      = json.loads( imported_dict )

# first let's just print the dictionary to make sure things worked out
print( "Here is our whole json object" )
print( imported_dict )

print( '_ ' * 10 )

# next we could print just the top tier keys
print( "Here are our top tier keys" )
for item in dict_from_json.keys():
    print( item )

print( '\n' )
print( '_ ' * 10 )
# next let's print the keys in our 'inventory' dictionary
print( "Here are the keys in inventory" )
for item in dict_from_json[ 'inventory' ].keys():
    print( item )
    
print( '\n' )
print( '_ ' * 10 )
# since we're on a roll, let's first print our keys, and
# then print their values
print( "Here are the keys and values in inventory" )
for key, value in dict_from_json[ 'inventory' ].items():
    print( key, 'contains', value )

print( '\n' )
print( '_ ' * 10 )
# That's still not very pretty, so let's see if we can make 
# something that's a little nicer
print( "Pretty printing our keys and values" )
for key, value in dict_from_json[ 'inventory' ].items():
    print( key, 'contains' )
    
    for item, quantity in value.items():
        print( quantity, item )
    
    print( '\n' )
```

With some easy ways to work with dictionaries under your belt challenge yourself to use these in an interesting way!