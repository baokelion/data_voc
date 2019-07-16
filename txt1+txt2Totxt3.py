category_set = ['plane', 'baseball-diamond', 'bridge', 'ground-track-field', 
'small-vehicle', 'large-vehicle', 'ship', 
'tennis-court', 'basketball-court',  
'storage-tank', 'soccer-ball-field', 
'roundabout', 'harbor', 
'swimming-pool', 'helicopter','container-crane']
for i in category_set:
	filename = i
	li = []
	a = open('./train/set/'+filename+'_train.txt')
	a_r = a.read()
	for i in a_r:
		li.append(i)
	a.close()
	b = open('./val/set/'+filename+'_val.txt')
	b_r = b.read()
	for j in b_r:
		li.append(j)
	b.close()

	c = open('./trainval/'+filename+'_trainval.txt','w')
	s=''
	c.write(s.join(li))
	c.close()
