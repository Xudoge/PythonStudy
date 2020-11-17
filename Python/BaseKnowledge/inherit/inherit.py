


class A:


    def __init__(self,value,name):
        self.value=value
        self.name=name
        print("这是一个父类方法")

    def hihi():
        print(self.name)

class B(A):

    def __init__(self,value,name):
        #A.__init__(self,value=1,name="a")
        super().__init__(value,name)
        print("这是一个子类类方法1")




b=B(1,"nameB")
print(b.name)

c=B(1,"nameC")

print(c.name)
print(b.name)