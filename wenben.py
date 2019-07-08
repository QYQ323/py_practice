#参考https://blog.csdn.net/lonely_feather/article/details/93414493
#https://www.cnblogs.com/shwee/p/9427975.html#C1
import tkinter 
# 导入tkinter库,实现GUI程序

#实例化object
win = tkinter.Tk()  # 创建窗口win
win.title('文本编辑器')  # 设置标题

#设置窗口大小，可有可无,根据喜好
win.geometry('500x300')  # 这里的乘是小x

entry_file = tkinter.Entry(win)  # 创建一个文本输入框
entry_file.pack()  # 放置该输入框


#我们如果要打开文件并保证最后关闭它，只需要这么做：
#with open("x.txt") as f:
#    data = f.read()
#    do something with data

# 打开文件
def do_open():
	file_path = entry_file.get()  # 获取文本框的内容
	with open(file_path) as f:
		# 打开文件
		content = f.read()  #一次性读取文件内容，对大文件不宜使用
		text.delete(0.0, tkinter.END)  # 清空文本框内容
		text.insert(tkinter.END, content)  # 在光标后插入内容

# 保存文件
def do_save():
	content = text.get(0.0, tkinter.END)  # 获取文本框内容
	file_path = entry_file.get()  # 文件路径
	with open(file_path, 'w') as f:
		f.write(content)

#按钮、便签tkinter.类(窗口,text='',尺寸，功能)
btn_open = tkinter.Button(win, text='打开', command=do_open)  # 创建按钮用于打开文件
btn_save = tkinter.Button(win, text='保存', command=do_save)  # 创建按钮用于保存文件
btn_open.pack()#放置按钮
btn_save.pack()

# 创建多行文本框，用于编辑文件
text = tkinter.Text(win)
text.pack() 

win.mainloop()  # 进入消息循环
