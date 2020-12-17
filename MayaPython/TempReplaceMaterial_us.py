#!/usr/bin/python 
# -*- coding: utf-8 -*-

import maya.cmds as cmd
# from maya import OpenMaya

import shutil 
import os

# textfield temp var
tfs=[]
# currentMayaProjectPath
defualtMayaProjectPath=cmd.workspace(q=1,openWorkspace=True)


def createWindow(pWindowTitle):
    
    windowID = 'myWindowID'
    
    if cmd.window(windowID, exists = True):
        cmd.deleteUI(windowID)
        
    cmd.window(windowID, title = pWindowTitle, sizeable = True, resizeToFitChildren = True)
    osd= cmd.rowColumnLayout(numberOfColumns = 2,ro=[1,"both" ,30],co=[1,"both" ,30])
    cmd.text(label = 'Way 01: ',parent=osd)
    cmd.rowColumnLayout(numberOfColumns = 3, columnWidth = [(1, 200), (2, 200), (3, 200)],columnOffset=[[3,"left",10]],rowSpacing=[[1,10]],parent=osd)
    cmd.text(label = 'Game File Path(Include /Game)')
    tf1= cmd.textField()
    tfs.append(tf1)
    cmd.button(label = 'Select', command = 'FileD(0)',h=20)
    cmd.text(label = 'LevelFBXFilePath(Include .fbx)')
    tf2=cmd.textField()
    tfs.append(tf2)
    cmd.button(label = 'Select', command = 'FileD(1)',h=20)
    cmd.text(label = 'MayaProjectPath')
    tf3=cmd.textField(text=defualtMayaProjectPath)
    tfs.append(tf3)
    cmd.button(label = 'Select', command = 'FileD(2)',h=20)
    
    cmd.text(label="")
    cmd.button(label = 'Import and Replace', command = 'ImportFunction()',h=50)

    cmd.text(label = 'Way 02: ',parent=osd,h=20)
    rcl=cmd.rowColumnLayout(numberOfRows=1,  rowAlign=[[1,"center"]],parent=osd,h=100,ro=[1,"both" ,30])
    cmd.rowColumnLayout(numberOfColumns = 3, columnWidth = [(1, 200), (2, 200), (3, 200)],columnOffset=[[3,"left",10]],rowSpacing=[[1,10]],parent=rcl,h=200,columnAlign=[[1,"center"]])
    cmd.text(label = 'If you have already\n imported ,pls click here')
    cmd.button(label = 'Replace Current Scence', command = 'ReplaceMaterial()',h=50)

    cmd.showWindow()


# fileDialog to select Path
def FileD(index):

    myFm=0
    if index==0:
        myFm=3
    elif index==1:
        myFm=1
    elif index==2:
        myFm=3
    else:
        pass

    path=cmd.fileDialog2(fm=myFm)
    strPath=str(path[0])
    
    cmd.textField(tfs[index],e = True, text= strPath)


# way 01 : button click
def ImportFunction():

    GamePath=cmd.textField(tfs[0],q=1,text=True)

    LevelFBXPath=cmd.textField(tfs[1],q=1,text=True)

    MayaProjectPath=cmd.textField(tfs[2],q=1,text=True)

    try:
        cmd.workspace(MayaProjectPath,o=True)
    except:
        pass

    for i in os.listdir(MayaProjectPath):
        if i=='sourceimages':
            for i in os.listdir(MayaProjectPath):
                if  i=='Game':
                    shutil.rmtree(MayaProjectPath+'/sourceimages/Game')

    isSuccess=False
    try:
        shutil.copytree(GamePath,MayaProjectPath+'/sourceimages/Game')
        print("Game copy success")
    except:
        print("Game copy false")

    try:
        cmd.file(LevelFBXPath,i=True,type="FBX",ra=True,mnc=False,op="FBX",namespace="UE4Map")
        print("fbx import success")
        isSuccess=True
    except:
        print("fbx import false")

    if isSuccess==True:
        ReplaceMaterial()

# SelectObjs=cmd.ls(selection=True)

# cmd.sets(fe="M_TempSG")


def NullFunc():
    pass


def TryFunction(Func,elseFunc=[],n=-1):
    try:
        Func()
    except:
        n=n+1
        if len(elseFunc)>n:
            TryFunction(elseFunc[n],elseFunc,n)
        else:
            pass


def ListPrint(List):
    for i in List:
        print(i+"\n")


