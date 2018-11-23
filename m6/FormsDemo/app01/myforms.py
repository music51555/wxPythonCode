from django import forms
from django.forms import widgets
from app01.models import *
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

class RegisterForm(forms.Form):
    username=forms.CharField(
        widget=widgets.TextInput(attrs={'class':'form-control'}),
        error_messages={'required':'用户名不能为空'},
        label='用户名',
    )
    password=forms.CharField(
        widget=widgets.PasswordInput(attrs={'class':'form-control'}),
        min_length=6,
        error_messages={'required': '密码不能为空'},
        label='密码',
    )
    r_password=forms.CharField(
        widget=widgets.TextInput(attrs={'class':'form-control'}),
        min_length=6,
        error_messages={'required': '确认密码不能为空'},
        label='确认密码',
    )
    email=forms.EmailField(
        widget=widgets.TextInput(attrs={'class':'form-control'}),
        error_messages={'required': '邮箱不能为空'},
        label='邮箱',
    )
    tel=forms.CharField(
        widget=widgets.TextInput(attrs={'class':'form-control'}),
        error_messages = {'required': '手机号不能为空'},
    )

    def clean_username(self):
        val=self.cleaned_data.get('username')

        ret=User.objects.filter(username=val)

        if len(val)<4 or len(val)>10:
            raise ValidationError('请输入4~16个字符的用户名')

        if ret:
            raise ValidationError('用户已存在')

        return val

    def clean(self):
        pwd=self.cleaned_data.get('password')
        r_pwd=self.cleaned_data.get('r_password')

        # 如果校验成功规则对象中的规则，如min_length=4,或clean_%s中的规则，如clean_password、clean_r_password，那么他们会被存储在cleaned_data字典中，否则就会在errors字典中，所以先从cleaned_data中查询出两个校验成功的字段值，如果可以查询出再进行两个字段之间的校验
        if pwd and r_pwd:
            if pwd==r_pwd:
                return self.cleaned_data
            else:
                raise ValidationError('两次密码不一致')




