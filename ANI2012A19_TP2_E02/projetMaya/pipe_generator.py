import maya.cmds as mc
import random

#Creation du tuyau

flappy = cmds.polyPipe(sh=10, h=20, name="Corps#")
bird = cmds.polyPipe(sh=3, h=3, name="Bordure#" )

myBlinn = cmds.shadingNode('blinn', asShader=True)
cmds.setAttr( myBlinn + '.color', 0, 1, 0, type="double3")
cmds.select( flappy, bird, replace=True )
cmds.hyperShade(assign=myBlinn)

cmds.move(0,5,0, bird)
cmds.scale(1.2,0.9,1.2, bird)

#Unir les elements du pipe
union = cmds.polyUnite(flappy, bird, name="Uni#")

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

    
