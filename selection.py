#Commande pour tout s�lectionner les �l�ments de la sc�ne

import maya.cmds as mc

maya.cmds.select(all=True)
sequence = maya.cmds.ls(selection=True)

if len(sequence) == 0:
  print "<la sc�ne est vide>\n"
else:
  enumerate(sequence)