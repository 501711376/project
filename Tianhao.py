mars=[12,23,34]
pavo=[211,23,432]
user=[0,0,0]
xdis=locA[0]-locB[0]
ydis=locA[1]-locB[1]
zdis=locA[2]-locB[2]

def calcdistance (locA, locB):
    global xdis
    xdis=locA[0]-locB[0]
    global ydis=locA[1]-locB[1]
    global zdis=locA[2]-locB[2]
    locA= mars
    locB=user
    

choice=input("where do you want to go")

calcdistance (0,0)

if choice== "mars":
    totaldistance=(xdis**2 + ydis**2 + zdis**2)**0.5
elif choice=="pavo":
    totaldistance=(xdis**2 + ydis**2 + zdis**2)**0.5
