###Zombies vs Humans
###Created by Ben Muirhead


import turtle
import random
import math
import operator
import time

wn = turtle.Screen()  
turtle.screensize(canvwidth=1000, canvheight=1000)
#random.seed(4)

numberofHumans=10
humanNames= ['alpha','beta','gamma','delta','epsilon','zeta','eta','theta','iota','kappa']
humans= ['alpha','beta','gamma','delta','epsilon','zeta','eta','theta','iota','kappa']

humanNames=humanNames[0:numberofHumans]
humans=humans[0:numberofHumans]


numberofZombies=10
zombieNames=['ein', 'zwei', 'drei', 'vier', 'funf','sechs','seiben','acht','neun','zehn']
zombies=['ein', 'zwei', 'drei', 'vier', 'funf','sechs','sieben','acht','neun','zehn']
zColors=['salmon','orange','pink','orange','gold','aqua','darkblue','green','magenta','khaki']

zombies=zombies[0:numberofZombies]
zombieNames=zombieNames[0:numberofZombies]
zColors=zColors[0:numberofZombies]

speed=0
hcount=1 #times humanNames
zcount=1 #times zombieNames
hspeed=10
zspeed=10
boxSize=250

#####
#Human Start Range
hradius=100
hSpread=50

#Initialize Humans
for j in range(0,hcount):   
    for i in range(0,len(humanNames)):
        humans[i] = turtle.Turtle()
        #humans[i].color(zColors[i])
        humans[i].speed(speed)
        humans[i].penup()
        if i == 0 and j == 0:
            #Draw Box       
            humans[i].goto(-boxSize,-boxSize)
            humans[i].pendown()
            humans[i].goto(boxSize,-boxSize)
            humans[i].goto(boxSize,boxSize)
            humans[i].goto(-boxSize,boxSize)
            humans[i].goto(-boxSize,-boxSize)
            #humans[i].write(" size: "+str(boxSize*2))
            humans[i].penup()            
        x=random.randint(-hradius,hradius)
        y=random.randrange(-1,3,2)*math.sqrt(hradius**2-x**2)+random.randint(-hSpread,hSpread)        
        x=x+random.randint(-hSpread,hSpread)
        humans[i].goto(x,y)
        humans[i].pendown()
        

#Zombie Start Range
radius1=30
radius2=200
z2Spread=30
#Initialize Zombies
for j in range(0,zcount):
    #for i in range(0,0):#len(zombies)/2):
        #zombies[i] = turtle.Turtle()
        #zombies[i].color(zColors[i])#'brown')
        #zombies[i].penup()
        #zombies[i].goto(random.randint(-radius1,radius1),random.randint(-radius1,radius1))
        #zombies[i].pendown()
    for i in range(0,len(zombieNames)):
            zombies[i] = turtle.Turtle()
            zombies[i].color(zColors[i])#'brown')
            zombies[i].penup()
            x=random.randint(-radius2,radius2)
            y=random.randrange(-1,3,2)*math.sqrt(radius2**2-x**2)+random.randint(-z2Spread,z2Spread)        
            x=x+random.randint(-z2Spread,z2Spread)            
            zombies[i].goto(x,y)
            zombies[i].pendown()    

    

