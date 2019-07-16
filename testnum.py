import os
dir = './obbxml'
lis = os.listdir(dir)
for i in range(0,len(lis)):
	(shotname,ext) = os.path.splitext(lis[i])
	f=open('./test.txt','r+')
	f.read()
	f.write(shotname+'\n')
	f.close()
