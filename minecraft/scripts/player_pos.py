#!/usr/bin/env python3

###
# Nathaniel Watson
# 2018-06-30
# De Anza College Academy
###

from mcpi import block
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    print(*pos)
