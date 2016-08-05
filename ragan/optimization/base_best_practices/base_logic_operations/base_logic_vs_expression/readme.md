# base_best_practices #
## Matthew Ragan ##
## 8.3.16 ##

### base_logical_vs_expressions ###
logical operations are hard in TouchDesigner. I still regularly struggle with the right implementation to a particular problem, and in some cases it's a matter of trial and error before you find the right solution.

In this case, we're looking at logic operations. In several instances I see examples of expression CHOPS that are essentially testing a logical state - is a value outside or inside of a set of bounds. Generally speaking, Python is very slow in touch. Miserably slow. That's not to say that it isn't useful, but it's not a tool we should aim at executing every frame unless it's absolutely necessary. Expression CHOPs use python expressions as parameter values, and these python expressions are then executed every frame as a test on the incoming values to the CHOP. This is generally more computationally expensive than an equivalent C++ operation.

Let's take a look at one option.

Here we have a noise CHOP with 10 time sliced channels. Looking at the expression CHOP our average cook time for 10 channels comes in around 0.03 ms, a logic CHOP performing the same operation comes in at 0.01 ms. In this case, the python rout for solving this logic question is significantly more expensive. 

While 0.03 vs 0.01 ms of cook time is seemingly inconsequential on the face of it, I see 5 expression CHOPs per animal in /ibera/lenses_keyhole_vr2/... with 15 animals total. While this isn't an issue at 10 channels, it can quickly become a bottle neck as the scale increases. 

- - - - -

pushing the previous idea a little harder, we can see that there's an additional area for optimization. In the previous example we were running our logic and expression CHOPs on 10 separate channels. 

If instead we thinking of running these operations on a single channel with multiple samples we get even better results. By both moving to an array of values over a independent channels and using a logic CHOP rather than expression CHOP, our cook time drops to 0.004 ms. This example is for 10 channels. If we instead think of 75 channels - which is closer to the number of expression CHOPs running currently in IBERA - our non optimized approach costs about 0.17 ms vs 0.004 ms for our optimized approach.

Here we need to pause for a moment. In the currently implemented approach there are individual expression CHOPs for each logical operation. Rather than the examples provided so far, that's more akin to 75 different CHOPs all running at the same time. The computational cost here is closer to 2.9 ms. While it's initially difficult to transition away from this approach, the long term payoff makes for a tremendous performance enhancement.