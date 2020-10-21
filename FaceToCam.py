import maya.cmds as cmds
import traceback
from functools import partial

def orient(objects ,cam_name='camera_test'):
   """
   Create  a aim constraint on multiple objects to a camera, and then delete the resulting constraint
   :param objects: an array of objects
   :param cam_name: the name of the camera to use for the constraint
   :return:
   """
   if cmds.objExists(cam_name):
       for mesh in objects:
           constraint_node = cmds.aimConstraint(cam_name, mesh, offset=[0, 0, 0], weight=1, aimVector=[0, 0, -1], upVector=[0, 1, 0],
                              worldUpType="vector", worldUpVector=[0, 1, 0], skip = ["x", "z"], o = [0, 180, 0])
           cmds.delete(constraint_node)
   else:
       cmds.error('The specified camera does not exist inside your scene: '+str(cam_name))

def cam_constraint_ui():
   """
   Launch Camera constraint Ui
   :return:
   """
   all_cameras = cmds.listCameras()

   ui_name = 'CamConstraintUI'

   if cmds.window(ui_name, exists=True):
       cmds.deleteUI(ui_name, wnd=True)

   my_window = cmds.window(ui_name,
                           title='Face Sel to Cam',
                           resizeToFitChildren=True,
                           sizeable=True,
                           w=90,h=250,
                           backgroundColor=(0.355, 0.65, 0.85),
                           )

   # -- init column layout
   cmds.columnLayout(adjustableColumn=True)

   cmds.text(label='Click on the camera button to make the operation:')

   #-- create all cams parameters
   for cam in all_cameras:
       cmds.button(label=str(cam), c='orient(cmds.ls(sl=1), cam_name = "'+str(cam)+'")')
       # cmds.button(label=str(cam), c=partial(orient, cmds.ls(sl=1), cam))

   ##cmds.button(label='Close', c='cmds.deleteUI(my_window, wnd=True)')

   # -- close column layout
   cmds.setParent('..')

   cmds.showWindow(my_window)


if __name__ == '__main__':
   try:
       cam_constraint_ui()
   except:
       print(traceback.format_exc())
       cmds.error('Something bad happend! Please read your script editor')

"""
# -- SNIPPET TO LAUNCH CAM CONSTRAINT UI -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -
import cam_constraint
reload(cam_constraint)

cam_constraint.cam_constraint_ui()
"""