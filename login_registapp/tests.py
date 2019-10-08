from django.test import TestCase

# Create your tests here.

import hashlib
#
# h = hashlib.sha256()
# h.update(b'123456')
# #获得二进制加密
# print(h.digest())
# #获得十六进制加密
# print(h.hexdigest())
# #盐
# h1 = hashlib.sha256()
# yan = b'666'
# h1.update(b'123456'+yan)
# # 构建一个sha256对象
# h2 = hashlib.sha256()
# #用户输入的密码，转成二进制
# mima = b'123456'
# #从数据库中取出盐
# yan = b'666'
# m = mima+yan
# # 对用户输入的密码加上从数据库中取出的盐再次进行加密，加密后和数据库中存的密文进行相比
# h2.update(b'123456'+yan)
# print(h2.hexdigest())
# print(h1.hexdigest())


msg = "123"

#unicode编码转换为utf-8编码
# print(msg.encode(encoding = "utf-8"))    ##b'123456'
#unicode编码转换为utf-8编码，再转化为unicode编码
# print(msg.encode(encoding = "utf-8").decode(encoding = "utf-8"))


h1 = hashlib.sha256()
yan = b'666'

h1.update(msg.encode(encoding = "utf-8")+yan)
print(h1.hexdigest())
# 构建一个sha256对象
h2 = hashlib.sha256()
#用户输入的密码，转成二进制
mima = msg.encode(encoding = "utf-8")
#从数据库中取出盐
yan2 = b'666'
# 对用户输入的密码加上从数据库中取出的盐再次进行加密，加密后和数据库中存的密文进行相比
h2.update(mima+yan2)
print(h2.hexdigest())

