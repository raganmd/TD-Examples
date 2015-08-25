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

### CHOP Execute ###

*Overview*

CHOP Executes are tremendously powerful method of scripting. This DAT allows you to tie the actions of CHOP Channels to scripted actions. This example looks at what information you have access to, and how to take fuller advantage of the CHOP Execute DAT.

**Core Concepts**
* CHOP Execute DATs
* Python Scripting with channels

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

### Drop Script ###

*Overview*

Drop scripts allow you to dynamically set a number of different elements based on drag and drop actions in you user interface. Understanding how this works can be a little mysterious at first. Here we look at the various args that are available when an item is dropped on a container, and how you might use that information. This might be used to set a file path for a whole folder, or a single image. 

**Core Concepts**
* Drop Script args
* Python Scripting with drop scripts

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