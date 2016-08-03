# base_best_practices #
## Matthew Ragan ##
## 8.3.16 ##

The best CHOPs are also the ones that need the most attention. The filter CHOP is by far one of my favorites. It's awesome, but it can also be expensive. Specifically, using multiple filter CHOPs is generally something you should avoid. We might go further to generalize that idea and consider that when possible we should avoid multiple operators when we might instead perform the same operation on a single array. 

Before we go further we have to take a moment and reconcile how to think about programming in touch... there isn't currently a good tool for teaching programmer-artists about object oriented programming in TouchDesigner, so hang on as we look at this together. In touch, we can think of an operator as an instance of an object - it carries it's own parameters, it's own memory, and it's own attributes. This is an imperfect analogy, but it's enough to get us started. Generally speaking, when possible it's better to use a single object (operator) with multiple samples than to use multiple objects (operators) with single samples. 

A bad analogy - in terms of traffic / roadway congestion, it's more efficient for commuters to ride single bus together than to each drive their own car. 

Where am I going with all of this? When thinking about CHOPs, it's usually faster / more computationally efficient to use a single operator with multiple samples than to use multiple operators.

In this example, the non-optimzied approach uses a single noise source and then selects out individual channels. Each channel then has an independent filter object (operator). At 10 objects, it is 3.5 times more expensive to use individual objects as compared to our optimized approach that performs the same operation with a single filter CHOP.