import random
import pygame
pygame.init()
font=pygame.font.SysFont("Arial", 26)
counter=0
widht,height=600,600
cell=30
FPS=10
x,y=widht//2,height//2
move={"UP":True,"DOWN":True,"LEFT":True,"RIGHT":True}
apple=(random.randrange(0,widht, cell),random.randrange(0,height,cell))
snake=[(x,y)]
lenght=1
move_x,move_y=0,0
window=pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake game")
clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                exit()
            elif event.key==pygame.K_w and move["UP"]:
                move_x=0
                move_y=-1
                move={"UP":True,"DOWN":False,"LEFT":True,"RIGHT":True}
            elif event.key==pygame.K_a and move["LEFT"]:
                move_x=-1
                move_y=0
                move={"UP":True,"DOWN":True,"LEFT":True,"RIGHT":False}
            elif event.key==pygame.K_s and move["DOWN"]:
                move_x=0
                move_y=1
                move={"UP":False,"DOWN":True,"LEFT":True,"RIGHT":True}
            elif event.key==pygame.K_d and move["RIGHT"]:
                move_x=1
                move_y=0   
                move={"UP":True,"DOWN":True,"LEFT":False,"RIGHT":True}        
    x+=move_x*cell
    y+=move_y*cell
    snake.insert(0,(x,y))
    if len(snake)>lenght:
        snake.pop()#delete last element in list
    if (x<0 or x > widht - cell or y< 0 or y>height - cell) or len(snake) != len(set(snake)):
        x,y= widht/2 , height/2
        snake=[(x,y)]
        lenght=1
        move_x,move_y=0,0
        counter=0
    if snake[0] == apple:
       apple=(random.randrange(0,widht, cell),random.randrange(0,height,cell))
       lenght+=1
       counter+=1

    clock.tick(FPS)
    window.fill("darkblue")
    for I in snake:
        if I==snake[0]:
            pygame.draw.rect(window,pygame.Color("yellow"),(I[0],I[1],cell-2,cell-2))
        else :pygame.draw.rect(window,pygame.Color("green"),(I[0],I[1],cell-2,cell-2))
    while apple in snake:
        apple=(random.randrange(0,widht, cell),random.randrange(0,height,cell))
    pygame.draw.rect(window,pygame.Color("red"),(*apple,cell,cell))
        



    text=font.render(F"СЧЕТ:{counter}",1,pygame.Color("orange"))
    window.blit(text,(5,5))
    pygame.display.update()
pygame.quit()