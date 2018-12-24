博客文章的描述，是截取了文章的一部分进行展示概要的：

**parse：**  美 /pɑrs/   解析

**parser：**   美 /pɑrsɚ/  解析器



#### 功能一：获取标签+字符串内容中的字符串

**1、切片操作：**

如果单纯的使用切片操作，对于带有`html`标签的文章，那么就会导致，截断至未闭合的标签，页面错乱展示

**2、`BeautifulSoup`**:

`BeautifulSoup`模块主要是用于通过解析器，对文本内容进行摘要，如同时包含标签和文本的文章内容，通过该模块的`html.parser`解析器，只摘要出文章内容，通过切片后，摘要出部分文章内容

**知识点1：**安装`pip3 install beautifulsoup4 `

**知识点2：**引入`from bs4 import BeautifulSoup`

**知识点3：`soup.text`**得到的是文章内容，去除了标签，对其切片操作后，得到文章概要

```python
def add_article(request):
        article_content=request.POST.get('article-content')
        
        # 得到soup对象，调用soup对象的text方法，只取出文章内容
        soup = BeautifulSoup(article_content, 'html.parser')
        desc = soup.text[:150].strip()

        article_obj=Article.objects.create(
            title=article_title, desc=desc, content=article_content, user_id=request.user.pk,category_id=category)

    return render(request, 'add_article.html', locals())
```



#### 功能二：过滤不合法的标签

**知识点一：`BeautifulSoup`**获取到的`soup`对象，是包含标签+标签值的

**知识点二：`soup.find_all()`**结果是一组列表，存储的是每一个标签对象

**知识点三：**标签对象拥有`name`属性，检查其值是否等于非法标签

**知识点四：**标签对象拥有`decompose`属性，将其在`soup`对象内容中删除，美 /,dikəm'poz/ 分解；腐烂 

```python
def add_article(request):
    user=UserInfo.objects.filter(username=request.user.username).first()

    if request.method == 'POST':
        article_title=request.POST.get('article-title')
        article_content=request.POST.get('article-content')
        category=request.POST.get('category')
        tag=request.POST.getlist('tag')

        # 通过html.parser解析器得到文章内容+标签对象soup
        soup = BeautifulSoup(article_content, 'html.parser')

        # find_all结果是一个列表，存储每一对标签和标签值[<p>hello</p>, <p>world</p>, <p><br/></p>, <br/>, <script>alert(123)</script>]
        # 每一个标签对象都有name属性，判断其值是否等于非法标签内容，调用标签对象的decompose方法将其删除，删除后soup对象中就不包含非法内容了
        for tag in soup.find_all():
            if tag.name == 'script':
                tag.decompose()

        desc = soup.text[:150].strip()

        # 存储文章内容时，直接使用去除非法标签后的str(soup)对象内容
        article_obj=Article.objects.create(
            title=article_title, desc=desc, content=str(soup), user_id=request.user.pk,category_id=category)

    return render(request, 'add_article.html', locals())
```

