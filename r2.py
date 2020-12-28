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
	for line in lines:
		s=line.split(' ')  #字串切割
		tiem=s[0]
		name=s[1]
		if s[1]=='Allen':
			for m in s[2:]:
				allen_word_count = allen_word_count + len(m)
		elif s[1]=='Tom':
			for m in s[2:]:
				Tom_word_count = Tom_word_count + len(m)
	print('Allen說了',str(allen_word_count) ,'字')
	print('Tom說了',str(Tom_word_count) ,'字')


# 寫入檔案
def write_file(filename,new):
	with open(filename, 'w', encoding='utf-8') as f:  #開啟檔案
		for line in new:
			f.write(line + '\n')

def main():
	lines= read_file('[LINE]Tome.txt')
	print(lines)
	convert(lines)
	#write_file('output.txt',lines)

main()