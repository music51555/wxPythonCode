from django import forms
from django.forms import widgets
from rbac.models import *
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError


class UserForms(forms.Form):
    name = forms.CharField(
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
        username = self.cleaned_data.get('name')
        user_obj = UserInfo.objects.filter(name = username)
        if not user_obj:
            raise ValidationError('用户不存在')
        else:
            return username

    def clean(self):
        username = self.cleaned_data.get('name')
        pwd = self.cleaned_data.get('password')

        if username and pwd:
            user_obj = UserInfo.objects.filter(name=username, password=pwd)
            if user_obj:
                return self.cleaned_data
            else:
                raise ValidationError('用户名或密码错误')
