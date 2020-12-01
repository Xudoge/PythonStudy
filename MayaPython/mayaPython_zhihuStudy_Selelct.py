
import maya.cmds as cmd

def Select():
    selectObject =cmd.ls(selection=True,type='mesh')
    for obj in selectObject:
        objType=cmd.objectType(obj)
        print(objType)

Select()