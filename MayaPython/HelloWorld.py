#/usr/bin/env python
# -*- coding: UTF-8 -*-
import maya.cmds as cmd


def checkSelect():
    list_select=[]
    if cmd.ls(sl=True)!=[]:
        list_select= cmd.ls(sl=True)
        return list_select
    else:
        return []

#坐标回归中心
def centerPivot():
    for i in checkSelect():
        cmd.xform(i, centerPivots=True)

#坐标回归世界中心
def pivotMoveToWorldPosition000():
    for i in checkSelect():
        Name=id
        cmd.move(0,0,0,Name +'.rotatePivot',Name +'.scalePivot',rpr=True)
        cmd.makeIdentity(Name,a=True)

#强制把一切归零
def meshMoveToWorldPosition000AndClean():
    centerPivot()
    for i in  checkSelect():
        cmd.move(0,0,0,i,rpr=True)
        cmd.makeIdentity(i,a=True)

#临时测试函数
def rotatorPivot():
    for i in checkSelect():
        Name=i
        cmd.xform(i, rotateTranslation=[90,0,90])


def mainGui():
    windowName='CC_Tool'
    windowTitle='CC_Tool1.0'

    try:
        cmd.deleteUI(windowName)
    except:
        pass

    cmd.window(windowName,title=windowTitle)
    cmd.columnLayout(adj=True)

    explain_ZeroPivot='轴枢回归中心'
    explain_Clean='轴枢回归中心，模型回归到网格中心'

    cmd.button(l='ZeroPivot',ann=explain_ZeroPivot,h=60,w=20,c='centerPivot()')
    cmd.button(l='Clean',ann=explain_Clean,h=60,w=20,c='meshMoveToWorldPosition000AndClean()')

    cmd.showWindow(windowName)

mainGui()

print("Hello world")