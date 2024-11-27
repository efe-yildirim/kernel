import numpy as np
def kernel(terrain,instruction,bot):

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
  def jump(bot):
    if bot[3]==0 and y_position+1<y and terrain[x_position,y_position+1,1]-terrain[x_position,y_position,1]==1:
      y_position+=1
    if bot[3]==1 and x_position+1<x and terrain[x_position+1,y_position,1]-terrain[x_position,y_position,1]==1:
      x_position+=1
    if bot[3]==2 and y_position-1>-1 and terrain[x_position,y_position-1,1]-terrain[x_position,y_position,1]==1:
      y_position-=1
    if bot[3]==3 and x_position-1>-1 and terrain[x_position-1,y_position,1]-terrain[x_position,y_position,1]==1:
      x_position-=1
    if bot[3]==0 and y_position+1<y and terrain[x_position,y_position+1,1]-terrain[x_position,y_position,1]<0:
      y_position=[x_position,y_position+1,1]
    if bot[3]==1 and x_position+1<x and terrain[x_position+1,y_position,1]-terrain[x_position,y_position,1]<0:
      x_position=terrain[x_position+1,y_position,1]
    if bot[3] == 2 and y_position - 1 > -1 and terrain[x_position, y_position - 1, 1] - terrain[x_position, y_position, 1]<0:
      y_position = terrain[x_position, y_position - 1, 1]
    if bot[3] == 3 and x_position - 1 > -1 and terrain[x_position - 1, y_position, 1] - terrain[x_position, y_position, 1]< 0:
      x_position= terrain[x_position - 1, y_position, 1]

  if instruction=='^':
    move_forward(bot)
  if instruction==">":
    turn_right(bot)
  if instruction=="<":
    turn_left(bot)
  if instruction=="@":
    switch_light(terrain)
  if instruction=="*":
    jump(bot)


terrain=np.array([
    [[0,0], [0,0], [0,0],[0,0], [0,0], [0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0], [0,0], [0,0],[0,0], [0,0], [0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0], [0,0], [0,0],[0,0], [0,0], [0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0], [0,0], [0,0],[0,0], [0,0], [0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0], [0,0], [0,0],[0,0], [0,0], [0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0], [0,0], [0,0],[0,0], [0,0], [0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0], [0,0], [0,0],[0,0], [0,0], [0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0], [0,0], [0,0],[0,0], [0,0], [0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0], [0,0], [0,0],[0,0], [0,0], [0,0],[0,0],[0,0],[0,0],[0,0]],
    [[0,0], [0,0], [0,0],[0,0], [0,0], [0,0],[0,0],[0,0],[0,0],[0,0]]

])
bot=[0,9,0,1]
instructions=["^","^",">","^","<","@"]
#print(kernel(terrain,instructions,bot))
#while True:
  #clear_output(wait=True)
  #a=input()

  #print(kernel(terrain,a,bot))

for instruction in instructions:
    kernel(terrain,instruction,bot)
map=terrain[:,:,0]
print(map)