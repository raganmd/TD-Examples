# Python in TouchDesigner #

## Programmer / Artist ##

**Matthew Ragan** | [ matthewragan.com](http://matthewragan.com)  

## example_extensions ##

Rounding out some of our work here with Python is to look extensions. If you've been following along with other posts you've probably already looked over some [extensions in this post](https://matthewragan.com/2015/07/05/touchdesigner-understanding-extensions/). If you're brand new to this idea, check out that example first. 

Rather than re-inventing the wheel and setting up a completely new example, let's instead look at our previous example of making a logger and see how that would be different with extensions as compared to a module on demand.

A warning for those following along at home, we're now knee deep in Python territory, so what' we'll find here is less specific to TouchDesigner and more of a look at using Classes in Python.

In our [previous example looking at modules](https://matthewragan.com/2016/07/12/python-in-touchdesigner-modules-touchdesigner/) we wrote several functions that we left in a text DAT. We used the [mod class](http://derivative.ca/wiki088/index.php?title=MOD_Class) in TouchDesigner to treat this text DAT as a python module. That's a neat trick, and for some applications and situations this might be the right approach to take for a given problem. If we're working on a stand alone component that we want to use and re-use with a minimal amount of additional effort, then extensions might be a great solution for us to consider. 

Wait, what are extensions?! Extensions are way that we can extend a custom component that we make in TouchDesigner. This largely makes several scripting processes much simpler and allows us to treat a component more like an autonomous object rather than a complex set of dependent objects. If you find yourself re-reading that last statement let's take a moment to see if we can find an analogy to help understand this abstract concept.

When we talked about [for loops](https://matthewragan.com/2016/07/06/python-in-touchdesigner-for-loop-touchdesigner/) we used a simple analogy about washing dishes. In that example we didn't bother to really think deeply about the process of washing dishes - we didn't think about how much detergent, how much water, water temperature, washing method, et cetera. If we were to approach this problem more programatically we'd probably consider making a whole class to deal with the process of washing dishes:

```python

class Dishes():
    
    def __init__( self ):
        return

    def Full_cycle( self, list_of_dishes ):
        # what if we want to wash and then dry?

        self.Wash( list_of_dishes, water_temp )
        self.Dry( list_of_dishes )

        return

    def Wash( self, list_of_dishes, water_temp ):
        # what does washing really entail
        # all of that would go here

        number_of_dishes    = len( list_of_dishes )
        detergent_amt       = self.Set_soap( number_of_dishes )
        water_temp          = self.Set_water_temp( water_temp )

        return

    def Dry( self, list_of_dishes ):
        # what does washing really entail
        # all of that would go here

        number_of_dishes     = len( list_of_dishes )
        dry_time             = self.Set_dry( number_of_dishes )
        return

    def Set_soap( self, number_of_dishes ):
        return

    def Set_water_temp( water_temp ):
        if water_temp == 'hot':
            temp            = 98

        elif water_temp == 'medium':
            temp            = 80

        if water_temp == 'low':
            temp            = 60

        return temp

    def Set_dry( self, number of dishes ):
        return
```

Okay, so the above seems awfully silly... what's going on here? In our silly example we can see that rather than one long function for Wash() or Dry(), we instead use several smaller helper functions in the process. Why do this? Well, for one thing it lets you debug your code much more easily. It also means that by separating out some of these elements into different processes we can fix a single part of our pipeline without having to do a complete refactor of the entire Wash() or Dry() methods. Why does that matter? Well, what if we decide that there's a better way to determine how much soap to use. Rather than having to sort through a single long complex method for Wash() we can instead just look at Set_soap(). It makes unit testing easier, and allows us to replace or develop that method outside the context of the larger method. It also means that if we're collaborating with other programmers we can divide up the process of writing methods.

What's this *self.* business? self. allows us to call a method from inside another method in the same class. This is where extensions begin to really shine as opposed to using modules on demand. We an also use things like [attributes](https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide) and [inheritance](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/).

Okay, so how can we think about actually using this?

Let's take a look at what this approach looks like in python:

```python
import datetime

log_file            = op( 'text_log_file' )
log_path            = "example_extensions/log_files/log.txt"

full_text           = '''{now}

Current Year        | {year}
Current Month       | {month}
Current Day         | {day}
Current Hour        | {hour}
Current Minute      | {minute}
Current Second      | {second}
Current Microsecond | {microsecond}
'''

raw_date_time       = "On {month}-{day}-{year} at {hour}:{minute}:{second}"

verbose_log_message = '''============================
VERBOSE MESSAGE

{date_time}
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

class Ext_example():

    def __init__( self ):
        '''The init function.

        We're not doing anything with our init function in this example
        so we'll leave this empty.

        Notes
        ---------------
        ''' 
        return

    def Log_date( self ):
        year                        = datetime.datetime.now().year
        month                       = datetime.datetime.now().month
        day                         = datetime.datetime.now().day
        hour                        = datetime.datetime.now().hour
        minute                      = datetime.datetime.now().minute
        second                      = datetime.datetime.now().second
        
        updated_log_date            = log_date.format( 
                                                        month       = month,
                                                        day         = day,
                                                        year        = year,
                                                        hours       = hour,
                                                        minutes     = minute,
                                                        seconds     = second
                                                    )
        
        return updated_log_date
    
    def Log_date_time( self ):
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

        date_time   = raw_date_time.format( 
                                        month   = month,
                                        day     = day,
                                        year    = year,
                                        hour    = hour,
                                        minute  = minute,
                                        second  = second
                                        )

        return date_time

    def Log_message( self, operator, message, verbose=False, text_port_print=True, append_log=True ):
        '''Logging Method.

        A simple look at how you might start to think about building a logger for a TouchDesigner
        application. A logger is a great way to build out files with time stamped events. The
        more complex a project becomes, the more important it can become to have some means
        of logging the operations of your program. Here's a simple look at what that might
        look like.
        
        Arguments
        --------------- 
        operator( touch object ) - the touch object whose path you'd like incldued in the log message
        message( str ) - a message to include in the log
        verbose( bool ) - a toggle for verbose or compact messages
        text_port_print( bool ) - a toggle to print to the text port, or not
        append_log( bool ) - a toggle to append to the log file , or not

        Example
        --------------- 
        target_op       = op( 'constant1' )
        message         = "This operator needs attention"

        parent().Log_message( target_op, message )

        also

        parent().Log_message( target_op, message, verbose = True )

        Returns
        ---------------
        None

        Notes
        ---------------
        You'll notice that some arguments receive default values. This is so you don't have
        to include them in the call. This means that by default the message will be compact, 
        will print to the text port, and will append the log file.
        '''

        path        = operator.path
        op_name     = operator.name

        # logic tests for verbose or compact
        if verbose:
            message = verbose_log_message.format(
                                                    date_time   = self.Log_date_time(),
                                                    operator    = op_name,
                                                    path        = path,
                                                    message     = message
                                                )

        else:
            message = log_message.format(
                                            now                 = self.Log_date_time(),
                                            operator            = op_name,
                                            path                = path,
                                            message             = message
                                        )
        
        # logic tests for text_port_print
        if text_port_print:
            print( message )
        
        else:
            pass

        # log tests for appending log
        if append_log:
            log_file.write( '\n' + message )

        else:
            pass

        # save the log file to disk - external from the TouchDesigner project   
        self.Save_log()

        return

    def Save_log( self ):
        '''Saves log to disk.

        This helper function saves the log file to disk.

        Notes
        ---------------
        None
        '''

        op( log_file ).save( log_path )

        return

    def Clear_log( self ):
        '''Clears Log File.

        This helper function clears the text dat used to hold the log file.

        Notes
        ---------------
        None
        '''

        op( log_file ).clear()

        return
```

So getting started we set up a couple of variables that we were going to reuse several times. Next we declared our class, and then nested our methods inside of that class. You'll notice that different from methods, we need to include the argument self in our method definitions:

```python
# syntax for just a function
def Clear_log():
    return

# syntax for just a method in a class
def Clear_log( self ):
    return
```

We can also see how we've got several helper functions here to get us up and running - ways to add to the log, save the log to an external file, a way to clear the log. We can imagine in the future we might want to add another method that both clears the log, and saves an empty file, like a reset. Since we've already broken those functions into their own methods we could simply add this method like this:

```python
def Reset_log():
    self.Clear_log()
    self.Save_log()
    return
```

Now it's time to experiment. 

Over the course of this series we've looked at lots of fundamental pieces of working with Python in TouchDesigner. Now it's your turn to start playing and experimenting.

Happy programming!