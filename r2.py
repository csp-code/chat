# 讀取檔案
def read_file(filename):
	lines=[]
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return(lines)

# 分析資料
def convert(lines):
	allen_word_count=0
	Tom_word_count=0
	allen_sticker_count=0
	Tom_sticker_count=0
	allen_image_count=0
	Tom_image_count=0	
	for line in lines:
		s=line.split(' ')  #字串切割
		time=s[0]
		name=s[1]
		if name=='Allen':
			if s[2]=='貼圖':
				allen_sticker_count = allen_sticker_count + 1
			elif s[2]=='圖片':
				allen_image_count = allen_image_count + 1
			else:	 
				for m in s[2:]:
					allen_word_count = allen_word_count + len(m)
		elif name=='Tom':
			if s[2]=='貼圖':
				Tom_sticker_count = Tom_sticker_count + 1
			elif s[2]=='圖片':
				Tom_image_count = Tom_image_count + 1
			else:
				for m in s[2:]:
					Tom_word_count = Tom_word_count + len(m)
					print(m)
	print('------------------------------------')
	print('Allen說了'+ str(allen_word_count) + '字')
	print('Allen傳了'+ str(allen_sticker_count) + '個貼圖')
	print('Allen傳了'+ str(allen_image_count) + '張圖片')
	print('------------------------------------')
	print('Tom說了'+ str(Tom_word_count) + '字')
	print('Tom傳了'+ str(Tom_sticker_count) + '個貼圖')
	print('Tom傳了'+ str(Tom_image_count) + '張圖片')
	print('------------------------------------')


# 寫入檔案
def write_file(filename,new):
	with open(filename, 'w', encoding='utf-8') as f:  #開啟檔案
		for line in new:
			f.write(line + '\n')

def main():
	lines= read_file('[LINE]Tome.txt')
	# print(lines)
	convert(lines)
	#write_file('output.txt',lines)

main()