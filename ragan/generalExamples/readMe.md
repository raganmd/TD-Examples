# TouchDesigner Examples #

## Programmer / Artist ##

**Matthew Ragan** | [ matthewragan.com](http://matthewragan.com)  

## Overview ##

Here  you'll find an extensive library of the code examples that I've put together for courses, the [TouchDesigner forum](http://derivative.ca/Forum/), and the [TouchDesigner Help Group](https://www.facebook.com/groups/touchdesignerhelp/) on Facebook. The examples here run the gamut of various applications and techniques, and as it stands this repo is a bit of a mess - in terms of organization. In the coming months I should have a better organizational structure, and better documentation. These things just take time. Meanwhile, download the code pack, and look through some examples.

Happy Programming

---

### Choose a Folder ###

*Overview*

This example looks at how you can use the UI Class to select a folder. This is often useful when you want to script a method for pointing your application to a specific directory on your computer. The UI class will allow you to do this without needing to exit perform mode.

**Core Concepts**
* Using the UI Class
* Python Scripting with panel elements

---

## CHOP Execute ##

### Matthew Ragan ###
_8.25.15_


## Summary ##

This example looks at a number of various applications for the [CHOP Execute DAT](http://www.derivative.ca/wiki088/index.php?title=CHOP_Execute_DAT). CHOP Executes are useful for any number of different applications, but having a complete understanding of them requires looking closely at the online documentation, and learning the ins and outs of the [The Channel Class](http://www.derivative.ca/wiki088/index.php?title=Channel_Class)

Here we have to LFOs that are used to append a two different Text DATs. In the first example, we have a multi channel LFO that prints out a statement which corresponds to the channel that's turning from off to on.

In the second example, we can see a report of the members of the Channel Class - this gives us a better sense of understanding what kind of information we can extract from a CHOP Execute event.


## Color Key ##
* **Magenta** - Read Me Files


## Storage Notes ##

None


## Major Components ##
* None


## Extensions or Modules on Demand ##
None

**Core Concepts**
* CHOP Execute DATs
* Python Scripting with channels

---

### Container Select ###

*Overview*

This example looks at how you might approach moving between several realtime rendered containers. In this network, three Container COMPs are nested inside of a master project. The Select COMP pulls the panel and background of a given container. This can be used both of moving between live rendered effects / environments, as well as to move between user interfaces. A table COMP is used to for the selection method, running a script that's controlled by a panel execute inside of the Table COMP.

**Core Concepts**
* The Table COMP
* Panel Executes
* The Select COMP
* Switching Containers and control Panels

### Copy Example ###

*Overview*

A simple example of how to copy the contents of one table to another using Python.

**Core Concepts**
* Python and Table DATs
* The copy command

---

## Drop Script Example  ##

### Matthew Ragan ###
_8.25.15_

## Summary ##

This example looks at a variety of Drag and Drop examples. Here you'll see the various methods for using drop scripts and the args returned when using them. Take a close look at the text DAT inside of each container called "dropScript" - this DAT is responsible for holding the script(s) run when any object is drag / dropped onto a container.


## Color Key ##
* **Magenta** - Read Me Files
* **White** - Examine DAT to see what is in storage
* **Black** - Template structure for setting the storage keys for this TOX


## Storage Notes ##

**uiColor** - A dictionary for UI color elements, each item is a list comprised of rgba, structured as [ r , g , b , a ]
* **BG** - Background
* **borderA** - border A
* **borderB** - border B
* **headerBG** - Header Background
* **headerBorderA** - Header Border A
* **headerBorderB** - Header Border B


## Major Components ##
1. **container1** - drag a file onto this component to see the path to the dropped file
2. **container2** - drag an image or movie file onto this component to see that file displayed as the image for this container.
3. **container3** - drag a folder from any directory on your computer onto this container to see the path to the folder. Inside you'll find a folder DAT which retrieves the contents of the folder.
4. **container4** - drag any file or folder onto this container to see all of the args returned by the drop action.


## Extensions or Modules on Demand ##
None

**Core Concepts**
* Drop Script args
* Python Scripting with drop scripts

---

### FIFO Example ###

*Overview*

FIFO, short for First In First Out, is more than just a produce stocking method at grocery stores and restaurants. This example looks at how the FIFO DAT works. You might consider using this DAT when you have a fixed data set that updates periodically. This allows you to keep entires until they're pushed out of the fixed table.

**Core Concepts**
* The Append Row Method for working with DATs
* Python Scripting
* CHOP Executes

### Learning Extensions ###

*Overview*

Extensions allow you to extend and modify custom components that you've created in TouchDesigner. The penultimate example of this is a custom movie player. Custom Extensions allow you to specify commands like Play(), Pause(), Stop(), Next(), and any other kind of function that you can dream up. While this may, at first, appear to have limited applications it is a tremendously powerful means of creating modular and reusable elements in TouchDesigner.

**Core Concepts**
* Extesnsions
* Class Creation
* Custom Functions
* Creating reusable modules

### Modules As Expressions ###

*Overview*

Occasionally, you may find that you need a complex scripting function for a parameter. While there's a tremendous amount that you can accomplish in single line expressions, there are limits. What then can you do to work around this problem? With a little bit of ingenuity, you can write a function to be called as a module on demand for a parameter. This network examines what that means, and how you can set that up.

**Core Concepts**
* Python Scripting
* Modules on Demand
* Parameter Expressions
* Modules as Parameters

### Op Viewer TOP and Component ###

*Overview*

There are a number of ways you can see or interact with Operators in a finished user interface. This Network examines what that means in terms of rastered pixels, and interactive elements. Look at both what an Op Viewer TOP and COMP do, and why you might use them in this example.

**Core Concepts**
* Operator Viewing

### Par Class .expr ###

*Overview*

While it's often useful to set parameters as static values, it can sometimes to be useful to set as an expression. With a bit of thinking and planning you can do this through scripting. This example looks at both setting parameters as fixed values, or as expressions.

**Core Concepts**
* Panel Execute DATs
* Python Scripting
* Setting parameters as expressions

### Referencing Parameters ###

*Overview*

Understanding the fundamentals of referencing is essential to working in TouchDesginer. Here we look at how to build references, and what they mean.

**Core Concepts**
* Referencing
* Python References

### Run a DAT ###

*Overview*

From time to time it's common to have a complex operation that requires more than a handful of lines of code. In these cases, it can sometimes be both cleaner programming, and helpful for your sanity to place these operations in a dedicated DAT. Here we look at how you can run that complex function or operation from another operator.

**Core Concepts**
* Python Scripting

### Shrink Instance Example ###

*Overview*

Complex scenes often require a programmer to think carefully about how to build an optimized scene for live playback. Here we look at how to set up a visualization that mirrors another installation.

**Core Concepts**
* Instancing
* Realtime Rendering
* GPU Optimization
* Python Scripting