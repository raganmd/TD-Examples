# TouchDesigner Facebook Help Group and Forum Files
## Programmer / Artist ##
**Matthew Ragan** | [ matthewragan.com](http://matthewragan.com)  

## Contents and Descriptions ##

### base_animation_different_duration ###


### base_animation_offset ###


### base_audio_reactive_revolve ###


### base_blob_track ###


### base_chop_math ###


### base_circles_and_graphs ###


### base_connect_example ###


### base_cooking_example ###


### base_countdown ###


### base_crop_text ###


### base_dispaly_fx ###


### base_drawing_cirlces ###


### base_every_2_minutes ###


### base_movie_player_with_extensions ###


### base_multi_module_config ###


### base_multi_output_config ###


### base_panel_execute ###


### base_particle_alpha_by_life ###


### base_particles_instance_force ###


### base_play_only_if_complete ###


### base_rotate_to_vector ###


### base_row_addition ###


### base_scalex_scaley ###


### base_setting_channels ###


### base_setting_resolution ###


### base_shuffle_chop ###


### base_stop_cooking ###


### base_switch_TOP ###


### base_text_arrangement ###


### base_trigger_only_when_3 ###


### base_two_colors_for_text ###


### base_two_panel_sync ###


### base_wire_fx_techniques ###


### container_blend_chop ###


### container_camera_animation ###


### container_camera_blend_comp ###


### container_channel_mask_via_osc ###


### container_childers_bin_and_display ###


### container_display_breakup ###


### container_drag_drop_container_get_path ###
_**5.19.16**_

**Original post / question**

>Another drag&drop question.
How do I drop a component onto another component, but not actually drop anything, only access the arguments. Essentially I just need the path of a child of the dragged component and use it in a drop script of the receiving component, without actually dropping the component itself. I find the drag and drop wiki page quite confusing.
>

All of the interesting stuff here is really happening in the drag/ drop script that's inside of container_drop.

Here the script is appending a text dat with information from the args that come from a drag / drop event.

The important consideration here is to make sure the replicants are set-up to be drag-drop ready. In our case that means that the replicated containers in container_drag. We want these to have their drag parameter set up correctly so that we can see args associated with them correctly display.

If you're curious to see all of the args associated with this kind of event you might uncomment the for loop at the top of the script and open the text port. Now you can see each of the args printed on its own line. 

### container_draw_path ###


### container_image_per_face ###


### container_instance_resize ###


### container_instance_rot ###

 
### container_instances_rotate_to_vector ###

 
### container_layout ###

 
### container_letter_particles ###

 
### container_live_draw ###

 
### container_manual_and_pattern_instancing ###

 
### container_moving_points ###


### container_object_tracer ###

 
### container_particles ###

 
### container_persistent_slider_vals ###

 
### container_presets_dict_method ###


### container_presets_table_method ###
 

### container_renderpick_drop ###

_**5.8.16**_

**Original post / question**

>Has anyone managed to make a drop script using renderpick? I'm trying to drop movie files onto rendered geometry ut renderpick stops working when you are "holding" a file from the os, even when strategy = always. I've tried using sleep() ut I can't get it.
>

### container_selects_to_stop_cooking ###
 

### container_simple_instance ###
 

### container_single_camera_along_path ###


### container_spiralgraph ###


### container_text_scroll_widths ###

 
### container_texture_sop_perspective_of_camera ###

 
### container_tiled_images ###

 
### container_using_selects ###


### container_xml_example ###
_**4.6.16**_

My suffering is your gain...
Here you'll find a simplified implementation of building out a multi-machine configuration file as XML or JSON. A list comp allows the user to add machines to you heart's content. Double click list comp fields to edit the machine name, edit the text fields to change attributes. Output either XML or JSON.
Some Highlights:
* uses extensions
* uses new global op shortcuts
* uses the list comp with custom parameters
* uses storage to transport all of the relevant data
* uses some fun dictionary loops
* uses doc strings for self documenting methods

### slider_mike ###
_**5.6.16**_

**Original post / question**

>Hi guys, I've got a chop that I want to show some number between 0 and 20. I have an increment value running to a speed chop into a null for that value. I want to have a button to stop incrementing it, (which is a multiply value in a math chop). I want a slider to continually be updated to show that chop value, but when I stop having it autoincrement, I want the slider to be able to control the chop value. Any suggestions?
>

### base_simple_motion_blur ###
_**5.20.16**_

A fast look at how to set-up motion blur.

### base_cell_contents ###
_**5.22.16**_

Original post / question:

>Here is what i want to do and am a little lost.
i have text in lets say the 0,0 cell in table one and a blank space in cell 0,3 in table 2
is there a command i can write to take the text in table 1 cut it and paste it in the feild in table 2. 
id like to do this with a interface so you select name one and it pastes in to slot 2.
>

In this example we have a table, and we want to copy the contents from one place in the table into another table.

For the sake of simplicity let's start with assuming that we're always copying to the same location.

Here we write a simple helper function that's an abstract form of what we're after:

```Python
target = op( 'table_target' )
source = op( 'table_source' )

def Copy_to_target( source_row, _source_col ):

    target[ 0, 0 ] = source[ source_row, _source_col ]

    return

```

Our helper fucntion takes a coordinate location in the table, and copies to the coordinate [ 0, 0] in our target table. 

Rather than write this as a single sciprt, we can instead use it as a module so we can call this action from multiple locations.

```Python
mod( 'text_copy_paste_script' ).Copy_to_target( 3, 3 )
```

Right click and run either text_example1 or text_example2 to see it in action.

### base_one_line_conditional_expressions ###
_**5.22.16**_

Conditional one line Python expressions can be used for a number of different applications.

Let's imagine a circumstance where we have two different sets of animation data. Depending on another variable we want to select the appropriate set of channels. 

In this example, both base comps are identical with one exception, the store key "animation_index".

In base_exampel1 animation_index is set to 0, while in base_example2 animation_index is set to 1. 

Let's take a closer look at our select CHOPs inside of our base components. Here we see a select with the following expression:

```Python
me.fetch( 'animation1' ) if me.fetch( 'animation_index' ) == 0 else me.fetch( 'animation2' )
```

We can pull apart the structure of this a little to better understand what's going on:

[ if_value ] [ logical_test ] [ else_value ]

Seen this way, we can see that the above single line expression looks something like this in plain English:

select op( 'null1' ) if the animation_index value is exactly 0, otherwise select op( 'null2' )

Let's look quickly at another example. In table1 we have two rows. The eval DATs below have the following expression:

```Python
op( 'table1' )[ 0, 0 ] if me.digits == 1 else op( 'table1' )[ 1, 0 ]
```

So here we can see that we select the cell in the [ 0, 0 ] position if our digits are 1, in all other cases we select the cell in the [ 1, 0 ] position.