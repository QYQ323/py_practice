def count_word(s):
	n = len(s)
	count = 0
	for i in range(n):
		if s[i] == " ":
			count += 1
	print("The word count is: ",count+1)

a = input("> ")
b = open(a)
count_word(b)
