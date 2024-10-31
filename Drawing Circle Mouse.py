import pygame
pygame.init()



screen = pygame.display.set_mode([500,500])

screen.fill('white')

class MyCircle():
     def __init__(self,color,pos,radius,width):
        self.c=color
        self.pos=pos
        self.r=radius
        self.w=width
        self.s=screen


     def draw(self):
         pygame.draw.circle(self.s,self.c,self.pos,self.r,self.w)


     def grow(self):
         self.r+=10    
         pygame.draw.circle(self.s,self.c,self.pos,self.r,self.w)  




                                