import maya.cmds as mc
import random

#Creation du tuyau
#Creation de la bordure
#Grouper les elements du pipe
dragon = cmds.polyPipe(sh=10, h=20, name="Cube#")
reptile = cmds.polyPipe(sh=3, h=3, name="Bordure#" )

myBlinn = cmds.shadingNode('blinn', asShader=True)
cmds.setAttr( myBlinn + '.color', 0, 1, 0, type="double3")
cmds.select( dragon, reptile, replace=True )
cmds.hyperShade(assign=myBlinn)

cmds.move(0,5,0, reptile)
cmds.scale(1.2,0.9,1.2, reptile)

union = cmds.polyUnite(dragon, reptile, name="Uni#")

transformPipe = union[0]
group1 = cmds.group(empty=True, name=transformPipe + '_group#')

#Position aleatoire
for i in range(5):
    
    x = random.uniform(-6.0, 6.0)
    y = random.uniform(-0.0, 4.0)
    z = random.uniform(-6.0, 6.0)
    
    instanceObj = cmds.instance(transformPipe, name = transformPipe + '_instance#')
   
    cmds.move(x, y, z, instanceObj)
   
    cmds.parent(instanceObj, group1)

    