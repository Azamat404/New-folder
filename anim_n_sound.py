import pygame
pygame.init()
window=(600,300)
FPS=15
steps=pygame.mixer.Sound("step.ogg")
class Dude():
    def __init__(self):
        self.images=[]
        self.images.append(pygame.image.load('stand.png'))
        self.images.append(pygame.image.load('walk 2.png'))
        self.images.append(pygame.image.load('walk.png'))
        self.move_index=0
        self.image=self.images[self.move_index]
        self.rect=self.image.get_rect()
        self.move=False
        self.speed=7
        self.left=False
        self.rect.y=100
    def update(self,keys):
        if keys[pygame.K_LEFT]:
            self.move=True
            self.left=True

            self.rect.x-=self.speed

        elif keys[pygame.K_RIGHT]:
            self.move=True
            self.left=False
            self.rect.x+=self.speed
        else :
            self.move=False
            steps.stop()
        if self.move==True:

            self.move_index+=1
            if self.move_index>2:
                self.move_index=1
            self.image=self.images[self.move_index]
        else :self.image=self.images[0]
        if self.left==True:
            self.image=pygame.transform.flip(self.image,True,False)
        if self.move_index == 2 and self.move:
            steps.play(-1)
def main():
    screen=pygame.display.set_mode(window)
    clock=pygame.time.Clock()
    dude=Dude()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    while True:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
        screen.fill(pygame.Color(150,255,0))
        
        dude.update(pygame.key.get_pressed())
        screen.blit(dude.image,dude.rect)

        pygame.display.update()
        clock.tick(FPS)
        

if __name__ =='__main__':
    main()
