import os
set_dir='./trainval'
lis_set=os.listdir(set_dir)
for set_i in range(0,len(lis_set)):
	set_filename=os.path.join(set_dir,lis_set[set_i])
	f=open(set_filename,"w")
	f.write("")
	f.close()



