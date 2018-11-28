from django import forms
from django.forms import widgets
from setCookie.models import *
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.contrib.auth.models import User
from django.contrib import auth

class UserForm(forms.Form):
    username=forms.CharField(
        label='用户名',
        widget=widgets.TextInput()
    )
    password=forms.CharField(
        label='密码',
        widget=widgets.PasswordInput()
    )

    def clean_username(self):
        username=self.cleaned_data.get('username')

        user_obj=User.objects.filter(username=username).first()
        print(user_obj)
        if user_obj:
            return username
        else:
            raise ValidationError('用户名不存在')

    # def clean(self):
    #     username=self.cleaned_data.get('username')
    #     password=self.cleaned_data.get('password')
    #
    #     if username and password:
    #         user_obj=UserClass.objects.filter(username=username,password=password)
    #
    #         if user_obj:
    #             return self.cleaned_data
    #         else:
    #             raise ValidationError('用户名或密码错误')
