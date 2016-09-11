# base_best_practices #
## Matthew Ragan ##
## 8.3.16 ##

Just like other operations can be ganged together, so too can chop executes. In this case, compare our two different approaches below. In the non optimized example we can see that we have independent executes for every select. This provides for very straightforward coding, but is not the most efficient approach. 

If we compare this to the optimized approach that uses only a single CHOP execute we see a much more efficient approach... though the python is slightly more abstract:

```python
op( 'text' + str( channel.index + 1 )  ).text = val
```

inside of op() we're constructing a string path to a target operator. In this case we want text1 - text10 as this corresponds to the text DATs that are in our network. We an join a string in python with the + operation, though we first need to do a bit of parsing and formatting.

The channel object refers to a single channel in the CHOP that's targeted by the CHOP execute DAT. The channel object has a member for the index of the channel - channel.index

Unlike touch objects who have a member called digits, our channel object doesn't have that... it does, however have an index value that's an integer. We can use this value, which starts at 0, and match it to our text DATs by first adding 1, then converting this integer to a string, and finally joining this to 'text'. This means that channel 0-9 now matches up with text1-10.

The .text call means that we're replacing the text in our DAT with val - the value of the channel. 

That's all well and good... but what can we do with it?

If we look over at the logic example, we can see that with a few extra lines we can do something like:

```python
if val >= 0.5:
	op( 'text' + str( channel.index + 1 a) ).text = 1
else:
	op( 'text' + str( channel.index + 1 ) ).text = 0
```

Here we're using a logical test to indicate what our next operation should be - if val is greater than or equal to 0.5 our targeted text DAT receives a value of 1, otherwise it receives a value of 0. Why does this matter? We might well think of how we could change table values, start or stop timers, or change any number of parameters this way. Better still, we might think about how we could remove a logical operation that's completed with a logic or expression CHOP, and instead just use this kind of approach. The "right" solution depends on a number of factors, but for inconsistent (operations that don't have to happen every frame) logical operations thinking of logic this way rather than with many additional operators might well be a solid move forward.