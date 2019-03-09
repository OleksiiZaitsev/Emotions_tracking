import time


def mapping():
	with open(fullpath, 'r') as f:
		weights,Z = eval(f.read())
		cmds.setAttr('blendShape3.x2_r_JDxLS', weights[0]*2)
		
		
		cmds.setAttr('blendShape3.c_FN', weights[1])
		cmds.setAttr('blendShape3.psd_surprised', weights[1]/2)
		
		cmds.setAttr('blendShape3.c_JD', weights[2])
		cmds.setAttr('blendShape3.c_CRUL', weights[2])
		Z = -int(Z)
		#cmds.xform('Head', rotation = (0,0, Z))
		
	#time.sleep(1/30)	
	cmds.refresh()
		

LABELS_LIST = ['1 - idle', '2 - jaw_open','3 - smile',]


path = r'D:\GitHub\udemy'
if not os.path.exists(path):
    path = r'E:\GitHub\udemy'

fullpath = os.path.join(path, "weights.txt")

weights = [] 
Z = []


cmds.scriptJob(killAll=True) 
cmds.scriptJob(event=["idle", mapping])


 