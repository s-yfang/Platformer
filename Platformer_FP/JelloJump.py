from pygame import *
from random import *

init()
size = width, height = 500, 650
screen = display.set_mode(size)

#music / sounds
mixer.music.load("music/Two Dots Theme Music.mp3")
mixer.music.play(-1,0) 

#fonts
arialFnt = font.SysFont("Arial",20)
comicFnt = font.SysFont("Comic Sans MS",20)
bigComicFnt = font.SysFont("Comic Sans MS",50)

myClock = time.Clock()

#set window caption
display.set_caption("JELLO JUMP")

#colours
grey = (111,111,111)
lightGrey = (232,232,232)
darkGrey = (100,100,100)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
pink = (255,174,201)
lightPink = (255,198,255)
yellow = (255,249,132)
cream = (255,254,236)
lightGreen = (197,241,135)

#backgrounds
seaPic = image.load("images/sea.png")
useSeaPic = transform.smoothscale(seaPic,screen.get_size())

cityPic = image.load("images/city.jpg")
useCityPic = transform.smoothscale(cityPic,screen.get_size())

skyPic = image.load("images/sky.jpg")
useSkyPic = transform.smoothscale(skyPic,screen.get_size())

moonPic = image.load("images/moon.jpg")
useMoonPic = transform.smoothscale(moonPic,(width+500,height))

#titles
menuPic = image.load("images/menu.png")
useMenuPic = transform.smoothscale(menuPic,screen.get_size())

startPic = image.load("images/start2.png")
usestartPic = transform.smoothscale(startPic,screen.get_size())

instructPic = image.load("images/instructions.jpg")
useInstructPic = transform.smoothscale(instructPic,screen.get_size())

#characters
blob1Pic = image.load("images/charLeft.png")
blob2Pic = image.load("images/char.png")

blueBlob1Pic = image.load("images/blueBlob1.png")
blueBlob2Pic = image.load("images/blueBlob2.png")

greenBlob1Pic = image.load("images/greenBlob1.png")
greenBlob2Pic = image.load("images/greenBlob2.png")

poop1Pic = image.load("images/poop1.png")
poop2Pic = image.load("images/poop2.png")

#item pics
starPic = image.load("images/star.png")
trampolinePic = image.load("images/trampoline.png")
heartPic = image.load("images/heart.png")

#enemy pics
enemyLeft = image.load("images/enemy1.png")
enemyRight = image.load("images/enemy2.png")

#platform pic
platPic = image.load("images/platform.png")

#char values
X = 0
Y = 1
VY = 2
ground = 3
left = 4
char = [width/2,height-60,0,True,False]

jumpTime = 0
hearts = 4

#setting
back = "sea"
player = "blob"

#scores
points = 0
gotStars = 0

#bullet 
bullets = []
coolTime = 0

#enemy list
enemies = []

#item list
items = []
                
#platform list
plats = [Rect(-10,height-60,width+10,60),Rect(150,height-160,100,20)]

for i in range(8):
    w = randint(100,120)
    plat = Rect(randint(0,width-w),randint(0,height-150),w,20)

    #platPicTrans = transform.scale(platPic, (w, 20))
    
    if plat not in plats:
        plats.append(plat)
        
#star list
stars = []

