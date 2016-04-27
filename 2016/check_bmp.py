#!/usr/bin/env python3
import struct
#python提供一个struct模块来解决butes和其他二进制数据类型转换
d = struct.pack('>I',10240099)
#pack函数把任意的数据类型变为bytes，第一个参数是处理参数
#>I：字节顺序是big-endian，网络序，I表示4字节无符号整数
print(d)
#b'\x00\x9c@c'
#bmp位图文件，可以用unpack读取出出来，然后判断：
bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH',bmp_header))
#unpack把bytes变成相应的数据类型
#(b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
#‘BM'/'BA'--位图大小--保留位0--实际图像偏移量--header的字节数--图像宽度--高度--始终为1--颜色数