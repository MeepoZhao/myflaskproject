# encoding = utf-8

from math import hypot

class Vector:
    # 初始化向量
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    # 向量字符串输出
    def __repr__(self):
        return "Vecor({},{})".format(self.x,self.y)
    
    # 计算向量的模
    def __abs__(self):
        return hypot(self.x,self.y)
    
    # 将模为0的向量判断为false
    def __bool__(self):
        return bool(self.x or self.y)
    
    # 模的加法
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    
    # 模的标量
    def __mul__(self,scalar):
        return Vector(self.x * scalar, self.y * scalar)
