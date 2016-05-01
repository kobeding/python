from PIL import Image,ImageDraw,ImageFont
import random
#在一个图片右上角添加一个数字（关于random的方法小结）
def rndInt():
	num = str(random.randint(0,100))
	#生成一个指定范围内的整数
	#print (num)
	return num
print(random.uniform(10,20))
#17.52672753143654
print(random.randrange(0,101,2))#随机偶数
print(random.random())#随机浮点数
#0.8303642719354455
print(random.choice('abcdefghijklmnopqrstuvwxyz'))#随机字符,或者：
print(chr(random.randint(65,90)))
L =[]
for i in range(5):
	str1 = chr(random.randint(65,90))
	L.append(str1)
print(''.join(L))
#JEEGB(0--48,a--97,A--65)
#join():将字符串 元组 列表中的元素以指定的字符(分隔符)连接成一个新的字符串
print(L)
K = [1,2,3,4,5,6,7]
random.shuffle(	K)#洗牌
print(K)
def add_num(img):
	draw = ImageDraw.Draw(img)
	myfont = ImageFont.truetype('/home/kobe/duv/python/testpy/ukai.ttf',size=20)
	fillcolor = 'red'   #"#ff0000"
	width,height = img.size
	draw.text((width-20,0),rndInt(),font=myfont,fill=fillcolor)
	img.save('result.jpg')
	return 0

if __name__ == "__main__":
	image = Image.open('test.jpg')
	add_num(image)