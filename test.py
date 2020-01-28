# print("Hello World")


# x = []
# x.append(0)
# x+=[1]
# x = x + [2]
# x = [3]+x
# print(x)
# x[0]=["Hi","world"]
# print(x)

# x=(0,1,2)

# x[0]=4

# x(x)
# print(x[0])
# x=[0,1,2,3,4]
# x={"key":"value","first_name":"Bob"}
# for item in x.keys():
#     print(str(item)+ " " + str(x[item]))
# print()

# def fun(to_out, end="\n", p_range=1):
#     for i in range(p_range):
#         print(to_out,end=str(end))

# fun(p_range=5, end=1, to_out="Hi")

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        self.y=4
        return 'hello world'
    
    def f_i(self):
        return self.i + self.y

class MyAwesomeClass(MyClass):
    def f_g(self):
        return self.f_i()+3
    
    def __str__(self):
        return str(self.f_g())

# x=MyClass()
# print(x.f())
# print(x)

try:
    print(4+"HI")
except:
    print("You're doing it wrong")