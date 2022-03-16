<!---
title: Importing OBJ into Blender
path: /buildtheearth/rendering/blender
version: 1.0.0
authors:
    - @VapoR
--->

# Importing OBJ into Blender

1. Install [MCprep](https://theduckcow.com/dev/blender/mcprep/) Blender addon. Installation instructions can be found on the website
2. Click `MCPrep` on the sidebar (top right, but to the left of the Outliner)
3. If you used Mineways, on the sidebar click `OBJ world import` and select your OBJ from earlier. If you used jMc2Obj, on the top left click `File`, `Import`, `Wavefront (.obj)`, then select your OBJ.
4. On the sidebar click `Prep Materials`

```eval_rst
.. image:: ../../../../images/blender_sidebar.png
    :width: 600
    :alt: Blender sidebar
```
 
If you used jMc2Obj, you may notice that the OBJ looks distorted, so try changing the `x/y/z` scales until the blocks are square cubes.
If you don't know how to reshape the OBJ, try selecting the build in Blender, on the right side panel enter in the search box `Transform`, then tweak the scales.

```eval_rst
.. image:: ../../../../images/transform.png
    :width: 600
    :alt: Transform
```