mars=(12,23,34)
pavo=(211,23,432)
user=(0,0,0)

#we din't need this here



def calcdistance (locA, locB):
    
    xdis=locA[0]-locB[0]
    ydis=locA[1]-locB[1]
    zdis=locA[2]-locB[2]
    
    totaldistance=(xdis**2 + ydis**2 + zdis**2)**0.5
    #retunr 0 for now
    return totaldistance
    
def navigate():
    choice=input("where do you want to go")

    #calcdistance (0,0)

    if choice== "mars":
        print("The distance is", calcdistance(mars,user))
        user=mars
        

    #totaldistance=(xdis**2 + ydis**2 + zdis**2)**0.5
    elif choice=="pavo":
        totaldistance=(xdis**2 + ydis**2 + zdis**2)**0.5
    navigate()

navigate()

