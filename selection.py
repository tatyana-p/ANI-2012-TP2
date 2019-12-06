#Commande pour tout sélectionner les éléments de la scène

import maya.cmds as mc

maya.cmds.select(all=True)
sequence = maya.cmds.ls(selection=True)

if len(sequence) == 0:
  print "<la scène est vide>\n"
else:
  enumerate(sequence)