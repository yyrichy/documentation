<!---
title: Creating an OBJ
path: /buildtheearth/rendering/mineways
version: 1.0.0
authors:
    - @VapoR
--->

# Creating an OBJ

The first step of making a render is creating an OBJ file from your world or schematic. The OBJ file will later be imported into Blender. There are two software options for creating an OBJ, Mineways and jMc2Obj. Neither support cubic chunks worlds. If you have a cubic chunks world you'll need to make a schematic or convert to a vanilla world with the Cubic Chunks Converter.
```eval_rst
.. note::
   Mineways is much less optimized than jMc2Obj, so that is why I don't recommend Mineways for huge areas. With jMc2Obj you can render huge areas (I once did all of downtown Seattle and more) when optmize mesh is checked, however it has its drawbacks. When it is checked, blocks like panes and walls may become 2D planes. If you uncheck optimize mesh, performance goes down drastically.
```
- Use Mineways If These Apply
  * You have a schematic or vanilla world (jMc2Obj doesn't support schematics)
  * You want a simple, small render (<500 x 500 blocks)
  * You don't care that banners and heads won't transfer properly, banners turn white and all heads turn into pumpkins

- Use jMc2Obj If These Apply
  * You have a vanilla world (1.13+ is supported, 1.12.2 should work but may be broken)
  * You want to render a large area (>500 x 500 blocks)
  * You want banners and custom heads to transfer (1.13+)

## Using Mineways

1. Download Mineways [here](https://www.realtimerendering.com/erich/minecraft/public/mineways/downloads.html#downloadImgs). If you have an issue look at the info on the website
2. Open Mineways
3. On the top left click `File`, `Open`
4. Navigate to your schematic or vanilla world and double click the `.schematic` or `level.dat`
5. Use left click and drag to move around
6. Use right click and drag to select a region to export
7. Note the `Height` and `Depth` sliders at the top of the screen. Only the blocks inside that range will be exported. Areas highlighted with purple inside the region will be exported
8. After selecting a region, click `File`, `Export for Rendering`
9. Select a folder to save the OBJ file, enter a name for the OBJ file, then click `Save`
10. A settings screen will pop up. Beginners just click `OK`
11. Wait until the blue progress bar at the bottom is complete, then exit the program. You should now have an OBJ (along with textures, etc) at the location specified in step 9
```eval_rst
.. note::
   If you run out of memory when exporting, click **Help**, and check **Give more export memory!**, then restart the program. If you ran out of memory it's likely a large area, in which case you should consider using jMc2Obj.
```

## Using jMc2Obj

1. Download jMc2Obj [here for 1.13+](https://cdn.discordapp.com/attachments/793250835294584864/888249927229124678/jMC2Obj-bte.zip) and [here for 1.12.2](https://github.com/jmc2obj/j-mc-2-obj/releases/download/50/jMc2Obj-dev_g50.jar)
2. If you downloaded the one for 1.13+, take the zip's contents out of the zip
3. Execute the jMc2Obj jar file by either opening your terminal/command prompt, navigating to the same directory as the jar and typing `java -jar JMC2OBJJARNAME.jar` or on Windows right click the jar, `Open With`, `Java...`
4. 
5. 

```eval_rst
After creating the OBJ and it's accompanying files, proceed to :doc:`importing-obj`.
```