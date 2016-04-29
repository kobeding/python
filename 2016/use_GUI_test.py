from tkinter import  *
import tkinter.messagebox as messagebox
#从Frame派生Application类，所有Widget的父容器
class  Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
#pack()方法把Widget加入到父容器中，并实现布局，grid()可以实现更复杂的布局
	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self,text='show',command=self.show)
		#用户点击hello(改为show)按钮，触发hello()，通过self.nameInput.get()获得用户输入文本
		self.alertButton.pack()
		#self.helloLabel = Label(self,text="Hello,world!")
		#self.helloLabel.pack()
		self.quitButton = Button(self,text='Quit',command=self.quit)
		#Button被点击时，触发self.quit()使程序退出
		self.quitButton.pack()
	def show(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message','Hello, %s' % name)
		#tkinter.messagebox.showinfo()可以弹出对话框
#实例化Application:
app = Application()
#设置窗口标题：
app.master.title('Hello World')
#主消息循环：
app.mainloop()
