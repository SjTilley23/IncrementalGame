import time
import pygame
import math

pygame.init()
pygame.font.init()
Type = pygame.font.SysFont("Tahoma", 72)
Type2 = pygame.font.SysFont("Tahoma", 36)
window = pygame.display.set_mode([1200 , 800])
run = True
number = 0
previousClick = 0
previousTick = 0
buttonColoration = 0
perclick = 1
perclickamount = 0
n1amount = 0
n2amount = 0
n3amount = 0
n4amount = 0
n5amount = 0
n6amount = 0
n7amount = 0
clock = pygame.time.Clock()
while run:
    tick = clock.tick()
    if tick < 10:
        sleepTime = 10 - tick
        time.sleep((sleepTime/1000))
    window.fill((119, 119, 119))
    
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


    # Names of the Purchases
    clickingPower = Type2.render("Clicking Power",True, (30,30,30))
    window.blit(clickingPower,(910,20)) 
    amounts = [ 1, 5, 20, 50, 100, 200, 500 ]
    for index, amount in enumerate(amounts):
        surface = Type2.render("+" + str(amount) + " Per Second", True, (0, 0, 0))
        window.blit(surface, (910, 120 + index * 100))
    
    # Number of purchases
    purchases = [perclickamount,n1amount,n2amount,n3amount,n4amount,n5amount,n6amount,n7amount]
    for index, amount in enumerate(purchases):
        purchasesFont = Type.render(str(amount), True, (0,0,0))
        window.blit(purchasesFont, (850,0 + index * 100))

    # Number +1 per Click
    click = pygame.mouse.get_pressed()
    if pygame.mouse.get_pos()[0] >= 550 and  pygame.mouse.get_pos()[0] <= 650 and  pygame.mouse.get_pos()[1] >= 350 and  pygame.mouse.get_pos()[1] <= 450:
        if previousClick == False and click[0]:
            buttonColoration = 60
            number = number + perclick
    seven = Type.render(str(number), True, (218,165,32))
    window.blit(seven, (50,20))
    
    #Gold Box
    pygame.draw.rect(window, (218,165,32),(30,22,300,90),10)
    Gold = Type.render("Gold",True,(218,165,32))
    window.blit(Gold, (340,22))

    # Button Reacting to clicking
    if buttonColoration > 0:
        buttonColoration = buttonColoration - 1
        pygame.draw.circle(window, (30,30,30),(600,400),50)

    # increasing clicking amount when buying upgrade
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 0 and  pygame.mouse.get_pos()[1] <= 100 and previousClick == False and click[0] and number - 20 >= 0:
        perclick = perclick + 3
        number = number - 20
        perclickamount = perclickamount + 1
    
    # n1 - 7 Buys
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 100 and  pygame.mouse.get_pos()[1] <= 200 and previousClick == False and click[0] and number - 20 >= 0:
        n1amount = n1amount + 1
        number = number - 20
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 200 and  pygame.mouse.get_pos()[1] <= 300 and previousClick == False and click[0] and number - 20 >= 0:
        n2amount = n2amount + 1
        number = number - 20
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 300 and  pygame.mouse.get_pos()[1] <= 400 and previousClick == False and click[0] and number - 20 >= 0:
        n3amount = n3amount + 1
        number = number - 20
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 400 and  pygame.mouse.get_pos()[1] <= 500 and previousClick == False and click[0] and number - 20 >= 0:
        n4amount = n4amount + 1
        number = number - 20
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 500 and  pygame.mouse.get_pos()[1] <= 600 and previousClick == False and click[0] and number - 20 >= 0:
        n5amount = n5amount + 1
        number = number - 20
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 600 and  pygame.mouse.get_pos()[1] <= 700 and previousClick == False and click[0] and number - 20 >= 0:
        n6amount = n6amount + 1
        number = number - 20
    if pygame.mouse.get_pos()[0] >= 900 and  pygame.mouse.get_pos()[0] <= 1200 and  pygame.mouse.get_pos()[1] >= 700 and  pygame.mouse.get_pos()[1] <= 800 and previousClick == False and click[0] and number - 20 >= 0:
        n7amount = n7amount + 1
        number = number - 20
    
    #n1 - 7 application
    if previousTick >= 1000:
        number = number + (n1amount * 1) + (n2amount * 5) + (n3amount * 20) + (n4amount * 50) + (n5amount * 100) + (n6amount * 200) + (n7amount * 500)
        previousTick = 0
    previousTick = previousTick + tick
    
    # Render
    previousClick = click[0]
    pygame.display.flip()
        
pygame.quit()
            