# expandFromFirst.py

import maya.cmds as cmds
#cmds.select(instanceObj) 

maya.cmds.select(all=True)
#sequence = maya.cmds.ls(selection=True)
#selectionList = cmds.ls( orderedSelection=True, type='transform' )
selectionList = cmds.ls(selection=True)

if len( selectionList ) >= 2:
    
#    targetName = transformPipe
    
    cmds.select('OISEAU', deselect=True)
    
    locatorGroupName = cmds.group( empty=True, name='expansion_locator_grp#' )
    
    maxExpansion = 100
    
    newAttributeName = 'expansion'
    
    if not cmds.objExists( '%s.%s' % ( transformPipe, newAttributeName ) ):
        
        cmds.select( transformPipe )
        
        cmds.addAttr( longName=newAttributeName, shortName='exp',
                      attributeType='double', min=0, max=maxExpansion,
                      defaultValue=maxExpansion, keyable=True )
    
    for objectName in selectionList:
        
        coords = cmds.getAttr( '%s.translate' % ( objectName ) )[0]
        
        OISEAU = cmds.spaceLocator( position=coords, name='%s_loc#' % ( objectName ) )[0]
        
        cmds.xform( OISEAU, centerPivots=True )
        
        cmds.parent( OISEAU, locatorGroupName )
        
        pointConstraintName = cmds.pointConstraint( [ transformPipe, OISEAU ], objectName, name='%s_pointConstraint#' % ( objectName ) )[0]
        
        cmds.expression( alwaysEvaluate=True, 
                         name='%s_attractWeight' % ( objectName ),
                         object=pointConstraintName,
                         string='%sW0=%s-%s.%s' % ( transformPipe, maxExpansion, transformPipe, newAttributeName ) )
        
        cmds.connectAttr( '%s.%s' % ( transformPipe, newAttributeName ), 
                          '%s.%sW1' % ( pointConstraintName, OISEAU ) )
        
        
    cmds.xform( locatorGroupName, centerPivots=True )
    
else:
    
    print 'veuillez selectionner deux objets ou plus'

def attribute_has(nodeName, attributeName):
  """fonction qui valide l'existence d'un attribut sur un noeud"""

  # valider si le noeud possède l'attribut
  if maya.cmds.objExists("%s.%s" % (nodeName, attributeName)):
    return True
  else:
    return False  