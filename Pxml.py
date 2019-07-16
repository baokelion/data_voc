import os
import re
import xml.etree.ElementTree as ET
xml_dir = './obbxml'
lis = os.listdir(xml_dir)
for i in range(0,len(lis)):
	xml_path = os.path.join(xml_dir,lis[i])
	tree = ET.parse(xml_path)
	root = tree.getroot()
	size = root.find('size')
	filename = root.find('filename').text
	width = int(size.find('width').text)
	height = int(size.find('height').text)
	labels = []
	labels_ignore = []
	for obj in root.findall('object'):
		label_flag=False
		name = obj.find('label').text
		#print('label')
		print(name)
		difficult = int(obj.find('difficult').text)
		if difficult == 1:
			difficult = -1
		else:
			difficult = 1
		set_dir='./set'
		lis_set=os.listdir(set_dir)
		for set_i in range(0,len(lis_set)):
			if label_flag == False:
				(set_shotname,set_extension) = os.path.splitext(lis_set[set_i])
				set_filename=lis_set[set_i]
				set_shotname=set_shotname[:-6] #根据train，val，test的不同位数修改数字
				print('set_filename set_shotname')
				print(set_filename)
				print(set_shotname)
				if name == set_shotname:
					label_flag = True
					(shotname,ext) = os.path.splitext(filename)
					set_filename=os.path.join(set_dir,set_filename)
					f=open(set_filename,"r+")
					count = 0
					for s in f.readlines():
						li = re.findall(shotname,s)
						if len(li) > 0:
							count = count + len(li)
					if count == 0:
						f.read()
						f.write(shotname+" "+str(difficult)+"\n")
					f.close()
					
			
		if label_flag == False:
			print("XXXXXXXXXXXXXXXXXXXError:"+name+"cannot find any txt")
			break


		
		# if difficult:
		# 	labels_ignore.append(name)
		# else:
		# 	labels.append(name)
	# print(filename)
	# print(width)
	# print(height)
	# print('labels')
	# print(labels)
	# print('ignore')
	# print(labels_ignore)
	



