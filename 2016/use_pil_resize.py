from PIL import Image,ImageFilter

#打开一个jpg图像文件，当前路径
im = Image.open('test.jpg')
#获得图像尺寸
w , h = im.size
print('Originnal image size: %s * %s' % (w,h))
#缩放50%:
im.thumbnail((w//2,h//2))#两个括号，传入一个列表？
print('Resize image to :%s * %s' % (w//2,h//2))
#把缩放后的图像用jpeg格式保存：
im.save('thumbnail.jpg','jpeg')
#应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('bulr.jpg','jpeg')