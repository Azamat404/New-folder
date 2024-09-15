import pygame
pygame.init()
x=640
y=480
window=pygame.display.set_mode((x,y))
FPS=30
clock=pygame.time.Clock()
ufo=pygame.image.load("Ufo.png")
ufo=pygame.transform.scale(ufo,(50,50))
ufo_rect=ufo.get_rect()
speed_ufo=10
frame=pygame.Rect(400,200,80,80)
box=pygame.Rect(200,200,80,80)
ball=pygame.Rect(x//2,y-100,20,20)
ball_x=1
font=pygame.font.SysFont("Arial",20,bold=True)
def move():
    global ball_x
    ball.x+=speed_ufo*0.5*ball_x
    if ball.right>= 640 or ball.left <=0:
        ball_x*=-1

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    key=pygame.key.get_pressed()
    if key[pygame.K_UP]:
        ufo_rect.y-=speed_ufo
    elif key[pygame.K_DOWN]:
        ufo_rect.y+=speed_ufo
    elif key[pygame.K_LEFT]:
        ufo_rect.x-=speed_ufo
    elif key[pygame.K_RIGHT]:
        ufo_rect.x+=speed_ufo
    window.fill((95,143,132))
    pygame.draw.rect(window,(0,0,255),box)
    pygame.draw.rect(window,(255,0,0),frame)
    pygame.draw.circle(window,(0,255,0),ball.center,20)
    text=font.render(F"Координаты:X{ufo_rect.x},Y{ufo_rect}",1,pygame.Color("yellow"))
    window.blit(text,(5,5))
    window.blit(ufo,ufo_rect)
    move()













    pygame.display.update()
    clock.tick(FPS)