def menu():
    running = True
    myClock = time.Clock()
    buttons = [Rect(width//2-50,y*70+250,100,40) for y in range(2)]
    vals = ["start","instructions"]
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"

        mpos = mouse.get_pos()
        mb = mouse.get_pressed()
        
        screen.blit(useMenuPic,(0,0))
        
        for b,v in zip(buttons,vals):
            draw.rect(screen,white,b)
            draw.rect(screen,pink,b,4)
            if b.collidepoint(mpos):
                draw.rect(screen,lightGrey,b)
                draw.rect(screen,pink,b,4)
                if mb[0]==1:
                    return v
            else:
                draw.rect(screen,white,b)
                draw.rect(screen,pink,b,4)

        playText = arialFnt.render("Play!",True,black)
        screen.blit(playText,(width//2-17,257))

        intructText = arialFnt.render("Instructions",True,black)
        screen.blit(intructText,(width//2-37,70+257))
                        
        display.flip()

def start():
    global back,player
    running = True
    
    backButtons = [Rect(x*145+6,height//2,50,50) for x in range(4)]
    backgrounds = ["sea","city","sky","moon"]

    charButtons = [Rect(x*145+10,height-80,50,50) for x in range(4)]
    characters = ["blob","blueBlob","greenBlob","poop"]

    go = Rect(width-104,62,86,95)

    smallSeaPic = transform.scale(seaPic,(50,50))
    smallCityPic = transform.scale(cityPic,(50,50))
    smallSkyPic = transform.scale(skyPic,(50,50))
    smallMoonPic = transform.scale(moonPic,(50,50))

    smallBlob2Pic = transform.scale(blob2Pic,(50,50))
    smallBlueBlob2Pic = transform.scale(blueBlob2Pic,(50,50))
    smallGreenBlob2Pic = transform.scale(greenBlob2Pic,(50,50))
    smallPoop2Pic = transform.scale(poop2Pic,(50,50))
    
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
            if evnt.type == KEYDOWN:
                running = False

        mpos = mouse.get_pos()
        mb = mouse.get_pressed()

        screen.blit(usestartPic,(0,0))

        #background buttons
        for r,v in zip(backButtons,backgrounds):
            draw.rect(screen,pink,r,5)
            if r.collidepoint(mpos):
                draw.rect(screen,white,r,5)
                if mb[0]==1:
                    back = v
            else:
                draw.rect(screen,pink,r,5)

        screen.blit(smallSeaPic,(6,height//2))
        screen.blit(smallCityPic,(145+6,height//2))
        screen.blit(smallSkyPic,(2*145+6,height//2))
        screen.blit(smallMoonPic,(3*145+6,height//2))

        #character buttons
        for b,c in zip(charButtons,characters):
            draw.rect(screen,pink,b,5)
            if b.collidepoint(mpos):
                draw.rect(screen,white,b,5)
                if mb[0]==1:
                    player = c
            else:
                draw.rect(screen,pink,b,5)

        screen.blit(smallBlob2Pic,(10,height-80))
        screen.blit(smallBlueBlob2Pic,(145+10,height-80))
        screen.blit(smallGreenBlob2Pic,(2*145+10,height-80))
        screen.blit(smallPoop2Pic,(3*145+10,height-80))

        #start button
        if go.collidepoint(mpos):
                draw.rect(screen,white,go,1)
                if mb[0]==1:
                    return "game"
                
        display.flip()

    return "menu"

def instructions():
    running = True
    screen.blit(useInstructPic,(0,0))
    
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
            if evnt.type == KEYDOWN:
                running = False
        
        display.flip()
        
    return "menu"

def drawScene(screen,char,points,enemies,bullets):
    
    #draw background
    if back == "sea":
        screen.blit(useSeaPic,(0,0))
    if back == "city":
        screen.blit(useCityPic,(0,0))
    if back == "sky":
        screen.blit(useSkyPic,(0,0))
    if back == "moon":
        screen.blit(useMoonPic,(0,0))
        
    #platforms
    for pl in plats:
        draw.rect(screen,grey,pl)
        draw.rect(screen,black,pl,2)

        #screen.blit(platPicTrans, (w
        screen.blit(blob1Pic,(char[X],char[Y]))

    #enemies
    for ex,ey,ed in enemies:
        if ed == 2:
            screen.blit(enemyRight,(ex,ey))
        if ed == -2:
            screen.blit(enemyLeft,(ex,ey))

    #stars
    for s in stars:
        screen.blit(starPic,s)

    #items
    for it in items:
        screen.blit(trampolinePic,(it[0],it[1]))

    #draw bullets
    for b in bullets:
        draw.circle(screen,black,(int(b[0]),int(b[1])),9) #outline
        draw.circle(screen,pink,(int(b[0]),int(b[1])),7)

    #draw hearts
    for h in range(hearts):
        screen.blit(heartPic,(40*h-10,25))
    
    #draw char
    if player == "blob":
        if char[left] == True:
            screen.blit(blob1Pic,(char[X],char[Y]))
        else:
            screen.blit(blob2Pic,(char[X],char[Y]))
    if player == "blueBlob":
        if char[left] == True:
            screen.blit(blueBlob1Pic,(char[X],char[Y]))
        else:
            screen.blit(blueBlob2Pic,(char[X],char[Y]))
    if player == "greenBlob":
        if char[left] == True:
            screen.blit(greenBlob1Pic,(char[X],char[Y]))
        else:
            screen.blit(greenBlob2Pic,(char[X],char[Y]))
    if player == "poop":
        if char[left] == True:
            screen.blit(poop1Pic,(char[X],char[Y]))
        else:
            screen.blit(poop2Pic,(char[X],char[Y]))
    
    #draw circle for power jump
    if jumpTime == 0:
        draw.ellipse(screen,yellow,(char[X]-9,char[Y]-8,75,75),3)
        
    #draw points
    draw.rect(screen,white,(0,0,72,30))
    draw.rect(screen,black,(0,0,72,30),2)
    scoreText = comicFnt.render(str(points),True,black)
    screen.blit(scoreText,(5,0))

    #draw star text   
    draw.rect(screen,white,(width-72,0,72,30))
    draw.rect(screen,black,(width-72,0,72,30),2)
    scoreText = comicFnt.render(str(gotStars),True,black)
    screen.blit(scoreText,(width-67,0))
    
    display.flip()    

def movePlats(plats,char):
    global points
    for pl in plats:
         
        #moves plat up when char falls
        if char[Y] >= height:
            pl.y -= 45
            #remove when above the screen
            if pl.y <= 0:
                plats.remove(pl)
                
        #remove when below the screen
        if pl.y >= height:
            plats.remove(pl)
            points += 100

        #spawns new plat
        while len(plats) < 8 and pl.y >= height: #allows for gameover
            w = randint(100,120)
            new = Rect(randint(0,width-w),randint(0,height//3-50),w,20)
            if new not in plats: #no overlap 
                plats.append(new)
                
def moveChar(char,plats,stars):
    keyP = key.get_pressed()
    
    #left/right 
    if keyP[K_LEFT]: 
        char[X] -= 10
        char[left] = True

    if keyP[K_RIGHT]: 
        char[X] += 10
        char[left] = False
        
    if char[ground]:
        char[VY] = -10
        char[ground] = False
        
    #add current speed to Y
    char[Y] += char[VY] 
    char[VY] += .5

    #char crosses the screen 
    if char[X] > width:
        char[X] = 0
    if char[X] < 0:
        char[X] = width

    #move stuff
    top = height//3

    if char[Y] <= top :
        above = top - char[Y]
        for pl in plats:
            pl.y += above
        for st in stars:
            st.y += above
        for it in items:
            it.y += above
        for en in enemies:
            en[1] += above
        char[Y] = top

def spawnStar():
    return Rect(randint(0,width-40),randint(0,height/2),40,40)

def collideStar(stars,char):
    global gotStars, hearts
    charRec = Rect(char[X],char[Y],55,50)
    
    for st in stars:
        #remove from list when collide
        if charRec.colliderect(st):
            stars.remove(st)
            gotStars += 1

    #gain extra heart when player gets 10 stars
    if gotStars == 10: 
        hearts += 1
        gotStars = 0

def spawnItem(plats):
    for p in plats:
        itemx = p.x
        itemy = p.y - 45
        return Rect(itemx,itemy,60,60)

def moveObj(char,objectList):
    for obj in objectList:

        #removes items when below screen
        if obj.y > height:
            objectList.remove(obj)

        #moves items up when char falls
        if char[Y] >= height:
            obj.y -= 45
            #remove when above the screen
            if obj.y <= 0:
                objectList.remove(obj)
                
def collideItem(items,char):
    charRec = Rect(char[X],char[Y],55,50)
    for it in items:
        itemRect = Rect(it)
        if charRec.colliderect(itemRect):
            char[VY] = -20
            items.remove(it)

def powerJump(char): 
    global jumpTime
    keys = key.get_pressed()

    #count before next power jump
    if jumpTime > 0:
        jumpTime -= 1

    if keys[K_z] and jumpTime == 0:
        jumpTime = 700
        char[VY] = -40

def spawnEnemy():
    #[x, y, walkDir] 
    x = choice([-100,width+100]) #random left or right spawn
    direct = 2
    if x == width+100: 
        direct = -2
    return [x, randint(0,height//2), direct]

def moveEnemy(enemies,char,points):
    for en in enemies:
        en[0] += en[2]

        #remove enemy when below screen
        if en[1] > height:
            enemies.remove(en)

        if points > 5000:
            en[0] += en[2] #makes enemies faster

        #moves enemy up when char falls
        if char[Y] >= height:
            en[1] -= 45
            #remove when above the screen
            if en[1] <= 0:
                enemies.remove(en)

def collideEnemy(enemies,char,bullets):
    global points, hearts
    charRec = Rect(char[X],char[Y],55,50)

    hits = [] #enemies collided with char
    for en in enemies:
        enemyRect = Rect(en[0],en[1],55,55)
        enemyTop = Rect(en[0],en[1]-10,55,5) 
        
        #jump on enemies
        if charRec.colliderect(enemyTop):
            if char[VY] > 0:  
                char[ground] = True
                char[VY] = 0
                char[Y] = enemyTop.y - (charRec.height + 20)
                points += 10

        #collide with enemy and lose heart
        if charRec.colliderect(enemyRect):
            enemies.remove(en)
            hearts -= 1 #lose life
            points -= 100 #lose points
            hits.append(en)
            
        #shoot enemy
        for b in bullets:
            bullectRect = Rect(b)
            if enemyRect.colliderect(bullectRect):
                if en not in hits: #to avoid shooting and colliding 
                    enemies.remove(en) #enemy at same time
                    points += 15

    #remove enemies in hit list
    for en in hits:
        hits.remove(en)

def collidePlat(char,plats):
    charRec = Rect(char[X],char[Y],55,50)
    for p in plats:
        if charRec.colliderect(p):
            if char[VY] > 0: 
                char[ground] = True
                char[VY] = 0
                char[Y] = p.y - (charRec.height + 20)

def shoot(bullets):
    global coolTime
    keys = key.get_pressed()

    #count down till next bullet
    if coolTime > 0:
        coolTime -= 1
        
    if keys[32] and coolTime == 0:
        coolTime = 15
        bullets.append(([char[X]+30,char[Y]+10,0,-8])) #[x,y,vx,vy]

    #move bullet
    for b in bullets:  
        b[1] += b[3]

        #remove bullet when above screen
        if b[1] < -10:
            bullets.remove(b)
            
def gameOver():
    running = True

    #gameover background
    if back == "sea":
        screen.blit(useSeaPic,(0,0))
    if back == "city":
        screen.blit(useCityPic,(0,0))
    if back == "sky":
        screen.blit(useSkyPic,(0,0))
    if back == "moon":
        screen.blit(useMoonPic,(0,0))
        
    #changes font colour for background
    fntCol = white
    if back == "sea":
        fntCol = black
   
    #scores
    gameover = bigComicFnt.render("Game Over",True,fntCol)
    score = comicFnt.render("Score: " + str(points),True,fntCol)
    stars = comicFnt.render("Stars: " + str(gotStars),True,fntCol)
    goBack = comicFnt.render("Press any key to exit",True,fntCol)

    #blit scores
    screen.blit(gameover,(131,120))
    
    screen.blit(score,(140,250))
    screen.blit(stars,(140,275))

    screen.blit(goBack,(152,450))

    display.flip()
    
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
            if evnt.type == KEYDOWN:
                running = False

def game():
    running = True
    while running:
        for evnt in event.get():   #checks all events that happen
            if evnt.type == QUIT:
                running = False
    
        #randomly spawn enemy
        if randint(1,80) == 1:
            if points > 5000 and len(enemies) < 6: 
                e = spawnEnemy()
                enemies.append(e)
            if len(enemies) < 4:
                e = spawnEnemy()
                enemies.append(e)
            
        #randomly spawn 1 item at a time
        if randint(1,80) == 1 and len(items) == 0:
            item = spawnItem(plats)
            items.append(item)

        #new stars
        if len(stars) == 0: 
            st = spawnStar()
            stars.append(st)

        #game over when fall
        if len(plats) == 0:
            gameOver()
            return "exit"

        #game over when lose all hearts
        if hearts == 0:
            gameOver()
            return "exit"

        collidePlat(char,plats)

        shoot(bullets)

        powerJump(char)
        
        moveChar(char,plats,stars)
        moveEnemy(enemies,char,points)
        movePlats(plats,char)

        moveObj(char,stars)
        moveObj(char,items)

        collideEnemy(enemies,char,bullets)
        collideItem(items,char)
        collideStar(stars,char)
        
        drawScene(screen,char,points,enemies,bullets)
        
        myClock.tick(60)

    return "start"

#select pages
running = True
page = "menu"
while page != "exit":
    if page == "menu":
        page = menu()
    if page == "start":
        page = start()
    if page == "game":
        page = game()    
    if page == "instructions":
        page = instructions()
    
quit()
