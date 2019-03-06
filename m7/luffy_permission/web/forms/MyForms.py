from django import forms
from django.forms import widgets
from rbac.models import *
from django.core.exceptions import ValidationError


class UserForms(forms.Form):
    username = forms.CharField(
        label='用户名', widget = widgets.TextInput(attrs = {'class':'form-control'}),
        error_messages={'required':'请填写必填项'}
    )
    password = forms.CharField(
        label='密码', widget = widgets.PasswordInput(attrs = {'class':'form-control'}),
        error_messages={'required': '请填写必填项'}
    )
    email = forms.EmailField(
        error_messages={'invalid': '邮箱格式错误','required': '请填写必填项'},
        widget = widgets.EmailInput(attrs = {'class':'form-control'})
    )

    def clean_name(self):
        username = self.cleaned_data.get('username')
        user_obj = UserInfo.objects.filter(username = username)
        if not user_obj:
            raise ValidationError('用户不存在')
        else:
            return username

    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #
    #     if username and password:
    #         user_obj = UserInfo.objects.filter(username=username,password=password).first()
    #         if user_obj:
    #             return self.cleaned_data
    #         else:
    #             raise ValidationError('用户名或密码错误')
