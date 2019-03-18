如何实现点击内容区域的按钮，所属的菜单仍然保持selected状态

首先在数据库中为每个菜单按钮，添加了pid字段，表示当前按钮权限的父级菜单id



```mysql
#id   title          url                        icon            menu_id     pid   
 1	 客户列表	/customer/list/	                fa-bath	            1	     null
 2	 添加客户	/customer/add/	                fa-bar-char        null        1
 3	 删除客户	/customer/list/(?P<cid>\d+)/	fa-bar-chart	   null        1
 4	 修改客户	/customer/edit/(?P<cid>\d+)/	fa-bar-chart	   null        1
 5	 批量导入	/customer/import/	            fa-bar-chart	   null        1
 6	 下载模板	/customer/tpl/	                fa-bar-chart	   null        1
 7	 账单列表	/payment/list/	                fa-shower	        1	     null
 8	 添加账单	/payment/add/	                fa-bar-chart	   null        7
 9	 删除账单	/payment/del/(?P<pid>\d+)/	    fa-bar-chart	   null        7
 10	 修改账单	/payment/edit/<?P<pid>\d+/	    fa-bar-chart	   null        7
 11	 个人信息	/userinfo/list	                fa-taxi	            2	     null
```



首先分别查询出了一级菜单和二级菜单，并组合成新的字典

```python
menu_queryset = Menu.objects.values('id','title','icon')
permission_query = Permission.objects.filter(role__userinfo__username=username).\
        values('id','title','icon','url','menu__title','menu__icon','pid')


# 一级菜单的字典，以及permission_list列表中包含的二级菜单字典
sorted_dict
{
    '信息管理': {
        'id': 1,
        'title': '信息管理',
        'icon': 'fa-bar-chart',
        'class': 'hide',
        'permission_list': [
            {
                'id': 1,
                'title': '客户列表',
                'icon': 'fa-bath',
                'url': '/customer/list/',
                'menu__title': '信息管理',
                'menu__icon': 'fa-bar-chart',
                'pid': None
            },
            {
                'id': 7,
                'title': '账单列表',
                'icon': 'fa-shower',
                'url': '/payment/list/',
                'menu__title': '信息管理',
                'menu__icon': 'fa-bar-chart',
                'pid': None
            }
        ]
    },
    '用户信息': {
        'id': 2,
        'title': '用户信息',
        'icon': 'fa-address-book-o',
        'class': 'hide',
        'permission_list': [
            {
                'id': 11,
                'title': '个人信息',
                'icon': 'fa-taxi',
                'url': '/userinfo/list',
                'menu__title': '用户信息',
                'menu__icon': 'fa-address-book-o',
                'pid': None
            }
        ]
    }
}
```



在中间件中完成了菜单和权限字典的配置

```python
# 首先从session中获取到上面准备完成的字典
sorted_dict = request.session.get(MENU_DICT_SESSION_KEY)

if sorted_dict:
    # 循环字典，循环的内容是字典一级菜单的title和对应的每一个一级菜单的字典
    for menu_title, menu_info in sorted_dict.items():
        # 循环综合字典的时候，循环所有权限列表
        for permission in permission_list:
            # 直到在permission_list中找出当前访问路径的权限字典
            if not request.path_info == permission['url']:
                continue
          # 找到了这条权限的字典，开始循环综合字典中的二级菜单的字典所在的列表permission_list
            for permission_dict in menu_info['permission_list']:
                # 首先判断一下当前访问的这个权限字典中有无pid属性，如果没有按照数据库表示为二级菜单，如果有则表示为按钮
                if permission['pid']:
                    # 得到当前权限字典的中的pid值，判断是否等于我正在循环的二级菜单列表中每个二级菜单字典的id，如果不等于就再次循环，直到找到当前权限的父级二级菜单字典
                    if not permission['pid'] == permission_dict['id']:
                        continue
                    # 为这个按钮权限的父级二级菜单添加class属性，变为selected，让他在html中加载时，获得该属性，变为选中状态，并将这个二级字典的一级菜单字典的class属性变为show可见状态
                    permission_dict['class'] = 'selected'
                    menu_info['class'] = 'show'
                # 如果点击的二级菜单，那么它是没有pid属性值的，为None
                else:
                    # 这时判断访问的二级菜单的路径是否等于当前访问的路径，如果不等于则再次循环下一个二级菜单字典，直到找到当前访问的路径权限等于的那个二级菜单路径，为其添加上selected类，并且如果这个二级菜单的一级菜单的类不是show可见状态，那么为其设置为show，因为初始化权限时，每一个一级菜单的class都为hide，让其在加载首页时，默认只显示一级菜单
                    if permission_dict['url'] == request.path_info:
                        permission_dict['class'] = 'selected'
                        if not menu_info['class'] == 'show':
                            menu_info['class'] = 'show'
                        break
```

