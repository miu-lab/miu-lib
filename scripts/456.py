
import hou 
print('================================ miu-lib =====================================')
print('Location : ' + hou.getenv('MIU'))
hou.setPreference("liveUpdates", "1")
print('Live Update Parameter during Playback is [ON]')
hou.hscript('autosave on')
print('Auto Save is [ON]')
print("To desactivate these options, delete this file : " + hou.getenv('MIU') + "/script/456.py")
print('==============================================================================')