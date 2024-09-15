import pygame
import time
import random
pygame.init()
window=(900,900)
pygame.display.set_caption("Orcanoid")
font=pygame.font.SysFont("Arial", 40)
tnof=pygame.font.SysFont("Arial", 40)
counter=0
center=window[0]/2,window[1]/2
Window=pygame.display.set_mode((window[0], window[1]))
backgraund=pygame.image.load('backgraund.png').convert()
backgraund=pygame.transform.scale(backgraund,(window[0], window[1]))
FPS=30
clock=pygame.time.Clock()
class Slab:
    def __init__(self,x,y,width,height,speed=0):
        self.x=x
        self.y=y
        self.slab_w=width
        self.slab_h=height
        self.slab_s=speed
        self.slab=pygame.Rect(self.x, self.y, self.slab_w ,self.slab_h)
    def move(self,keys):
        if keys[pygame.K_LEFT] and self.slab.left>0:
            self.slab.left-=self.slab_s
        elif keys[pygame.K_RIGHT] and self.slab.right<window[0]:
            self.slab.right+=self.slab_s
class Ball:
    def __init__(self):
        self.ball_radius=20
        self.ball_speed=6
        self.ball=pygame.Rect(center[0],center[1],self.ball_radius*2,self.ball_radius*2)
        self.bx=random.choice([-1,1])
        self.by=random.choice([-1])
    def move(self):
        self.ball.x+=self.ball_speed*self.bx
        self.ball.y+=self.ball_speed*self.by
        if self.ball.centerx< self.ball_radius or self.ball.centerx> window[0]- self.ball_radius:
            self.bx=-self.bx
        if self.ball.centery<self.ball_radius:
            self.by=-self.by
platform=Slab(window[0]//2-150,window[1]-60,300,30,15)
ball=Ball()
def detect_collision(bx,by,ball,rect):
    if bx>0:
        delta_x=ball.right-rect.left
    else :delta_x=rect.right-ball.left
    if by>0:
        delta_y=ball.bottom-rect.top
    else:delta_y=rect.bottom-ball.top
    if delta_x>delta_y:
        by=-by
    elif delta_y> delta_x:
        bx=-bx
    return bx,by
block_box=[Slab(x,y,100,30).slab for y in range(20,161,40) for x in range(15,786,110)]
def main():
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    global FPS,counter
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    exit()
        platform.move(pygame.key.get_pressed())
        ball.move()
        if ball.ball.colliderect(platform.slab):
            ball.bx,ball.by=detect_collision(ball.bx,ball.by,ball.ball,platform.slab)
        hit_index=ball.ball.collidelist(block_box)
        if  FPS>93:
            text=tnof.render("You won",1,pygame.Color("black"))
            Window.blit(text,(400,400))
            time.sleep(3)
            exit()
        if hit_index!= -1:
            ball.bx,ball.by=detect_collision(ball.bx,ball.by,ball.ball,block_box[hit_index])
            block_box.pop(hit_index)
            FPS+=2
            counter+=1
        Window.blit(backgraund,(0,0))
        pygame.draw.rect(Window,pygame.Color("blue"),platform.slab)
        pygame.draw.circle(Window,pygame.Color("yellow"),ball.ball.center,ball.ball_radius)
        [pygame.draw.rect(Window,pygame.Color("orange"),block)for block in block_box]
        text=font.render(F"СЧЕТ:{counter}",1,pygame.Color("black"))
        Window.blit(text,(300,300))
        pygame.display.update()
        clock.tick(FPS)
if __name__ =='__main__':
    main()
        #elif FPS==110:
            #pygame.display.set_caption("You lose")  
            
    
        


































    pygame.quit()