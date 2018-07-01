###                                                                                                    
# Nathaniel Watson                                                                                     
# 2018-06-26                                                                                           
# De Anza College Academy                                                                              
###

"""
See mc API at https://www.stuffaboutcode.com/p/minecraft-api-reference.html.
"""

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

def house(n):
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
    if n < 10:
       raise ValueError("n must be >= 10.")

    DOOR_HEIGHT = 3
    x, y, z = mc.player.getTilePos()
    x += 2
    mc.setBlocks(x, y, z, x + n, y + n, z + n, COBBLESTONE)
    # Carve out the inside with air blocks.
    mc.setBlocks(x + 1, y, z + 1, x + n - 1, y + n - 1, z + n - 1, AIR)
    # Make the door
    mid = x/n
    mc.setBlocks(x + mid - 1, y, z, x + mid + 1, y + DOOR_HEIGHT, z, AIR)
    # Put torch pointing up above door
    mc.setBlock(x + mid, y + DOOR_HEIGHT + 1, z - 1, COBBLESTONE)
    mc.setBlock(x + mid, y + DOOR_HEIGHT + 2, z - 1, block.TORCH.id, 5)
    # Glass roof
    mc.setBlocks(x, y, z + n - 1, x + n, y + n, z + n, GLASS_PANE)
    # Wooden floor
    mc.setBlocks(x + 1, y, z + 1, x + n - 1, y, z + n - 1, WOOD, 15) # 15 is Jungle (only bark)
    # Windows all all 4 sides
    mc.setBlocks(x, y + 2, z, x + n, y + 2, z, GLASS) # front wall
    mc.setBlocks(x, y + 2, z + 1, x, y + 2, z + n, GLASS) # left wall
    mc.setBlocks(x + n, y + 2, z, x + n, y + 2, z + n, block.GLASS.id) # right wall
    mc.setBlocks(x, y + 2, z + n, x + n, y + 2, z + n, block.GLASS.id) # back wall
    # Bedroom wall
    mc.setBlocks(x + mid, y, z + mid, x + n - 1, y + n - 1, z + mid, COBBLESTONE)
    # A single, activated TNT block
    mc.setBlock(x + 2, y, z + 2, TNT, 1)
    # A pile of activated TNT in the bedroom
    mc.setBlocks(x + mid + 2, y, z + mid + 2, x + mid + 5, y + mid, z + mid + 5, TNT, 1)
    # Moat
    depth = y - 3
    mc.setBlocks(x - 3, depth, z - 3, x + n + 3, depth, z - 3, WATER) # front side
    mc.setBlocks(x - 3, depth, z + n + 3, x + n + 3, depth, z + n + 3, WATER) # back side
    mc.setBlocks(x - 3, depth, z - 2, x - 3, depth, z + n + 2, WATER) # left side
    mc.setBlocks(x + n + 3, depth, z - 2, x + n + 3, depth, z + n + 2, WATER) # right side

def clear_space(n):
    """
    Args:
        n - `int`. The number of blocks to clear in all directions.
    """
    x, y, z = mc.player.getTilePos()
    mc.setBlocks(x, y, z, x + n, y + n , z + n, AIR)

def player_ids():
    ids = mc.getPlayerEntityIds()
    return ids

def move_player(player_id, x, y, z):
   mc.player.setPos(player_id, x, y, z)
    
