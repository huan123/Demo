# def log(func):
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
#
# @log
# def now():
#     print("2018-9-10")
#
# now()

def huan(func):
    def decorate(*args, **kwargs):
        print("huan的装饰器")
        print("查看被装饰函数的参数")
        print(args, kwargs)
        return func(*args, **kwargs)
    return decorate

@huan
def test(*args, **kwargs):
    print("我是被装饰的函数test")
    print("*args")
    print(args)
    print("kwargs")
    print(kwargs)
    return "test"


t = test(1, 2, 3, a = 10, b = 20)
print(t)






