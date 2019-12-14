import maya.cmds as mc
import random

#Couleur aleatoire

color = cmds.shadingNode( 'blinn', asShader=True)

for i in range(6):
    
    r = random.uniform(0.0, 1.0)
    v = random.uniform(0.0, 1.0)
    b = random.uniform(0.0, 1.0)
   
    instanceObj = cmds.instance(transformPipe, name = transformPipe + '_instance#')

    cmds.setAttr (color + '.color', r,v,b, type = "double3")   
    cmds.select( flappy, bird, replace=True )
    cmds.hyperShade(assign=color)