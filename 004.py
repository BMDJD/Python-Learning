import pygame as pyg
from pygame.locals import *
from time import sleep
from sys import exit

pyg.init()

scr = pyg.display.set_mode((1366,768))

while True:
  for xyz in pyg.event.get():
    if xyz.type == QUIT:
      exit()
  '''    
  这里可以写一些其他的代码 
  '''
  pyg.display.update()
