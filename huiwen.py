def huiwen(s):
	n = len(s)
	j = len(s)
	for i in range(int (n/2+1)):
		if s[i] == s[j-1]:
			j = j-1

	if j<=int (n/2):
		print("This word is plalindrome.")
	else:
		print("This word is not plalindrome.")
a = input("> ")
huiwen(a)