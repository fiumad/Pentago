import sys

from pygame import draw
from rotate import clock, counter
import pygame
from pygame.locals import *
 
topLeft = [(146, 64),(202, 64),(260, 65),(144, 126),(203, 127),(260, 127),(145, 188),(202, 188),(261, 189)]
topRight = [(349, 66),(408, 64),(464, 65),(350, 127),(407, 127),(463, 127),(350, 189),(407, 189),(464, 189)]
botRight = [(349, 258),(407, 259),(463, 260),(350, 323),(407, 323),(465, 324),(349, 382),(406, 384),(464, 384)]
botLeft = [(146, 260),(202, 261),(259, 260),(146, 322),(203, 321),(260, 321),(146, 383),(202, 384),(261, 383)]
#data = [["0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0"]]
data = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
spots = [[(146, 64),(202, 64),(260, 65),(144, 126),(203, 127),(260, 127),(145, 188),(202, 188),(261, 189)],[(349, 66),(408, 64),(464, 65),(350, 127),(407, 127),(463, 127),(350, 189),(407, 189),(464, 189)],
[(349, 258),(407, 259),(463, 260),(350, 323),(407, 323),(465, 324),(349, 382),(406, 384),(464, 384)],
[(146, 260),(202, 261),(259, 260),(146, 322),(203, 321),(260, 321),(146, 383),(202, 384),(261, 383)]]


def findDist(p1, p2):
  x1 = p1[0]
  x2 = p2[0]
  y1 = p1[1]
  y2 = p2[1]

  dist = ((abs(x2-x1))**2 + abs(y2-y1)**2)**.5
  return dist


def findSpot(coords):
  x = coords[0]
  y = coords[1]

  if x < 320:
    if y < 240:
      check = topLeft
    elif y >= 240:
      check = botLeft
  else:
    if y < 240:
      check = topRight
    else:
      check = botRight
  minXDist = 20000000
  minYDist = 20000000

  for i in range(len(check)):
    xDist = abs(x - check[i][0])
    yDist = abs(y - check[i][1])
    if xDist <= minXDist and yDist <= minYDist:
      minXDist = xDist 
      minYDist = yDist
      spot = check[i]
  return spot  

def findSpotOther(coords):
  x = coords[0]
  y = coords[1]

  if x < 320:
    if y < 240:
      check = topLeft
      quad = 0
    elif y >= 240:
      check = botLeft
      quad = 3
  else:
    if y < 240:
      check = topRight
      quad = 1
    else:
      check = botRight
      quad = 2
  minXDist = 20000000
  minYDist = 20000000
  minDist = 20000000
  for i in range(len(check)):
    if findDist(check[i],coords) < minDist:
      minDist = findDist(check[i],coords)
      number = i
  return (quad,number)  



def drawPieces(data):
  for i in range(len(data)):
    for j in range(len(data[i])):
      if data [i][j] != 0:
        #print(data[i][j])
        #print(spots[i][j])
        None
      if data[i][j] == 1:
        pygame.Surface.blit(screen, white, spots[i][j])
        #print("drawing white")
      elif data[i][j] == 2:
        pygame.Surface.blit(screen, black, spots[i][j])
        #print("drawing black")
  pygame.display.update()        








pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
blk = (0,0,0)
red = (191, 8, 26)
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
board = pygame.image.load('board.jpg') 
legend = pygame.image.load('legend.png')
white = pygame.image.load('white.png')
white = pygame.transform.scale(white, (30,30))

black = pygame.image.load('black.png')
black = pygame.transform.scale(black, (30,30))
current_piece = white
turn = "White"

#legend = pygame.transform.scale(legend,(30,30))
font = pygame.font.SysFont(None, 22)

# Game loop.
while True:
  turnText = font.render(turn, True, blk, red)
  pos_text = font.render(str(pygame.mouse.get_pos()), True, blk, red)
  pygame.mouse.set_visible(False)
  screen.fill((43, 0, 0))
  screen.blit(board,(0,0))
  keys = pygame.key.get_pressed()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == MOUSEBUTTONDOWN:
      print(pygame.mouse.get_pos())
      if current_piece == white:
        current_piece = black
        turn = "Black"
        #print("black")
      else:
        current_piece = white
        turn = "White"
        #print("white")
      spot = findSpot(pygame.mouse.get_pos())
      change = findSpotOther(pygame.mouse.get_pos())
      if current_piece == white:
        data[change[0]][change[1]] = 2
      else:
        data[change[0]][change[1]] = 1
      print(data)
      pygame.display.update()




              
  # Update.
  
  # Draw.
  

  pygame.Surface.blit(screen,pos_text,(300,450))
  pygame.Surface.blit(screen,turnText,(10,10))
  #pygame.Surface.blit(screen, legend,(30,300))
  
  drawPieces(data)
  pygame.Surface.blit(screen, current_piece, pygame.mouse.get_pos())
  pygame.display.flip()
  fpsClock.tick(fps)