str = 'aeiou'
def pig(s):
	n = len(s)
	i = 0
	for j in range(5):
		if s[i] == str[j]:
			i+=1
	#如果最后一个是辅音
	if i ==n-1:
		return s+'-ay'
	else:#辅音前+辅音后
		return s[0:i]+s[i+1:]+'-'+s[i]+'ay'
b = input("> ")
a = pig(b)
print(a)