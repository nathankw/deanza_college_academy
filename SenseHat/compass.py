from sense_emu import SenseHat
#from sense_hat import SenseHat
sense = SenseHat()

while True:
    heading = sense.get_compass()
    print(heading)
    if heading < 45 or heading > 315:
        sense.show_letter("N")
    elif heading < 135:
        sense.show_letter("E")
    elif heading < 225:
        sense.show_letter("S")
    else:
        sense.show_letter("W")
