import numpy as np
def custom_cmap(m):
  m = np.array(m)
  new = np.zeros(shape=m.shape)
  new = new.tolist()

  for i in range(0,m.shape[0]):
    for j in range(0,m.shape[1]):
      if m[i][j]==1:#black
        new[i][j]=[0,0,0]
      elif m[i][j]==2:#green
        new[i][j]=[0,255,0]
      elif m[i][j]==3:#blue
        new[i][j]=[0,0,255]
      elif m[i][j]==4:#cyan
        new[i][j]=[0,255,255]
      elif m[i][j]==5:#magenta
        new[i][j]=[255,0,255]
      elif m[i][j]==6:#yellow
        new[i][j]=[255,255,0]
      elif m[i][j]==7:#red
        new[i][j]=[255,0,0]
  from numpy.core.memmap import uint8
  m1 = np.array(new,dtype=uint8)

  red = []
  for i in range(m.shape[0]):
    for j in range(m.shape[1]):
      red.append(m1[i][j][0])

  green = []
  for i in range(m.shape[0]):
    for j in range(m.shape[1]):
      green.append(m1[i][j][1])
  blue = []
  for i in range(m.shape[0]):
    for j in range(m.shape[1]):
      blue.append(m1[i][j][2])

  red = np.array(red,dtype=uint8)
  green = np.array(green,dtype=uint8)
  blue = np.array(blue,dtype=uint8)
  
  red = red.reshape(m.shape[0],m.shape[1])
  green = green.reshape(m.shape[0],m.shape[1])
  blue = blue.reshape(m.shape[0],m.shape[1])


  rgb = np.dstack((red,green,blue))

  return rgb
