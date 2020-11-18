

import maya.cmds as cmd
import random

# Delete a poly
cubeList = cmd.ls('myCube')+cmd.ls('mySphere')


if len(cubeList) > 0:
    cmd.delete(cubeList)



# Create a poly
pCube = cmd.polyCube(w = 10, h = 10, d = 10, name = 'myCube')
# pSphere =cmd.polySphere( axis=[3,0,0],radius=200,name='mySphere' )


# move ,scale ,rotate

cmd.move(0,100,0,pCube)
cmd.scale(10,20,10,pCube)
cmd.rotate(random.uniform(-100.0,100.0),0,0,pCube)