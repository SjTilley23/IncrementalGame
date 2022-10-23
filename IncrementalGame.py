import time
import pygame
import math

pygame.init()
pygame.font.init()
Type = pygame.font.SysFont("Tahoma", 72)
Type2 = pygame.font.SysFont("Tahoma", 36)
Type3 = pygame.font.SysFont("Tahoma",12)
window = pygame.display.set_mode([1200 , 800])
run = True
number = 0
previousClick = 0
previousTick = 0
buttonColoration = 0
rawTime2 = 0
perclick = 1
perclickamount = 0
n1amount = 0
n2amount = 0
n3amount = 0
n4amount = 0
n5amount = 0
n6amount = 0
n7amount = 0
buyShift = 0
perClickCost = 20
n1cost = 20
n2cost = 20 
n3cost = 20 
n4cost = 20 
n5cost = 20 
n6cost = 20 
n7cost = 20 
clock = pygame.time.Clock()
while run:
    
    window.fill((119, 119, 119))
    
    #Fps Counter
    clock.tick()
    fPS = Type3.render(str(math.trunc(clock.get_fps())) + " fps", True, (0,0,0))
    window.blit(fPS, (0,0))
    
    # Event Log
    for event in pygame.event.get():
        
        # Quitting
        if event.type == pygame.QUIT:
            run = False
    
    # Things on Screen Excluding Number
    pygame.draw.circle(window, (255,0,0),(600,400),50)
    pygame.draw.rect(window, (225,225,225), (900,0,350,800))
    rectangleCoordinates = [0,100,200,300,400,500,600,700]
    for index, amount in enumerate(rectangleCoordinates):
        pygame.draw.rect(window, (0,0,0), (900, amount, 350,100),5)
    pygame.draw.line(window, (218,165,32),(0,107),(600,107),5)

    # Names of the Purchases
    clickingPower = Type2.render("Clicking Power",True, (30,30,30))
    window.blit(clickingPower,(910,0)) 
    amounts = [ 1, 5, 20, 50, 100, 200, 500 ]
    for index, amount in enumerate(amounts):
        surface = Type2.render("+" + str(amount) + " Per Second", True, (0, 0, 0))
        window.blit(surface, (910, 100 + index * 100))
   
    # Number of purchases
    purchases = [perclickamount,n1amount,n2amount,n3amount,n4amount,n5amount,n6amount,n7amount]
    for index, amount in enumerate(purchases):
        purchasesFont = Type.render(str(amount), True, (0,0,0))
        widthOfText = purchasesFont.get_width()
        window.blit(purchasesFont, (900 - widthOfText,0 + index * 100))

    # Number +1 per Click
    click = pygame.mouse.get_pressed()
    if pygame.mouse.get_pos()[0] >= 550 and  pygame.mouse.get_pos()[0] <= 650 and  pygame.mouse.get_pos()[1] >= 350 and  pygame.mouse.get_pos()[1] <= 450:
        if previousClick == False and click[0]:
            buttonColoration = 8
            number = number + perclick
    seven = Type.render(str(number) + " Gold", True, (218,165,32))
    window.blit(seven, (50,20))

    # Button Reacting to clicking
    if buttonColoration > 0:
        buttonColoration = buttonColoration - 1
        pygame.draw.circle(window, (30,30,30),(600,400),50)

    # increasing clicking amount when buying clicking power
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 0 and  pygame.mouse.get_pos()[1] <= 100 and previousClick == False and click[0] and number - 20 >= 0:
        perclick = perclick + 1
        number = number - perClickCost
        perclickamount = perclickamount + 1
    
    # n1 - 7 Buys
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 100 and  pygame.mouse.get_pos()[1] <= 200 and previousClick == False and click[0] and number - 20 >= 0:
        n1amount = n1amount + 1
        number = number - n1cost
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 200 and  pygame.mouse.get_pos()[1] <= 300 and previousClick == False and click[0] and number - 20 >= 0:
        n2amount = n2amount + 1
        number = number - n2cost
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 300 and  pygame.mouse.get_pos()[1] <= 400 and previousClick == False and click[0] and number - 20 >= 0:
        n3amount = n3amount + 1
        number = number - n3cost
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 400 and  pygame.mouse.get_pos()[1] <= 500 and previousClick == False and click[0] and number - 20 >= 0:
        n4amount = n4amount + 1
        number = number - n4cost
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 500 and  pygame.mouse.get_pos()[1] <= 600 and previousClick == False and click[0] and number - 20 >= 0:
        n5amount = n5amount + 1
        number = number - n5cost
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 600 and  pygame.mouse.get_pos()[1] <= 700 and previousClick == False and click[0] and number - 20 >= 0:
        n6amount = n6amount + 1
        number = number - n6cost
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 700 and  pygame.mouse.get_pos()[1] <= 800 and previousClick == False and click[0] and number - 20 >= 0:
        n7amount = n7amount + 1
        number = number - n7cost
    
    #n1 - 7 application
    rawTime = clock.get_time()
    rawTime2 = rawTime + rawTime2
    if rawTime2 >= 1000:
        number = number + (n1amount * 1) + (n2amount * 5) + (n3amount * 20) + (n4amount * 50) + (n5amount * 100) + (n6amount * 200) + (n7amount * 500)
        rawTime2 = 0
    
    #per second counter
    perSecond = Type2.render(str((n1amount * 1) + (n2amount * 5) + (n3amount * 20) + (n4amount * 50) + (n5amount * 100) + (n6amount * 200) + (n7amount * 500)) + " G/s", True, (0,0,0))
    window.blit(perSecond, (30,110))

    #Display Costs
    Costslist = [perClickCost,n1cost,n2cost,n3cost,n4cost,n5cost,n6cost,n7cost]
    for index, amount in enumerate(Costslist):
            costFont = Type2.render(str(amount) + " g",True,(0,0,0))
            window.blit(costFont, (1020, 50 + (index * 100)))

    # Render
    previousClick = click[0]
    pygame.display.flip()
    clock.tick(30)
        
pygame.quit()
            
