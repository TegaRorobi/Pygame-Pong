
import pygame
from random import *
black=(0,0,0)
white=(255,255,255)
magenta=(255,255,0)
pygame.init()
class Paddle(pygame.sprite.Sprite):

    def __init__(self,color, width, height) -> None:
        super().__init__()    
        self.image=pygame.Surface([width,height])
        self.image.fill(black)
         
        pygame.draw.rect(self.image,color,[0,0,width,height])
        self.rect=self.image.get_rect()   

    def moveUp(self,pixels):
        self.rect.y-=pixels
        if self.rect.y< 0:
            self.rect.y=0

    def moveDown(self,pixels):
        self.rect.y+=pixels
        if self.rect.y>400:
            self.rect.y=400

class Ball(pygame.sprite.Sprite):
    def __init__(self,color,width,height) -> None:
        #call the parent class instructor
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(black)
        #draw the sprite ball 
        pygame.draw.rect(self.image,color,[0,0,width,height])
        self.velocity=[randint(4,8),randint(-8,8)]

        self.rect=self.image.get_rect()

    def update(self):
        self.rect.x+=self.velocity[0]
        self.rect.y+=self.velocity[1]
    def bounce(self):
        self.velocity[0]=-self.velocity[0]
        self.velocity[1]=randint(-8,8)
      
screen=pygame.display.set_mode((700,500))
pygame.display.set_caption("This is a pong game made by deciphrexx programming")
#define some colors

paddleA=Paddle((255,0,0),10,100)
paddleA.rect.x=10
paddleA.rect.y=200

paddleB=Paddle((0,0,255),10,100)
paddleB.rect.x=680
paddleB.rect.y=200

ball=Ball(magenta,20,20)
ball.rect.x=345
ball.rect.y=195

all_sprites_list=pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

score_a=0
score_b=0

running=True
clock=pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        # if event.type==pygame.KEYDOWN:
        #     if event.key==pygame.K_q:
        #         pa.moveup(5)
        #     if event.key==pygame.K_a:
        #         pa.movedown(5)
        #     if event.key==pygame.K_p:
        #         pb.moveup(5)
        #     if event.key==pygame.K_l:
        #         pb.movedown(5)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_q]:
        paddleA.moveUp(5)
    if keys[pygame.K_a]:
        paddleA.moveDown(5)
    if keys[pygame.K_p]:
        paddleB.moveUp(5)
    if keys[pygame.K_l]:
        paddleB.moveDown(5)  

    all_sprites_list.update()

    if ball.rect.x>=690: 
        score_a+=1
        ball.velocity[0]=-ball.velocity[0]

    if ball.rect.x<=0:
        score_b+=1
        ball.velocity[0]=-ball.velocity[0]

    if ball.rect.y>490:
        ball.velocity[1]=-ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1]=-ball.velocity[1]

    if pygame.sprite.collide_mask(ball,paddleA) or pygame.sprite.collide_mask(ball,paddleB):
        ball.bounce()
    screen.fill(black)
    pygame.draw.line(screen,(0,255,0), (349, 0),(349,500),  5)
    pygame.draw.line(screen, white, (220, 60),(480,60),  5)

    font=pygame.font.Font(None,74)
    text=font.render(str(score_a),1,(255,0,0))
    screen.blit(text,(240,10))
    text=font.render(str(score_b),1,(0,0,255))
    screen.blit(text,(420,10))
    # text=font.render("Scores :",1,white)
    # screen.blit(text,(10,10))
    all_sprites_list.draw(screen)
    pygame.display.update()
	#limit to 60 frames per second
    clock.tick(60)
pygame.quit()





#import winsound
#winsound.playSound("bounce.wav",winsound.SND_ASYNC)