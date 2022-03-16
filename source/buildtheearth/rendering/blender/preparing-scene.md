<!---
title: Preparing Scene in Blender
path: /buildtheearth/rendering/blender
version: 1.0.0
authors:
    - @VapoR
--->

# Preparing Scene in Blender

So this is the big one. Blender has unlimited possibilities, and there are an unlimited amount of things you could do with your render. But here are some basic ways to present your build.  

I suggest familiarising yourself with Blender's controls and layout before preceding, but if you don't want to then read [the next section](#basic-controls).

## Basic Controls

- Use scroll wheel to zoom in and out
- Use joystick looking sphere at the top right to change perspective
- Hold middle click and move mouse to change perspective
- Hold shift and middle click then move mouse to pan around

Watch [this](https://www.youtube.com/watch?v=K6Sm7DAPTGE) if you don't understand.

## Lighting

There are two basic ways to light your scene, HDRIs and lights/lamps (sun, area, etc). I will cover using HDRIs, as they provide easy, quick, realistic lighting.

### HDRI

1. Click `Shading` on top to go to the Shader editor
2. On the left middle switch shader type from `Object` to `World`. You should see in the middle bottom (node editor) the two nodes `Background` and `World Output`
3. On the top left click `Edit`, `Preferences`, `Add-ons`
4. In the search bar enter `Node Wrangler` and check the box next to `Node: Node Wrangler`
5. Go back to the shader editor and left click `Background`, and `CTRL + T`
6. The nodes `Texture Coordinate`, `Mapping`, and `Enviornment Texture` should pop up
7. Download a 2k HDRI from [Poly Haven](https://polyhaven.com/hdris)
8. Click `Open` on the `Enviornment Texture` node, and select your HDRI

### Render Engine

1. For Minecraft renders it's best looking to use cycles. As of writing cycles X hasn't been released with it, but you can mess around with it in alpha.
2. To enable switch to cycles from eevee (default engine), go to the right side panel in the `Layout` editor, and select `Render Properties`, `Render Engine`, and select `Cycles`
3. On the top right of the 3d viewport click the sphere `Viewport Shading`

```eval_rst
.. image:: ../../../../images/viewport_shading.png
    :width: 600
    :alt: Viewport Shading
```

## Camera

1. In the `Layout` editor in the `3D Viewport` on the top left click `Add`, `Camera`
2. On the right side of the `3D Viewport` click the camera icon
3. On the right sidebar click `View`, `View`, `View Lock`, `Lock`: check `Camera to View`
4. Now when you move around the camera will also move around
5. I suggest increasing the camera focal length (like decreasing Minecraft FOV) by selecting the Camera, going to the right side bar, clicking the green camera icon, and changing `Lens`, `Focal Length`

```eval_rst
.. image:: ../../../../images/camera_focal_length.png
    :width: 600
    :alt: Camera Focal Length
```

## Ground

One of trillions of possibilities is to only show the Minecraft build's ground in the image, and another is to make a plane and extend it, another is to use an "Infiinite Background" (explained in the next section).
## Background

You can either use the background of the HDRI, which can sometimes work or sometimes look completely unrealistic, not show anything except the Minecraft build in the image, or hide the HDRI background and use an "infinte background".

### HDRI Background

Just position the camera where you can only see the ski of the HDRI in the image.

```eval_rst
.. image:: ../../../../images/drybol.png
    :width: 600
    :alt: Drybol
```

### No Background

Just position the camera where you can only see the Minecraft build in the image.

```eval_rst
.. image:: ../../../../images/kirk_iceland.png
    :width: 600
    :alt: Iceland
```

### Infinite Background

Common techinique in real world photos, now in Blender. Watch [this](https://www.youtube.com/watch?v=1kULKsUEctw) or [this](https://www.youtube.com/watch?v=5UCc3Z_-ibs) or maybe [this](https://www.youtube.com/watch?v=8FUzeMY6b18).

```eval_rst
.. image:: ../../../../images/boston.png
    :width: 600
    :alt: Boston
```

I'm sure I missed some things, if they're not in [the extra page](extra), tell me on Discord. Of course I'm not going to cover every single thing that can be done in Blender.