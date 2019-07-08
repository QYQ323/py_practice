str = ['a','e','i','o','u']
def count_s(s):
	n = len(s)
	count = 0
	count_a = 0
	count_e = 0
	count_i = 0
	count_o = 0
	count_u = 0
#统计元音字母的数量
#	for i in range(n):
#		for j in range(5):
#			if s[i] == str[j]:
#				count+=1
	for i in range(n):
		if s[i] == 'a':
			count_a+=1
		elif s[i] =='e':
			count_e+=1
		elif s[i] =='i':
			count_i+=1
		elif s[i] =='o':
			count_o+=1
		elif s[i] =='u':
			count_u+=1
	print(f"元音的个数为:{count_a+count_e+count_i+count_o+count_u}\n"
			f"a的个数为{count_a}:\ne的个数为:{count_e}\n"
			f"i的个数为:{count_i}\no的个数为:{count_o}\n"
			f"u的个数为:{count_u}\n")

a = input("> ")
count_s(a)