# way 02: button click
def ReplaceMaterial():
    
    mats=cmd.ls(mat=True)

    print("all materials :")
    print(mats)
    print("\n\n")
    print("------------------------------- \n")

    # selectObjects=cmd.ls(orderedSelection=True)

    count=0
    for obj in mats:

        cmd.select(cl=True)
        count=count+1
        #print(str(obj))
        print("------------------ "+str(count) +" ---- " +str(obj) +" ----------------------\n")

        if cmd.objectType(obj)!="phong":
            continue

        NameList= cmd.listConnections(obj,c=True)
        # ListPrint(NameList)
        listlen=len(NameList)

        # print("#####################################")
        # ListPrint(NameList)
        # print("#####################################")

        num=0

        # collect att information
        baseColor=""
        Spec=""
        Normal=""
        Metal=""
        Rough=""

        OldSG=""
        while num<listlen:
            
            TypeName=NameList[num]
            FN=NameList[num+1]
            
            if str(TypeName).endswith("ambientColor"):
            #    Metal=cmd.getAttr(str(FN)+".fileTextureName")
                Metal=FN      
            elif str(TypeName).endswith("specularColor"):
            #    Spec=cmd.getAttr(str(FN)+".fileTextureName")
                Spec=FN
            elif str(TypeName).endswith("normalCamera"):
                Normal=FN

                # FNList= cmd.listConnections(FN,c=True)
                # AttrName=str(FN)
                # for i in range(0,len(FNList)):
                #     if str(FNList[i]).endswith("bumpValue"):
                #         TypeName=FNList[i+1]
                #         break
                # Normal=cmd.getAttr(AttrName+".fileTextureName") 

            elif str(TypeName).endswith("reflectedColor"):
            #    Rough=cmd.getAttr(str(FN)+".fileTextureName")  
                Rough=FN 
            elif str(TypeName).endswith("color"):
            #   baseColor=cmd.getAttr(str(FN)+".fileTextureName")
                baseColor=FN

            elif str(TypeName).endswith("outColor"):
                OldSG=FN

            num=num+2
        
        print("baseColor: "+str(baseColor))
        print("Spec: "+str(Spec))
        print("Normal: "+str(Normal))
        print("Metal: "+str(Metal))
        print("Rough: "+str(Rough))

        # create new shading node
        AnName=str(obj)+"_arnold"
        SGName=str(obj)+"SG"
        newNode=cmd.shadingNode("aiStandardSurface",asShader=True,name=AnName)
        # selectionList=[]
        cmd.sets(renderable=True,nss=True,em=True,name= SGName)
        cmd.connectAttr(AnName+".outColor", SGName+".surfaceShader",f=True)

        if  baseColor!="":
            cmd.connectAttr(baseColor+".outColor",AnName+".baseColor",f=True)

        if  Spec!="":
            cmd.connectAttr(Spec+".outColor",AnName+".specularColor",f=True)
        

        def MetalCon():
            cmd.connectAttr(Metal+".outColor.outColorR",AnName+".diffuseRoughness",f=True)

        if  Metal!="":
            TryFunction(MetalCon)

        def RoughCon():
            cmd.connectAttr(Rough+".outColor.outColorR",AnName+".specularRoughness",f=True)

        if  Rough!="":
            TryFunction(RoughCon)

        def NormalNTN():
            cmd.connectAttr(Normal+".outNormal",AnName+".normalCamera",f=True)
        def NormalCTN():
            cmd.connectAttr(Normal+".outColor",AnName+".normalCamera",f=True)

        if Normal!="":
            TryFunction(NormalNTN,[NormalCTN])

        cmd.select(cl=True)
        cmd.hyperShade(o=obj)
        UsedObject=cmd.ls(selection=True)
        print("usedObject: ")
        print(UsedObject)

        if len(UsedObject)>0:
            cmd.sets(fe=SGName)
       
        cmd.delete(obj)
        cmd.delete(OldSG)
        print(obj+" move success ")
    
#-------------------------------------main----------------------------------------

createWindow('MyWindow')

# ReplaceMaterial()

# path=r"C:\Users\122\Desktop\Maya\1112"
# path2=r"C:\Users\122\Desktop\Maya\NewProject2"

# fileName="mmm"

# try:
#     a=cmd.workspace(path,o=True)
# except:
#     pass

# cmd.workspace(create=path)
# try:
#     cmd.workspace(path,newWorkspace=True)
# except:
#     pass

# dl=cmd.workspace( q=1,fileRule=True)
# v=[]
# dllen=len(dl)/2
# for i in range(0,dllen):
#     v.append([ str(dl[i*2]), str(dl[i*2+1])])
#     os.
#     cmd.workspace(path,fr=[ dl[i*2], dl[i*2+1]])

# # cmd.workspace(create=path)
# # cmd.workspace(path,objectType=dl)
# # cmd.workspace(path,newWorkspace=True)

# print(dl)
# print("eee")
