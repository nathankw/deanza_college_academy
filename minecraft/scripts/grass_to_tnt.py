#!/usr/bin/env python3

###
# Nathaniel Watson
# 2018-06-30
# De Anza College Academy
###

from mcpi import block
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def trailing_blocks(block_id):
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x, y, z, block.TNT.id, 1)
    
