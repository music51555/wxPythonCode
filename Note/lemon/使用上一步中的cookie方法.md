反射

hasattr(类，'方法名/属性名')

setattr()

getattr()

delattr()



在执行测试用例时，如果某一步的请求需要借助上一步响应体中的某个属性，如cookie，那么可以

1、使用setUp()

2、使用全局变量

3、使用反射