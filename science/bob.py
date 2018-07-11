import turtle
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

def chat():
    mc.postToChat("Howdy!")

turtle.home()
turtle.onkey(chat, "t")
turtle.listen()
