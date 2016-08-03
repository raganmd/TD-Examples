# base_best_practices #
## Matthew Ragan ##
## 8.3.16 ##

### base_non_optimized ###
Sadly, timer CHOPs arne't as cheap as we might hope that they could be. Timers in a limited capacity are excellent tools, but once you start to get large numbers of them they quickly eat cycles. Here we can see that 10 timers are roughly 20 times as expensive as a single speed CHOP with 10 channels. The catch, of course, is that a speed CHOP isn't as straightforward to use. 

Take some time to look at the reset parameter for the speed CHOP - which allows you to reset all channels at once, as well as how toggling a value in the reset column of the DAT will allow you to reset a single channel. 