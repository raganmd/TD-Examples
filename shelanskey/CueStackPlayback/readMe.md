Questions about this material can be sent to ishelanskey@gmail.com.
More info on my website (http://design.ianshelanskey.com)

#Cue Stack Playback Example
Here is an example of a cue based playback system. Inside the network you will find a small GUI to control the active cue as well as some useful system info like current FPS, cooktime, and which AB deck is currently displayed. All of the content is kept in the component labeled 'content'.   

##Switcher
Inside the component labeled switcher is an AB deck video switcher. This is all drive by a CHOP execute that handles time and which deck is switched to next. 

##GOTO cue
This is a useful component for creates cues in a cue stack. Enter a number into the field and it will set 'pane1' to look inside the component holding that cue. Not used in playback. 