dictHumans= dict(zip(humanNames,humans))
dictZombies= dict(zip(zombieNames,zombies))
dTraveled=[]
trials=500
rounds=0
###Movement
#for t in range(0,trials):
while rounds<trials: #(len(humans)>1 or rounds<trials):
    #Move Humans
    for i in range(0,len(humans)):
        #print("hello")
        hx=humans[i].pos()[0]
        hy=humans[i].pos()[1]
        hdistances={}
        objectsX={}
        objectsY={}
        for j in range(0,len(zombies)):
            zx=zombies[j].pos()[0]
            zy=zombies[j].pos()[1]
            distance=math.sqrt((hx-zx)**2 + (hy-zy)**2)
            #if rounds%5==0:
                #zombies[j].write(round(distance,0),False)
            hdistances[zombies[j]]=distance
         
            objectsX[zombies[j]]=[hx-zx,distance,(hx-zx)/distance]
            objectsY[zombies[j]]=[hy-zy,distance,(hy-zy)/distance]
        d2r=hx-boxSize
        d2l=hx+boxSize
        d2t=hy-boxSize
        d2b=hy+boxSize
        
        
        
        objectsX['right']=[d2r,abs(d2r),1]
        objectsX['left']=[d2l,abs(d2l),1]
        objectsX['top']=[0,1,1]
        objectsX['bottom']=[0,1,1]  
        
        objectsY['right']=[0,1,1]  
        objectsY['left']=[0,1,1]  
        objectsY['top']=[d2t,abs(d2t),1]
        objectsY['bottom']=[d2b,abs(d2b),1]
        
        sObjectsX = sorted(objectsX.items(),key=lambda x: x[1][1], reverse=False)
        sObjectsY = sorted(objectsY.items(),key=lambda x: x[1][1], reverse=False)
        
        xWeight1=0
        xWeight2=0
        xWeight3=0
        for weight in objectsX.keys():
            xWeight1+=objectsX[weight][0]
            xWeight2+=objectsX[weight][1]
            xWeight3+=(objectsX[weight][0])/(((objectsX[weight][1]))**2)
        yWeight1=0  
        yWeight2=0
        yWeight3=0
        for weight in objectsY.keys():
            yWeight1+=objectsY[weight][0]
            yWeight2+=objectsY[weight][1]
            yWeight3+=(objectsY[weight][0])/(((objectsY[weight][1]))**2)
        #print(objectsX)
        #print(objectsY)
        #print(xWeight3)
        #print(yWeight3)
        dx2=xWeight3
        dy2=yWeight3
        mx2=hspeed*dx2/math.sqrt(dx2**2+dy2**2)
        my2=hspeed*dy2/math.sqrt(dx2**2+dy2**2)
        #mx2=dx2/math.sqrt(dx2**2+dy2**2)
        #my2=dy2/math.sqrt(dx2**2+dy2**2)        
        
        #wallDist={}
        #wallDist['right']=abs(boxSize-humans[i].pos()[0])        
        #wallDist['left']=abs(-boxSize-humans[i].pos()[0])
        #wallDist['top']=abs(boxSize-humans[i].pos()[1])
        #wallDist['bottom']=abs(-boxSize-humans[i].pos()[1])
        #hdistances.update(wallDist) 
      
        
        #sHdistances = sorted(hdistances.items(),key=lambda x: x[1], reverse=False)
        #c=sHdistances[0][0]
        #if c in (wallDist.keys()):
            #if c=='right':
                #mx=hspeed*-1
                #my=hspeed*0
                ##print(c)
            #if c=='left':
                #mx=hspeed*1
                #my=hspeed*0
                ##print(c)
            #if c=='top':
                #mx=hspeed*0
                #my=hspeed*-1
                ##print(c)
            #if c=='bottom':
                #mx=hspeed*0
                #my=hspeed*1
                ##print(c)
        #else:                                                    
            #cZombie=dictZombies[c]
        #dx=humans[i].pos()[0]-cZombie.pos()[0]
        #dy=humans[i].pos()[1]-cZombie.pos()[1]
        #mx=hspeed*dx/math.sqrt((hx-zx)**2 + (hy-zy)**2)
        #my=hspeed*dy/math.sqrt((hx-zx)**2 + (hy-zy)**2)
            
        
        humans[i].goto(hx+mx2,hy+my2)
        
        #print round(dx2,5),round(dy2,5)
        #print(round(mx2,2),round(my2,2), math.sqrt(mx2**2+my2**2))
        dTraveled.append(math.sqrt(mx2**2+my2**2))
    
    
    
    ###Move zombies
    
    #if 1==1:
    for i in range(0,len(zombies)):
        #print humans[i]+str(humans[i].pos())
        zx=zombies[i].pos()[0]
        zy=zombies[i].pos()[1]
        zdistances={}
        for j in range(0,len(humans)):
            hx=humans[j].pos()[0]
            hy=humans[j].pos()[1]
            distance=math.sqrt((zx-hx)**2 + (zy-hy)**2)
            #zombies[j].write(round(distance,0),False)
            zdistances[humans[j]]=distance
            #print distances
        sZdistances = sorted(zdistances.items(),key=lambda x: x[1], reverse=False)
        
        #c=sZdistances[0][0]
        #cHuman=dictHumans[c]
            
        cHuman=sZdistances[0][0]
        dx=zombies[i].pos()[0]-cHuman.pos()[0]
        dy=zombies[i].pos()[1]-cHuman.pos()[1]
        mx=zspeed*dx/math.sqrt((zx-hx)**2 + (zy-hy)**2)
        my=zspeed*dy/math.sqrt((zx-hx)**2 + (zy-hy)**2)
        #cHuman.goto(hx+mx,hy+my)
        zombies[i].goto(zx-mx,zy-my)
        #print math.sqrt(mx**2+my**2)
        
    
    hlength=len(humans)    
    zlength=len(zombies)    
    for i in range(0,hlength):
        for j in range(0,zlength):
            hx=humans[i].pos()[0]
            hy=humans[i].pos()[1]
            zx=zombies[j].pos()[0]
            zy=zombies[j].pos()[1] 
            distance=math.sqrt((zx-hx)**2 + (zy-hy)**2)
            if distance<25:
                #print ("round "+str(rounds)+" "+str(zombies[j])+" ("+str(zombieNames[j].color()[0])+")"+"->"+str(humans[i])+": "+str(round(distance,1)))
                humans[i].color('red')
    
                
    
    
    
    toDelete=[]
    toDeleteList=[]
    for k in range(0,len(humans)):
        if 'red' in humans[k].color():
            toDelete.append(k)
    
    list.sort(toDelete, reverse=True)
    for n in toDelete:
        toDeleteList.append(humanNames[n])
    
    if len(toDeleteList)>0:
        print("Deleting "+ str(toDeleteList))
    
    #print "Deleting "+str(toDelete)
    for m in toDelete:
        del humans[m]
        del humanNames[m]
    
    
    
    #print "End of round "+str(rounds)
    #print ("---")
    if len(humans) == 0:
        break
    
    rounds=rounds+1


print("This set started with "+str(numberofHumans)+" humans and "+str(numberofZombies)+" Zombies.")
print("It lasted "+str(rounds)+" rounds with "+str(len(humans))+" survivors")

wn.exitonclick()
