import maya.cmds as mc

#Animation de Flappy bird. Ne pas utiliser avec Unity.
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

#Fusion
cmds.polyUnite( 'eye1', 'eye2', 'mouth', 'body', 'pupil1', 'pupil2', n='OISEAU' )

#Animation finale
if len('OISEAU') > 0:

  maya.cmds.setKeyframe('OISEAU', time=1, attribute='translateX', value=0.0)
  maya.cmds.setKeyframe('OISEAU', time=1, attribute='translateY', value=0.0)
  maya.cmds.setKeyframe('OISEAU', time=1, attribute='scaleY', value=0.691)
  maya.cmds.setKeyframe('OISEAU', time=1, attribute='scaleX', value=1.446)
  maya.cmds.setKeyframe('OISEAU', time=1, attribute='scaleZ', value=1.457)
  maya.cmds.setKeyframe('OISEAU', time=2, attribute='translateX', value=0.0)
  maya.cmds.setKeyframe('OISEAU', time=2, attribute='translateY', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=2, attribute='scaleY', value=1.2)
  maya.cmds.setKeyframe('OISEAU', time=2, attribute='scaleX', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=2, attribute='scaleZ', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=2, attribute='rotateZ', value=0.0)
  
  maya.cmds.setKeyframe('OISEAU', time=2, attribute='translateX', value=0.0)
  maya.cmds.setKeyframe('OISEAU', time=2, attribute='translateY', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=2, attribute='scaleY', value=1.2)
  maya.cmds.setKeyframe('OISEAU', time=2, attribute='scaleX', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=2, attribute='scaleZ', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=10, attribute='translateX', value=6.0)
  maya.cmds.setKeyframe('OISEAU', time=10, attribute='translateY', value=12.0)
  maya.cmds.setKeyframe('OISEAU', time=10, attribute='scaleY', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=10, attribute='scaleX', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=10, attribute='scaleZ', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=10, attribute='rotateZ', value=-180.0)
  
  maya.cmds.setKeyframe('OISEAU', time=10, attribute='translateX', value=6.0)
  maya.cmds.setKeyframe('OISEAU', time=10, attribute='translateY', value=12.0)
  maya.cmds.setKeyframe('OISEAU', time=10, attribute='scaleY', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=10, attribute='scaleX', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=10, attribute='scaleZ', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=18, attribute='translateX', value=11.0)
  maya.cmds.setKeyframe('OISEAU', time=18, attribute='translateY', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=18, attribute='scaleY', value=1.2)
  maya.cmds.setKeyframe('OISEAU', time=18, attribute='scaleX', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=18, attribute='scaleZ', value=1.0)
  
  maya.cmds.setKeyframe('OISEAU', time=18, attribute='translateX', value=12.0)
  maya.cmds.setKeyframe('OISEAU', time=18, attribute='translateY', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=18, attribute='scaleY', value=1.2)
  maya.cmds.setKeyframe('OISEAU', time=18, attribute='scaleX', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=18, attribute='scaleZ', value=1.0)
  maya.cmds.setKeyframe('OISEAU', time=20, attribute='translateX', value=12.0)
  maya.cmds.setKeyframe('OISEAU', time=20, attribute='translateY', value=0.0)
  maya.cmds.setKeyframe('OISEAU', time=20, attribute='scaleY', value=0.691)
  maya.cmds.setKeyframe('OISEAU', time=20, attribute='scaleX', value=1.446)
  maya.cmds.setKeyframe('OISEAU', time=20, attribute='scaleZ', value=1.457)
  maya.cmds.setKeyframe('OISEAU', time=20, attribute='rotateZ', value=-360.0)
