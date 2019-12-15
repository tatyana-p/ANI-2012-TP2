maya.cmds.select('OISEAU')
sequence = maya.cmds.ls(selection=True)

if len(sequence) == 0:
  print "<la scène est vide>\n"
else:
  enumerate(sequence)
  
def attribute_read(nodeName, attributeName):
  """fonction de lecture d'une valeur d'un attribut assigné à un noeud"""

  # valider si le noeud possède l'attribut
  if maya.cmds.objExists("%s.%s" % (nodeName, attributeName)):
    # extraire et retourner la valeur de l'attribut
    return maya.cmds.getAttr("%s.%s" % (nodeName, attributeName))
  else:
    print u"<fonction 'attribute_read' annulée, car l'attribut '%s' n'existe pas sur le noeud '%s'>" % (attributeName, nodeName)
    return None
    
def attribute_write(nodeName, attributeName, attributeValue):
  """fonction d'écriture d'une valeur dans un attribut assigné à un noeud"""

  # valider si le noeud possède l'attribut
  if maya.cmds.objExists("%s.%s" % (nodeName, attributeName)):
    # assigner la nouvelle valeur de l'attribut
    maya.cmds.setAttr("%s.%s" % (nodeName, attributeName), attributeValue)
  else:
    print u"<fonction 'attribute_write' annulée, car l'attribut '%s' n'existe pas sur le noeud '%s'>" % (attributeName, nodeName)

transformNodeCube = sequence[0]

currentTranslateX = attribute_read(transformNodeCube, 'translateX')
currentTranslateY = attribute_read(transformNodeCube, 'translateY')
currentTranslateZ = attribute_read(transformNodeCube, 'translateZ')

print "<avant écriture la valeur de translateX est %s>" % str(currentTranslateZ)
print "<avant écriture la valeur de translateY est %s>" % str(currentTranslateZ)
print "<avant écriture la valeur de translateZ est %s>" % str(currentTranslateZ)

attribute_write(transformNodeCube, 'translateX', 10.0)
attribute_write(transformNodeCube, 'translateY', 10.0)
attribute_write(transformNodeCube, 'translateZ', 10.0)


print "<après écriture la valeur de translateX est %s>" % str(attribute_read(transformNodeCube, 'translateX'))
print "<après écriture la valeur de translateY est %s>" % str(attribute_read(transformNodeCube, 'translateY'))
print "<après écriture la valeur de translateZ est %s>" % str(attribute_read(transformNodeCube, 'translateZ'))