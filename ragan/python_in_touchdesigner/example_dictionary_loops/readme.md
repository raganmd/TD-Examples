# Python in TouchDesigner #

## Programmer / Artist ##

**Matthew Ragan** | [ matthewragan.com](http://matthewragan.com)  

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


[Learn more about enumerate()](https://docs.python.org/3.4/library/functions.html#enumerate)
[Learn more about items()](https://docs.python.org/3.4/library/stdtypes.html#dict)