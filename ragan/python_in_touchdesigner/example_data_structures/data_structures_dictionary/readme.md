# Python in TouchDesigner #

## Programmer / Artist ##

**Matthew Ragan** | [ matthewragan.com](http://matthewragan.com)  

## example_data_structures_dictioaries ##

Dictionaries are another type of data structure that we can use in Python. They're similar to lists in that we can store information in them, and retrieve them easily. Dictionaries, however, are distinctly different from lists. Where lists are index based - which is to say that they have a specific order - dictionaries are key based. 

What does that mean, and why do we care?! We think of dictionaries as being a pair of things a key, and a value. We might think of this as a name and its corresponding piece of information. Let's look at something simple to get started. To get started let's go back to our grocery example when we were talking about lists. In making a list for our trip to the grocery store we listed all of the items we needed from the store. We didn't however, make any notes about quantity. Let's quickly make that list again:

```python
grocery_list = [ 'eggs' , 'milk' , 'bread' , 'butter' , 'coffee' ]
```

This is great, and it tells us lots of information, but maybe not all of the information we need. If I'm going to the store myself, this is a fine list. If I'm asking someone else to pick up these things for me, well then I need at least one other piece of information - quantity. If we're using lists, we might do something clever, like make a list of lists with two items - the grocery item, and the desired quantity. That might look something like this:

```python
grocery_list = [ 
    ['eggs' , '1 dozen' ] , 
    ['milk' , '1 pint' ] , 
    ['bread' , '2 loaves' ] , 
    ['butter' , '1 lb' ] , 
    ['coffee', '2 lbs' ]
]
```

This works fine, and might be a great way to hold onto this information. We can, however, use a dictionary to do this same thing. In this case we're going to think of our grocery items as a keys, and quantities as values. Let's look at what means:

```python
grocery_list = {
    'eggs' : '1 dozen' , 
    'milk' : '1 pint' , 
    'bread' : '2 loaves' , 
    'butter' : '1 lb' , 
    'coffee': '2 lbs'
}
```

It's important to note that I've used some indenting to make this easier to read, but another perfectly valid way to write this dictionary would be:

```python
grocery_list = { 'eggs' : '1 dozen' , 'milk' : '1 pint' , 'bread' : '2 loaves', 'butter' : '1 lb' , 'coffee': '2 lbs' }
```

I just happen to think that anytime you can make something easier to read by a human, the better.

Okay,  let's talk about syntax here for a second. So the first thing we did was declare our dictionary as a variable. Next we used curly brackets to open our dictionary ( {} - these are curly brackets ). Next we wrote out our dictionary as key and value pairs separated by a colon - keys on the left, values on the right. Now in this example all of our values were strings, but they could just as easily have been integers, floats, booleans, lists, or even other dictionaries. 

This is all well and good, but how do we get things out of our dictionary? We know how to retrieve things from a list, but a dictionary is a little different. When retrieving something from a dictionary we typically use a key. Let's consider our first example again for a second. Let's say we want to print out the quantity of eggs that we're supposed to get from the store. We can do that like this:

```python
print( grocery_list[ 'eggs' ] )
```

We can also retrieve the contests of dictionary with .keys() and .values():

```python
print( grocery_list.keys() )
print( grocery_list.values() )
```

In both of these cases we get a list of keys or values.

It's also important to know how to add items to our dictionary. There are a few ways to go about this, but let's just look at one for now. We should start by creating an empty dictionary:

```python
my_dictionary = {}
```

Now that we have an empty dictionary, we can add items to it. We do this by starting with the dictionary name, then placing the key in square brackets ([] these things), followed by an equal sign, and then what we want to be placed into the dictionary as the value. Let's look at an example:

```python
my_dictionary[ 'new_item1' ] = "cookies"
```

Okay, now that we've added one key value pair, let's print out the keys and values in our list (to practice), and add a few more items:

```python
my_dictionary = {}

my_dictionary[ 'new_item1' ] = "cookies"

print( my_dictionary.keys() )
print( my_dictionary.values() )

my_dictionary[ 'new_item2' ] = "cell_phones"

print( my_dictionary.keys() )
print( my_dictionary.values() )

my_dictionary[ 'new_item3' ] = 55

print( my_dictionary.keys() )
print( my_dictionary.values() )

my_dictionary[ 'new_item4' ] = [ 1 , 2 , 3 ]

print( my_dictionary.keys() )
print( my_dictionary.values() )
```

Wait... what did we just do there with item4?! Most of that should look pretty straightforward, and hopefully that makes sense for the most part. It is not, however, the most exciting part of using dictionaries. Dictionaries become the most exciting when we start to see how we can nest other lists or dictionaries inside of them.

Let's look at a dictionary of mixed contents:

```python
my_dictionary = { 
    "apple" : "these are delicious" , 
    "orange" : 12 , 
    "kiwi" : 55.5 , 
    "lots_of_things" : [
        "paper" , 
        "pens" ,
        44 , 
        10.4
    ] 
}
```

So we know how to get to the values associated with "apple" , "orange" , and "kiwi" , but how do we get to the contents of that list? Well, we can write something like this:

```python
print( my_dictionary[ 'lots_of_things' ][ 0 ] )
print( my_dictionary[ 'lots_of_things' ][ 1 ] )
print( my_dictionary[ 'lots_of_things' ][ 2 ] )
print( my_dictionary[ 'lots_of_things' ][ 3 ] )
```

Here we see the same syntax that we use when retrieving list items. 

That's wonderful! So what about when we store dictionaries inside of dictionaries? Let's look at a simple example. We can start by creating a dictionary with fruit's as our keys. Each fruit will have a corresponding dictionary of quantity, origin, and if the fruit is organic. Okay, what would that look like:

```python
my_dictionary_of_dictionaries = { 
    "apple" : {
        "quantity" : 10 ,
        "origin" : "Vermont" ,
        "organic" : True    
    } , 
    "orange" : {
        "quantity" : 20 ,
        "origin" : "Califronia" ,
        "organic" : False
    } , 
    "kiwi" : {
        "quantity" : 26 ,
        "origin" : "Mexico" ,
        "organic" : False
    } , 
    "grapes" : {
        "quantity" : 50 ,
        "origin" : "Preu" ,
        "organic" : True
    }
}
```

That's pretty snazzy and all, but how do we pull things out of this data structure? We can follow the example we learned with lists, but instead of using index values, we can instead use keys. Let's look at just apple to get started:

```python
print( "Let's just look at apple" )
print( "quanitity -" , my_dictionary_of_dictionaries[ 'apple' ][ 'quantity' ] )
print( "origin -" , my_dictionary_of_dictionaries[ 'apple' ][ 'origin' ] )
print( "organic -" , my_dictionary_of_dictionaries[ 'apple' ][ 'organic' ] )
```

Here we can see that we start with our dictionary, with a key in square brackets, followed by another key in square brackets. Practice retrieving other keys - what about grapes, or oranges? Also practice by adding other keys inside of the fruit dictionaries. Don't forget to pay careful attention to where you've placed your commas and, remember that keys are strings so they need quotation marks.

Once you've done that, let's consider how we might use something like a dictionary here in TouchDesigner. We're going to look something a little complex, but still relatively simple to help us get our bearings. Dictionaries can be a great help to us when we want to do things like creating save states. Let's first think about what it would mean to set the properties of a text TOP with the contents of a dictionary.

Let's start by making our dictionary. I'm going to use the same names for our dictionary keys that we find in our parameter names - just to make sure we know exactly where a value is going.

```python
top_dictionary = { 
    "text" : 'monkey' , 
    "fontsizex" : 15 ,
    "alignx" : 1 ,
    "aligny" : 1 ,
    "fontcolorr" : 1.0 ,
    "fontcolorg" : 0.0 ,
    "fontcolorb" : 0.0 ,
    "fontalpha" : 1.0 ,
    "bgcolorr" : 0.0 ,
    "bgcolorg" : 0.0 ,
    "bgcolorb" : 0.0 ,
    "bgalpha" : 1.0
}
``` 

Now let's flesh out our script to change the parameters of our TOP:

```python
target_text = op( 'text1' )

target_text.par.text = top_dictionary[ 'text' ]
target_text.par.fontsizex = top_dictionary[ 'fontsizex' ]
target_text.par.alignx = top_dictionary[ 'alignx' ]
target_text.par.aligny = top_dictionary[ 'aligny' ]
target_text.par.fontcolorr = top_dictionary[ 'fontcolorr' ]
target_text.par.fontcolorg = top_dictionary[ 'fontcolorg' ]
target_text.par.fontcolorb = top_dictionary[ 'fontcolorb' ]
target_text.par.fontalpha = top_dictionary[ 'fontalpha' ]
target_text.par.bgcolorr = top_dictionary[ 'bgcolorr' ]
target_text.par.bgcolorg = top_dictionary[ 'bgcolorg' ]
target_text.par.bgcolorb = top_dictionary[ 'bgcolorb' ]
target_text.par.bgalpha = top_dictionary[ 'bgalpha' ]
```

That's pretty great - but goodness that's a lot of work just to change some settings. How might we think about using this idea to create a preset system? We're not that far off form this idea at this point, so let's dig in a little deeper. To really make this work, we need to revisit our dictionary. Specifically, we need to encapsulate our presets inside another layer. We need to make them their own dictionary as a set of values for another key. For example, we might want a named structure like "preset1" , "preset2" etc. to be how we retrieve settings. Let's change our dictionary to make that happen:

```python
top_dictionary = { 
    "preset1" : {
        "text" : 'monkey' , 
        "fontsizex" : 15 ,
        "alignx" : 1 ,
        "aligny" : 1 ,
        "fontcolorr" : 1.0 ,
        "fontcolorg" : 0.0 ,
        "fontcolorb" : 0.0 ,
        "fontalpha" : 1.0 ,
        "bgcolorr" : 0.0 ,
        "bgcolorg" : 0.0 ,
        "bgcolorb" : 0.0 ,
        "bgalpha" : 1.0
        } ,
    "preset2" : {
        "text" : 'pig' , 
        "fontsizex" : 80 ,
        "alignx" : 1 ,
        "aligny" : 0 ,
        "fontcolorr" : 0.0 ,
        "fontcolorg" : 0.0 ,
        "fontcolorb" : 1.0 ,
        "fontalpha" : 1.0 ,
        "bgcolorr" : 1.0 ,
        "bgcolorg" : 1.0 ,
        "bgcolorb" : 1.0 ,
        "bgalpha" : 1.0
    }
}
```

Not bad. Now, how can apply these presets to our top? To do this we're going to do one tricky thing. We're going to write our scripts so that a python variable can stand in our first key. This will mean that we only need to change a single variable before re-running our script. That would look like this:

```python

target_text = op( 'text1' )
dictionary_preset = 'preset2'

target_text.par.text = top_dictionary[ dictionary_preset ][ 'text' ]
target_text.par.fontsizex = top_dictionary[ dictionary_preset ][ 'fontsizex' ]
target_text.par.alignx = top_dictionary[ dictionary_preset ][ 'alignx' ]
target_text.par.aligny = top_dictionary[ dictionary_preset ][ 'aligny' ]
target_text.par.fontcolorr = top_dictionary[ dictionary_preset ][ 'fontcolorr' ]
target_text.par.fontcolorg = top_dictionary[ dictionary_preset ][ 'fontcolorg' ]
target_text.par.fontcolorb = top_dictionary[ dictionary_preset ][ 'fontcolorb' ]
target_text.par.fontalpha = top_dictionary[ dictionary_preset ][ 'fontalpha' ]
target_text.par.bgcolorr = top_dictionary[ dictionary_preset ][ 'bgcolorr' ]
target_text.par.bgcolorg = top_dictionary[ dictionary_preset ][ 'bgcolorg' ]
target_text.par.bgcolorb = top_dictionary[ dictionary_preset ][ 'bgcolorb' ]
target_text.par.bgalpha = top_dictionary[ dictionary_preset ][ 'bgalpha' ]
```

Alright. Looking closely at the above, we can see that we need only change the variable "dictionary_preset" in order to fetch a whole different set of values. Not bad, right? 

Take some time to experiment with these ideas. As we head forward we're going to start to look at how we can use executes and for loops to see how we can really start to make headway in using Python. We've laid a lot of ground work so we can really plow ahead.

[Learn more about Python Data Structures](https://docs.python.org/3.3/tutorial/datastructures.html)
[THP 494 & 598 | Python Dictionaries](http://matthewragan.com/2015/03/31/thp-494-598-python-dictionaries-touchdesigner/)
[TouchDesigner | FB HelpGroup | Presets](http://matthewragan.com/2015/07/29/touchdesigner-fb-helpgroup-presets/)