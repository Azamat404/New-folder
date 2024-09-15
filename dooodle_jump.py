import pygame 
import random
import sys
pygame.init()
width=400
height=600
font=pygame.font.SysFont("Arial", 26)
FPS=30
FPS_clock=pygame.time.Clock()
counter=0
screen=pygame.display.set_mode((width,height))
class Doodle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed=0
        self.color="green"
        self.image=pygame.Surface((50,50))
        self.image.fill((0,255,0))
        self.rect=self.image.get_rect()
        self.last_collided_platform=None
        self.rect.center=(width//2,height//2)
    def jump(self):
        self.speed-=15
    def update(self):

        self.speed+=0.8
        self.rect.y+=self.speed
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right<width:
            self.rect.x+=5
        elif  keys[pygame.K_LEFT] and self.rect.left>0:
            self.rect.x-=5
class Platform(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.Surface((100,10))
        self.image.fill((255,255,255))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
def create_platforms():
    platforms_y=[]
    while len(platforms_y)<6:
        new_y=random.randint(0,height -10)
        if all(((abs(new_y-y))>60)   for y in platforms_y):
            platforms_y.append(new_y)

    for y in platforms_y:
        p=Platform(random.randint(0,width-100),y)
        all_sprites.add(p)
        platforms.add(p)
def write(surface,text,size,x,y):
    font=pygame.font.SysFont("Arial", size)
    text_surface=font.render(text,True,(255,255,255))
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surface.blit(text_surface,text_rect)
def start_screen():
    screen.fill((0,0,0))
    write(screen,"Doodle Jump",48,width//2,height//4)
    start_button=pygame.Rect(width//2-50,height//2+50,100,50)
    pygame.draw.rect(screen,(0,255,0),start_button)
    write(screen ,"Start",25,width/2,height//2+60)
    pygame.display.flip()
    live=True
    while live:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    live=False
def gameover_screen():
    screen.fill((0,0,0))
    write(screen,"Game over",48,width//2,height//4)
    write(screen ,"Press any button to restart",25,width/2,height//2+60)
    pygame.display.flip()
    live=True
    while live:

        for event in pygame.event.get():
          if event.type==pygame.QUIT:
            sys.exit()
          if event.type==pygame.KEYDOWN:
                live=False
def loop():
    global all_sprites, platforms,doodle
    all_sprites.add(doodle)
    create_platforms()
    collided_platforms=set()
    running=True
    counter=0
    
    while running:
        #print(doodle.speed,doodle.rect.y)

        for event in pygame.event.get():
          if event.type==pygame.QUIT:
            running=False
            
        all_sprites.update()
        if doodle.speed >0 :
            hits=pygame.sprite.spritecollide(doodle,platforms,False) 
            if hits:
                doodle.rect.y=hits[0].rect.top-doodle.rect.height
                doodle.jump()
                doodle.last_collided_platform=hits[0]
                if hits[0] not in collided_platforms:
                    counter+=1
                    collided_platforms.add(hits[0])
                #print(doodle.last_collided_platform,hits[0])

        if doodle.rect.top<=height/2:
            doodle.rect.y+=abs(doodle.speed)
        
            for plat in platforms:
                plat.rect.y+=abs(doodle.speed)
                if plat.rect.top>=height:
                    plat.kill()
                    new_y=random.randint(-10, 0)
                    if all(abs(new_y-p.rect.y)>60 for p in platforms):
                        p=Platform(random.randint(0,width-100),new_y)
                        all_sprites.add(p)
                        platforms.add(p)
        if doodle.rect.top>height:
            running=False
        screen.fill("black")
        all_sprites.draw(screen,doodle)


        text=font.render(F"СЧЕТ:{counter}",1,pygame.Color("orange"))
        screen.blit(text,(5,5))
        pygame.display.flip()
        FPS_clock.tick(FPS)
    gameover_screen()
while True:
    start_screen()
    doodle=Doodle()
    all_sprites= pygame.sprite.Group()
    platforms=pygame.sprite.Group()
    loop()
pygame.quit()