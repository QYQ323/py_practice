str = 'aeiou'
def count_s(s):
	n = len(s)
	count = 0
	for i in range(n):
		for j in range(5):
			if s[i] == str[j]:
				count+=1

	return count

a = input("> ")
b = count_s(a)
print(b)