mars = (12, 23, 34)
pavo = (211, 23, 432)
user = (0, 0, 0)

def main(winstyle = 0):
    # Initialize pygame
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print ('Warning, no sound')
        pygame.mixer = None

    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

def calcdistance(locA, locB):
    xdis = locA[0] - locB[0]
    ydis = locA[1] - locB[1]
    zdis = locA[2] - locB[2]

    totaldistance = (xdis ** 2 + ydis ** 2 + zdis ** 2) ** 0.5
    return totaldistance


def transfer():
    choice = input("mars is a transfer station, where else do you want to go")
    if choice == "pavo":
        print("The distance is", calcdistance(pavo, user))
    elif choice == "starting point":
        print("the distance is 42.76680956068619, welcome back")


def navigate():
    choice = input("where do you want to go")

    if choice == "mars":
        print("The distance is", calcdistance(mars, user))

        user == pavo

        transfer()




    elif choice == "pavo":
        print("The distance is", calcdistance(pavo, user), ",Pavo is the last station")
    elif choice != "mars" or "pavo":
        print("destination name isn't corret, please enter again.")
        navigate()


navigate()