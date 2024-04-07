import numpy as np
import random as r
import sys
import pygame
from time import sleep

cancel=False
size = 60   # Size of the world
life = 500  # Number of random cells
gen=0

def setup(size, life):  # Setting up random cells
    arr=np.zeros((size, size), int)
    for i in range(life):
        x=r.randrange(0,size)
        y=r.randrange(0,size)
        arr[x,y]=1
    return arr

def glider(arr, posx, posy):  # Setting up a Glider
    arr[posx, posy]=1
    arr[posx+1, posy]=1
    arr[posx+2, posy]=1
    arr[posx+2, posy+1]=1
    arr[posx+1, posy+2]=1
    return arr

def blinker(arr, posx, posy):  # Setting up a Blinker
    arr[posx, posy]=1
    arr[posx+1, posy]=1
    arr[posx-1, posy]=1
    return arr

def nextgen(arr, size):
    d=np.array([[1,1],
             [1,0],
             [1,-1],
             [0,1],
             [0,-1],
             [-1,1],
             [-1,0],
             [-1,-1]])
    temparr=np.zeros((size, size), int)
    for y in range(size):
        for x in range(size):
            neighbors=0
            for i in range(8):
                tx=x+d[i][0]
                if tx > size-1: tx=0
                if tx <0: tx=size-1

                ty=y+d[i][1]
                if ty > size-1: ty=0
                if ty <0: ty=size-1            

                if arr[tx,ty]==1: neighbors+=1

            if arr[x,y]==0 and neighbors ==3: temparr[x,y]=1
            if arr[x,y]==1 and neighbors <2: temparr[x,y]=0
            if arr[x,y]==1 and (neighbors ==2 or neighbors ==3): temparr[x,y]=1
            if arr[x,y]==1 and neighbors >3: temparr[x,y]=0
    return temparr
      
np.set_printoptions(threshold=sys.maxsize)

# Initial Setup of Life-Objekts
field=setup(size, life)
field=glider(field, 5,5)
field=glider(field, 10,10)
field=blinker(field, 20,20)

pygame.init()
pygame.display.set_caption('Conways Game of Life')
screen = pygame.display.set_mode([6*size, 6*size])
blue = (0,0,255)
while True:
    gen+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: cancel=True
    if cancel: break

    field=nextgen(field, size)
    
    screen.fill((255,255,255))
    for x in range(size):
        for y in range(size):
            if field[x,y]==1:
                pygame.draw.rect(screen, blue, pygame.Rect(6*x, 6*y, 6, 6))
    pygame.display.flip()
    
pygame.quit()
print("*** Ende nach",gen,"Generationen")
