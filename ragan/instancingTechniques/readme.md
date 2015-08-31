# Instancing Techniques #
---

### Matthew Ragan ###
_[matthewragan.com](http://matthewragan.com)_  
_8.31.15_


---
## Summary ##
Here we have an examination of various instancing techniques to explore and pull apart. Instancing is a powerful way to take full advantage of your GPU along with the rendering engine of TouchDesigner, the challenge is understanding how to set that up so it behaves the way you expect / want. 


## Color Key ##
* **Magenta** - Read Me Files
* **Purple** - Textures
* **Green** - Instancing CHOP / SOP networks; the logic of organizing our instances. 

## Storage Notes ##
None


## Major Components ##
* **[pixelMappingGeometry](http://matthewragan.com/2015/08/18/advanced-instancing-pixel-mapping-geometry-touchdesigner/)** - This is an interesting examination of a technique that I enjoy using for various projects. Essentially, we pull apart an image file, and use the color information of the pixels to color our instances. It has the effect of looking like a pixel mapped effect with geometry. This component looks at the various steps involved in this process, and other elements that you might choose to play with.
* **[puzzlePieces](http://matthewragan.com/2015/08/26/advanced-instancing-puzzle-pieces-touchdesigner/)** - Experimenting with the idea how you might re-arrange instances textures. This example has several different approaches that you might use, and in this base COMP you'll find examples of what these approaches might look like.
* **[animationComp](http://matthewragan.com/2015/08/24/advanced-instancing-instancing-with-the-animation-comp-touchdesigner/)** - For more complex animation sequences using instances you might choose to use the animation COMP as a way to determine the specific behaviors and movements of your geometry. For artist programmers experienced with key-framed environments this approach is especially useful as it involves time line based concepts that are easy to see expressed in real time in TouchDesigner.
* **textureArray** - This example looks at how you might extract textures from a properly prepared movie file in order to create a texture array of images. In this technique we use a texture3D TOP.
* **cacheSelectCube** - This example looks at how you might extract textures from a properly prepared movie file in order to create a texture array of images. In this technique we use a cache TOP.
* **rotateVector** - This example looks at how we might use the rotate to parameter of the geo instancing to change the orientation of our instances based on the normals of some source geometry.
* **lineFormation** - A common operation I do with instancing is creating photo montage sequences, and filmstrip trip tics. Depending on what you need, there are two different ways you might consider approach this problem. One would be to place all of your images in line, so you can pan down them.
* **circleFormation** - Similar to the line formation example, you might also want to place your images in a circle, pointed towards the camera. Spinning the camera or instances gives the illusion of images passing by. This is a great method for creating an endless loop of set images.


## Extensions or Modules on Demand ##
None


_documentation written in markdown_