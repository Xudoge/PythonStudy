

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

# create instance
pCubeTransform=pCube[0]
pCubeIns=cmd.instance(pCubeTransform,name=pCubeTransform+'_Instance')

# loop Create Instance
for i in range(0,50):
    pCubeIns=cmd.instance(pCubeTransform,name=pCubeTransform+'_Instance'+str(i))
    cmd.move(0,10*i,0,pCubeIns)
    cubeList.append(pCubeIns)
   

for i in cubeList:
    cmd.delete(i)
pCube = cmd.polyCube(w = 10, h = 10, d = 10, name = 'myCube')

# hide Object
cmd.hide(pCube)
cmd.showHidden(pCube)

# Group Object
instGroup =cmd.group(empty=True,name='myInstGroup')

for i in range(0,50):
    for i in range(0,50):
        pCubeIns=cmd.instance(pCubeTransform,name=pCubeTransform+'_Instance'+str(i))
        cmd.move(0,10*i,0,pCubeIns)
        cmd.parent(pCubeIns,instGroup)


# Create a window
def createWindow(pWindowTitle):
    windowId='MyWindowID'
    if cmd.window(windowId,exists=True):
        cmd.deleteUI(windowId)

    cmd.window(windowId, title = pWindowTitle, sizeable = False, resizeToFitChildren = True)

    # cmd.rowColumnLayout(numberOfColumns = 3, columnWidth = {(1, 75), (2, 60), (3, 60)})
    # cmd.text(label='my text one')

    cmd.showWindow()

createWindow('MyWindow')