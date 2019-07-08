#这种方法是采用列表的reverse方法，先将s转换为列表，然后通过reverse方法反转，然后通过join连接为字符串。
#reverse()是把列表方向排序;
def reverse_s(s):
	a = list(s)
	a.reverse()
	return (''.join(a))

b = input("> ")
a = reverse_s(b)
print(a)