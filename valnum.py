import os
dir = './obbxml_val'
lis = os.listdir(dir)
for i in range(0,len(lis)):
	(shotname,ext) = os.path.splitext(lis[i])
	f=open('./val.txt','r+')
	f.read()
	f.write(shotname+'\n')
	f.close()
