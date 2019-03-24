 Python全栈第16期



#### 1.python中逻辑运算符有哪些? 它们之间有什么区别?

```python
and
连接条件，当and两侧的条件均为True时才会执行判断下的代码块

or
连接条件，or两侧的条件，只要有一侧为True，就会执行判断下的代码块

not
取反，如
'alex' not in names表示字符串不在当前的序列中
```



#### 2.如下比较运算分别返回什么？

如果

**a = 15，b = 9**

```python
a == b # 返回False，因为15!=9

a != b # 返回True，因为15!=9

a > b # 返回True，因为15大于9

(a - 5) < b #返回False，因为10大于9

a >= b ** 2 #返回False，15小于b的2次方

(a + 13 - 10 * 2) <= (b // 2 * 5 + 35 % 4) # 比较运算符左侧得到结果8，比较运算符右侧得到结果23，结果为False
```



#### 3.定义字符串I'm Lemon, I love Python automated testing！

提示：使用双引号还是单引号呢？

```python
# 使用双引号，因为字符串中有单引号
test = "I'm Lemon, I love Python automated testing！"
```





#### 4.把website = 'http://www.python.org'中的python字符串取出来

提示：可以使用字符串切片

```python
website[11:-4]
```





#### 5.将给定字符串前后的空格除去，把PHP替换为Python

 best_language = "     PHP is the best programming language in the world!      "

```python
best_language.strip().replace('PHP','Python')
```





#### 6.演练字符串操作

```
my_hobby = "Never stop learning!"
```

- 截取从 2 ~ 6位置 的字符串

- ```python
  my_hobby[1:7]
  ```

- 截取从 2 ~ 末尾的字符串

  ```python
  my_hobby[1:-1]
  ```

- 截取从 开始~ 6 位置 的字符串

  ```python
  my_hobby[:7]
  ```

- 截取完整的字符串

  ```python
  my_hobby[:]
  ```

- 从开始位置，每隔一个字符截取字符串

  ```pythoN
  my_hobby[::2]
  ```

- 从索引 3 开始，每隔2个取一个

  ```
  my_hobby[3::3]
  ```

- 截取从 2 ~ 末尾-1的字符串

  ```python
  my_hobby[1:-1]
  ```

- 截取字符串末尾两个字符

  ```python
  my_hobby[-2:]
  ```

- 字符串的逆序（拓展）

  ```
  my_hobby[::-1]
  ```

  



#### 7.去生鲜超市买橘子

- 收银员输入橘子的价格，单位：**元／斤**
- 收银员输入用户购买橘子的重量，单位：**斤**
- 计算并且 **输出** 付款金额

```python
def shopping():
	shopping_per_price = int(input('请输入橘子每斤的单价：'))
	shopping_weight = int(input('请输入购买的斤数：'))
	return '请付款：{0}元'.format(shopping_per_price * shopping_weight)
shopping()
```



> 思考：如果输入的不是一个数字，执行程序会怎样？如何解决呢？

```pythoN
1、可以将输入的内容强制转换为整型
2、可以判断用户的输入，如：
while True:
  shopping_per_price = int(input('请输入橘子每斤的单价：'))
	if shopping_per_price.isdigit():
		shopping_per_price = int(shopping_per_price)
    break
	else:
		print('请重新输入')
```