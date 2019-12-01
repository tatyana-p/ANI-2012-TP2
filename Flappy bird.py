import maya.cmds as mc
import random
cmds.file(force=1, newFile=1)
cmds.modelEditor(cmds.getPanel(withFocus=True), edit=True, displayLights='all')
cmds.modelEditor(cmds.getPanel(withFocus=True), edit=True, shadows=True)

#Creation de l'oiseau
#Parties du corps
cmds.polySphere(n='body',sx=2, sy=20, r=1)

cmds.polySphere(n='eye1', sx=2, sy=20, r=0.40)
cmds.move(0.5,0.5,0.5,'eye1')

cmds.polySphere(n='pupil1', sx=2, sy=20, r=0.20)
cmds.move(0.65,0.65,-0.65,'pupil1')

cmds.polySphere(n='pupil2', sx=2, sy=20, r=0.20)
cmds.move(0.65,0.65,0.65,'pupil2')

cmds.polySphere(n='eye2', sx=2, sy=20, r=0.40)
cmds.move(0.5,0.5,-0.5,'eye2')
cmds.polyTorus(n='mouth', sx=0.5, sy=0.5, r=0.4, sr=0.4 )
cmds.move(0.5,0,0,'mouth')
#Couleurs
myBlinn = cmds.shadingNode('blinn', asShader=True)
cmds.setAttr( myBlinn + '.color', 0, 0, 0, type="double3")
cmds.select( 'pupil1', 'pupil2', replace=True )
cmds.hyperShade(assign=myBlinn)
myBlinn = cmds.shadingNode('blinn', asShader=True)
cmds.setAttr( myBlinn + '.color', 1, 0, 0, type="double3")
cmds.select( 'body', replace=True )
cmds.hyperShade(assign=myBlinn)
myBlinn = cmds.shadingNode('blinn', asShader=True)
cmds.setAttr( myBlinn + '.color', 1, 0.5, 0, type="double3")
cmds.select( 'mouth', replace=True )
cmds.hyperShade(assign=myBlinn)
#Groupage
cmds.group( 'eye1', 'eye2', 'mouth', 'body', 'pupil1', 'pupil2', n='OISEAU' )
cmds.move(0,11,0,'OISEAU')

#Creation du tuyau
cmds.polyPipe( n='tube', sh=10, h=20 )
#Creation de la bordure
cmds.polyPipe( n='tubebordure', sh=3, h=3 )
cmds.move(0,5,0)
cmds.scale(1.2,0.9,1.2)
#Grouper les elements du pipe
cmds.group( 'tube','tubebordure', n='PIPE' )
#Position aleatoire
x = random.uniform(-6.0, 6.0)
y = random.uniform(-4.0, 4.0)
z = random.uniform(-6.0, 6.0)
for i in range(5):
    mc.move(x, y, z, 'PIPE')
        
#Creation du tuyau 2
cmds.polyPipe( n='tube2', sh=10, h=20 )
#Creation de la bordure 2
cmds.polyPipe( n='tubebordure2', sh=3, h=3 )
cmds.move(0,5,0)
cmds.scale(1.2,0.9,1.2)
#Grouper les elements du pipe 2
cmds.group( 'tube2','tubebordure2', n='PIPE2' )
#Position aleatoire
x = random.uniform(-6.0, 6.0)
y = random.uniform(-1.0, 4.0)
z = random.uniform(-6.0, 6.0)
for i in range(5):
    mc.move(x, y, z, 'PIPE2')
    
#Creation du tuyau 3
cmds.polyPipe( n='tube3', sh=10, h=20 )
#Creation de la bordure 3
cmds.polyPipe( n='tubebordure3', sh=3, h=3 )
cmds.move(0,5,0)
cmds.scale(1.2,0.9,1.2)
#Grouper les elements du pipe 3
cmds.group( 'tube3','tubebordure3', n='PIPE3' )
#Position aleatoire
x = random.uniform(-6.0, 6.0)
y = random.uniform(-0.0, 4.0)
z = random.uniform(-6.0, 6.0)
for i in range(5):
    mc.move(x, y, z, 'PIPE3')
    
#Application du shader et couleur verte
myBlinn = cmds.shadingNode('blinn', asShader=True)
cmds.setAttr( myBlinn + '.color', 0, 1, 0, type="double3")
cmds.select( 'PIPE', 'PIPE2', 'PIPE3', replace=True )
cmds.hyperShade(assign=myBlinn)

#Creation du sol et mur, assigner un matériel et couleur
cmds.polyPlane( n='plafond', w=20, h=20)
cmds.move(0,20,0)
cmds.polyPlane( n='mur', w=20, h=20)
cmds.move(0,10,-10)
cmds.rotate(90,0,0)
cmds.polyPlane( n='sol', w=20, h=20)
cmds.polyPlane( n='bordure', w=20, h=10)
cmds.rotate(90,0,0)
cmds.move(0,-5,10)
myBlinn = cmds.shadingNode('blinn', asShader=True)
cmds.setAttr( myBlinn + '.color', 0, 0.4, 1, type="double3") 
cmds.select( 'mur', 'plafond', 'bordure', 'sol', replace=True )
cmds.hyperShade(assign=myBlinn)

#Creation de spot orange et ajustements des parametres
cmds.spotLight(n='mySpotLight', coneAngle=120, intensity=2.5)
cmds.move(-9,16,0)
cmds.rotate(-80,0,34)
cmds.spotLight(n='mySpotLight', edit=True, penumbra=10) 
cmds.spotLight(n='mySpotLight', edit=True, dropOff=8.5)
cmds.spotLight(n='mySpotLight', edit=True, rgb=[0.92,0.67,0.34])

#Creation de lumiere ambiante et ajustements des parametres
cmds.ambientLight(n='ambiantLight', intensity=0.2)
cmds.move(0,19,0)
cmds.rotate(-90,45,0)
cmds.spotLight(n='ambientLight', edit=True, penumbra=1) 
cmds.spotLight(n='ambientLight', edit=True, dropOff=10)
cmds.spotLight(n='ambientLight', edit=True, rgb=[0.92,0.67,0.34])

#Creation de spot orange 2 et ajustements des parametres
cmds.spotLight(n='mySpotLight2', coneAngle=120, intensity=2.5)
cmds.move(11,16,0)
cmds.rotate(80,0,90)
cmds.spotLight(n='mySpotLight2', edit=True, penumbra=10) 
cmds.spotLight(n='mySpotLight2', edit=True, dropOff=8.5)
cmds.spotLight(n='mySpotLight2', edit=True, rgb=[0.92,0.67,0.34])

# sélectionner tous les éléments de la scène

maya.cmds.select(all=True)
sequence = maya.cmds.ls(selection=True)

if len(sequence) == 0:
  print "<la scène est vide>\n"
else:
  enumerate(sequence)