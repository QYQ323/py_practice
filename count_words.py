from sys import argv
script,input_file = argv
def count_words(s):

	n = len(s)
	count = 0
	for i in range(n):
		if s[i] == " "or s[i] == "\n":
			count += 1
	print("The word count is: ",count+1)


txt_file = open(input_file)
txt = txt_file.read()
count_words(txt)
txt_file.close()