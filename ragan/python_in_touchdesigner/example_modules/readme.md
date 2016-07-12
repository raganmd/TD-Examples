# Python in TouchDesigner #

## Programmer / Artist ##

**Matthew Ragan** | [ matthewragan.com](http://matthewragan.com)  

## example_modules ##

There are a number of ways that we might use modules on demand in TouchDesigner. Before we get too far along, however, we might first ask "what is a module on demand?"

According to the [TouchDesigner wiki](http://derivative.ca/wiki088/index.php?title=MOD_Class):

```
The MOD class provides access to Module On Demand object, which allows DATs to be dynamically imported as modules. It can be accessed with the mod object, found in the automatically imported td module. Alternatively, one can use the regular python statement: import. Use of the import statement is limited to modules in the search path, where as the mod format allows complete statements in one line, which is more useful for entering expressions. Also note that DAT modules cannot be organized into packages as regular file system based python modules can be.
```

What does this mean? It's hard to sum up in just a single sentence, but the big thing to take away is that we can essentially use any text DAT to hold whole functions for us that we can then call whenever we want.

Let's take a closer look at this process. We'll start with some simple ideas, then work our way up to something a little more complicated.

First we turn things way down, and just think about storing variables. To be clear, we probably wouldn't use this in a project, but it can be helpful for us when we're trying to understand what exactly is going on here.

Let's create a new text DAT and call it "text_variables", inside let's put the following text:

```python
width       = 1280
height      = 720

budget      = 'small'
```

Using the mod class we can access these variables in other operators! To do this we'll use the following syntax:

```python
mod( 'text_variables' ).width
mod( 'text_variables' ).height
mod( 'text_variables' ).budget
```

Try adding a constant CHOP, and a text TOP to your network and using the expressions above to retrieve these values.

Next try printing these values:

```python
print( mod( 'text_variables' ).width )
print( mod( 'text_variables' ).height )
print( mod( 'text_variables' ).budget )
```

So, it looks like we can access the contents of a module as a means of storing variables. That's hip. Let's take a moment and circle back to one of the other use cases that we've already seen for a module. More than just a single value, we can also put a whole dictionary in a module and then call it on demand. We've already done this in some of our previous examples, but we can take a quick look at that process again to make sure we understand.

Let's create a new text DAT called "text_dictionary_as_module", inside of this text DAT let's define the following dictionary:

```python
fruit = {
    "apple" : 10,
    "orange"    : 5,
    "kiwi"  : 16
}
```

Let's first print the whole dictionary object:

```python
print( mod( 'text_dictionary_as_module' ).fruit )
```

Alternatively, we can also access individual keys in the dictionary:

```python
mod( 'text_dictionary_as_module' ).fruit[ 'apple' ]
mod( 'text_dictionary_as_module' ).fruit[ 'orange' ]
mod( 'text_dictionary_as_module' ).fruit[ 'kiwi' ]
```

What can you do with this?! Well, you might store your config file in a text DAT that you can call from a module on demand. You might use this to store configuration variables for your UI - colors, fonts, etc. ; you might decide to use this to configure some portion of a network, or to hold on to data that you want to recall later; or really any number of things.

Before we get too excited about storing variables in modules on demand, let's look at an even more powerful feature that will help us better understand where they really start to shine. 

Up next we're going to look at writing a simple function that we can use as a module on demand. In addition to writing some simple little functions, we're also going to embrace docstrings - a feature of the python language that makes documenting your work easier. Docstings allow us to leave behind some notes for our future selves, or other programmers. One of the single most powerful changes you can make to how you work is to document your code. It's a difficult practice to establish, and can be frustrating to maintain - but it is hands down one of the most important changes you can make in how you work. 

Alright, I'll get off my documentation soapbox for now. Let's write a few methods and see how this works in TouchDesigner.

We can start by creating a new text DAT called "text_simple_reutrn", inside of this DAT we'll write out our new functions:

```python
def multi_by_two( value ):
    '''Multiplies input value by 2

    A simple example function to see how we can use modules on demand.
    This module takes a single argument which is multiplied by 2 and
    then returned from the function.
    
    Arguments
    --------------- 
    value( int / float ) - numeric value to be multiplied by 2

    Returns
    ---------------
    new_val( int / float ) - value * 2

    Notes
    ---------------
    These are doc strings - they're a feature of the Python language
    and make documenting your code all easier. This format is based largely
    on Google's Python documentation format - though not exactly. It's 
    generally good practice to document your work, leaving notes both for 
    your future self, as well as for other programmers who might be using
    your code in the future.
    '''
    new_val             = value * 2
    
    return new_val

def logic_test( even_or_odd ):
    '''Tests if input value is even or odd

    This is a simple little function to test if an integer is even or odd.
    
    Arguments
    --------------- 
    even_or_odd( int ) - an integer to be tested as even or odd

    Returns
    ---------------
    test( str ) - string result of the even / odd test

    Notes
    ---------------
    These are doc strings - they're a feature of the Python language
    and make documenting your code all easier. This format is based largely
    on Google's Python documentation format - though not exactly. It's 
    generally good practice to document your work, leaving notes both for 
    your future self, as well as for other programmers who might be using
    your code in the future.
    '''
    if even_or_odd % 2:
        test                = "this value is odd"

    else:
        test                = "this value is even"

    return test


def logic_test_two( value ):
    '''Silly logit test example

    Another simple function, this one to see another example of a 
    logic test working in a module on demand.
    
    Arguments
    --------------- 
    value( int / float / str / bool ) - a value to be tested

    Returns
    ---------------
    test( str ) - a string indicating the status of the test

    Notes
    ---------------
    These are doc strings - they're a feature of the Python language
    and make documenting your code all easier. This format is based largely
    on Google's Python documentation format - though not exactly. It's 
    generally good practice to document your work, leaving notes both for 
    your future self, as well as for other programmers who might be using
    your code in the future.
    '''
    if value == "TouchDesigner":
        test                = "Nice work"

    else:
        test                = "Try again"

    return test
```

Great! But what can we do with these?
We can start by using some eval DATs or print statements to see what we've got. I'm going to use eval DATs. Let's add several to our network and try out some calls to our new module on demand. First let's look at the generic syntax:

**mod( name_of_text_dat ).name_of_method**

In practice that will look like:
```python
mod( 'text_simple_reutrn' ).multi_by_two( 5 )
mod( 'text_simple_reutrn' ).multi_by_two( 2.5524 )
mod( 'text_simple_reutrn' ).logic_test( 5 )
mod( 'text_simple_reutrn' ).logic_test( 6 )
mod( 'text_simple_reutrn' ).logic_test_two( "TouchDesigner" )
```

Now we can see that we wrote several small functions that we can then call from anywhere, as long as we know the path to the text DAT we're using as a module on demand! Here's where we start to really unlock the potential of modules on demand. As we begin to get a better handle on the kind of function we might write / need for a project we can begin to better understand how to take full advantage of this feature in TouchDesiger.

## Doc Strings ##
Since we took the time to write out all of those doc strings, let's look at how we might be able to print them out! Part of what's great about doc strings is that there's a standard way to retrieve them, and therefore to print them. This means that you can quickly get a some information about your function printed right in the text port. Let's take a closer look by printing out the doc stings for all of our functions:

```python
# first let's clear the text port to make sure we're starting fresh
clear()

# Here we're printing out the doc strings for multi_by_two
print( "The Doc Strings for multi_by_two are:" )
print( '\n' ) 
print( mod( 'text_simple_reutrn' ).multi_by_two.__doc__ )

# Here we're printing out the doc strings for lotic_test
print( "The Doc Strings for logic_test:" )
print( '\n' ) 
print( mod( 'text_simple_reutrn' ).logic_test.__doc__ )

# Here we're printing out the doc strings for logic_test_two
print( "The Doc Strings for logic_test_two:" )
print( '\n' ) 
print( mod( 'text_simple_reutrn' ).logic_test_two.__doc__ )
```

That worked pretty well! But looking back at this it seems like we repeated a lot of work. [We just learned about for loops](https://matthewragan.com/2016/07/06/python-in-touchdesigner-for-loop-touchdesigner/), so let's look at how we could do the same thing with a loop instead:

```python
# first let's clear the text port to make sure we're starting fresh
clear()

# rather than wasting our time writing all the code in the other example, 
# instead let's write a for loop to automate that process.
# We'll start by first making a list of all of the methods we want to print 
# doc strings for
methods                         = [
                                "multi_by_two",
                                "logic_test",
                                "logic_test_two"
                                    ]

# next we'll make a smiple placeholder expression that we can 
# pass each method into so we can print it out easily
doc_string_temp                 = "mod( 'text_simple_reutrn' ).{target_function}.__doc__"

# finally we write a little for loop to go through all items in our list
# and pretty print their doc strings to the text port
for method in methods:
    print( "The Doc Strings for {} are:".format( method ) )
    temp_doc                    = doc_string_temp.format( target_function = method )
    print( eval( temp_doc ) )
    print( "= "  * 10 )

```

## A Practical Example ##
This is all fun and games, but what can we do with this? There are any number of functions you might write for a project, but part of what's exciting here is the ability to write something re-usable in Python. What might that look like? Well, let's look at an example of a logger. There are a number of events we might want to log in TouchDesigner when we have a complex project.

In our case we'll write out a method that allows a verbose or compact message, a way to print it to the text port or not, and a way to append a file or not. Alright, here goes:

```python
import datetime

log_file            = op( 'text_log' )

full_text           = '''{now}

Current Year        | {year}
Current Month       | {month}
Current Day         | {day}
Current Hour        | {hour}
Current Minute      | {minute}
Current Second      | {second}
Current Microsecond | {microsecond}
'''

verbose_log_message = '''============================
VERBOSE MESSAGE

On {month}-{day}-{year} at {hour}:{minute}:{second}
----------------------------
operator            || {operator}
At Network Location || {path}

----------------------------
Logged
{message}
============================
'''

log_message         = '''----------------------------
{now}
----------------------------
{operator}
{path}
{message}
'''

def Full_date():
    '''Create a formatted time stamp

    A look at how we might create a formatted time stamp to use with
    various logging applications.
    
    Arguments
    --------------- 
    None

    Returns
    ---------------
    formatted_text( str ) - a string time stamp

    Notes
    ---------------
    '''

    now         = datetime.datetime.now()
    year        = datetime.datetime.now().year
    month       = datetime.datetime.now().month
    day         = datetime.datetime.now().day
    hour        = datetime.datetime.now().hour
    minute      = datetime.datetime.now().minute
    second      = datetime.datetime.now().second
    microsecond = datetime.datetime.now().microsecond

    formatted_text = full_text.format(
                                        now         = now,
                                        year        = year,
                                        month       = month,
                                        day         = day,
                                        hour        = hour,
                                        minute      = minute,
                                        second      = second,
                                        microsecond = microsecond
                                        )
    return formatted_text

def Log_message( operator, message, verbose=False, text_port_print=True, append_log=True ):
    '''Logging Method.

    A simple look at how you might start to think about building a logger for a TouchDesigner application. A logger is a great way to build out files with time stamped events. The more complex a project becomes, the more important it can become to have some means of logging the operations of your program. Here's a simple look at what that might look like.
    
    Arguments
    --------------- 
    operator( touch object ) - the touch object whose path you'd like included in the log message
    message( str ) - a message to include in the log
    verbose( bool ) - a toggle for verbose or compact messages
    text_port_print( bool ) - a toggle to print to the text port, or not
    append_log( bool ) - a toggle to append to the log file , or not

    Returns
    ---------------
    None

    Notes
    ---------------
    You'll notice that some arguments receive default values. This is so you don't have
    to include them in the call. This means that by default the message will be compact, 
    will print to the text port, and will append the log file.
    '''

    now         = datetime.datetime.now()
    year        = datetime.datetime.now().year
    month       = datetime.datetime.now().month
    day         = datetime.datetime.now().day
    hour        = datetime.datetime.now().hour
    minute      = datetime.datetime.now().minute
    second      = datetime.datetime.now().second
    microsecond = datetime.datetime.now().microsecond

    path        = op( operator ).path
    op_name     = op( operator ).name

    if verbose:
        message = verbose_log_message.format(
                                                month       = month,
                                                day         = day,
                                                year        = year,
                                                hour        = hour,
                                                minute      = minute,
                                                second      = second,
                                                operator    = op_name,
                                                path        = path,
                                                message     = message
                                            )
    else:
        message = log_message.format(
                                        now                 = now,
                                        operator            = op_name,
                                        path                = path,
                                        message             = message
                                    )
    
    if text_port_print:
        print( message )
    
    else:
        pass

    if append_log:
        log_file.write( '\n' + message )

    else:
        pass
    return
```

So now that we've written out the method, what would call for this look like?
```python
operator = me

message ='''
Just a friendly message from your TouchDesigner Network.
Anything could go here, an error message an init message.

You dream it up, and it'll print
'''

# print and append log file with a verbose log message
mod( 'text_module1' ).Log_message( operator, message, verbose = True )

# print and append log file with a compact log message
# mod( 'text_module1' ).Log_message( operator, message )


# append log file with verbose log message
# mod( 'text_module1' ).Log_message( operator, message, verbose = True, text_port_print = False )


# print a compact log message
# mod( 'text_module1' ).Log_message( operator, message, append_log = False )
```

Take a moment to look at the example network and then un-comment a line at a time in the text DAT with the script above. Take note of how things are printed in the text port, or how they're appended to a file. This is our first generalized function that has some far reaching implications for our work in touch. Here we've started with a simple way to log system events, both to a file and to the text port. This is also a very re-usable piece of code. There's nothing here that's highly specific to this project, and with a little more thought we could turn this into a module that could be dropped into any project.

## Local Modules ##
We've learned a lot so far about modules on demand, but the one glaring shortcoming here is that we need the path to the text DAT in question. That might not be so bad in some cases, but in complex networks writing a relative path might be complicated, and using an absolute path might be limiting. What can we do to solve this problem. We're in luck, as there's one feature of modules we haven't looked at just yet. We can simplify the calling / locating of modules with a little extra organization. 

First we need to add a base and rename it to "local", inside of this base add another base and rename it to "modules". Perfect. I'm going to reuse one of our existing code examples so we can see a small change in syntax here. I've also changed the name of the text DAT inside of local>modules to "simple_return". 

```python
mod.simple_return.multi_by_two( 5 )
mod.simple_return.multi_by_two( 2.5524 )
mod.simple_return.logic_test( 5 )
mod.simple_return.logic_test( 6 )
mod.simple_return.logic_test_two( "TouchDesigner" )
mod.simple_return.logic_test_two( 10 )
```

Looking at the above, we can see that we were able to remove the parentheses after "mod". But what else changed? Why is this any better? The benefit to placing this set of functions in local>modules is that as long as you're inside of this component, you no longer need to use a path to locate the module you're looking for.

Alright, now it's time for you to take these ideas out for a test drive and see what you can learn.