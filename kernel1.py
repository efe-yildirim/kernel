from IPython.display import clear_output
import numpy as np
def kernel(terrain,instructions,bot):

  map=terrain[:,:,0]
  x,y=map.shape
  y_position=bot[0]
  x_position=bot[1]
  def direction_setter(bot,a):
    if a==1:
      bot[3]=(bot[3]+1) % 4
    if a==-1:
      bot[3]=(bot[3]-1) % 4
  def move_forward(bot):
    if bot[3]==2:
      if bot[1]+1<y:
        bot[1]+=1
    if bot[3]==1:
      if bot[0]+1<x:
        bot[0]+=1
    if bot[3]==0:
      if bot[1]-1>=0:
        bot[1]-=1
    if bot[3]==3:
      if bot[0]-1>=0:
        bot[0]-=1
  def turn_left(bot):
      a=-1
      direction_setter(bot,a)
  def turn_right(bot):
      a=1
      direction_setter(bot,a)
  def switch_light(terrain):
      terrain[x_position,y_position,0]=3
  def jump(bot): #It can only jump up for now.
    if bot[3]==0 and y_position+1<y and terrain[x_position,y_position+1,1]>terrain[x_position,y_position,1]:
      y_position+=1
    if bot[3]==1 and x_position+1<x and terrain[x_position+1,y_position,1]>terrain[x_position,y_position,1]:
      x_position+=1
    if bot[3]==2 and y_position-1>-1 and terrain[x_position,y_position-1,1]>terrain[x_position,y_position,1]:
      y_position-=1
    if bot[3]==3 and x_position-1>-1 and terrain[x_position-1,y_position,1]>terrain[x_position,y_position,1]:
      x_position-=1


  for i in instructions:
    if i=="^":
      move_forward(bot)
    if i==">":
      turn_right(bot)
    if i=="<":
      turn_left(bot)
    if i=="@":
      switch_light(terrain)
    if i=="*":
      jump(bot)
    map=terrain[:,:,0]
  return map
