<!---
title: Creating OBJ File
path: /buildtheearth/rendering/mineways
version: 1.0.0
authors:
    - @VapoR
--->

# Creating an OBJ

The first step of making a render is creating an OBJ file from your world or schematic. There are two software options for creating an OBJ, Mineways and jMc2Obj. Neither support cubic chunks worlds. If you have a cubic chunks world you'll need to make a schematic or convert to a vanilla world with the Cubic Chunks Converter.
- Use Mineways If These Apply
  * You have a schematic or vanilla world(jMc2Obj doesn't support schematics)
  * You want a simple, small render (<500 x 500 blocks)
  * You don't care that banners and heads won't transfer properly
```eval_rst
.. note::
   Mineways is much less optimized than jMc2Obj, so that is why I don't recommend Mineways for huge areas.
   Banners turn white and all heads turn into pumpkins.
```
- Use Mineways If These Apply
  * You want to render a large area (>500 x 500 blocks)
  * You want banners and custom heads to transfer
```eval_rst
.. note::
   With jMc2Obj you can render huge areas (I once did all of downtown Seattle and more) when optmize mesh is checked, however it has its drawbacks. When it is checked, blocks like panes and walls may become 2D planes. If you uncheck optimize mesh, performance goes down drastically.
```
## Using Mineways

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eget ultrices diam. Maecenas ac lobortis erat. Nullam maximus tempus dui, ut tempor enim gravida eu. Morbi vitae maximus mi, eget dapibus augue. Pellentesque pharetra elit rhoncus odio eleifend, vel placerat lorem vulputate. Phasellus dictum dolor at libero lacinia sollicitudin. Mauris euismod, elit non convallis rutrum, libero metus condimentum quam, in vehicula elit eros sed massa.

In sed tellus tincidunt, semper lacus in, pulvinar arcu. Nullam congue lacus vel risus feugiat mattis. Integer et fringilla risus, vitae semper elit. Maecenas sodales fermentum orci a tristique. Nunc vehicula efficitur ornare. Pellentesque vehicula, orci sit amet accumsan mollis, libero odio varius lacus, eu varius elit sem in sapien. Proin auctor mi a enim faucibus dignissim. Proin vel mattis purus, a condimentum ante. Praesent ac nunc lacus. Nam nunc est, interdum sit amet ornare non, viverra ac ipsum. Maecenas maximus enim eget magna ullamcorper efficitur. Etiam auctor id dui non commodo. Donec a porta urna, non luctus odio. Curabitur semper ligula eu dui hendrerit, et tincidunt erat varius.

1. Lorem ipsum dolor sit amet, *consectetur adipiscing elit*. Nulla eget ultrices diam. Maecenas ac lobortis erat.
2. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eget ultrices diam. Maecenas ac lobortis erat.
3. Lorem ipsum dolor sit amet, consectetur adipiscing elit. **Nulla eget ultrices diam.** Maecenas ac lobortis erat.

In sed tellus tincidunt, semper lacus in, pulvinar arcu. Nullam congue lacus vel risus feugiat mattis. Integer et fringilla risus, vitae semper elit. Maecenas sodales fermentum orci a tristique. Nunc vehicula efficitur ornare. Pellentesque vehicula, orci sit amet accumsan mollis, libero odio varius lacus, eu varius elit sem in sapien. Proin auctor mi a enim faucibus dignissim. Proin vel mattis purus, a condimentum ante. Praesent ac nunc lacus. Nam nunc est, interdum sit amet ornare non, viverra ac ipsum. Maecenas maximus enim eget magna ullamcorper efficitur. Etiam auctor id dui non commodo. Donec a porta urna, non luctus odio. Curabitur semper ligula eu dui hendrerit, et tincidunt erat varius.

## Using JMC2OBJ

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eget ultrices diam. Maecenas ac lobortis erat. Nullam maximus tempus dui, ut tempor enim gravida eu. Morbi vitae maximus mi, eget dapibus augue. Pellentesque pharetra elit rhoncus odio eleifend, vel placerat lorem vulputate. Phasellus dictum dolor at libero lacinia sollicitudin. Mauris euismod, elit non convallis rutrum, libero metus condimentum quam, in vehicula elit eros sed massa.

In sed tellus tincidunt, semper lacus in, pulvinar arcu. Nullam congue lacus vel risus feugiat mattis. Integer et fringilla risus, vitae semper elit. Maecenas sodales fermentum orci a tristique. Nunc vehicula efficitur ornare. Pellentesque vehicula, orci sit amet accumsan mollis, libero odio varius lacus, eu varius elit sem in sapien. Proin auctor mi a enim faucibus dignissim. Proin vel mattis purus, a condimentum ante. Praesent ac nunc lacus. Nam nunc est, interdum sit amet ornare non, viverra ac ipsum. Maecenas maximus enim eget magna ullamcorper efficitur. Etiam auctor id dui non commodo. Donec a porta urna, non luctus odio. Curabitur semper ligula eu dui hendrerit, et tincidunt erat varius.

Morbi tincidunt dui non lectus porttitor, ac convallis tellus luctus. Duis molestie faucibus volutpat. Nunc sed orci sit amet metus ultricies fringilla non vitae orci. Nullam porta nisl sit amet nisl tristique, vitae lacinia nulla vestibulum. Sed consequat felis neque, eget rutrum est iaculis vel. In pharetra augue quis augue egestas, sit amet pretium eros fermentum. Quisque egestas ipsum vitae mauris posuere, sit amet sodales ligula sodales. Proin interdum turpis augue, ac scelerisque risus semper sed. Nam lacus enim, tincidunt in ultricies vitae, porttitor a lorem. Mauris at convallis arcu. Morbi vitae velit semper, aliquam diam ut, porta elit. Cras iaculis massa sit amet est rhoncus, id tristique nibh convallis. Sed non nunc luctus, dictum nulla at, tempus velit. Aliquam non lacus non arcu suscipit semper vitae ut ipsum. Pellentesque dui metus, efficitur sit amet molestie in, vestibulum sed elit. Maecenas non felis congue, egestas erat eget, laoreet elit.

Donec pellentesque, turpis vitae maximus pellentesque, metus lectus eleifend metus, eget faucibus velit dolor at dolor. Praesent venenatis, velit nec gravida tempus, tortor nisi fringilla elit, quis congue diam sem a turpis. Duis id maximus ipsum, eu efficitur erat. Morbi nec leo enim. Vivamus malesuada orci efficitur lacus finibus, sit amet mattis purus vehicula. Nam posuere pellentesque nunc, sed pretium arcu tristique non. Aliquam erat volutpat.

Nulla ullamcorper enim nec tortor rutrum suscipit. Aenean mi leo, eleifend in nunc et, feugiat pretium sapien. Nunc scelerisque ac risus ac varius. Ut at egestas metus, eu cursus sapien. Fusce nec quam id erat volutpat consequat. Nullam lacus orci, volutpat a nulla sed, tristique ultrices nisi. Nam non felis condimentum, faucibus nibh venenatis, condimentum justo. Cras mattis suscipit molestie. Phasellus suscipit laoreet faucibus. Praesent quis orci turpis. Pellentesque eget lobortis ex, non pellentesque orci. Sed facilisis dui et purus tincidunt finibus.

Aliquam sit amet egestas metus, nec aliquam purus. Proin viverra turpis non odio auctor, rutrum ultricies urna volutpat. In aliquam, lectus at tincidunt blandit, dui magna dignissim felis, vitae maximus enim urna porttitor erat. Nunc ut velit at elit elementum cursus nec eu urna. Donec eget volutpat dolor. Etiam et vestibulum lorem, at suscipit libero. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nulla lobortis posuere mauris a tincidunt. Sed mollis tortor mauris, eget blandit eros placerat sit amet. Suspendisse vehicula convallis eros, eu sollicitudin urna fermentum feugiat. Suspendisse potenti. Sed a ante est. Nullam justo massa, pharetra vel velit nec, laoreet bibendum neque. Praesent fermentum libero nec tellus aliquam, commodo accumsan ipsum ultrices.