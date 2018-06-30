from PIL import Image, ImageFont, ImageDraw
# PIL的ImageFont用于加载字体，以供ImageDraw用
# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图

# 打开一个jpg图像文件
image = Image.open('0.jpg')
# 获得图像尺寸:
w, h = image.size
# 设置字体,和字体大小
font = ImageFont.truetype('MissBrooks.TTF', 60,index=0)
# 创建一个可用来对image进行操作的对象。对所有即将使用ImageDraw中操作的图片都要先进行这个对象的创建。
draw = ImageDraw.Draw(image)
# draw.text
# 在图像内添加文字

draw.text((w-180, 30),"Goohack",fill=(84,166,243),font=font)
image.save('1.png', 'jpeg')


