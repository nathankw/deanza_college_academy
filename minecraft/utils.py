###
# Nathaniel Watson
# 2018-06-26
# De Anza College Academy
###

"""
See mc API at https://www.stuffaboutcode.com/p/minecraft-api-reference.html.
"""
import time
import turtle

from mcpi import block
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

AIR = block.AIR.id
COBBLESTONE = block.COBBLESTONE.id
GLASS = block.GLASS.id
GLASS_PANE = block.GLASS_PANE.id
TNT = block.TNT.id
WATER = block.WATER.id
WOOD = block.WOOD.id

def house(n=10):
    """
    Build a house with equal width, length, and height. There is a door in the middle of the front
    wall of the house.  The floors are wooden with the Jungle data type setting, and the roof is
    also wooden.

    Args:
        n: `int`.  Specifies the dimensions of the house to be n x n x n. Due to minimal layout
          of the house, n should be >= 10

    Raises:
        ValueError: The value of parameter n is too small (< 10).
    """
#    if n < 10:
#       raise ValueError("n must be >= 10.")

    DOOR_HEIGHT = 2
    x, y, z = mc.player.getTilePos()
    x += 1 # Don't build over Steve

    #First clear some space:
    OFFSET = 3
    mc.setBlocks(x - OFFSET, y, z - OFFSET, x + n + OFFSET, y + n + OFFSET, z + n + OFFSET, AIR)
    mc.setBlocks(x, y, z, x + n, y + n, z + n, COBBLESTONE)
    # Carve out the inside with air blocks.
    mc.setBlocks(x + 1, y, z + 1, x + n - 1, y + n - 1, z + n - 1, AIR)
#    # Glass roof
    mc.setBlocks(x, y + n, z, x + n, y + n, z + n, GLASS_PANE)
#    # Wooden floor
    mc.setBlocks(x + 1, y -1, z + 1, x + n - 1, y - 1, z + n - 1, WOOD, 15) # 15 is Jungle (only bark)
#    # Windows all all 4 sides
    WIN_HEIGHT = y + 1
#    mc.setBlocks(x, WIN_HEIGHT, z, x + n, WIN_HEIGHT, z, GLASS) # front wall
#    mc.setBlocks(x, WIN_HEIGHT, z + 1, x, WIN_HEIGHT, z + n, GLASS) # left wall
#    mc.setBlocks(x + n, WIN_HEIGHT, z, x + n, WIN_HEIGHT, z + n, block.GLASS.id) # right wall
#    mc.setBlocks(x, WIN_HEIGHT, z + n, x + n, WIN_HEIGHT, z + n, block.GLASS.id) # back wall
    # Make the door
    mid = n/2
    mc.setBlocks(x + mid - 1, y, z, x + mid + 1, y + DOOR_HEIGHT, z, AIR)
#    # Bedroom wall
    mc.setBlocks(x + mid, y, z + mid, x + n - 1, y + n - 1, z + mid, COBBLESTONE)
#    # A single, activated TNT block
    mc.setBlock(x + 2, y, z + 2, TNT, 1) #    # A pile of activated TNT on the glass roof
    mc.setBlocks(x + mid, y + n, z + mid, x + n, y + n + 5, z + mid, TNT, 1)
#    # Moat
#    depth = y - 3
#    mc.setBlocks(x - 3, depth, z - 3, x + n + 3, depth, z - 3, WATER) # front side
#    mc.setBlocks(x - 3, depth, z + n + 3, x + n + 3, depth, z + n + 3, WATER) # back side
#    mc.setBlocks(x - 3, depth, z - 2, x - 3, depth, z + n + 2, WATER) # left side
#    mc.setBlocks(x + n + 3, depth, z - 2, x + n + 3, depth, z + n + 2, WATER) # right side

turtle.onkey(house, "h")

def clear_space(n):
    """
    Clears an area n x n x n encircling the player's position.

    Args:
        n - `int`. The number of blocks to clear in all directions.
    """
    x, y, z = mc.player.getTilePos()
    mc.setBlocks(x - n, y, z - n, x + n, y + n , z + n, AIR)

def clear_space_below_too(n):
    """
    Same as clear_space() above, but also clears below.
    And also adds a house!

    Args:
        n - `int`. The number of blocks to clear in all directions.
    """
    x, y, z = mc.player.getTilePos()
    mc.setBlocks(x - n, y - n, z - n, x + n, y + n , z + n, AIR)
    if n > 15:
        house(n - 10)

def dont_hit_blocks(block_types):
    """
    Any player that hits a one of the forbidden blocks will be teleported 64 blocks into the air.

    Args:
        block_types: `list` of block IDs not to hit.
    """
    while True:
        hits = mc.events.pollBlockHits()
        for h in hits:
            pos = h.pos
            block_id = mc.getBlock(*pos)
#            # Check which type of block was hit
            if block_id in block_types:
#                # See who hit it
                player_id = h.entityId
                x, y, z = mc.entity.getPos(player_id)
                # Teleport player into air
                mc.entity.setPos(player_id, x, 64, z)

def player_ids():
    ids = mc.getPlayerEntityIds()
    return ids

def move_player(player_id, x, y, z):
   mc.entity.setPos(player_id, x, y, z)

def digout(player_id):
    """
    Changes the specified player's y reading to -10.
    Useful if they're misbehaving since they'll need to find a way out.
    """
    x, y, z = mc.player.getPos()
    y = -10
    mc.entity.setPos(player_id, x, y, z)
    mc.setBlocks(x - 1, y, z - 1, x + 1, y, z + 1, AIR)

def trailing_blocks(block_id, data_values=[]):
    """
    Anywhere the player goes, a block of the given ID will be placed
    at the player's current position.
    """
    while True:
        x, y, z = mc.player.getTilePos()
        mc.setBlock(x, y, z, block_id, *data_values)
        #time.sleep(0.1)

def trailing_blocks_delay(block_id, data_values=[]):
    """
    Same as trailing_blocks() above, but adds a 0.3s delay.
    """
    while True:
        x, y, z = mc.player.getTilePos()
        mc.setBlock(x, y, z, block_id, *data_values)
        time.sleep(0.3)

#def tunnel_man():
#     x, y, z = mc.player.getPos()
     
turtle.listen()
