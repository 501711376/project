mars=[12,23,34]
pavo=[211,23,432]
user=[0,0,0]
def calcdistance (locA, locB):
    xdis=locA[0]-locB[0]
    ydis=locA[1]-locB[1]
    zdis=locA[2]-locB[2]
    locA= mars
    locB=user

totaldistance= ((xdis**2 + ydis**2 + zdis**2)**1/2
