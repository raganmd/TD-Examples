# Python in TouchDesigner #

## Programmer / Artist ##

**Matthew Ragan** | [ matthewragan.com](http://matthewragan.com)  

## example_op_class ##

[The OP Class](http://www.derivative.ca/wiki088/index.php?title=OP_Class)

Taking some time to really understand how you might take better advantage of classes when using Python in TouchDesigner is well worth the time and effort - even if frustrating and intimidating at first. Chances are, you've already used some class methods without even knowing it, and here we're going to take a quick opportunity to better understand them, and how you might use them. 

In the last example we looked at functions, and I mentioned that methods are also functions - in the same way that all squares are rectangles, but squares are a special kind of rectangle. Similarly, methods are a special kind of function. Special in that they belong to a class. In a highly simplified way, we might think of a class as a grouping a functions with a particular purpose. We can also use dot notation to access the members of a class. Let's look at a simple example. For a hot second we're going to depart from TouchDesigner and just talk about this problem as a programmer, then we'll return to how this works and looks in Touch. Let's imagine you want to put together a set of conversion tools. One approach would be to put all of your conversion functions together into one big class. If you're only dealing with a few hundred lines of code that might be fine, but over time you're likely going to need to keep updating this class, or you might find that it's thousands of lines long suddenly and a bit unruly to wrangle. You might instead choose to separate functions into different classes that are thematically related. We might, in this case, choose to write a Temperature Conversion Class, and a Measurement Conversion Class as separate collections of code. That might look like this:

```Python
class TemperatureConversion():
    
    def F_to_C( self, temp_in_F ):

        temp_in_C = ( temp_in_F - 32 ) * ( 5/9 )
    
    return temp_in_C

    def C_to_F( self, temp_in_C ):
        
        temp_in_F = ( temp_in_C * ( 9/5 ) ) + 32
    
    return temp_in_F

class MeasurementConversion():
    
    def Inches_to_Centimeters( self, inches ):
        
        centimeters = inches * 2.54

    return centimeters

    def Centimeters_to_Inches( self centimeters ):
        
        inches = centimeters * 0.39
    
    return inches
```

So what's the benefit here? Now when calling one of these functions we can use dot notation in order to get the results. For example:

```Python
print( TemperatureConversion.F_to_C( 50 ) )
print( TemperatureConversion.C_to_F( 100 ) )
print( MeasurementConversion.Inches_to_Centimeters( 12 ) )
print( MeasurementConversion.Centimeters_to_Inches( 1200 ) )
```

Organizationally, here we can easily see how our different classes give us a quick way to separate functions. Whew. Alright, that's a lot of back-story in order to help us have a way to think about classes in TouchDesigner. We have to think / know about classes because that's a part of organizational structure that we're relying on when we use any dot notation for a method call. The Op Class applies to all operators in TouchDesigner, which means that the methods associated with it can be called in relation to any op - part of the reason we're working through what that means.

Okay, let's look at some examples. If you haven't already looked at the wiki page about the [Op Class](http://www.derivative.ca/wiki088/index.php?title=OP_Class), you should do that now.

In the next group of examples we're going to use the Eval DAT in order to see how we can evaluate expressions quickly and easily. I frequently use the Eval DAT for just this reason, so I can see which parts of my expressions are working and which parts aren't. Okay. Let's first look at digits:

```Python
me.digits
```

Digits returns the integer number associated with an operator. In the example above we get the digits for the operator in question. In the example network it's returning the digits for the operator table1.

Let's look at another use of digits:

```Python
op( 'table2' ).digits
```

In this example we're asking for the digits for table2. Now, it might seem a little useless to ask for the digits of an operator you already know the digits for, but it's not hard to imagine a situation where this becomes very handy. This is especially useful when we use replicators. 

```Python
parent().digits
```

The above, for example, is a great way to get get the digits of a parent. When using a replicator you might use this approach to increment through the rows of a source table. 

Let's look at some variations on the way you might retrieve the name of an operator:

```Python
parent().name
me.parent().name
op( '..' ).name
op( '/python_in_touchdesigner/example_op_class' ).name
```

All of the above return the same result. parent() is a method that accepts an argument for relational distance. Let's say we wanted to get information from our grandparent component:

```Python
parent(2).name
me.parent(2).name
op( '../..' ).name
op( '/python_in_touchdesigner' ).name
```

Great, but what other kinds of methods can we use? Before the findOp DAT existed, you might use the findChildren() method to retrieve information about operators in a given component. In this case, I'm using a table generate rows for every operator in a component, and then using an Eval DAT to write one expression that's uniquely evaluated for each row:

```Python
parent().children[ me.inputRow ]
```

Alright, one more time let's go back to the wiki article on the Op Class. This time we're going to take what we've learned about the Eval DAT, and what we've learned about classes to look at all of the methods we have access to for a text TOP. Let's write out an expression for each of the methods:

```Python
'valid' op( 'text2' ).valid
'id'    op( 'text2' ).id
'name'  op( 'text2' ).name
'path'  op( 'text2' ).path
'digits'    op( 'text2' ).digits
'base'  op( 'text2' ).base
'passive'   op( 'text2' ).passive
'time'  op( 'text2' ).time
'activeViewer'  op( 'text2' ).activeViewer
'allowCooking'  op( 'text2' ).allowCooking
'bypass'    op( 'text2' ).bypass
'cloneImmune'   op( 'text2' ).cloneImmune
'current'   op( 'text2' ).current
'display'   op( 'text2' ).display
'expose'    op( 'text2' ).expose
'lock'  op( 'text2' ).lock
'selected'  op( 'text2' ).selected
'render'    op( 'text2' ).render
'viewer'    op( 'text2' ).viewer
'nodeHeight'    op( 'text2' ).nodeHeight
'nodeWidth' op( 'text2' ).nodeWidth
'nodeX' op( 'text2' ).nodeX
'nodeY' op( 'text2' ).nodeY
'nodeCenterX'   op( 'text2' ).nodeCenterX
'nodeCenterY'   op( 'text2' ).nodeCenterY
'inputs'    op( 'text2' ).inputs
'outputs'   op( 'text2' ).outputs
'type'  op( 'text2' ).type
'subType'   op( 'text2' ).subType
'label' op( 'text2' ).label
'family'    op( 'text2' ).family
'isFilter'  op( 'text2' ).isFilter
'minInputs' op( 'text2' ).minInputs
'maxInputs' op( 'text2' ).maxInputs
'isMultiInputs' op( 'text2' ).isMultiInputs
'visibleLevel'  op( 'text2' ).visibleLevel
'isBase'    op( 'text2' ).isBase
'isCHOP'    op( 'text2' ).isCHOP
'isCOMP'    op( 'text2' ).isCOMP
'isDAT' op( 'text2' ).isDAT
'isMAT' op( 'text2' ).isMAT
'isObject'  op( 'text2' ).isObject
'isPanel'   op( 'text2' ).isPanel
'isSOP' op( 'text2' ).isSOP
'isTOP' op( 'text2' ).isTOP
```

You'll notice that I've separated the name of the method from the expression with a tab. This way when we feed our Eval DAT we get two columns - one with the name of the method, and another with the returned value.

You'll notice that some methods are marked as ( Read Only ). This means that we can see information in calling these methods, but we can't change anything about our Operator. Let's look at an example of how we can make a change to an operator. Color is something we can change for any operator. I'm going to add three text DATs to my network. One operator to act on, and two text DATs where I'm going to write a simple script. First let's change the color of our operator to red:

```Python
target_op = op( 'text1' )

target_op.color = ( 1 , 0  , 0 )
```

If we right click and run this script we'll see that we've changed the color of our operator! Wait, let's change it back:

```Python
target_op = op( 'text1' )

target_op.color = ( 0.5450000166893005 , 0.5450000166893005 , 0.5450000166893005 )
```

Perfect. This might seem like a silly example, but it brings to our attention how we might use various class methods to make changes to our networks. As a quick note, you might notice that I've written my scripts in two lines when I could have written them in one. Right? Why write:

```Python
target_op = op( 'text1' )

target_op.color = ( 1 , 0  , 0 )
```

When I could just write:

```Python
op( 'text1' ).color = ( 1 , 0  , 0 )
```

Part of the way that I work these days is to anticipate that I'm going to incorporate the pieces of a test script into a larger method or function. Separating the operator from the function call makes it much easier to begin thinking about how I might extend this simple script in the future. I could easily start to think of writing a function that looked like:

```Python
def Make_ops_red( op_path ):
    target_op = op( op_path )

    target_op.color = ( 1, 0, 0 )
    return
```

Okay, let's look at one other interesting thing we might consider. What if we wanted to script the processing adding ops to a network? We can do just this with the copy method:

```Python
# create a new variable called new_op
# this is also a copy of the operator out 1
new_op = parent().copy( op( 'moviefilein1' ) )

# since we've defind our new op with the variable
# name new_op we can continue to use this name
# our next step will be to give it a name
new_op.name = 'moviefilein_new_op'

# finally we're going to change the location of
# our new operator. In this example we want it
# created at a location in relation to our original
# operator. We start by finding the original operator's
# y position, and then subtract 200
new_op.nodeY = op( 'moviefilein1' ).nodeY - 100
```

There are, of course, many more things you can do with the Op Class - my hope is that this helps you get a sense of where to start and pushes you to start experimenting a little more.