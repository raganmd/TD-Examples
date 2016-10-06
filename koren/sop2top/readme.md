Basic Sop2Top component
Converts point position into texture for further vertex shader manipulations.
Its very basic but can be very handy, maybe the community will might want to develop it further .
For best results use same particle count in every file.
If not possible make sure the first frame contain the max number of particles in your sequence (it will work but introduce flickering) .

Tested only with Houdini .bhclassic format files. 
----------------------------------------------------------------------

Instructions  :

1.drag the SopToTop tox file to touch designer 
 
2.choose import particle sequence folder and export texture folder.

3.press on convert.

4.press play , if slow you can cache it.

5.drag TextureToVertex tox ,connect wires and enjoy.
 
Barak Koren