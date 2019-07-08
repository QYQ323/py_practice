#采用切片的方法，设置步长为-1，也就是反过来排序。
#切片a=(1,2,3,4),a[:]=a[::]=(1,2,3,4)
def reverse_s(s):
	return (s[::-1])#步长为负数，从序列最后一个开始切片
b = input("> ")
a = reverse_s(b)
print (a)