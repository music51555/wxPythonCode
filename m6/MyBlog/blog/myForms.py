from django import forms
from django.forms import widgets
from blog.models import *
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

class UserForm(forms.Form):
    username=forms.CharField(
        min_length=4,
        label='用户名',
        # error_messages有required必填项检查，还有invalid邮箱格式校验
        error_messages={'required':'用户名不能为空'},
        widget=widgets.TextInput(attrs={'class':'form-control'})
    )
    password=forms.CharField(
        min_length=6,
        label='密码',
        error_messages={'required': '密码不能为空'},
        widget=widgets.PasswordInput(attrs={'class':'form-control'})
    )
    r_password=forms.CharField(
        min_length=6,
        label='确认密码',
        error_messages={'required': '确认密码不能为空'},
        widget=widgets.PasswordInput(attrs={'class':'form-control'})
    )
    email=forms.EmailField(
        label='邮箱',
        error_messages={'required': '邮箱不能为空','invalid': '邮箱格式不正确'},
        widget=widgets.EmailInput(attrs={'class':'form-control'})
    )

    # 局部钩子，校验单一字段，clean_username
    def clean_username(self):
        username=self.cleaned_data.get('username')

        user=UserInfo.objects.filter(username=username)

        if not user:
           return user
        else:
            # 当前字段报出异常后，就会存储在error字典中，当在ajax中循环时，就会将其根据id_+key.next.text存储为标签值
            raise ValidationError('用户已存在')

    # 全局钩子在errors字典中的key是__all__，在ajax返回的data中获取
    def clean(self):
        pwd=self.cleaned_data.get('password')
        r_pwd=self.cleaned_data.get('r_password')

        if pwd==r_pwd:
            return self.cleaned_data
        else:
            raise ValidationError('两次密码不一致')