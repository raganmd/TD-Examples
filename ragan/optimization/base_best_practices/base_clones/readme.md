# base_best_practices #
## Matthew Ragan ##
## 8.3.16 ##

### base_non_optimized ###
Clones are HUGE time savers. By cloning an operator you're pointing to another operator that should be used as the template for how the targeted clone is organized. In IBERA, the animal base elements are all individually copied. This means that making a change across all 15 instances also means changing parameters in 15 different places. I'm too old for that kind of busy work. All clones will have the same parameters and layout as the master operator. This means that you can make a change in a single base COMP, and know that it will propagate to all clones.

That does, however, come with some important considerations. When working with clones it becomes very important to think about how you're selecting information to drive that clone so it behaves as a unique operation. In the optimized example look at how parent().digits is used to set the seed value in the cloned bases. 

In IBERA, you might place relevant variables in a table then select those variables based on a parents digits... for example, row 1 might contain all the necessary variables for animal1. In general, if you find yourself repeating any data entry in touch in more than 3 places then there is a faster and easier way address what you're doing. I have done a lot of miserable hard coding, and learned this lesson the hardest ways possible. The sooner you can start thinking about how to programatically approach problems and organization in your networks, the more time you can spend on making the art.