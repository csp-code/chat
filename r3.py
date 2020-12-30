
lines = []
with open('3.txt','r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

str1= []
for line in lines:
	str1=line.split(' ')
	time=str1[0][:5]
	name=str1[0][5:]
	print(name)

