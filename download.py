import random,requests
def name(st):
	if 'video' in st:
		n=''
		for w in range(10):
			letter=random.choice('qweruioplkjhmnbfvcdsxza')
			n+=letter
		n+='.mp4'
	elif 'jpg' in st:
		n=''
		for w in range(10):
			letter=random.choice('qazxwswedcvrtgbnhyujmkilop')
			n+=letter
		n+='.jpg'
	else:
		n=None
	return n


def do(l):
	for z in l:
		try:
			named=name(z)
			raw=requests.get(z).content
			gg=open(named, 'wb')
			gg.write(raw)
			gg.close()
		except Exception:
			print('Error!!!', named, z)
			continue

b=open('a', 'r')
lines=b.readlines()
li=[]
for x in lines:
	if len(x)>12:
		li.append(x[:-1])
do(li)
